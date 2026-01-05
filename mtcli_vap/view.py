from .conf import DIGITOS as D


class VAPView:
    """
    View responsável por:
      - formatar o VAP em texto puro (acessível a leitores de tela);
      - produzir saída alinhada e legível, sem elementos gráficos.
    """

    def __init__(self, sort: str = "volume", rows: int = 0):
        """
        Args:
            sort: critério de ordenação ("volume" ou "price")
            rows: quantidade máxima de linhas exibidas (0 = todas)
        """
        self.sort = sort
        self.rows = rows

    def _format_number(self, value: float) -> str:
        """
        Formata volumes no padrão numérico brasileiro:
        separador de milhar com ponto.
        """
        try:
            n = int(round(value))
            return f"{n:,}".replace(",", ".")
        except Exception:
            return str(int(value))

    def render(self, vap_dict: dict) -> str:
        if not vap_dict:
            return "Nenhum dado de VAP encontrado.\n"

        # ordenação
        if self.sort == "price":
            ordered_items = sorted(vap_dict.items(), key=lambda kv: kv[0])
        else:
            ordered_items = sorted(
                vap_dict.items(), key=lambda kv: kv[1], reverse=True
            )

        # volume TOTAL do VAP (antes de aplicar rows)
        total_volume = sum(v for _, v in ordered_items) or 1.0

        # aplica limite de linhas APENAS para exibição
        if self.rows and self.rows > 0:
            items = ordered_items[: self.rows]
        else:
            items = ordered_items

        lines = [
            "--------------------------------------------",
            "Volume At Price (VAP)",
            "--------------------------------------------",
            f"{'Preço'.ljust(12)} | {'Volume'.rjust(12)} | %",
            "--------------------------------------------",
        ]

        price_strings = [f"{p:.{D}f}" for p, _ in items]
        max_price_w = max((len(s) for s in price_strings), default=0)

        for (p, v), p_str in zip(items, price_strings):
            price_field = p_str.rjust(max_price_w)
            vol_field = self._format_number(v).rjust(12)

            # percentual SEMPRE relativo ao VAP total
            percent = (v / total_volume) * 100
            percent_field = f"{percent:5.1f}"

            lines.append(
                f"{price_field} | {vol_field} | {percent_field}"
            )

        return "\n".join(lines) + "\n"

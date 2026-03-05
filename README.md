# mtcli-vap
  
Plugin **Volume At Price (VAP)** para o **mtcli**, inspirado no **Volume At Price do Profit (Nelógica)**, com foco em **leitura de volume por preço**, **acessibilidade** e **uso em terminal**.
    
O `mtcli-vap` apresenta o VAP de forma **textual**, ordenável e scriptável, ideal para traders que trabalham com **price action, fluxo de ordens e volume**, sem dependência de gráficos.
  
---
  
##Características
  
- **Volume At Price por preço**
- **Distribuição de volume ao longo do range do candle**
- **Ordenação por volume ou por preço**
- **Percentual do volume total por nível**
- **Totalmente acessível** (compatível com NVDA, JAWS, leitores de tela)
- **Arquitetura MVC** (Model / View / Controller)
- Fácil de testar e evoluir
- Saída em **texto puro**, ideal para CLI, logs e pipes
  
---
  
## 🎯 Objetivo do projeto
  
Este plugin busca reproduzir **conceitualmente** o comportamento do **Volume At Price do Profit**, respeitando as limitações do MetaTrader 5 (uso de candles em vez de Times & Trades), mas aplicando técnicas que reduzem vieses comuns, como:
  
- Concentrar todo o volume no preço de fechamento  
- Distribuir o volume entre todos os níveis do candle  
  
O resultado é um **mapa de volume por preço muito mais fiel**, utilizável em leitura de fluxo e contextos de day trade.
  
---
  
## Instalação
  
Este plugin faz parte do ecossistema **mtcli**.
  
```bash
pip install mtcli-vap
````
    
Clone o repositório e instale em modo desenvolvimento:
  
```bash
git clone https://github.com/seu-usuario/mtcli-vap.git
cd mtcli-vap
pip install -e .
```
  
> É necessário ter o **MetaTrader 5** instalado e configurado no sistema.
  
---
    
## Uso básico
  
```bash
mtcli vap --symbol WDOF26
```
  
Saída (exemplo):
  
```text
--------------------------------------------
Volume At Price (VAP)
--------------------------------------------
   Preço |       Volume | %
--------------------------------------------
102.450 |     12.340 | 18.2
102.500 |      9.810 | 14.5
102.400 |      7.220 | 10.7
```
  
---
  
## Opções disponíveis
  
### Símbolo
  
```bash
--symbol, -s
```
  
Símbolo do ativo no MetaTrader 5.

Exemplo:
  
```bash
mtcli vap --symbol WINZ25
```
  
---
  
### Timeframe
  
```bash
--period, -p
```
  
Timeframe usado para construir o VAP.
  
Valores aceitos:
  
```
M1, M5, M15, M30, H1, H4, D1
```
  
---
  
### Número de candles
  
```bash
--limit, -l
```
  
Quantidade de candles analisados.
  
Exemplo:
  
```bash
mtcli vap --symbol WDOF26 --limit 300
```
  
---
  
### Ordenação
  
```bash
--sort volume|price
```

* `volume` (padrão): mostra primeiro os preços mais relevantes
* `price`: mostra o VAP como um mapa contínuo de preços
  
Exemplos:
  
```bash
mtcli vap --symbol WDOF26 --sort volume
mtcli vap --symbol WDOF26 --sort price
```
  
---
  
## Como o VAP é calculado
  
1. Os candles são obtidos via **MetaTrader 5**
2. O volume de cada candle é extraído (`real_volume` ou `tick_volume`)
3. O range `[low, high]` do candle é dividido respeitando o **tick size**
4. O volume é **distribuído igualmente** entre todos os níveis de preço
5. Os volumes são agregados por preço
  
Essa abordagem aproxima o cálculo do **VAP real baseado em negócios**, utilizado no Profit.
  
---
  
## Estrutura do projeto (MVC)
  
```
mtcli_vap/
├── cli.py          # Interface de linha de comando (Click)
├── controller.py   # Orquestra Model → View
├── model.py        # Cálculo do VAP
├── view.py         # Renderização textual acessível
├── conf.py         # Configurações (DIGITOS, TICK_SIZE)
```
  
---
  
## Acessibilidade
  
Este plugin foi projetado para:
  
* Uso sem gráficos
* Saída textual clara
* Compatibilidade com leitores de tela
* Leitura sequencial e previsível
  
Isso o torna adequado para:
  
* Ambientes headless
* Traders com deficiência visual
* Automação e scripts
  
---
  
## Roadmap (planejado)
  
* [ ] Destaque do **POC** (Point of Control)
* [ ] Cálculo de **VAH / VAL** (Value Area)
* [ ] Filtro `--top N`
* [ ] Delta por preço (quando houver fonte de dados)
* [ ] Integração com Market Profile textual
  
---
  
## ⚠️ Limitações conhecidas
  
* O MetaTrader 5 não fornece **Times & Trades completos**
* O VAP é uma **aproximação baseada em candles**
* Não há agressão real de compra/venda (por enquanto)
  
Mesmo assim, a distribuição por range reduz significativamente os vieses tradicionais.
  
---
  
## Contribuições
  
Contribuições são bem-vindas.
  
Sugestões comuns:
  
* Otimização de performance
* Novos formatos de saída
* Métricas de fluxo
* Integração com outras fontes de dados
  
Abra uma issue ou envie um pull request.
  
---
  
## Licença
  
MIT License.
  
---
  
## Inspiração
  
* Volume At Price — **Profit / Nelógica**
* Market Profile
* Tape Reading
* Price Action baseado em volume
  

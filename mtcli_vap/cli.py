import click


def calcular():
    return "Funcionou!"


@click.command()
@click.version_option(package_name="plugin-exemplo")
def vap():
    """Ajuda do comando."""
    resultado = calcular()
    click.echo(f"{resultado}")


if __name__ == "__main__":
    vap()

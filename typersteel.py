import typer

# CLI entrypoint is defined via typer.run(main)


def main(
    name: str,
    lastname: str = typer.Option("", help="Фамилия пользователя."),
    formal: bool = typer.Option(False, "--formal", "-f", help="Использовать формальное приветствие."),
) -> None:
    """Говорит 'Привет' пользователю, опционально используя фамилию и формальный стиль."""
    if formal:
        typer.echo(f"Добрый день, {name} {lastname}!")
        return

    typer.echo(f"Привет, {name}!")


if __name__ == "__main__":
    typer.run(main)

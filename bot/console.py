from datetime import datetime
from rich import print


def time_now():
    dt = datetime.now()
    dtime = dt.strftime("%X")
    return f"[italic white]{dtime}[/] |"


class console():

    def nanostyle(text): print(f'[magenta]{text}[/magenta]')

    def log(text): print(f'{time_now()} [[dim]INFO[/]]:\t{text}')

    def botlog(text): print(f'{time_now()} [[blue]DISCORD[/]]:\t{text}')

    def system(text): print(f'{time_now()} {text}')

    def warn(text): print(f'{time_now()} [[bold underline yellow]WARN[/]]:\t{text}')

    def error(text): print(f'{time_now()} [[bold underline red]ERR![/]]:\t{text}')

    def success(text): print(f'{time_now()} [[bold #32cd32]OK[/]]:\t{text}')

    def notice(text): print(f'{time_now()} [[bold]NOTE[/]]:\t{text}')

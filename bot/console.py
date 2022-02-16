from datetime import datetime
from rich import print


def time_now():
    dt = datetime.now()
    dtime = dt.strftime("%X")
    return f"[italic white]{dtime}[/] |"


class console():
    # These functions are used for convenience. It's not pretty, but it works?
    nanostyle = lambda text : print(f'[magenta]{text}[/magenta]')

    log = lambda text : print(f'{time_now()} [[dim]INFO[/]]:\t{text}')

    botlog = lambda text : print(f'{time_now()} [[blue]DISCORD[/]]:\t{text}')

    system = lambda text : print(f'{time_now()} {text}')

    warn = lambda text : print(f'{time_now()} [[bold underline yellow]WARN[/]]:\t{text}')

    error = lambda text : print(f'{time_now()} [[bold underline red]ERR![/]]:\t{text}')

    success = lambda text : print(f'{time_now()} [[bold #32cd32]OK[/]]:\t{text}')
    
    notice = lambda text : print(f'{time_now()} [[bold]NOTE[/]]:\t{text}')
import datetime
from rich import console, print

x = datetime.datetime.now()
xtime = x.strftime("%X")
fxtime = f"[white]{xtime}[/] |"

class console():
    def nanostyle(text):
        print(f'[magenta]{text}[/magenta]')

    def log(text):
        print(f'{fxtime} [dim]INFO: {text}[/]')

    def botinfo(text):
        print(f'{fxtime} [blue]BOT-INFO: {text}[/]')

    def warn(text):
        print(f'{fxtime} [bold underline yellow]WARN: {text}[/]')

    def error(text):
        print(f'{fxtime} [bold underline red]ERRO: {text}[/]')

    def print(text):
        print(text)
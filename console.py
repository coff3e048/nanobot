import datetime
from rich import console, print

x = datetime.datetime.now()
xtime = x.strftime("%X")

class console():
    def nanostyle(text):
        print(f'[magenta]{text}[/magenta]')

    def log(text):
        print(f'[white]{xtime}[/] | [dim]INFO: {text}[/]')

    def botinfo(text):
        print(f'[white]{xtime}[/] | [blue]BOT-INFO: {text}[/]')

    def warn(text):
        print(f'[white]{xtime}[/] | [bold underline yellow]WARN: {text}[/]')

    def error(text):
        print(f'[white]{xtime}[/] [dim red]|[/] [bold underline red]ERRO: {text}[/]')

    def print(text):
        print(text)
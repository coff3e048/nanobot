from datetime import datetime
from rich import print


class console():

    def _print(logtype = "log", text = str):
        x = datetime.now()
        xtime = x.strftime("%X")
        fxtime = f"[italic white]{xtime}[/] |"

        if logtype == 'nanostyle':
            text = f'[magenta]{text}[/magenta]'
        elif logtype == 'log':
            text = f'{fxtime} [dim]INFO: {text}[/]'
        elif logtype == 'botlog':
            text = f'{fxtime} [blue]BOT-INFO: {text}[/]'
        elif logtype == 'system':
            text=f'{fxtime} {text}'
        elif logtype == 'warn':
            text = f'{fxtime} [bold underline yellow]WARN: {text}[/]'
        elif logtype == 'error':
            text = f'{fxtime} [bold underline red]ERRO: {text}[/]'
        elif logtype == 'success':
            text = f'{fxtime} [bold #32cd32]OK: {text}[/]'
        print(text)

    def nanostyle(text):
        console._print('nanostyle',text)
          
    def log(text):
        console._print('log',text)

    def botlog(text):
        console._print('botlog',text)

    def system(text):
        console._print('system',text)

    def warn(text):
        console._print('warn',text)

    def error(text):
        console._print('error',text)

    def success(text):
        console._print('success',text)

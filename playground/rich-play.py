from time import sleep
import logging
from rich.logging import RichHandler
from rich import pretty
from rich import print, pretty
from rich.panel import Panel
from rich.table import Column
from rich.progress import Progress, BarColumn, TextColumn

with Progress() as progress:
    task = progress.add_task("twiddling thumbs", total=10)
    for job in range(10):
        progress.console.print(f"Working on job #{job}")
        progress.advance(task)

text_column = TextColumn("{task.description}", table_column=Column(ratio=1))
bar_column = BarColumn(bar_width=None, table_column=Column(ratio=2))
progress = Progress(text_column, bar_column, expand=True)

with progress:
    for n in progress.track(range(100)):
        progress.print(n)
        sleep(0.1)

print(Panel("Hello, [red]World!"))

print("[italic red]Hello[/italic red] World!", locals())

pretty.install()


FORMAT = "%(message)s"
logging.basicConfig(
    level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)

log = logging.getLogger("rich")
log.info("Hello, World!")

try:
    print(1 / 0)
except Exception:
    log.exception("unable print!")

"""
1. Class name Logger
2. static method debug(message: str)
3. static method info(message: str)
4. static method warning(message: str)
5. static method error(message: str)
6. static method critical(message: str)
7. static method exception(message: str)
"""

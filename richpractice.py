import sys
from rich import print
from rich.console import Console
from datetime import datetime

with open("report.txt", "a") as report_file:
    console = Console(file=report_file,record=True)
    console.print([12,24,37])
    console.rule(f"Report Generated {datetime.now().ctime()}")
console.save_html("demo.html")
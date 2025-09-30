from rich import print as rprint
from rich.table import Table
from rich.panel import Panel

# 변수
name = "Alice"
age = 25
score = 95.5
data = {"name": name, "age": age, "score":score}

#1
rprint(f"[bold green]Hello, {name}![/] Your score is [cyan]{score:.2f}[/].")

#2
panel_text = f"""
[bold]Student Indo[/]
 - Name : [yellow]{name}[/]
 - Age  : [magenta]{age}[/]
 - Score: [cyan]{score:.2f}[/]
 """
rprint(Panel(panel_text, title="Profile", border_style="blue"))

#3
table = Table(title="Records")
table.add_column("Key", style="bold")
table.add_column("Value")
for k, v in data.items():
    table.add_row(k, str(v))
rprint(table)

#4
rprint("2025", "09", "23", sep="-", end="✅\n")
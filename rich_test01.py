from rich.console import Console
from rich.table import Table


console = Console()

console.print("[deep_pink] Loading the sell's report")

table = Table(title="[blue_violet]Sell's report[/blue_violet]")

table.add_column("Product")
table.add_column("Value")

table.add_row("[orange_red1]Macbook[/orange_red1]", "$1000")
table.add_row("[orange_red1]Magic Keyboard[/orange_red1]", "$200")
table.add_row("[orange_red1]USB Hub[/orange_red1]", "$15")
table.add_row("[orange_red1]Magic mouse[/orange_red1]", "$100")

console.print(table)

console.print("[bold_green]The pipeline ran successfully[/bold_green]")
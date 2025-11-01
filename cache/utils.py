from rich.console import Console
from rich.table import Table

console = Console()

def print_nodes_table(nodes):
    table = Table(title='NebulaCache Cluster State')
    table.add_column('Node ID', style='cyan')
    table.add_column('Alive', style='magenta')
    table.add_column('Keys', style='green')
    for n in nodes:
        table.add_row(n['id'], '✅' if n['alive'] else '❌', str(n['keys']))
    console.print(table)

def info(msg):
    console.print(f'[bold blue][INFO][/bold blue] {msg}')

def warn(msg):
    console.print(f'[bold yellow][WARN][/bold yellow] {msg}')

def error(msg):
    console.print(f'[bold red][ERR][/bold red] {msg}')

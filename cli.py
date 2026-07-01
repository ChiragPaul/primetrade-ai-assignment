import typer
from typing import Optional
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

from bot.client import get_binance_client
from bot.validators import validate_order_params
from bot.orders import place_futures_order
from bot.logging_config import setup_logger

app = typer.Typer(help="Binance Futures Testnet Trading Bot CLI")
console = Console()
logger = setup_logger()

@app.command()
def place_order(
    symbol: str = typer.Option(..., "--symbol", "-s", help="Trading pair symbol, e.g., BTCUSDT"),
    side: str = typer.Option(..., "--side", help="BUY or SELL"),
    order_type: str = typer.Option(..., "--type", "-t", help="MARKET or LIMIT"),
    quantity: float = typer.Option(..., "--quantity", "-q", help="Order quantity in base asset"),
    price: Optional[float] = typer.Option(None, "--price", "-p", help="Price (Required for LIMIT)")
):
    """
    Place a new order on the Binance Futures Testnet.
    """
    # 1. Validation
    is_valid, err_msg = validate_order_params(symbol, side, order_type, quantity, price)
    if not is_valid:
        console.print(Panel(f"[bold red]Validation Error:[/bold red] {err_msg}", title="Error", border_style="red"))
        raise typer.Exit(code=1)

    # 2. Summary Table
    table = Table(title="Order Request Summary")
    table.add_column("Parameter", style="cyan", no_wrap=True)
    table.add_column("Value", style="magenta")
    
    table.add_row("Symbol", symbol.upper())
    table.add_row("Side", side.upper())
    table.add_row("Order Type", order_type.upper())
    table.add_row("Quantity", str(quantity))
    if price is not None:
        table.add_row("Price", str(price))

    console.print(table)
    
    # 3. Client Initialization & Order Placement
    try:
        with console.status("[bold green]Connecting to Binance Testnet & Placing Order...[/bold green]"):
            client = get_binance_client()
            response, error = place_futures_order(client, symbol, side, order_type, quantity, price)
            
    except Exception as e:
        console.print(Panel(f"[bold red]Initialization Error:[/bold red]\n{str(e)}", title="Failure", border_style="red"))
        raise typer.Exit(code=1)

    # 4. Result Output
    if error:
        console.print(Panel(f"[bold red]Failed to place order:[/bold red]\n{error}", title="Failure", border_style="red"))
        raise typer.Exit(code=1)
    else:
        # Extract useful info for the success panel
        order_id = response.get('orderId', 'N/A')
        status = response.get('status', 'N/A')
        executed_qty = response.get('executedQty', 'N/A')
        avg_price = response.get('avgPrice', 'N/A')
        
        success_msg = (
            f"[bold green]Order Placed Successfully![/bold green]\n\n"
            f"Order ID: [cyan]{order_id}[/cyan]\n"
            f"Status: [cyan]{status}[/cyan]\n"
            f"Executed Qty: [cyan]{executed_qty}[/cyan]\n"
            f"Average Price: [cyan]{avg_price}[/cyan]"
        )
        console.print(Panel(success_msg, title="Success", border_style="green"))

if __name__ == "__main__":
    app()

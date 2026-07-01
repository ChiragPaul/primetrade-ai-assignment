def validate_order_params(symbol: str, side: str, order_type: str, quantity: float, price: float = None):
    """
    Validates the input parameters for placing an order.
    Returns (True, "") if valid, or (False, "error message") if invalid.
    """
    symbol = symbol.upper()
    side = side.upper()
    order_type = order_type.upper()

    if side not in ["BUY", "SELL"]:
        return False, f"Invalid side: '{side}'. Must be BUY or SELL."

    if order_type not in ["MARKET", "LIMIT", "STOP_MARKET"]:
        return False, f"Invalid order type: '{order_type}'. Must be MARKET, LIMIT, or STOP_MARKET."

    if quantity <= 0:
        return False, "Quantity must be greater than 0."

    if order_type == "LIMIT":
        if price is None or price <= 0:
            return False, "Price must be provided and > 0 for LIMIT orders."
            
    if order_type == "STOP_MARKET":
        if price is None or price <= 0:
            return False, "Stop price must be provided and > 0 for STOP_MARKET orders."

    return True, ""

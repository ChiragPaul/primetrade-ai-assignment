from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException
from .logging_config import setup_logger

logger = setup_logger()

def place_futures_order(client: Client, symbol: str, side: str, order_type: str, quantity: float, price: float = None):
    """
    Places an order on Binance Futures.
    Supports MARKET and LIMIT.
    """
    symbol = symbol.upper()
    side = side.upper()
    order_type = order_type.upper()
    
    logger.info(f"Attempting to place {order_type} order for {side} {quantity} {symbol}")
    
    params = {
        'symbol': symbol,
        'side': side,
        'type': order_type,
        'quantity': quantity
    }
    
    if order_type == 'LIMIT':
        params['timeInForce'] = 'GTC'
        params['price'] = price
        
    try:
        logger.debug(f"Order parameters: {params}")
        response = client.futures_create_order(**params)
        logger.info(f"Order placed successfully. Order ID: {response.get('orderId')}")
        logger.debug(f"Full API Response: {response}")
        return response, None
    except BinanceAPIException as e:
        err_msg = f"Binance API Error [{e.status_code}]: {e.message}"
        logger.error(err_msg)
        return None, err_msg
    except BinanceRequestException as e:
        err_msg = f"Network/Request Error: {e}"
        logger.error(err_msg)
        return None, err_msg
    except Exception as e:
        err_msg = f"Unexpected Error: {str(e)}"
        logger.error(err_msg, exc_info=True)
        return None, err_msg

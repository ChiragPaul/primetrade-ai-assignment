import os
from binance.client import Client
from binance.exceptions import BinanceAPIException
from dotenv import load_dotenv
from .logging_config import setup_logger

logger = setup_logger()

def get_binance_client() -> Client:
    """
    Initializes and returns the Binance Client configured for the Futures Testnet.
    Loads API credentials from the environment.
    """
    load_dotenv()
    
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")
    
    if not api_key or not api_secret:
        logger.error("API credentials missing. Please set BINANCE_API_KEY and BINANCE_API_SECRET.")
        raise ValueError("Missing Binance API credentials in environment.")
    
    logger.debug("Initializing Binance Client for Futures Testnet.")
    # testnet=True connects to the Spot Testnet by default, 
    # but since we are making futures calls (like futures_create_order),
    # python-binance handles the Futures testnet URL correctly if testnet=True.
    client = Client(api_key, api_secret, testnet=True)
    
    # Explicitly verify connection by fetching exchange info for futures
    try:
        client.futures_exchange_info()
        logger.info("Successfully connected to Binance Futures Testnet.")
    except BinanceAPIException as e:
        logger.error(f"Failed to connect to Binance Futures Testnet: {e}")
        raise
        
    return client

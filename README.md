# Binance Futures Testnet Trading Bot

A simplified Python application that places orders on the Binance Futures Testnet (USDT-M). It features a clean architecture, comprehensive logging, and an enhanced Command Line Interface (CLI) using `Typer` and `Rich`.

## Features
- **Place Orders**: Supports `MARKET` and `LIMIT` orders.
- **Support Both Sides**: `BUY` (Long) and `SELL` (Short).
- **Validation**: Strict input validation to catch errors before making API requests.
- **Enhanced CLI UX**: Richly formatted tables and panels for clear execution summaries.
- **Robust Logging**: Detailed file logging (`trading_bot.log`) for debugging API responses and errors, while keeping the console output clean.

## Setup Instructions

### 1. Prerequisites
- Python 3.8+
- A Binance Futures Testnet account. 
  - Go to [Binance Futures Testnet](https://testnet.binancefuture.com/) and register.
  - Generate your API Key and API Secret.

### 2. Installation
Clone the repository (or extract the zip) and install the dependencies:

```bash
# Optional: Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configuration
Copy the sample environment file and add your credentials:

```bash
cp .env.example .env
```
Open `.env` and fill in your API keys:
```
BINANCE_API_KEY=your_actual_testnet_api_key
BINANCE_API_SECRET=your_actual_testnet_api_secret
```

## How to Run Examples

Use the `cli.py` entry point. You can run `--help` to see the available options:
```bash
python cli.py --help
```

### Example 1: Place a MARKET Order
Buy 0.01 BTCUSDT at the current market price.
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

### Example 2: Place a LIMIT Order
Sell 0.01 BTCUSDT at a specific limit price (e.g., $70,000).
```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 70000
```



## Assumptions
- You are trading USDT-Margined perpetual contracts (USDT-M).
- The `BINANCE_API_KEY` and `BINANCE_API_SECRET` must specifically belong to the **Testnet**, not the main Binance exchange.
- LIMIT orders are hardcoded to `timeInForce='GTC'` (Good 'Til Canceled) as per common defaults.

## Project Structure
```
trading_bot/
├── bot/
│   ├── __init__.py
│   ├── client.py           # Initializes the Binance Client for Testnet
│   ├── logging_config.py   # Configures rotating logs to file and concise console output
│   ├── orders.py           # Core logic for futures_create_order wrapping
│   └── validators.py       # Input validation for symbol, side, type, quantity, price
├── cli.py                  # CLI application using Typer and Rich
├── .env.example            # Environment variables template
├── requirements.txt        # Project dependencies
└── README.md               # This file
```

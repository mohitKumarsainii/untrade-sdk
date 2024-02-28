#create_order_without_target_stop_loss
from untrade.client import Client
from pprint import pprint

client = Client()

def create_order_without_target_stop_loss():
    try:
        response = client.create_order(
            symbol="BTCUSDT",
            side="BUY",
            type="MARKET",
            market="COIN-M",
            quantity=100,
            leverage=10
        )
        print("Order Created Successfully:")
        pprint(response,sort_dicts = False)

    except Exception as e:
        print(f"Error creating order: {e}")
create_order_without_target_stop_loss()

# Parameters:
# symbol (string): The trading pair symbol (e.g., BTCUSDT, ETHUSDT).
# side (string): 'BUY' or 'SELL'.
# type (string): 'LIMIT' or 'MARKET'.
# market (string): 'SPOT', 'COIN-M', or 'USD-M'.
# quantity (float, optional): Trade quantity.
# leverage (int, optional): Leverage for the trade (for non-SPOT markets).
# target (float, optional): Target price.
# stop_loss (float, optional): Stop loss price.
# price (float, optional): Entry price (for LIMIT orders).
# position (float, optional): Position size.
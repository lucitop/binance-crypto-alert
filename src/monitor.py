import time
from datetime import datetime
from binance.client import Client
from notifications import send_notification

def get_price(client, pair):
    try:
        price_data = client.get_symbol_ticker(symbol=pair)
        return float(price_data['price'])
    except Exception as e:
        print(f"Failed to fetch price for {pair}: {e}")
        return None

def check_price_change(client, pair, initial_price):
    current_price = get_price(client, pair)
    if current_price is None:
        return None, None
    change = (current_price - initial_price) / initial_price * 100
    return current_price, change

def monitor_pairs(client, pb, pairs, threshold, refresh_rate, reset_interval):
    initial_prices = {pair: get_price(client, pair) for pair in pairs}
    
    for pair, initial_price in initial_prices.items():
        if initial_price is None:
            print(f"Failed to get initial price for {pair}. Skipping...")
    
    last_reset_time = time.time()

    while True:
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"\nPC TIME: {current_time}")
        
        if reset_interval is not None and (time.time() - last_reset_time) >= reset_interval * 60:
            initial_prices = {pair: get_price(client, pair) for pair in pairs}
            print("Reset initial prices for all pairs.")
            last_reset_time = time.time()
            print("-" * 60)

        for pair, initial_price in initial_prices.items():
            if initial_price is None:
                continue
            
            try:
                current_price, change = check_price_change(client, pair, initial_price)
                if current_price is not None and abs(change) >= threshold:
                    message = f"The price of {pair} has changed by {change:.2f}%"
                    print(f"Notification sent: Price Alert for {pair} - {message}")
                    send_notification(pb, f"Price Alert for {pair}", message)

                print(f"Checked {pair} - Current price: {current_price} | Change: {change:.2f}%")
                print("-" * 60)

            except Exception as e:
                print(f"Error monitoring {pair}: {e}")

        time.sleep(refresh_rate)

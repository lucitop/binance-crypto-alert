import os
from dotenv import load_dotenv
from binance.client import Client
from pushbullet import Pushbullet
from config import load_crypto_groups
from monitor import monitor_pairs

def main():
    load_dotenv()
    api_key = os.getenv('BINANCE_API_KEY')
    api_secret = os.getenv('BINANCE_API_SECRET')
    pb_token = os.getenv('PUSHBULLET_TOKEN')

    if not api_key or not api_secret or not pb_token:
        print("Error: API keys or Pushbullet token not found in the environment variables.")
        return

    client = Client(api_key, api_secret)
    pb = Pushbullet(pb_token)
    crypto_groups = load_crypto_groups('../data/crypto_groups.json')

    print("Available groups to monitor or enter 'all' to monitor all groups:")
    for group in crypto_groups:
        print(group)

    lower_to_original_group_map = {key.lower(): key for key in crypto_groups}

    while True:
        group_name_to_monitor = input("Enter the group name you want to scan from the list above or 'all': ").strip().lower()

        if group_name_to_monitor == 'all':
            pairs = [pair for group in crypto_groups.values() for pair in group]
            if not pairs:
                print("No pairs found in any group.")
                continue
            break
        elif group_name_to_monitor in lower_to_original_group_map:
            original_group_name = lower_to_original_group_map[group_name_to_monitor]
            pairs = crypto_groups.get(original_group_name, [])
            if not pairs:
                print(f"No pairs found for group: {original_group_name}. Please try again.")
                continue
            break
        else:
            print("Invalid group name. Please enter a correct group name.")

    while True:
        try:
            threshold = float(input("Enter the percentage change threshold for notifications: "))
            break
        except ValueError:
            print("Invalid input for threshold. Please enter a number.")

    while True:
        try:
            refresh_rate = float(input("Enter the refresh rate (in seconds): "))
            break
        except ValueError:
            print("Invalid input for refresh rate. Please enter a number.")

    while True:
        reset_interval_input = input("Enter the interval (in minutes) to reset percentage change, or '0' or nothing to disable: ").strip()
        if reset_interval_input == "" or reset_interval_input == "0":
            reset_interval = None
            break
        else:
            try:
                reset_interval = int(reset_interval_input)
                break
            except ValueError:
                print("Invalid input for reset interval. Please enter a number or '0' to disable.")

    monitor_pairs(client, pb, pairs, threshold, refresh_rate, reset_interval)

if __name__ == "__main__":
    main()

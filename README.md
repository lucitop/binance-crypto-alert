# Binance Crypto Alert (BCA)

**Binance Crypto Alert (BCA)** is a Python-based application that tracks specified cryptocurrencies and sends notifications to your desktop and mobile devices using Pushbullet. You can customize the tracking parameters, including the percentage change threshold and the refresh interval, to receive real-time alerts based on your criteria.

## Features
- **Track Multiple Cryptocurrencies:** Monitor multiple crypto pairs specified by the user.
- **Customizable Alerts:** Set custom thresholds for percentage changes in prices.
- **Real-Time Notifications:** Receive instant alerts on your desktop and mobile devices via Pushbullet.
- **Flexible Refresh Rates:** Users can set how often the prices are refreshed.
- **Reset Interval Option:** Option to reset the percentage change calculations at regular intervals.

## Setup
**API Keys:** Create a .env file in the root directory and add your Binance API and secret keys:
```
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret
PUSHBULLET_API_KEY=your_pushbullet_api_key
```

**Cryptocurrency Groups:** Modify the crypto_groups.json in the data folder to include the cryptocurrencies you want to monitor.

## Usage
**Run the application:**
```
python src/main.py
```

**Follow the prompts:** Enter the group name, percentage change threshold, refresh rate, and reset interval as prompted by the application.

## Contributing
Feel free to fork this project, create a new branch, and submit a pull request.

import requests
from datetime import datetime

def get_price():
    try:
        r = requests.get("https://api.delta.exchange/v2/tickers/ETHUSDT", timeout=10).json()
        return float(r['result']['mark_price'])
    except:
        return 2630.0

price = get_price()
atm = int(round(price/100)*100)
credit = price * 0.011
daily_target = price * 0.0055

print(f"--- AUTO TRADE {datetime.now()} IST ---")
print(f"ETH: ${price}")
print(f"Trade: BUY {atm-250}P + SELL {atm}P + SELL {atm}C + BUY {atm+250}C")
print(f"Credit: ${credit:.2f} | Daily Target: ${daily_target:.2f}")

# Log save karo
with open("eth_paper.csv","a") as f:
    f.write(f"{datetime.now()},{price},{atm},{credit:.2f}\n")

print("✅ Log saved")

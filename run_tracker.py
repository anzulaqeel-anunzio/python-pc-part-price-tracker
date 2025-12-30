# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import json
import csv
import os
from datetime import datetime
from price_tracker.tracker import get_price

PRODUCTS_FILE = "products.json"
OUTPUT_FILE = "price_log.csv"

def main():
    print("Starting PC Part Price Tracker...")
    
    if not os.path.exists(PRODUCTS_FILE):
        print(f"{PRODUCTS_FILE} not found.")
        return

    with open(PRODUCTS_FILE, 'r') as f:
        products = json.load(f)

    results = []
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for product in products:
        price = get_price(product['url'])
        print(f"  {product['name']}: {price}")
        results.append({
            "timestamp": timestamp,
            "name": product['name'],
            "price": price,
            "url": product['url']
        })

    # Append to CSV
    file_exists = os.path.exists(OUTPUT_FILE)
    with open(OUTPUT_FILE, 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["timestamp", "name", "price", "url"])
        if not file_exists:
            writer.writeheader()
        writer.writerows(results)

    print(f"\nLogged check to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

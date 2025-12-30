# PC Part Price Aggregator (Python)

A Python web scraper that tracks prices of PC components from a mock e-commerce site.

> [!NOTE]
> This scraping tool is for educational purposes. To scrape real sites like Amazon or Newegg, you must implement more robust headers, proxies, and respect `robots.txt`.

## Features

-   **Track Products**: Monitor specific URLs for price changes.
-   **CSV Logging**: Append new price checks to a CSV log.
-   **Configurable**: Easily add new products to track via `config.json`.
-   **User-Agent Rotation**: Basic mechanism to simulate different browsers.

## Installation

1.  **Clone the repository**
2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  Add products to `products.json`.
2.  Run the tracker:
    ```bash
    python run_tracker.py
    ```

## Contact

Developed for Anunzio International by Anzul Aqeel.
Contact +971545822608 or +971585515742.

## License

MIT


---
### 🔗 Part of the "Ultimate Utility Toolkit"
This tool is part of the **[Anunzio International Utility Toolkit](https://github.com/anzulaqeel/ultimate-utility-toolkit)**.
Check out the full collection of **180+ developer tools, scripts, and templates** in the master repository.

Developed for Anunzio International by Anzul Aqeel.

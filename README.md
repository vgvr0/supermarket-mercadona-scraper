# Supermarket-Mercadona-Scraper

![Mercadona Cover](LogoMercadona.png)

Supermarket-Mercadona-Scraper is a Python-based web scraper designed to extract and organize product data from the Mercadona supermarket website.

## Features

- Automated browsing through product categories and subcategories.
- Extraction of product details including name, image, and price.
- Utilizes Selenium WebDriver for dynamic page interaction.

## Usage

The main script is contained in the file `scraper.py`. Here's a basic usage example:

```python
from scraper import Driver
from datetime import datetime
import time
import random
from bs4 import BeautifulSoup

# Initialize the driver
driver = Driver(
    browser="chrome",
    uc=True,
    headless2=False,
    incognito=False,
    agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    do_not_track=True,
    undetectable=True
)
```


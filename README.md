# Supermarket-Mercadona-Scraper

![Mercadona Cover](LogoMercadona.png)

Supermarket-Mercadona-Scraper is a Python-based web scraper designed to extract and organize product data from the Mercadona supermarket website.

![OS](https://img.shields.io/badge/os-linux%20%7C%20macOS%20%7C%20windows-blue&logoColor=white)

![Regex](https://img.shields.io/badge/regex-007ACC?style=for-the-badge&logo=regex&logoColor=white)
![CSV](https://img.shields.io/badge/CSV-FFB13B?style=for-the-badge&logo=csv&logoColor=white)
![Time](https://img.shields.io/badge/Time-007ACC?style=for-the-badge&logo=clock&logoColor=white)
![Random](https://img.shields.io/badge/Random-007ACC?style=for-the-badge&logo=dice&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Keyboard](https://img.shields.io/badge/Keyboard-007ACC?style=for-the-badge&logo=keyboard&logoColor=white)
![Funciones Aux](https://img.shields.io/badge/Funciones%20Aux-007ACC?style=for-the-badge&logo=code&logoColor=white)
![Datetime](https://img.shields.io/badge/Datetime-007ACC?style=for-the-badge&logo=calendar&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4B8BBE?style=for-the-badge&logo=beautifulsoup&logoColor=white)
![SeleniumBase](https://img.shields.io/badge/SeleniumBase-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)

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


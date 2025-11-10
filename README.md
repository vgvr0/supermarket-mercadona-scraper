# Supermarket-Mercadona-Scraper

![Mercadona Cover](LogoMercadona.png)

Supermarket-Mercadona-Scraper is a Python-based web scraper designed to extract and organize product data from the Mercadona supermarket website. This tool automatically navigates through all product categories and subcategories, extracting comprehensive product information and saving it to CSV format.

![OS](https://img.shields.io/badge/os-linux%20%7C%20macOS%20%7C%20windows-blue&logoColor=white)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![SeleniumBase](https://img.shields.io/badge/SeleniumBase-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4B8BBE?style=for-the-badge&logo=beautifulsoup&logoColor=white)

## ✨ Features

- **🔄 Automated Category Navigation**: Systematically browses through all Mercadona product categories and subcategories
- **📊 Comprehensive Data Extraction**: Captures product name, price, image URL, and category information
- **🛡️ Anti-Detection Technology**: Uses undetectable Chrome driver to avoid bot detection
- **📍 Postal Code Support**: Handles location-based pricing and availability
- **💾 CSV Export**: Automatically saves data with timestamped filenames
- **⚡ Robust Error Handling**: Graceful handling of connection issues and page load problems
- **🎯 Smart Element Waiting**: Intelligent waiting for dynamic content to load
- **🔀 Random Delays**: Implements human-like browsing patterns to avoid detection

## 🚀 Recent Improvements (v2024.11)

- ✅ **Updated Dependencies**: Migrated to latest SeleniumBase for better stability
- ✅ **Enhanced Anti-Detection**: Improved undetectable browsing capabilities
- ✅ **Better Error Handling**: More robust exception handling and recovery mechanisms
- ✅ **Optimized Performance**: Reduced unnecessary waits and improved scraping speed
- ✅ **Code Documentation**: Added comprehensive comments and docstrings
- ✅ **Modular Architecture**: Separated auxiliary functions for better maintainability
- ✅ **Cross-Platform Compatibility**: Tested on Windows, macOS, and Linux

## 📋 Requirements

- Python 3.8 or higher
- Chrome/Chromium browser
- Active internet connection

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/[username]/supermarket-mercadona-scraper.git
   cd supermarket-mercadona-scraper
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   pip install seleniumbase
   ```

   > **Note**: The Chrome driver will be automatically downloaded on first run.

## 🎯 Quick Start

1. **Run the scraper:**
   ```bash
   python scraper.py
   ```

2. **Enter your postal code when prompted:**
   ```
   Introduce tu código postal (ej: 28001): 28001
   ```

3. **Wait for the scraping to complete**. The script will:
   - Open Chrome browser
   - Navigate to Mercadona website
   - Accept cookies and enter postal code
   - Systematically scrape all categories
   - Save results to `mercadona_YYYY-MM-DD.csv`

## 📁 Output Format

The scraper generates a CSV file with the following columns:

| Column | Description | Example |
|--------|-------------|---------|
| `titulo` | Product name | "Leche Entera Hacendado" |
| `imagen` | Product image URL | "https://..." |
| `precio` | Product price (€) | "1.25" |
| `categoria` | Product category | "Lácteos y Huevos" |

## 🔧 Configuration

### Driver Settings
The scraper uses optimized browser settings for reliability:

```python
driver = Driver(
    browser="chrome",           # Uses Chrome browser
    uc=True,                   # Undetectable Chrome mode
    headless2=False,           # Visible browser (set True for headless)
    incognito=False,           # Regular browsing mode
    agent='Mozilla/5.0...',    # Custom user agent
    do_not_track=True,         # Privacy protection
    undetectable=True          # Advanced bot detection evasion
)
```

### Customization Options
- **Headless Mode**: Set `headless2=True` for background execution
- **Custom Delays**: Modify `time.sleep()` values for different timing
- **Output Format**: Customize the `mercadona_csv()` function for different formats

## 🏗️ Project Structure

```
supermarket-mercadona-scraper/
├── scraper.py              # Main scraping script
├── funcionesAux.py         # Auxiliary functions for element handling
├── requirements.txt        # Python dependencies
├── README.md              # This documentation
└── mercadona_YYYY-MM-DD.csv # Generated output files
```

## 🐛 Troubleshooting

### Common Issues

**Chrome Driver Issues:**
- The driver downloads automatically on first run
- Ensure Chrome browser is installed and updated

**Connection Timeouts:**
- Check your internet connection
- Mercadona website might be temporarily unavailable

**Postal Code Errors:**
- Use valid Spanish postal codes (5 digits)
- Some areas might not have Mercadona delivery

**Bot Detection:**
- The script includes anti-detection measures
- If blocked, wait some time before retrying

## 🤝 Contributing

Contributions are welcome! Please feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## ⚖️ Legal Notice

This tool is for educational and research purposes only. Please:
- Respect Mercadona's terms of service
- Use responsibly and avoid overloading their servers
- Consider the legal implications in your jurisdiction

## 📞 Support

If you encounter any issues or have questions:
1. Check the troubleshooting section
2. Review existing issues in the repository
3. Create a new issue with detailed information

---

**⭐ If this project helped you, please give it a star!**


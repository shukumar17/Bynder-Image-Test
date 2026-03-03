# Image Scraper - Usage Guide

## ✅ WebDriver Issue - RESOLVED

The **WinError 193** issue has been successfully fixed! The problem was caused by corrupted ChromeDriver cache files. The script now automatically clears the cache before initializing the WebDriver.

---

## 🚀 How to Run the Script

### Method 1: Interactive Mode (Recommended for Beginners)

1. **Activate Virtual Environment** (if not already activated):
   ```powershell
   .venv\Scripts\Activate.ps1
   ```

2. **Run the Script**:
   ```powershell
   python image_scraper.py
   ```

3. **Enter URLs** when prompted:
   ```
   Enter URL(s) separated by commas (or press Enter to use example): https://example.com, https://another-site.com
   ```

4. **Check Results**:
   - Excel file: `Bynder.xlsx`
   - Screenshots folder: `screenshots/`

---

### Method 2: Programmatic Usage

Edit the `main()` function in `image_scraper.py`:

```python
def main() -> None:
    """Main entry point for the script."""
    # Your URLs here
    urls = [
        "https://dev.marcjacobs.com",
        "https://www.example.com",
        # Add more URLs as needed
    ]
    
    # Create scraper and run
    scraper = ImageScraper(output_file="Bynder.xlsx")
    scraper.run(urls)
```

Then run:
```powershell
.venv\Scripts\Activate.ps1
python image_scraper.py
```

---

## 📋 What the Script Does

1. **Fetches Web Pages**: Visits each URL you provide
2. **Extracts Image Links**: Finds all `<img>` tags and video poster images
3. **Takes Screenshots**: Captures a screenshot of each image URL
4. **Creates Excel Report**: Generates `Bynder.xlsx` with:
   - Column A: Image URL
   - Column B: Screenshot thumbnail
   - Column C: Status (Pass/Fail)

---

## 🔧 Troubleshooting

### If WebDriver Issues Return:

1. **Clear Cache Manually**:
   ```powershell
   Remove-Item -Recurse -Force $env:USERPROFILE\.wdm
   Remove-Item -Recurse -Force $env:USERPROFILE\.cache\selenium
   ```

2. **Reinstall Packages**:
   ```powershell
   .venv\Scripts\Activate.ps1
   pip uninstall -y selenium webdriver-manager
   pip install selenium webdriver-manager
   ```

3. **Verify Chrome Installation**:
   - Ensure Google Chrome is installed and updated
   - Check Chrome version: `chrome://version/`

4. **Check Python Architecture**:
   ```powershell
   python -c "import platform; print(platform.architecture())"
   ```
   Should show: `('64bit', 'WindowsPE')`

### Common Errors:

- **"No images found"**: The URL may not contain any `<img>` tags or may require authentication
- **Screenshot fails**: The image URL may be blocked or require special headers
- **Timeout errors**: Increase timeout in `_initialize_driver()` method

---

## 📦 Dependencies

All required packages are in `requirements.txt`:
- `selenium` - Browser automation
- `webdriver-manager` - Automatic ChromeDriver management
- `beautifulsoup4` - HTML parsing
- `requests` - HTTP requests
- `openpyxl` - Excel file creation
- `Pillow` - Image processing

---

## 🎯 Example Output

**Bynder.xlsx Structure:**

| Image URL | Screenshot | Status |
|-----------|------------|--------|
| https://example.com/img1.jpg | [thumbnail] | Pass |
| https://example.com/img2.png | [thumbnail] | Pass |
| https://example.com/img3.gif | [thumbnail] | Fail |

**Screenshots Folder:**
```
screenshots/
├── screenshot_1.png
├── screenshot_1_thumb.png
├── screenshot_2.png
├── screenshot_2_thumb.png
└── ...
```

---

## 💡 Tips

1. **Multiple URLs**: Separate URLs with commas when entering interactively
2. **Headless Mode**: Script runs in headless mode (no browser window) by default
3. **Custom Excel Name**: Change `output_file` parameter in `ImageScraper()` constructor
4. **Screenshot Quality**: Modify thumbnail size in `create_excel_report()` method

---

## 🆘 Need Help?

If you encounter any issues:

1. Check the console output for error messages
2. Review the log messages (they show what's happening)
3. Verify all URLs are valid and accessible
4. Ensure you have internet connection
5. Run the `fix_webdriver.py` script if WebDriver issues persist

---

## ✨ Features

- ✅ Automatic ChromeDriver management
- ✅ Cache clearing to prevent corruption
- ✅ Headless browser operation
- ✅ Screenshot validation
- ✅ Excel report with embedded images
- ✅ Comprehensive error handling
- ✅ Detailed logging
- ✅ Support for relative and absolute URLs
- ✅ Video poster image detection

---

**Happy Scraping! 🎉**
# Image Scraper and Screenshot Validator

A Python-based automation tool that scrapes image URLs from web pages, validates them by taking screenshots, and generates Excel reports with the results.

## 🚀 Quick Start for Teammates

### Prerequisites
1. **Python 3.8 or higher** - [Download Python](https://www.python.org/downloads/)
2. **Google Chrome browser** - [Download Chrome](https://www.google.com/chrome/)
3. **Git** (optional, for cloning) - [Download Git](https://git-scm.com/downloads/)

### Installation Steps

#### Option 1: Using Git (Recommended)
```bash
# Clone the repository
git clone <repository-url>
cd image-scraper

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### Option 2: Manual Download
1. Download the project as a ZIP file
2. Extract to your desired location
3. Open terminal/command prompt in the extracted folder
4. Run the following commands:
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate virtual environment
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   
   # Install dependencies
   pip install -r requirements.txt
   ```

### Running the Tool

```bash
# Make sure virtual environment is activated
python image_scraper.py
```

## 📋 Features

- ✅ **Universal URL Support**: Works with any website - not limited to specific sites
- ✅ **Interactive Authentication**: Prompts user if URLs are password-protected and collects credentials
- ✅ **HTTP Basic Authentication**: Supports password-protected websites with username/password
- ✅ **Parallel Processing**: Uses 10 workers for faster screenshot capture
- ✅ **Organized Output**: Creates a `Tests` folder with subfolders for each page
- ✅ Scrapes image URLs from:
  - `<picture>` tags (including `<source>` and nested `<img>` tags)
  - Elements with class `tile-swatches`
  - Elements with class `nosto-container`
  - Handles `srcset` attributes with multiple image URLs
- ✅ **HTTPS-only filtering**: Automatically filters out non-HTTPS URLs
- ✅ **Amplience detection**: Fails images containing 'amplience' in URL
- ✅ **Screenshots for Failed Cases Only**: Saves time and storage
- ✅ Generates **separate Pass and Fail Excel reports** for each page URL with:
  - Page URL
  - Image URLs
  - Screenshot thumbnails (200x200px) for failed cases
  - Failure reasons (for failed scenarios)
- ✅ **Smart validation**: Detects error messages like "No results for url found" and "Bad Request"
- ✅ **Automatic cleanup**: Deletes screenshots folder after saving to Excel
- ✅ Handles errors gracefully with comprehensive logging
- ✅ Follows Python best practices and security guidelines

## 📖 How to Use This Tool

### Step-by-Step Guide

1. **Start the Tool**
   ```bash
   python image_scraper.py
   ```

2. **Enter Page URLs**
   - You can enter one or multiple URLs separated by commas
   - Example: `https://example.com, https://another-site.com`

3. **Authentication (if needed)**
   - The tool will ask: "Is the URL password protected? (yes/no)"
   - If yes, enter your username and password when prompted
   - If no, just press Enter or type 'no'

4. **Provide Folder Names**
   - For each page URL, you'll be asked to provide a base filename
   - This will create a folder inside the `Tests` directory
   - Example: If you enter "ProductPage", it will create:
     - `Tests/ProductPage/ProductPage_Pass.xlsx`
     - `Tests/ProductPage/ProductPage_Fail.xlsx`

5. **Wait for Processing**
   - The tool uses 10 parallel workers for faster processing
   - You'll see progress updates in the console
   - Screenshots are captured ONLY for failed cases

6. **Check Results**
   - Navigate to the `Tests` folder
   - Open the subfolders to find your Excel reports
   - **Pass Excel**: Contains all successfully validated images
   - **Fail Excel**: Contains failed images with screenshots and failure reasons

## 💡 Usage Examples

### Example 1: Single Page Without Authentication

```
$ python image_scraper.py

Enter page URL(s) separated by commas: https://example.com
Is the URL password protected? (yes/no): no

Processing Page 1/1: https://example.com
Enter base filename for this page (press Enter for 'Bynder_Page_1'): ExampleSite

Processing 45 images in parallel with 10 workers...
Progress: 45/45 screenshots completed
✓ Pass scenarios saved to: Tests/ExampleSite/ExampleSite_Pass.xlsx
✓ Fail scenarios saved to: Tests/ExampleSite/ExampleSite_Fail.xlsx
```

### Example 2: Multiple Pages With Authentication

```
$ python image_scraper.py

Enter page URL(s) separated by commas: https://site1.com, https://site2.com
Is the URL password protected? (yes/no): yes

Please enter authentication credentials:
Username: myuser
Password: ********
✓ Authentication credentials set for user: myuser

Processing Page 1/2: https://site1.com
Enter base filename for this page (press Enter for 'Bynder_Page_1'): Site1_Test

Processing Page 2/2: https://site2.com
Enter base filename for this page (press Enter for 'Bynder_Page_2'): Site2_Test
```

### Programmatic Usage

You can also use the `ImageScraper` class in your own code:

```python
from image_scraper import ImageScraper

# Without authentication
scraper = ImageScraper()

# With authentication
scraper = ImageScraper(username="myuser", password="mypass")

# Process URLs (creates separate Pass/Fail Excel files for each page)
urls = [
    "https://example.com",
    "https://another-site.com"
]

scraper.run_with_page_wise_excel(urls)
```

**Authentication Options:**

1. **Interactive prompts** (default when running `python image_scraper.py`)
2. **Programmatic credentials** (pass to `ImageScraper` constructor)
3. **Config file fallback** (optional `config.py` with `AUTH_CONFIG` dictionary)

## 📁 Output Structure

The tool creates a well-organized folder structure:

```
project-root/
├── Tests/                          # Main test results folder
│   ├── ProductPage/               # Folder for first page
│   │   ├── ProductPage_Pass.xlsx  # Passed validations
│   │   └── ProductPage_Fail.xlsx  # Failed validations
│   ├── HomePage/                  # Folder for second page
│   │   ├── HomePage_Pass.xlsx
│   │   └── HomePage_Fail.xlsx
│   └── ...
├── image_scraper.py
├── requirements.txt
└── README.md
```

### Excel Report Structure

#### Pass Scenarios Excel (`{filename}_Pass.xlsx`)
| Column | Content | Description |
|--------|---------|-------------|
| A | Page URL | The URL of the page being tested |
| B | Image URL | The URL of the validated image |
| C | Screenshot | Empty (no screenshots for passed cases) |
| D | Failure Reason | Empty (passed validation) |

#### Fail Scenarios Excel (`{filename}_Fail.xlsx`)
| Column | Content | Description |
|--------|---------|-------------|
| A | Page URL | The URL of the page being tested |
| B | Image URL | The URL of the failed image |
| C | Screenshot | 200x200px thumbnail of the failed image |
| D | Failure Reason | Detailed error message (e.g., "Amplience found in URL", "Bad Request") |

### Temporary Files
- **Screenshots Folder**: Created during processing, automatically deleted after saving to Excel
- **Thumbnail Images**: Resized versions embedded in Excel, cleaned up after processing

## How It Works

1. **Interactive Input**: Prompts user for URLs and authentication credentials
2. **URL Validation**: Validates input URLs to ensure they're properly formatted
3. **Authentication Setup**: Configures HTTP Basic Authentication if credentials provided
4. **Page Scraping**: Uses BeautifulSoup with authentication to parse HTML and extract image URLs from:
   - `<picture>` tags and nested elements
   - Elements with class `tile-swatches`
   - Elements with class `nosto-container`
5. **HTTPS Filtering**: Filters out non-HTTPS URLs automatically
6. **URL Normalization**: Converts relative URLs to absolute URLs
7. **Screenshot Capture**: Uses Selenium WebDriver to navigate to each image and capture screenshots
8. **Smart Validation**: 
   - Checks for "Amplience" in URLs (auto-fail)
   - Detects error messages: "No results for url found", "Bad Request"
   - Verifies screenshot file creation and size
9. **Separate Excel Reports**: Creates Pass and Fail Excel files for each page URL
10. **Automatic Cleanup**: Deletes screenshots folder after saving to Excel

## Error Handling & Validation

### Automatic Failure Detection
- **Non-HTTPS URLs**: Automatically filtered out before processing
- **Amplience URLs**: Any URL containing "amplience" is marked as Fail
- **Error Messages**: Detects and fails on:
  - "No results for url found: consider case sensitivity"
  - "Bad Request" responses
  - 404 or "not found" errors
- **No Images Found**: Pages with zero images are logged as failures

### Error Handling
- Invalid URLs are logged and skipped
- Network errors are caught and logged with details
- Failed screenshots are separated into Fail Excel file with reasons
- WebDriver errors are handled gracefully with troubleshooting tips
- All errors are logged with timestamps and context
- Empty credentials are detected and handled (proceeds without auth)

## Security Features

- **No hardcoded credentials**: All credentials are provided interactively or programmatically
- **HTTP Basic Authentication**: Secure credential handling for protected sites
- **Credential embedding**: Safely embeds credentials in URLs for Selenium WebDriver
- **Input validation**: Validates all URLs before processing
- **Safe HTML parsing**: Uses BeautifulSoup for secure HTML parsing
- **Timeout protection**: Network requests have configurable timeouts
- **Resource cleanup**: Automatic cleanup of WebDriver and temporary files
- **Comprehensive error handling**: All exceptions caught and logged
- **Optional config file**: Supports `config.py` as fallback (not required)

## Logging

The script provides detailed logging:
- INFO: Progress updates and successful operations
- WARNING: Non-critical issues (e.g., no images found)
- ERROR: Critical errors with context

Logs are displayed in the console with timestamps.

## 🔧 Troubleshooting

### Common Issues and Solutions

#### 1. Chrome Driver Issues

**Problem**: "ChromeDriver not found" or version mismatch errors

**Solutions**:
- Ensure Google Chrome browser is installed and up to date
- The script automatically downloads the correct ChromeDriver version
- If issues persist, try:
  ```bash
  # On Windows PowerShell (run as Administrator)
  Remove-Item -Recurse -Force $env:USERPROFILE\.wdm
  Remove-Item -Recurse -Force $env:USERPROFILE\.cache\selenium
  
  # Then reinstall packages
  pip uninstall selenium webdriver-manager -y
  pip install selenium webdriver-manager
  ```

#### 2. Virtual Environment Issues

**Problem**: "pip: command not found" or packages not installing

**Solutions**:
- Make sure virtual environment is activated (you should see `(venv)` in your terminal)
- On Windows: `venv\Scripts\activate`
- On macOS/Linux: `source venv/bin/activate`
- If still not working, try: `python -m pip install -r requirements.txt`

#### 3. Memory Issues

**Problem**: System slowing down or running out of memory

**Solutions**:
- The tool uses 10 parallel workers by default (optimized for performance)
- For very large numbers of images (500+), process URLs one at a time
- Screenshots are resized to 200x200px thumbnails to save memory
- Temporary screenshots are automatically cleaned up

#### 4. Network Errors

**Problem**: Timeout errors or connection failures

**Solutions**:
- Ensure stable internet connection
- Some websites may block automated requests - try with authentication
- Check if the website is accessible in your regular browser
- The script includes proper User-Agent headers for compatibility

#### 5. Permission Errors

**Problem**: "Permission denied" when creating folders or files

**Solutions**:
- Run terminal/command prompt as Administrator (Windows) or use `sudo` (macOS/Linux)
- Ensure you have write permissions in the project directory
- Check if antivirus software is blocking file creation

### Getting Help

If you encounter issues not covered here:
1. Check the console logs for detailed error messages
2. Ensure all prerequisites are installed correctly
3. Try running with a simple test URL first
4. Contact the tool maintainer with:
   - Error message from console
   - Operating system and Python version
   - Steps to reproduce the issue

## Customization

You can customize various parameters:

```python
# Provide authentication credentials programmatically
scraper = ImageScraper(username="myuser", password="mypass")

# Modify screenshot directory (in the class)
self.screenshot_dir = "my_screenshots"

# Adjust timeouts (create config.py file)
REQUEST_TIMEOUT = 60  # HTTP request timeout in seconds
PAGE_LOAD_TIMEOUT = 60  # Selenium page load timeout

# Change screenshot size (in create_excel_report_for_page method)
img.thumbnail((300, 300))  # 300x300px thumbnails

# Modify row height for Excel images
ws.row_dimensions[row].height = 200  # Adjust height
```

### Optional Config File

Create `config.py` for default settings (optional):

```python
# config.py
AUTH_CONFIG = {
    'username': 'default_user',
    'password': 'default_pass'
}
REQUEST_TIMEOUT = 30
PAGE_LOAD_TIMEOUT = 30
```

**Note**: Interactive credentials override config file settings.

## Dependencies

- **requests**: HTTP library for fetching web pages
- **beautifulsoup4**: HTML parsing and scraping
- **selenium**: Browser automation for screenshots
- **openpyxl**: Excel file creation and manipulation
- **Pillow**: Image processing and resizing
- **webdriver-manager**: Automatic WebDriver management

## License

This project is provided as-is for educational and practical purposes.

## Contributing

Feel free to enhance this project by:
- Adding support for more image sources (e.g., CSS backgrounds)
- Implementing parallel processing for faster execution
- Adding support for authentication-required pages
- Creating a GUI interface
- Adding export to other formats (CSV, JSON, etc.)

## Author

Created as a mini project for web scraping and automation tasks.
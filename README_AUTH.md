# Authentication Configuration Guide

## Overview
The Image Scraper now supports HTTP Basic Authentication for accessing protected URLs. This allows you to scrape images from password-protected websites.

## Configuration Setup

### 1. Using config.py (Recommended)

The scraper automatically loads credentials from `config.py`. This file has been created with the following structure:

```python
AUTH_CONFIG = {
    'username': 'storefront',
    'password': '72MarcJacobs'
}
```

**To update credentials:**
1. Open `config.py` in your editor
2. Modify the `username` and `password` values
3. Save the file
4. Run the scraper normally

### 2. Using Command-Line Arguments (Alternative)

You can also pass credentials programmatically:

```python
from image_scraper import ImageScraper

scraper = ImageScraper(
    output_file="Bynder.xlsx",
    username="your_username",
    password="your_password"
)
scraper.run(urls)
```

## How Authentication Works

### HTTP Basic Authentication
The scraper uses HTTP Basic Authentication for:
- **Page scraping**: When fetching HTML content with `requests` library
- **Screenshot capture**: When navigating to image URLs with Selenium

### URL Format
For protected sites, you can provide URLs in two formats:

1. **Standard format** (credentials from config.py):
   ```
   https://dev.marcjacobs.com/us-en/home
   ```

2. **URL with embedded credentials** (alternative):
   ```
   https://username:password@dev.marcjacobs.com/us-en/home
   ```

## Security Best Practices

### 1. Keep config.py Private
- **Never commit** `config.py` to version control
- Add it to `.gitignore`:
  ```
  config.py
  ```

### 2. Use Environment Variables (Advanced)
For production environments, consider using environment variables:

```python
import os

AUTH_CONFIG = {
    'username': os.getenv('SCRAPER_USERNAME', 'default_user'),
    'password': os.getenv('SCRAPER_PASSWORD', 'default_pass')
}
```

Then set environment variables:
```powershell
# Windows PowerShell
$env:SCRAPER_USERNAME="your_username"
$env:SCRAPER_PASSWORD="your_password"
```

### 3. Encrypt Sensitive Data
For enhanced security, consider encrypting credentials using libraries like `cryptography`.

## Usage Examples

### Example 1: Basic Usage with config.py
```bash
python image_scraper.py
```
Enter URL when prompted:
```
https://dev.marcjacobs.com/us-en/home
```

### Example 2: Multiple Protected URLs
```bash
python image_scraper.py
```
Enter URLs separated by commas:
```
https://dev.marcjacobs.com/us-en/home, https://dev.marcjacobs.com/us-en/products
```

### Example 3: Programmatic Usage
```python
from image_scraper import ImageScraper

urls = [
    "https://dev.marcjacobs.com/us-en/home",
    "https://dev.marcjacobs.com/us-en/products"
]

scraper = ImageScraper(output_file="Bynder.xlsx")
scraper.run(urls)
```

## Troubleshooting

### Authentication Failures

**Problem**: 401 Unauthorized error
- **Solution**: Verify credentials in `config.py` are correct
- Check if the username/password have special characters that need URL encoding

**Problem**: 403 Forbidden error
- **Solution**: The credentials may be correct, but you don't have permission to access the resource
- Contact the site administrator for proper access rights

**Problem**: Screenshots show login page instead of images
- **Solution**: The site may use form-based authentication instead of HTTP Basic Auth
- You may need to implement custom login logic using Selenium

### Logging
The scraper logs authentication status:
```
2024-03-02 10:15:30,123 - INFO - Authentication enabled for user: storefront
2024-03-02 10:15:31,456 - INFO - Using HTTP Basic Authentication for: dev.marcjacobs.com
```

Check logs to verify authentication is being applied correctly.

## Configuration File Reference

### config.py Structure
```python
# Authentication Configuration
AUTH_CONFIG = {
    'username': 'your_username',
    'password': 'your_password',
}

# Timeout settings
REQUEST_TIMEOUT = 30  # seconds for HTTP requests
PAGE_LOAD_TIMEOUT = 30  # seconds for Selenium page loads
```

### Optional: Site-Specific Credentials
You can extend `config.py` to support multiple sites:

```python
AUTH_CONFIG = {
    'username': 'default_user',
    'password': 'default_pass',
    'site_credentials': {
        'dev.marcjacobs.com': {
            'username': 'storefront',
            'password': '72MarcJacobs'
        },
        'other-site.com': {
            'username': 'other_user',
            'password': 'other_pass'
        }
    }
}
```

## Support

For issues or questions:
1. Check the logs for detailed error messages
2. Verify your credentials are correct
3. Ensure the target site uses HTTP Basic Authentication
4. Review the troubleshooting section above

## Notes

- The scraper automatically detects if credentials are provided and applies them
- If no credentials are configured, the scraper works normally for public URLs
- Authentication is applied to both page scraping and screenshot capture
- Credentials are embedded in URLs for Selenium to handle authentication dialogs

"""WebDriver Troubleshooting and Fix Script

This script helps diagnose and fix common WebDriver issues on Windows.
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path


def print_section(title):
    """Print a formatted section header."""
    print("\n" + "="*60)
    print(f"  {title}")
    print("="*60 + "\n")


def check_python_architecture():
    """Check if Python is 32-bit or 64-bit."""
    print_section("Python Architecture Check")
    
    import platform
    arch = platform.architecture()[0]
    python_version = sys.version
    
    print(f"Python Version: {python_version}")
    print(f"Architecture: {arch}")
    
    if arch == "32bit":
        print("\n⚠️  WARNING: You're using 32-bit Python!")
        print("   This may cause compatibility issues with ChromeDriver.")
        print("   Consider installing 64-bit Python for better compatibility.")
        return False
    else:
        print("\n✓ Using 64-bit Python (Recommended)")
        return True


def check_chrome_installation():
    """Check if Google Chrome is installed."""
    print_section("Google Chrome Check")
    
    chrome_paths = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    ]
    
    for path in chrome_paths:
        if os.path.exists(path):
            print(f"✓ Chrome found at: {path}")
            try:
                # Try to get Chrome version
                result = subprocess.run(
                    [path, "--version"],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                if result.stdout:
                    print(f"  Version: {result.stdout.strip()}")
            except Exception as e:
                print(f"  Could not determine version: {e}")
            return True
    
    print("✗ Google Chrome not found!")
    print("  Please install Google Chrome from: https://www.google.com/chrome/")
    return False


def clear_webdriver_cache():
    """Clear the webdriver-manager cache."""
    print_section("Clearing WebDriver Cache")
    
    cache_paths = [
        Path.home() / ".wdm",
        Path.home() / ".cache" / "selenium",
    ]
    
    for cache_path in cache_paths:
        if cache_path.exists():
            try:
                shutil.rmtree(cache_path)
                print(f"✓ Cleared cache: {cache_path}")
            except Exception as e:
                print(f"✗ Failed to clear {cache_path}: {e}")
        else:
            print(f"  Cache not found: {cache_path}")


def reinstall_packages():
    """Reinstall selenium and webdriver-manager."""
    print_section("Reinstalling Packages")
    
    print("Uninstalling old packages...")
    try:
        subprocess.run(
            [sys.executable, "-m", "pip", "uninstall", "-y", "selenium", "webdriver-manager"],
            check=True
        )
        print("✓ Old packages uninstalled")
    except subprocess.CalledProcessError as e:
        print(f"✗ Uninstall failed: {e}")
        return False
    
    print("\nInstalling fresh packages...")
    try:
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "--upgrade", "selenium", "webdriver-manager"],
            check=True
        )
        print("✓ Packages installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Installation failed: {e}")
        return False


def test_webdriver():
    """Test WebDriver initialization."""
    print_section("Testing WebDriver")
    
    try:
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.chrome.options import Options
        from webdriver_manager.chrome import ChromeDriverManager
        
        print("Initializing ChromeDriver...")
        
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        
        driver_path = ChromeDriverManager().install()
        print(f"ChromeDriver installed at: {driver_path}")
        
        service = Service(driver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        print("✓ WebDriver initialized successfully!")
        
        # Test navigation
        driver.get("https://www.google.com")
        print(f"✓ Successfully navigated to: {driver.current_url}")
        
        driver.quit()
        print("✓ WebDriver test completed successfully!")
        return True
        
    except Exception as e:
        print(f"✗ WebDriver test failed: {e}")
        return False


def main():
    """Main execution function."""
    print("\n" + "#"*60)
    print("#  WebDriver Troubleshooting and Fix Script")
    print("#"*60)
    
    # Run diagnostics
    python_ok = check_python_architecture()
    chrome_ok = check_chrome_installation()
    
    if not chrome_ok:
        print("\n⚠️  Please install Google Chrome before proceeding.")
        return
    
    # Ask user if they want to proceed with fixes
    print_section("Recommended Actions")
    print("This script will:")
    print("  1. Clear WebDriver cache")
    print("  2. Reinstall selenium and webdriver-manager")
    print("  3. Test WebDriver initialization")
    
    response = input("\nProceed with fixes? (yes/no): ").strip().lower()
    
    if response not in ['yes', 'y']:
        print("\nExiting without making changes.")
        return
    
    # Apply fixes
    clear_webdriver_cache()
    
    if reinstall_packages():
        test_webdriver()
    
    print_section("Summary")
    print("If the test was successful, you can now run your image_scraper.py")
    print("If issues persist, please check:")
    print("  - Windows Defender or antivirus blocking ChromeDriver")
    print("  - Firewall settings")
    print("  - User permissions for the .wdm cache directory")
    print("\n" + "#"*60 + "\n")


if __name__ == "__main__":
    main()

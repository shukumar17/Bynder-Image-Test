# Image Scraper Tool - Team Guide

## What Does This Tool Do?

This tool helps us **test images on websites**. It:
1. Visits any web page you give it
2. Finds all the images on that page
3. Checks if each image works properly
4. Creates an Excel report showing:
   - ✅ Which images **passed** (working fine)
   - ❌ Which images **failed** (broken or from Amplience)
   - Screenshots of failed images
   - Reasons why images failed

### Why Do We Need This?

Instead of manually checking hundreds of images on a website, this tool does it automatically in minutes!

---

## How to Set Up the Tool on Your Computer

### Step 1: Check What You Need

Before starting, make sure you have:
- ✅ **Python 3.8 or newer** installed ([Download here](https://www.python.org/downloads/))
- ✅ **Google Chrome browser** ([Download here](https://www.google.com/chrome/))
- ✅ **Git** (optional, for downloading) ([Download here](https://git-scm.com/downloads/))

### Step 2: Download the Tool

**Option A: Using Git (Recommended)**
```bash
# Open your terminal/command prompt and run:
git clone https://github.com/shukumar17/Bynder-Image-Test.git
cd Bynder-Image-Test
```

**Option B: Manual Download**
1. Go to: https://github.com/shukumar17/Bynder-Image-Test
2. Click the green "Code" button
3. Click "Download ZIP"
4. Unzip the file to a folder on your computer
5. Open terminal/command prompt in that folder

### Step 3: Set Up Python Environment

```bash
# Create a virtual environment
python -m venv venv

# Activate it:
# On Windows:
venv\Scripts\activate

# On Mac/Linux:
source venv/bin/activate

# You should see (venv) appear in your terminal
```

### Step 4: Install Required Packages

```bash
pip install -r requirements.txt
```

**That's it! You're ready to use the tool.**

---

## How to Run the Tool

### Quick Start

1. **Open your terminal/command prompt**
2. **Navigate to the project folder**
3. **Make sure your virtual environment is active** (you should see `(venv)` in the terminal)
4. **Run the tool:**

```bash
python image_scraper.py
```

### What Happens Next?

The tool will ask you some questions:

#### Question 1: Enter URLs
```
Enter page URL(s) separated by commas: 
```
**What to do:** Type the website URL(s) you want to test
- Single URL: `https://example.com`
- Multiple URLs: `https://example.com, https://another-site.com`

#### Question 2: Password Protection
```
Is the URL password protected? (yes/no):
```
**What to do:** 
- Type `yes` if the website requires login
- Type `no` if it's a public website
- If you said yes, you'll be asked for username and password

#### Question 3: Folder Name
```
Enter base filename for this page (press Enter for 'Bynder_Page_1'):
```
**What to do:** Give a name for this test (like "Homepage" or "ProductPage")
- This creates a folder with your test results
- Just press Enter to use the default name

### What Happens During Processing?

You'll see messages like:
```
Processing 45 images in parallel with 10 workers...
Progress: 10/45 screenshots completed
Progress: 20/45 screenshots completed
...
Progress: 45/45 screenshots completed
✓ Pass scenarios saved to: Tests/Homepage/Homepage_Pass.xlsx
✓ Fail scenarios saved to: Tests/Homepage/Homepage_Fail.xlsx
```

---

## Where Are My Results?

After the tool finishes, check the **`Tests`** folder:

```
Tests/
├── Homepage/
│   ├── Homepage_Pass.xlsx    ← Images that work fine
│   └── Homepage_Fail.xlsx    ← Broken images with screenshots
├── ProductPage/
│   ├── ProductPage_Pass.xlsx
│   └── ProductPage_Fail.xlsx
```

### Understanding the Excel Files

**Pass Excel File** (Homepage_Pass.xlsx):
- Lists all images that loaded successfully
- No screenshots (they work fine!)

**Fail Excel File** (Homepage_Fail.xlsx):
- Lists all broken/failed images
- **Includes screenshots** of what the error looks like
- **Failure reason** explaining why it failed

---

## Common Issues & Solutions

### Issue 1: "Python not found"
**Solution:** Install Python from https://www.python.org/downloads/
- Make sure to check "Add Python to PATH" during installation

### Issue 2: "pip not found"
**Solution:** Try using `python -m pip install -r requirements.txt` instead

### Issue 3: Virtual environment not activating
**Solution:** 
- Windows: Make sure you're in the project folder and run `venv\Scripts\activate`
- Mac/Linux: Run `source venv/bin/activate`

### Issue 4: ChromeDriver errors
**Solution:** 
- Make sure Google Chrome is installed and updated
- The tool downloads ChromeDriver automatically, but if it fails:
  - Close all Chrome windows
  - Run the tool again

### Issue 5: "Permission denied" errors
**Solution:**
- Windows: Run Command Prompt as Administrator
- Mac/Linux: You might need to use `sudo` or check folder permissions

---

## Demo Script for Your Team

When demonstrating the tool, follow this script:

### 1. Introduction (1 minute)
"This tool automatically tests all images on a website and creates an Excel report showing which images work and which are broken."

### 2. Show the Setup (2 minutes)
```bash
# Show them the folder structure
ls  # or dir on Windows

# Show activating virtual environment
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # Mac/Linux
```

### 3. Run the Tool (3 minutes)
```bash
python image_scraper.py
```

**Walk through each prompt:**
- "I'm entering the URL of our homepage"
- "The site is password protected, so I'll enter yes"
- "I'm naming this test 'Homepage_Test'"
- "Now the tool is checking all images - see the progress?"

### 4. Show the Results (2 minutes)
```bash
# Navigate to Tests folder
cd Tests/Homepage_Test

# Show both Excel files
ls  # or dir on Windows
```

**Open the Fail Excel file and show:**
- Column A: Which page was tested
- Column B: The broken image URL
- Column C: Screenshot of the error
- Column D: Why it failed (e.g., "Amplience found in URL")

### 5. Q&A (2 minutes)
Common questions:
- "How long does it take?" → Depends on number of images, usually 2-5 minutes
- "Can I test multiple pages?" → Yes! Just separate URLs with commas
- "What if I get an error?" → Check the troubleshooting section in this guide

---

## Quick Reference Card

### Every Time You Use the Tool:

1. Open terminal in project folder
2. Activate environment: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Mac/Linux)
3. Run tool: `python image_scraper.py`
4. Answer the questions
5. Check results in `Tests` folder

### What the Tool Checks:

✅ **PASS** if:
- Image loads successfully
- Image is from HTTPS (secure)
- No error messages appear

❌ **FAIL** if:
- Image URL contains "amplience"
- Image shows "Bad Request" error
- Image shows "404 Not Found"
- Image is not HTTPS (not secure)
- Page has no images at all

---

## Tips for Best Results

1. **Test one page at a time** when learning the tool
2. **Use descriptive folder names** like "Homepage_Jan2024" instead of "Test1"
3. **Keep Chrome closed** when running the tool (it opens its own browser)
4. **Check your internet connection** before running large tests
5. **Don't close the terminal** while the tool is running

---

## Need Help?

If you get stuck:
1. Check the "Common Issues" section above
2. Look at the error message in the terminal - it usually tells you what's wrong
3. Ask the team member who set this up
4. Check the full README.md file for more details

---

## Summary

This tool saves us hours of manual work by automatically:
- Finding all images on web pages
- Testing if they work
- Creating detailed Excel reports
- Taking screenshots of broken images
- Organizing everything in easy-to-read folders

**Time to test 100 images manually:** ~2 hours  
**Time with this tool:** ~5 minutes

---

**Questions? Contact:** [Your Name/Team Lead]

**Last Updated:** January 2024

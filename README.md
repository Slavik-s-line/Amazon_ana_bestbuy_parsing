# Support engineer test task

This repository is a part of a test assignment.

## Prerequisites

1. Unpack test repository
2. Install Python3.7 or higher  
https://www.python.org/downloads/  
####NB:  
It's strongly recommended to install `pip` and set `PATH` along with Python3 installation if possible.
3. Install `pip` for `Python3` (if it was omitted on the previous step)  
https://pip.pypa.io/en/stable/installation/
4. Install `virtualenv` for `Python3` (optional but recommended)  
https://virtualenv.pypa.io/en/latest/
5. Windows users: install `Git Bash`  
https://www.stanleyulili.com/git/how-to-install-git-bash-on-windows/  
The next steps should be performed using it or any other Unix-style command line environment.
6. Navigate to the root of test repository, e.g.  
`cd {/specify/your/path/to/}support_engineer_test_task`
7. Create virtual environment (optional but recommended), e.g.  
- Mac/Linux users: `python3 - m virtualenv env`
- Windows users: `py -3 -m virtualenv env`
8. Activate virtual environment (optional but recommended), e.g. 
- Mac/Linux users: `source env/bin/activate`
- Windows users: `source env/Scripts/activate`
9. Install dependencies, e.g.:  
`pip3 install -r requirements.txt`
10. Mac/Linux users:
- set PATH, e.g.: `export PATH=$PATH:/usr/local/bin`
11. Download the latest stable `chromedriver` release for your OS
- https://chromedriver.chromium.org/
12. Put chromedriver binary to:
- Mac & Linux users: `/usr/local/bin`
- Windows users: `C:\Windows`
13. Install Google Chrome browser compatible with previously installed `chromedriver` version 
- https://www.google.com/chrome/

## Test assignment

1. Create a Selenium (https://selenium-python.readthedocs.io/) script as a part of `test_shopping` test case. Replace `pass` statement (Line 2) with the script
2. It's only allowed to define UI elements using:
- Xpath selectors (https://www.guru99.com/xpath-selenium.html): find by ID, Class, Link, etc.
- CSS selectors (https://saucelabs.com/resources/articles/selenium-tips-css-selectors)
- BeautifulSoup library (https://beautiful-soup-4.readthedocs.io/en/latest/)
3. The script should be based on the following scenario:
- user visits `amazon.com` website
- user fills out a search field with the product name and activates search ==>  
==> a page with search results is displayed.
- user looks for the product of specified color having maximum reviews count 
- user extracts minimum product price (with applied discount - if any) from the page
- user assigns `amazon_price` = product price
- user visits `bestbuy.com` website
- user chooses `United States` country
- user fills out a search field with the product name and activates search ==>  
==> a page with search results is displayed.
- user looks for the product of specified color having maximum reviews count 
- user extracts minimum product price (with applied discount - if any) from the page
- user assigns `bestbuy_price` = product price
4. Uncomment the last assert from the test script (Line 6).
5. Run the test case with Selenium in headless mode (already set up in `confest.py` module). From project root it would be:   
- Mac/Linux users: `python3 -m pytest tests/test_shopping.py`
- Windows users: `py -3 -m pytest tests/test_shopping.py`  
There's a 50/50 possibility it fails. That's OK.
6. Provide the results as a new Git repository. 

### NB:   
For debugging purposes, Selenium can be run in non-headless mode. Have a look at comments in `conftest.py` (Line 9).


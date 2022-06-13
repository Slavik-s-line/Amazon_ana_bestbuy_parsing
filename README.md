# Support engineer test task

This repository is a part of a test assignment.

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


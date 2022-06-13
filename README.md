# Support engineer test task

This repository is a part of a test assignment.

## Test assignment

The script is based on the following scenario:
- user visits `amazon.com` website
- user fills out a search field with the product name and activates search ==>  
==> a page with search results is displayed.
- user looks for the product having maximum reviews count 
- user extracts minimum product price (with applied discount - if any) from the page
- user assigns `amazon_price` = product price
- user visits `bestbuy.com` website
- user chooses `United States` country
- user fills out a search field with the product name and activates search ==>  
==> a page with search results is displayed.
- user looks for the product having maximum reviews count 
- user extracts minimum product price (with applied discount - if any) from the page
- user assigns `bestbuy_price` = product price

Run the test case with Selenium in headless mode (already set up in `confest.py` module). 

Result of test case:
![image](https://user-images.githubusercontent.com/78733510/173388346-03e7a2e2-fa09-42dd-a43d-766cd6de8ac7.png)

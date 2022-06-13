from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def amazon():
    path = r"C:\\Windows\\chromedriver.exe"
    product = "macbook air m1 16gb"
    driver = webdriver.Chrome(path)
    driver.get("https://www.amazon.com/ref=nav_logo")
    driver.find_element(By.ID, 'twotabsearchtextbox').send_keys(product)
    driver.find_element(By.CLASS_NAME, "nav-right").click()
    amazon_list = []

    def make_amazon_lists():
        item_titles = driver.find_elements(By.XPATH, '//*[@class="a-section a-spacing-small a-spacing-top-small"]')
        for tittle in item_titles:
            if "MacBook Air" in tittle.text and "16GB" in tittle.text and "M1" in tittle.text:
                line = tittle.text.split("\n")
                if line[2][0] == "$":
                    amazon_list.append(line)

    while True:
        try:
            make_amazon_lists()
            driver.find_element(By.XPATH,
                                '//*[@class ="s-pagination-item s-pagination-next s-pagination-button'
                                ' s-pagination-separator" and not(@aria-disabled)]').click()
            time.sleep(2)
        except NoSuchElementException:
            break
    max_review = 0
    amazon_price = 0
    for elem in amazon_list:
        if int(elem[1]) > max_review:
            max_review = int(elem[1])
            amazon_price = float(elem[2][1:].replace(",", "") + "." + elem[3])
        elif int(elem[1]) == max_review:
            if float(elem[2][1:].replace(",", "") + "." + elem[3]) < amazon_price:
                amazon_price = float(elem[2][1:].replace(",", "") + "." + elem[3])
    driver.close()
    driver.quit()
    return amazon_price


def bestbuy():
    path = r"C:\\Windows\\chromedriver.exe"
    product = "macbook air m1 16gb"
    driver = webdriver.Chrome(path)
    driver.get("https://www.bestbuy.com/")
    driver.find_element(By.CLASS_NAME, "us-link").click()
    driver.find_element(By.ID, 'gh-search-input').send_keys(product)
    driver.find_element(By.CLASS_NAME, "header-search-button").click()
    time.sleep(5)
    tittle_list = []
    price_list = []
    review_list = []
    tittles = driver.find_elements(By.CLASS_NAME, "sku-title")
    for i in driver.find_elements(By.CLASS_NAME, "price-block"):
        price_list.append(float(i.text.split("\n")[0][1:].replace(",", "")))
    for i in driver.find_elements(By.CLASS_NAME, "ratings-reviews"):
        line = i.text.split("\n")[1]
        if "Not" in line:
            review_list.append(0)
        else:
            review_list.append(int("".join(line[1:-1].split()[:-1])))
    bestbuy_price = 0
    max_review = 0
    for tittle in tittles:
        if "MacBook Air" in tittle.text and "16GB" in tittle.text and "M1" in tittle.text:
            tittle_list.append(tittle.text)
            if review_list[tittles.index(tittle)] > max_review:
                bestbuy_price = price_list[tittles.index(tittle)]
            elif review_list[tittles.index(tittle)] == max_review:
                if price_list[tittles.index(tittle)] < bestbuy_price:
                    bestbuy_price = price_list[tittles.index(tittle)]
    driver.close()
    driver.quit()
    return bestbuy_price


def test_shopping():
    amazon_price = amazon()
    bestbuy_price = bestbuy()
    assert amazon_price > bestbuy_price

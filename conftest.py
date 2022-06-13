import pytest
from selenium import webdriver


@pytest.fixture()
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    # in order to turn off/on headless mode please comment/uncomment a line below
    options.add_argument('headless')
    options.add_argument('disable-infobars')
    options.add_argument('window-size=1920x1080')
    options.add_argument('--verbose')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    wd = webdriver.Chrome(options=options)
    wd.implicitly_wait(5)
    request.addfinalizer(wd.quit)
    return wd

from page_object.HomePage import HomePage
from selenium import webdriver


def test_amazon1():
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.fr/")
    driver.maximize_window()
    driver.quit()


def test_page_object():
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.fr/")

    home_page = HomePage(driver)
    home_page.closeCookies()
    home_page.openAllMenu()
    home_page.openBookCategory()
    home_page.openAllBooks()

    ## example draft PR



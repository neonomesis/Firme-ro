from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


PATH = "../chromedriver 2"
# cui = "38781286, 1819608, 20649658, 15227070, 4774845d"

options = Options()
options.page_load_strategy = "eager"
driver = Chrome(PATH, options=options)


def login():
    try:
        driver.get("https://www.romanian-companies.eu/search.asp")
        driver.find_element(By.ID, "rememlg").click()
        driver.find_element(By.NAME, 'nume').send_keys('bunescu.vasile@gmail.com')
        driver.find_element(By.NAME, 'pwd').send_keys('Vasea1997'+ Keys.ENTER)
        expected_conditions = driver.find_element(By.LINK_TEXT, "Cont deja utilizat de la adresa")
        expected_conditions.accept()

    except Exception as e:
        print(e)
        pass

if __name__ == '__main__':
    try:
        login()
    except Exception as e:
        print(e)
    finally:
        # driver.close()
        pass

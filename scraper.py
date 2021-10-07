from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pyautogui
import json

PATH = "../chromedriver 2"
# cui = "38781286"

options = Options()
options.page_load_strategy = "eager"
driver = Chrome(PATH, options=options)


def initialization(input_list):
    results = []
    for cui in input_list:
        driver.get("https://www.romanian-companies.eu/search.asp")
        getting_cui()
        item = paersin_one()
        results.append(item)
    save_to_file(results)

def getting_cui():
    try:
        ss = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "searchfor")))
        for x in input_list:
            ss.send_keys(x + Keys.ENTER)
        WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CLASS_NAME, 'input-group-btn'))).click()
        driver.implicitly_wait(10)
        driver.find_element(By.CLASS_NAME, 'clickable-row').click()
        driver.switch_to_window(driver.window_handles[1])
    except Exception as e:
        print(e)

def paersin_one():
    fieldss = []
    html_code = driver.page_source
    soup = BeautifulSoup(html_code,  "html.parser")

    fields = soup.find(id="date-de-identificare").find_all("tr")

    name = fields[1] 
    fiscal = fields[2]
    other = fields[3]
   
    print("ww38781286")

    return  {
        'name' : name.text,
        'fiscal code' : fiscal.text,
        'other inforrmation': other.text
    }

def save_to_file(py_dict):
    try:
        with open("test.json", "w") as f:
            f.write(json.dumps(py_dict, ensure_ascii=False))
            f.close()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    try:
        input_string = input('Enter cui...')
        input_list = input_string.split(',')
        initialization(input_list)
    except Exception as e:
        print(e)
    finally:
        driver.close()

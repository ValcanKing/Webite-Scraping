from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json
URL = "https://motorregister.skat.dk/dmr-kerne/koeretoejdetaljer/visKoeretoej"


def conv(f):
    lst = f.split('\n')
    res_dct = {lst[i]: lst[i + 1] for i in range(2, len(lst)-1, 2)}
    return res_dct


searchterm = input("Enter the Stelnr:")

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(URL)

button = driver.find_element(By.ID, "stelnr")
button.click()

command = driver.find_element(By.ID, "soegeord")
command.send_keys(searchterm)

search = driver.find_element(By.ID, "fremsoegKtBtn")
search.click()

data1 = driver.find_element(By.CLASS_NAME, "h-tab-content-inner")
dim1 = conv(data1.text)

butt = driver.find_element(By.ID, "tabSetNextBtn")
butt.click()

data2 = driver.find_element(By.CLASS_NAME, "h-tab-content")
dim2 = conv(data2.text)

butt = driver.find_element(By.ID, "tabSetNextBtn")
butt.click()


data3 = driver.find_element(By.CLASS_NAME, "h-tab-content")
dim3 = conv(data3.text)


butt = driver.find_element(By.ID, "tabSetNextBtn")
butt.click()

data4 = driver.find_element(By.CLASS_NAME, "h-tab-content")
dim4 = conv(data4.text)

butt = driver.find_element(By.ID, "tabSetNextBtn")
butt.click()

data5 = driver.find_element(By.CLASS_NAME, "h-tab-content")
dim5 = conv(data5.text)

lst = [{"1.køretøj": dim1}, {"2.Tekniske oplysninger": dim2}, {"3.Syn": dim3},
       {"4.Forsikring": dim4}, {"5. Dispensationer og tilladelser": dim5}]

json.dumps(lst)
with open(searchterm+'.json', 'w', encoding='utf-8') as f:
    json.dump(lst, f, ensure_ascii=False)

driver.quit()

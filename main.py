from time import sleep

import numpy as np
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers import get_data_from_riders


driver = webdriver.Firefox(executable_path='./geckodriver')
driver.get("https://www.letour.fr/es/historia")
sleep(5)

close_cookies = driver.find_element_by_id('onetrust-accept-btn-handler')
close_cookies.click()

sleep(5)
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//button[text()="2016"]'))
)

element.click()
sleep(5)

driver.execute_script("window.scrollTo(200,1600)")
more_riders = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'a.btn'))
)
more_riders.click()


riders_info_elements = driver.find_elements_by_tag_name('tr')
riders_list = [rider_row for rider_row in riders_info_elements if rider_row.text != '']
riders_info = [rider.find_elements_by_xpath(".//*") for rider in riders_list]

riders_data_to_df = get_data_from_riders(riders_info)
columns = ['Corredor', 'No.', '', 'Equipo', "Tiempo", 'Diferencia', 'B', 'P']

df = pd.DataFrame(np.array(riders_data_to_df), columns=columns)
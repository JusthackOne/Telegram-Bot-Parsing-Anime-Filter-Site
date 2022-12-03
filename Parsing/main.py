import time
import pickle
import re
import os

from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert

from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains


from bs4 import BeautifulSoup
from fake_useragent import UserAgent


class Driver:
    def __init__(self):
        self.useragent = UserAgent()
        self.chrome_options = Options()
        self.chrome_options.add_argument("--no-sandbox")
        # self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument(f'user-agent={self.useragent.random}')

        self.driver = webdriver.Chrome(executable_path='chromedriver',
                                       chrome_options=self.chrome_options)

        # self.driver.set_window_size(1360, 900)
        self.wait = WebDriverWait(self.driver, 2)
        self.wait_long = WebDriverWait(self.driver, 5)
        self.wait_long_2 = WebDriverWait(self.driver, 40)
        self.action = ActionChains(self.driver)

    def start_parsing(self, link):
        self.driver.get('https://h5.tu.qq.com/web/ai-2d/cartoon/index?parent_trace_id=cf36d024-cafe-039e-ff60-51afd70cd26a&amp;root_channel=qq_sousuo&amp;current_channel=imageQRCode&amp;level=11')
        # Принятие соглашения
        try:
            self.wait_long.until(EC.element_to_be_clickable((By.CLASS_NAME, '_confirm-btn_1fu81_42')))
            self.driver.find_element(By.CLASS_NAME, '_confirm-btn_1fu81_42').click()
        except:
            self.driver.close()
            self.driver.quit()
            return False
        # Нажатие кнопки 1
        try:
            self.wait_long.until(EC.visibility_of_element_located((By.CLASS_NAME, '_action-panel_shsfk_64')))
            self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        except:
            self.driver.close()
            self.driver.quit()
            return False
        try:
            self.wait_long.until(EC.element_to_be_clickable((By.CLASS_NAME, '_action-panel_shsfk_64')))
            self.driver.find_element(By.CLASS_NAME, '_action-panel_shsfk_64').click()
        except:
            self.driver.close()
            self.driver.quit()
            return False
        # Нажатие кнопки для отправки имя файла
        try:
            self.wait_long.until(EC.element_to_be_clickable((By.CLASS_NAME, '_choose-actions_shsfk_36')))
            self.driver.find_element(By.CLASS_NAME, '_choose-actions_shsfk_36').click()
        except:
            self.driver.close()
            self.driver.quit()
            return False

        path = os.path.abspath(link)
        print('Путь до файла:\n' + path)

        self.driver.find_elements(By.TAG_NAME, 'input')[-1].send_keys(path)
        # Нажатие кнопки 2
        try:
            self.wait_long_2.until(EC.element_to_be_clickable((By.CLASS_NAME, '_action-btn-left_mvguu_154')))
        except:
            self.driver.close()
            self.driver.quit()
            return False

        # Скриншот колучившегося фото
        soup = BeautifulSoup(self.driver.page_source, 'lxml')
        photo = soup.find_all('img', attrs={'src':re.compile("https://activity.tu.qq.com/mqq/ai_painting_anime/share/")})[0]
        self.driver.get(photo['src'])
        try:
            self.wait_long.until(EC.visibility_of_element_located((By.TAG_NAME, 'img')))
            self.driver.find_element(By.TAG_NAME, 'img').screenshot('photo_parsing/' + link.replace('photo_original/', '').replace('jpg', 'png'))
        except:
            self.driver.close()
            self.driver.quit()
            return False
        print('done')
        self.driver.close()
        self.driver.quit()
        print('удачно закрылся браузер')
        return True



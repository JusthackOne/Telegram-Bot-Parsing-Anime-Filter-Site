import time
import pickle

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
         # self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument(f'user-agent={self.useragent.random}')

        self.driver = webdriver.Chrome(executable_path='chromedriver',
                                       chrome_options=self.chrome_options)

        self.driver.set_window_size(1360, 900)
        self.wait = WebDriverWait(self.driver, 3)
        self.wait_long = WebDriverWait(self.driver, 15)
        self.action = ActionChains(self.driver)

    def start_parsing(self, link):
        self.driver.get('https://h5.tu.qq.com/web/ai-2d/cartoon/index?parent_trace_id=cf36d024-cafe-039e-ff60-51afd70cd26a&amp;root_channel=qq_sousuo&amp;current_channel=imageQRCode&amp;level=11')
        time.sleep(10)
        #if os.path.isfile(f'cookies/{num}_cookies') == False:
         #   return
        for cookie in pickle.load(open(f'cookies/cookies', "rb")):
            self.driver.add_cookie(cookie)
        # Принятие соглашения
        self.wait_long.until(EC.visibility_of_element_located((By.CLASS_NAME, '_confirm-btn_1fu81_42')))
        self.driver.find_element(By.CLASS_NAME, '_confirm-btn_1fu81_42').click()
        # Нажатие кнопки 1
        self.wait_long.until(EC.visibility_of_element_located((By.CLASS_NAME, '_action-panel_shsfk_64')))
        self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        self.driver.find_element(By.CLASS_NAME, '_action-panel_shsfk_64').click()
        # Нажатие кнопки для отправки имя файла
        self.wait_long.until(EC.visibility_of_element_located((By.CLASS_NAME, '_choose-actions_shsfk_36')))
        self.driver.find_element(By.CLASS_NAME, '_choose-actions_shsfk_36').click()
        self.driver.find_elements(By.TAG_NAME, 'input')[-1].send_keys(r"C:\Users\User\Desktop\Telegram-Bot-Parsing-Anime-Filter-Site\photo.jpg")

        # Нажатие кнопки 2
        self.wait_long.until(EC.visibility_of_element_located((By.CLASS_NAME, '_action-btn-left_mvguu_154')))
        self.driver.find_element(By.CLASS_NAME, '_action-btn-left_mvguu_154').click()
        # Скриншот колучившегося фото
        self.wait_long.until(EC.visibility_of_element_located((By.CLASS_NAME, '_save-pic-container-content-image_mvguu_284')))
        time.sleep(3)
        self.driver.find_element(By.CLASS_NAME, '_save-pic-container-content-image_mvguu_284').screenshot(f'screenshot.png')

        time.sleep(60)

        driver.quit()
        driver.close()



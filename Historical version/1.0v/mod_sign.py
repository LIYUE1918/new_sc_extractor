from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
#pip install webdriver-manager
from webdriver_manager.chrome import ChromeDriverManager
import time
chrome_options = Options()
chrome_options.add_argument("--headless")  # 不显示浏览器
chrome_options.add_argument("--disable-gpu")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
def login_sim_companies(email, password):
    """使用Selenium模拟登录Sim Companies网站"""
    try:
        driver.get("https://www.simcompanies.com/signin/")
        time.sleep(5)
        wait = WebDriverWait(driver, 20)  # 设置显式等待

        driver.get("https://www.simcompanies.com/signin/")
        time.sleep(5)
        wait = WebDriverWait(driver, 20)  # 设置显式等待

        email_field = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="email"]')))
        password_field = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="password"]')))

        email_field.send_keys(email)
        password_field.send_keys(password)

        password_field.send_keys(Keys.RETURN)
        time.sleep(10)  # 等待登录完成

        cookies = driver.get_cookies()
        session_cookies = {cookie['name']: cookie['value'] for cookie in cookies}
        print("登录成功，已获取cookies！")
        return session_cookies
    except Exception as e:
        print(f"登录时出现问题: {e}")
        print("Page Source:", driver.page_source)  # 打印页面源码
        return None
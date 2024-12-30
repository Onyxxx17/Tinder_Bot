from selenium import webdriver
from selenium.common import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

EMAIL = 'YOUR EMAIL'
PASSWORD = 'YOUR PASSWORD'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://tinder.com")

time.sleep(2)
login_button = driver.find_element(By.XPATH, value='//*[@id="q2098069830"]/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]/div')
login_button.click()

time.sleep(1)
facebook_login = driver.find_element(By.XPATH, value='//*[@id="q369688754"]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div[2]/div/div')
facebook_login.click()


base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
time.sleep(2)
email = driver.find_element(By.NAME, value='email')
email.send_keys(EMAIL)

password = driver.find_element(By.NAME, value='pass')
password.send_keys(PASSWORD)

facebook_login_button = driver.find_element(By.ID, value='loginbutton')
facebook_login_button.send_keys(Keys.ENTER)

time.sleep(6)
continue_login = driver.find_element(By.CSS_SELECTOR, ".x1lliihq.x6ikm8r.x10wlt62.x1n2onr6.xlyipyv.xuxw1ft")
continue_login.click()

time.sleep(4)
driver.switch_to.window(base_window)
# time.sleep(20)
# driver.switch_to.window(base_window)
#
allow_location = driver.find_element(By.XPATH, value= '//*[@id="q369688754"]/div/div[1]/div/div/div[3]/button[1]/div[2]/div[2]/div')
allow_location.click()

decline_cookies = driver.find_element(By.XPATH, value = '//*[@id="q369688754"]/div/div[2]/div/div/div[1]/div[2]/button/div[2]/div[2]/div')
decline_cookies.click()

notifications_off = driver.find_element(By.XPATH, value = '//*[@id="q369688754"]/div/div/div/div/div[3]/button[2]/div[2]/div[2]/div')
notifications_off.click()
# print(driver.title)

time.sleep(10)

for i in range(1,100):
    time.sleep(2)
    try:
        like_button = driver.find_element(By.XPATH, value = '//*[@id="main-content"]/div[1]/div/div/div/div[1]/div/div/div[4]/div/div[4]/button')
        like_button.click()

    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
            match_popup.click()

            # Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            time.sleep(2)
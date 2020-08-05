import time

from selenium.webdriver.chrome import webdriver

try:

    browser = webdriver.Chrome()
    # 需要安装chrome driver, 和浏览器版本保持一致
    browser.get('https://shimo.im/login?from=home')


    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/input').send_keys('*****')
    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/input').send_keys('****')
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/button').click()

except Exception as e:
    print(e)
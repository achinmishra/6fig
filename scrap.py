import os


from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from random import randint

from useragent import FakeUserAgentGeneration

i = 0
while i is not 10:
    uas = FakeUserAgentGeneration()
    user_agent = uas.load_fake_user_agent()
    print(user_agent)


    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument('--disable-infobars')
    chrome_options.add_argument('--profile-directory=Default')
    chrome_options.add_argument('--incognito')
    chrome_options.add_argument('--disable-plugins-discovery')
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument(f'user-agent={user_agent}')


    print(os.path.abspath("chromedriver"))
    # driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"), chrome_options=chrome_options, desired_capabilities=chrome_options.to_capabilities())
    driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver", chrome_options=chrome_options, desired_capabilities=chrome_options.to_capabilities())
    driver.get("https://www.crunchbase.com/organization/snapdeal")

    try:
        print(driver.page_source)
        magnifying_glass = driver.find_element_by_id("section-funding-rounds")
        print("HERE")
        if magnifying_glass.is_displayed():
            magnifying_glass.click()
        else:
            menu_button = driver.find_element_by_css_selector(".menu-trigger.local")
            menu_button.click()

        search_field = driver.find_element_by_id("site-search")
        search_field.clear()
        search_field.send_keys("Olabode")
        search_field.send_keys(Keys.RETURN)
        assert "Looking Back at Android Security in 2016" in driver.page_source
    except Exception:
        pass
    print(driver.page_source)
    driver.close()
    sleep(randint(10,20))
    i = i + 1


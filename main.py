import time

from selenium import webdriver
from fake_useragent import UserAgent
import random
from selenium.webdriver.common.by import By
import re
import requests
from bs4 import BeautifulSoup as Soup
import logging


def selenium_wrapping():
    user_agent = UserAgent().random

    print(user_agent)
    options = webdriver.FirefoxOptions()
    options.add_argument(f'user-agent={user_agent}')
    driver = webdriver.Firefox(options=options)

    driver.set_window_position(random.randrange(0, 900, 350), random.randrange(0, 400, 200))
    driver.set_window_size(random.randrange(1024, 1490, 150), random.randrange(768, 1280, 150))

    try:
        driver.get('https://www.farpost.ru/')
        # element = driver.find_element(By.XPATH, "//a[@href='/vladivostok/service/']")
        # element.click()
        #
        # element = driver.find_element(By.XPATH, "//a[@href='/vladivostok/service/internet/']")
        # element.click()

        headers = driver.execute_script(
            "var req = new XMLHttpRequest();req.open('GET', document.location, false);req.send(null);return req.getAllResponseHeaders()")
        headers = re.split('\r\n|: ', headers)
        headers = {headers[i-1]: headers[i] for i in range(1, len(headers), 2)}

        cookies = {
            'path': '/',
            'domain': '.farpost.ru',
            'secure': 'True',
            'httpOnly': 'False',
            'sameSite': 'None'
        }
        for item in driver.get_cookies():
            cookies[item['name']] = item['value']
            if item['expiry']: cookies['expiry'] = str(item['expiry'])

        return headers, cookies

    except Exception as e:
        print(e)

    finally:
        driver.close()
        driver.quit()


def start_request():
    response = requests.get('https://www.farpost.ru/')
    print(response.cookies)
    print(response.headers)

if __name__ == "__main__":
    headers, cookies = selenium_wrapping()
    while True:
        response = requests.get('https://www.farpost.ru/vladivostok/service/internet', cookies=cookies, headers=headers)
        soup = Soup(response.content, 'html.parser')
        title = soup.find("title").text
        print(title)

        if title == 'Фарпост - доска объявлений':
            headers, cookies = selenium_wrapping()
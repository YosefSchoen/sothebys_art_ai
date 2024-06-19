from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Pages.ResultsPage import ResultsPage

import json


with open('Config/config.json') as file:
    config_data = json.load(file)


# todo make summary pages show lots
# todo scrape images
# todo comment code
# todo get category of art
# todo make work on aws lambda

def set_up_chromedriver():
    service = Service(ChromeDriverManager(driver_version='126.0.6478.61').install())
    options = Options()
    #options.add_argument('--headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("start-maximized")

    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    driver = webdriver.Chrome(service=service, options=options)
    return driver


def make_selenium_work(driver):
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
        Object.defineProperty(navigator, 'webdriver', {
          get: () => undefined
        })
      """
    })

    driver.execute_cdp_cmd("Network.enable", {})
    driver.execute_cdp_cmd('Network.setUserAgentOverride', {
        "userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})


def main(page_id, collection_id):
    driver = set_up_chromedriver()
    make_selenium_work(driver=driver)
    home_page = HomePage(driver=driver, config_data=config_data)
    home_page.get_page()
    home_page.go_to_login_page()
    login_page = LoginPage(driver=driver, config_data=config_data)
    login_page.login()
    login_page.go_to_home_page()

    results_page = ResultsPage(
        driver=driver,
        config_data=config_data,
        page_id=page_id,
        page_url=config_data['LINKS']['RESULTS_LINK']+'&p='+str(page_id),
        collection_id=collection_id
    )

    results = results_page.get_page_results()
    return results


if __name__ == '__main__':
    main(0, 0)

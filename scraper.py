import json
from typing import List

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Pages.ResultsPage import ResultsPage
from entities import Collection


with open('Config/config.json') as file:
    config_data = json.load(file)


def set_up_chromedriver() -> webdriver:
    service = Service(ChromeDriverManager(driver_version=config_data['WEB_DRIVER']['CHROME_VERSION']).install())
    options = Options()

    for option in config_data['WEB_DRIVER']['OPTIONS']:
        options.add_argument(option)

    for experimental_option in config_data['WEB_DRIVER']['EXPERIMENTAL']:
        options.add_experimental_option(experimental_option['NAME'], experimental_option['VALUE'])

    driver = webdriver.Chrome(service=service, options=options)
    return driver


def make_selenium_work(driver) -> None:
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
        Object.defineProperty(navigator, 'webdriver', {
          get: () => undefined
        })
      """
    })

    driver.execute_cdp_cmd("Network.enable", {})
    driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": user_agent})


def main(page_id: int) -> List[Collection]:
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
        page_url=config_data['LINKS']['RESULTS_LINK']+'&p='+str(page_id)
    )

    results = results_page.get_page_results()
    driver.quit()
    return results


if __name__ == '__main__':
    main(0)

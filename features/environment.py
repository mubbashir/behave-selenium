import os

from selenium import webdriver

GRID_HUB_URL = os.environ.get('GRID_HUB_URL')


def before_feature(context, feature):
    if GRID_HUB_URL is None:
        fp = webdriver.FirefoxProfile()
        context.browser = webdriver.Firefox(firefox_profile=fp)
    else:
        desired_capabilities = webdriver.DesiredCapabilities.FIREFOX
        context.browser = webdriver.Remote(
            desired_capabilities=desired_capabilities,
            command_executor=GRID_HUB_URL
        )


def after_feature(context, feature):
    context.browser.quit()

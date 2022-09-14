import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1280
    browser.config.window_height = 1024
    yield


@pytest.fixture()
def open_and_quit_browser_automation_practice_form():
    browser.open('/automation-practice-form')
    yield
    browser.quit()


@pytest.fixture()
def open_and_quit_browser_webtables():
    browser.open('/webtables')
    yield
    browser.quit()



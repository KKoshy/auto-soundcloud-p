import logging
from pathlib import Path

import allure
import pytest
from playwright.sync_api import sync_playwright

from libs.pages.home_page import HomePage
from libs.pages.locators import HomePageSelectors

log = logging.getLogger(__name__)


def test_env_setup():
    pw = sync_playwright().start()
    browser = pw.chromium.launch(
        headless=False,
        args=[
            "--window-size=1000,800",
            "--disable-blink-features=AutomationControlled",
            "--disable-dev-shm-usage",
            "--disable-gpu",
            "--no-sandbox",
        ],
    )
    context = browser.new_context(viewport={"width": 1000, "height": 800})
    page = context.new_page()
    page.goto("https://soundcloud.com", timeout=120000)
    page.wait_for_load_state("networkidle")

    # handling cookies
    home = HomePage(page=page)
    if home.pw_utils.wait_for_selector(HomePageSelectors.COOKIE_DIALOG, ignore_timeout=True):
        home.reject_cookies()

    return page, browser, pw


def test_env_teardown(browser, pw):
    browser.close()
    pw.stop()


@pytest.hookimpl(tryfirst=True)
def pytest_collection_modifyitems(items):
    """
    Modifying the test cases before it starts
    """
    repo = "auto-souncloud-p"
    for item in items:
        item.add_marker(allure.story(repo))
        _file = Path(item.nodeid.split("::")[0])
        item.add_marker(allure.parent_suite(repo))
        suite = "".join(_file.parent.parts[1])
        item.add_marker(allure.suite(suite))
        sub_suite = item.nodeid.split("::")[1]
        item.add_marker(allure.sub_suite(sub_suite))


@pytest.fixture(scope="module")
def portal():
    page, browser, pw = test_env_setup()
    yield page
    test_env_teardown(browser, pw)

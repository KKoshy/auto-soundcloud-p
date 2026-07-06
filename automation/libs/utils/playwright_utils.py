import logging
from typing import Literal, Optional

from playwright.sync_api import Page, TimeoutError

log = logging.getLogger(__name__)


class PlaywrightUtils:
    def __init__(self, page: Page) -> None:
        self.page = page

    def wait_for_selector(
        self,
        selector: str,
        state: Optional[Literal["attached", "detached", "hidden", "visible"]] = None,
        timeout: int = 20000,
        ignore_timeout: bool = False,
    ):
        log.info("Playwright: waiting for element")
        try:
            self.page.locator(selector).wait_for(state=state, timeout=timeout)
        except TimeoutError:
            if ignore_timeout:
                return False
            raise
        return True

    def click_selector(self, selector: str, timeout: int = 20000):
        log.info("Playwright: clicking element")
        self.wait_for_selector(selector=selector, timeout=timeout)
        self.page.locator(selector=selector).click(timeout=timeout)

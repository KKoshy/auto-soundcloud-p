import logging

from playwright.sync_api import Page, expect

from libs.pages.base_page import BasePage
from libs.pages.locators import DiscoverPageSelectors

log = logging.getLogger()


class DiscoverPage(BasePage):
    def __init__(self, page: Page) -> None:
        self.page = page
        super().__init__(page)

    def should_have_sound_cloud_button(self):
        log.info("Playwright: checking for SoundCloud button")
        self.pw_utils.wait_for_selector(DiscoverPageSelectors.SOUND_CLOUD)
        expect(self.page.locator(DiscoverPageSelectors.SOUND_CLOUD)).to_be_enabled()
        return self

    def should_have_home_button(self):
        log.info("Playwright: checking for home button")
        self.pw_utils.wait_for_selector(DiscoverPageSelectors.HOME)
        expect(self.page.locator(DiscoverPageSelectors.HOME)).to_be_enabled()
        return self

    def should_have_feed_button(self):
        log.info("Playwright: checking for feed button")
        self.pw_utils.wait_for_selector(DiscoverPageSelectors.FEED)
        expect(self.page.locator(DiscoverPageSelectors.FEED)).to_be_enabled()
        return self

    def should_have_library_button(self):
        log.info("Playwright: checking for library button")
        self.pw_utils.wait_for_selector(DiscoverPageSelectors.LIBRARY)
        expect(self.page.locator(DiscoverPageSelectors.LIBRARY)).to_be_enabled()
        return self

    def should_have_search_bar(self):
        log.info("Playwright: checking for search bar")
        self.pw_utils.wait_for_selector(DiscoverPageSelectors.SEARCH_BAR)
        expect(self.page.locator(DiscoverPageSelectors.SEARCH_BAR)).to_be_editable()
        return self

    def should_have_sign_in_button(self):
        log.info("Playwright: checking for sign in button")
        self.pw_utils.wait_for_selector(DiscoverPageSelectors.SIGN_IN)
        expect(self.page.locator(DiscoverPageSelectors.SIGN_IN)).to_be_enabled()
        return self

    def should_have_create_account(self):
        log.info("Playwright: checking for create account button")
        self.pw_utils.wait_for_selector(DiscoverPageSelectors.CREATE_ACCOUNT)
        expect(self.page.locator(DiscoverPageSelectors.CREATE_ACCOUNT)).to_be_enabled()
        return self

    def should_have_upload_button(self):
        log.info("Playwright: checking for upload button")
        self.pw_utils.wait_for_selector(DiscoverPageSelectors.UPLOAD)
        expect(self.page.locator(DiscoverPageSelectors.UPLOAD)).to_be_enabled()
        return self

    def should_have_discover_tracks_header(self):
        log.info("Playwright: checking for header")
        self.pw_utils.wait_for_selector(DiscoverPageSelectors.DISCOVER_TRACKS_HEADER)
        expect(self.page.locator(DiscoverPageSelectors.DISCOVER_TRACKS_HEADER)).to_be_visible()
        return self

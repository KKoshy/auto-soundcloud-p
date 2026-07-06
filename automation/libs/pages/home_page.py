import logging

from playwright.sync_api import Page, expect

from libs.pages.base_page import BasePage
from libs.pages.discover_page import DiscoverPage
from libs.pages.locators import HomePageSelectors

log = logging.getLogger(__name__)


class HomePage(BasePage):
    def __init__(self, page: Page) -> None:
        self.page = page
        super().__init__(page)

    def reject_cookies(self):
        log.info("Playwright: rejecting cookies")
        self.pw_utils.wait_for_selector(HomePageSelectors.COOKIE_DIALOG)
        self.pw_utils.click_selector(HomePageSelectors.REJECT_ALL)
        expect(self.page.locator(HomePageSelectors.COOKIE_DIALOG)).not_to_be_visible()
        return self

    def validate_home_page_qr_code(self):
        log.info("Playwright: validating qr code")
        self.pw_utils.wait_for_selector(HomePageSelectors.QR_CODE)
        qr = self.page.locator(HomePageSelectors.QR_CODE)
        qr.screenshot(path="home_qr.png")
        link, _ = self.validate_qr("home_qr.png")
        assert "https://sc.soundcloud.com" in link
        return self

    def click_trending_playlists(self):
        log.info("Playwright: click explore trending playlists")
        self.pw_utils.click_selector(HomePageSelectors.EXPLORE_TRENDING_PLAYLISTS)
        return DiscoverPage(self.page)

    def should_have_top_logo(self):
        log.info("Playwright: checking for SoundCloud logo at top")
        self.pw_utils.wait_for_selector(HomePageSelectors.TOP_LOGO)
        expect(self.page.locator(HomePageSelectors.TOP_LOGO)).to_be_visible()
        return self

    def should_have_sign_in_button(self):
        log.info("Playwright: checking for sign in button")
        self.pw_utils.wait_for_selector(HomePageSelectors.SIGN_IN)
        expect(self.page.locator(HomePageSelectors.SIGN_IN)).to_be_enabled()
        return self

    def should_have_create_account(self):
        log.info("Playwright: checking for create account button")
        self.pw_utils.wait_for_selector(HomePageSelectors.CREATE_ACCOUNT)
        expect(self.page.locator(HomePageSelectors.CREATE_ACCOUNT)).to_be_enabled()
        return self

    def should_have_search_bar(self):
        log.info("Playwright: checking for search bar")
        self.pw_utils.wait_for_selector(HomePageSelectors.SEARCH_BAR)
        expect(self.page.locator(HomePageSelectors.SEARCH_BAR)).to_be_editable()
        return self

    def should_have_for_artists_link(self):
        log.info("Playwright: checking for for artists link")
        self.pw_utils.wait_for_selector(HomePageSelectors.FOR_ARTISTS)
        expect(self.page.locator(HomePageSelectors.FOR_ARTISTS)).to_be_enabled()
        return self

    def should_have_upload_your_own_link(self):
        log.info("Playwright: checking for upload your own link")
        self.pw_utils.wait_for_selector(HomePageSelectors.UPLOAD_YOUR_OWN)
        expect(self.page.locator(HomePageSelectors.UPLOAD_YOUR_OWN)).to_be_enabled()
        return self

    def should_have_explore_trending_playlists_link(self):
        log.info("Playwright: checking for explore trending playlists link")
        self.pw_utils.wait_for_selector(HomePageSelectors.EXPLORE_TRENDING_PLAYLISTS)
        expect(self.page.locator(HomePageSelectors.EXPLORE_TRENDING_PLAYLISTS)).to_be_enabled()
        return self

    def should_have_find_out_more_link(self):
        log.info("Playwright: checking for find out more button")
        self.pw_utils.wait_for_selector(HomePageSelectors.FIND_OUT_MORE_LINK)
        expect(self.page.locator(HomePageSelectors.FIND_OUT_MORE_LINK)).to_be_enabled()
        return self

    def should_have_footer_logo_link(self):
        log.info("Playwright: checking for SoundCloud footer logo link")
        self.pw_utils.wait_for_selector(HomePageSelectors.FOOTER_LOGO_LINK)
        expect(self.page.locator(HomePageSelectors.FOOTER_LOGO_LINK)).to_be_enabled()
        return self

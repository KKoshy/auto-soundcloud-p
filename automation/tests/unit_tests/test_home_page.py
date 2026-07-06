import logging

import pytest

from libs.pages.home_page import HomePage

log = logging.getLogger(__name__)


@pytest.fixture(scope="module")
def home_page(portal):
    home = HomePage(portal)
    return home


@pytest.mark.unittest
class TestHomePage:
    def test_top_logo(self, home_page: HomePage):
        home_page.should_have_top_logo()

    def test_sign_in_button(self, home_page: HomePage):
        home_page.should_have_sign_in_button()

    def test_create_account_button(self, home_page: HomePage):
        home_page.should_have_create_account()

    def test_for_artists_link(self, home_page: HomePage):
        home_page.should_have_for_artists_link()

    def test_search_bar(self, home_page: HomePage):
        home_page.should_have_search_bar()

    def test_upload_your_own_link(self, home_page: HomePage):
        home_page.should_have_upload_your_own_link()

    def test_explore_trending_playlists_link(self, home_page: HomePage):
        home_page.should_have_explore_trending_playlists_link()

    def test_home_page_qr_code(self, home_page: HomePage):
        home_page.validate_home_page_qr_code()

    def test_find_out_more_link(self, home_page: HomePage):
        home_page.should_have_find_out_more_link()

    def test_footer_logo_link(self, home_page: HomePage):
        home_page.should_have_footer_logo_link()

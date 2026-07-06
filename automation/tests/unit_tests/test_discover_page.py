import logging

import pytest


from libs.pages.discover_page import DiscoverPage
from libs.pages.home_page import HomePage

log = logging.getLogger(__name__)


@pytest.fixture(scope="module")
def discover_page(portal):
    home = HomePage(portal)
    discover = home.click_trending_playlists()
    return discover


@pytest.mark.unittest
class TestDiscoverPage:
    def test_sound_cloud_button(self, discover_page: DiscoverPage):
        discover_page.should_have_sound_cloud_button()

    def test_home_button(self, discover_page: DiscoverPage):
        discover_page.should_have_home_button()

    def test_feed_button(self, discover_page: DiscoverPage):
        discover_page.should_have_feed_button()

    def test_library_button(self, discover_page: DiscoverPage):
        discover_page.should_have_library_button()

    def test_search_bar(self, discover_page: DiscoverPage):
        discover_page.should_have_search_bar()

    def test_sign_in_button(self, discover_page: DiscoverPage):
        discover_page.should_have_sign_in_button()

    def test_create_account_button(self, discover_page: DiscoverPage):
        discover_page.should_have_create_account()

    def test_upload_button(self, discover_page: DiscoverPage):
        discover_page.should_have_upload_button()

    def test_discover_tracks_header(self, discover_page: DiscoverPage):
        discover_page.should_have_discover_tracks_header()

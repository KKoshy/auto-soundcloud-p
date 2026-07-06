import logging

import cv2
from playwright.sync_api import Page

from libs.utils.playwright_utils import PlaywrightUtils

log = logging.getLogger(__name__)


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.base_url = ""
        self.pw_utils = PlaywrightUtils(page)

    def validate_qr(self, path: str):
        image = cv2.imread(path)
        detector = cv2.QRCodeDetector()
        data, bbox, _ = detector.detectAndDecode(img=image)
        return data, bbox

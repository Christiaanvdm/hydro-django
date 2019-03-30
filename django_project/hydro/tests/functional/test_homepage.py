# coding=utf-8
import unittest

from hydro.tests.functional.utils import SeleniumTestCase, selenium_flag_ready


class TestHomepage(SeleniumTestCase):

    @unittest.skipUnless(
        selenium_flag_ready(),
        'Selenium test was not setup')
    def test_homepage(self):
        # test that driver perfectly configured
        self.assertTrue(self.driver)

        self.driver.get(self.live_server_url)
        self.assertIn('hydro', self.driver.title)

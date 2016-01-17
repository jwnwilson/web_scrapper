"""
    @Author: Noel Wilson (jwnwilson@hotmail.co.uk)
    @Date: 17/01/2016

    Web Scrapper unit tests
"""
import os
import sys
import unittest
import logging
from web_scrapper_modules.web_scrapper import WebScrapper
from requests.exceptions import ConnectionError, MissingSchema

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
logger = logging.getLogger(__name__)


class TestUnitTests(unittest.TestCase):
    """
    Unit tests for exercise
    """
    def test_webscrapper_constructor(self):
        """
        Test WebScrapper constructor parsed a website as intended
        as a number
        :return: None
        """
        websc = WebScrapper(url="http://www.google.com")
        web_obj = websc.web_object['']

        self.assertEqual(web_obj.title.string, "Google")

    def test_webscrapper_read_site(self):
        """
        Test WebScrapper read site command returns expected output and raises exceptions
        as a number
        :return: None
        """
        websc = WebScrapper()
        websc.read_site("http://www.google.com")
        web_obj = websc.web_object['']

        self.assertEqual(web_obj.title.string, "Google")
        self.assertRaises(MissingSchema, websc.read_site, "not a website")
        self.assertRaises(ConnectionError, websc.read_site, "https://www.testtestest.com")

    def test_webscrapper_get_object(self):
        """
        Test WebScrapper get object will return a parsed webpage
        :return: None
        """
        websc = WebScrapper()
        websc.read_site("http://www.google.com")
        web_obj = websc.get_web_object()

        self.assertEqual(web_obj.title.string, "Google")

    def test_webscrapper_get_path(self):
        """
        Test WebScrapper get object will return a parsed webpage
        :return: None
        """
        websc = WebScrapper()
        websc.read_site("http://www.google.com")
        web_obj = websc.get_web_object()

        self.assertEqual(web_obj.title.string, "Google")

    def test_webscrapper_get_object_from_url(self):
        """
        Test WebScrapper get object will return a parsed webpage
        :return: None
        """
        websc = WebScrapper()
        websc.read_site("http://www.google.com")
        web_obj = websc.get_web_object_from_url("http://www.google.com")

        self.assertEqual(web_obj.title.string, "Google")

    def test_webscrapper_set_current_path(self):
        """
        Test WebScrapper get object will return a parsed webpage
        :return: None
        """
        websc = WebScrapper()
        websc.read_site("https://www.google.com")
        websc.read_site("https://www.google.com/doodles")
        websc.set_current_path("")
        web_obj = websc.get_web_object()

        self.assertEqual(web_obj.title.string, "Google")

        websc.set_current_path("/doodles")
        web_obj = websc.get_web_object()

        self.assertEqual(web_obj.title.string, "Google Doodles")

    def test_webscrapper_get_title(self):
        """
        Test WebScrapper get object will return a parsed webpage
        :return: None
        """
        websc = WebScrapper()
        websc.read_site("http://www.google.com")
        title = websc.get_title()

        self.assertEqual(title, "Google")

    def test_webscrapper_get_description(self):
        """
        Test WebScrapper get object will return a parsed webpage
        :return: None
        """
        websc = WebScrapper()
        websc.read_site("http://www.google.com/doodles")
        description = websc.get_description()

        self.assertEqual(description, "See more doodles at google.com/doodles!")

    def test_webscrapper_get_child_elements(self):
        """
        Test WebScrapper get object will return a parsed webpage
        :return: None
        """
        websc = WebScrapper()
        websc.read_site("http://www.google.com/doodles")
        web_obj = websc.get_web_object()
        web_child_obj = websc.get_child_elements(web_obj, "div", ids=["content"])[0]

        self.assertEqual(web_child_obj.get('id'), "content")

    def test_webscrapper_get_page_size(self):
        """
        Test WebScrapper get object will return a parsed webpage
        :return: None
        """
        websc = WebScrapper()
        size = websc.get_url_page_size("http://www.noel-wilson.co.uk")

        self.assertEqual(size, "3.1KiB")

if __name__ == "__main__":
    unittest.main()
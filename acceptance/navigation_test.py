import os

from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time


class NavigationTest(unittest.TestCase):

    def setUp(self):
        # Set up the Chrome WebDriver
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8000")

    def test_click_link_and_navigate(self):
        driver = self.driver

        # Find the link by link text and click it
        link = driver.find_element(By.LINK_TEXT, "Home")  # Change text as needed
        link.click()

        # Wait briefly for the page to load
        time.sleep(2)

        # Verify the new page has expected content
        self.assertIn("Message Board - Home", driver.title)  # Or check for a specific element/text

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

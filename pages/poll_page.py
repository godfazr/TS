# from selenium import webdriver
from locators.poll_locators import PollPageLocators

class PollPage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return 'https://stage1-vote.pollstream.com/8610'
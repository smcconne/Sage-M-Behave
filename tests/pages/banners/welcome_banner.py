from selenium import webdriver
import os
from configparser import ConfigParser
from selenium.webdriver.common.keys import Keys

def has_loaded(context):
	return context.utils.check_visible_xpath("//app-welcome-banner")

def close_welcome_banner(context):
	context.utils.select_xpath("//button[contains(@aria-label, 'Close Welcome Banner')]").click()
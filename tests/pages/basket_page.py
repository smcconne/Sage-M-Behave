from selenium import webdriver
import os
from configparser import ConfigParser
from selenium.webdriver.common.keys import Keys

def has_loaded(context):
	return context.utils.check_visible_xpath("//app-basket")

def go_to_address_select_page(context):
	context.utils.select_css_clickable("button#checkoutButton").click()
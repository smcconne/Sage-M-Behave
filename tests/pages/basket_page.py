from selenium import webdriver
import os
from configparser import ConfigParser
from selenium.webdriver.common.keys import Keys
import time

def has_loaded(context):
	return context.utils.check_visible_xpath("//app-basket")

def go_to_address_select_page(context):
	time.sleep(2)
	
	context.utils.wait_until_clickable_css("button#checkoutButton")
	context.utils.select_css("button#checkoutButton").click()
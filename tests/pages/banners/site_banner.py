from selenium import webdriver
import os
from configparser import ConfigParser
from selenium.webdriver.common.keys import Keys

def go_to_all_products_page(context):
	context.utils.select_xpath("//button[contains(@aria-label, 'Back to homepage')]").click()

def toggle_account_menu(context):
	context.utils.select_xpath("//button[contains(@aria-label, 'Show/hide account menu')]").click()

def go_to_login_page(context):
	toggle_account_menu(context)
	context.utils.select_xpath("//button[contains(@aria-label, 'Go to login page')]").click()
	
def check_if_logged_in(context):
	return context.utils.check_visible_xpath("//button[contains(@aria-label, 'Show the shopping cart')]")
	
def check_if_logged_out(context):
	return context.utils.check_invisible_xpath("//button[contains(@aria-label, 'Show the shopping cart')]")
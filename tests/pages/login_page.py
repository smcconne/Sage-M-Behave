from selenium import webdriver
import os
from configparser import ConfigParser
from selenium.webdriver.common.keys import Keys

def has_loaded(context):
	return context.utils.check_visible_xpath("//app-login")

def enter_credentials(context, email, password):
	context.utils.select_css("input#email").send_keys(email)
	context.utils.select_css("input#password").send_keys(password)
	context.utils.select_css("button#loginButton").click()

def toggle_account_menu(context):
	context.utils.select_xpath("//button[contains(@aria-label, 'Show/hide account menu')]").click()

def go_to_login_page(context):
	toggle_account_menu(context)
	context.utils.select_xpath("//button[contains(@aria-label, 'Go to login page')]").click()
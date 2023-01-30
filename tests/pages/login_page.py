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

def go_to_registration_page(context):
	context.utils.select_css("div#newCustomerLink a").click()
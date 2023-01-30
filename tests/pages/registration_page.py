from selenium import webdriver
import os
from configparser import ConfigParser
from selenium.webdriver.common.keys import Keys

def has_loaded(context):
	return context.utils.check_visible_xpath("//app-register")

def enter_credentials(context, email, password):
	context.utils.select_css("input#emailControl").send_keys(email)
	context.utils.select_css("input#passwordControl").send_keys(password)
	context.utils.select_css("input#repeatPasswordControl").send_keys(password)
	context.utils.select_css("mat-select[name='securityQuestion']").click()
	context.utils.select_css("mat-option#mat-option-14").click()
	# Really great movie (hard-coded for now)
	context.utils.select_css("input#securityAnswerControl").send_keys("Son of the White Mare")
	context.utils.select_css("button#registerButton").click()
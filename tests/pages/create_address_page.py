from selenium import webdriver
import os
from configparser import ConfigParser
from selenium.webdriver.common.keys import Keys
from faker import Faker

def has_loaded(context):
	return context.utils.check_visible_xpath("//app-address-create")

def enter_random_address(context):
	fake = Faker()
	context.utils.select_css("input#mat-input-1").send_keys(fake.country())
	context.utils.select_css("input#mat-input-2").send_keys(fake.name())
	context.utils.select_css("input#mat-input-3").send_keys("1234567890")
	context.utils.select_css("input#mat-input-4").send_keys(fake.postcode())
	context.utils.select_css("textarea#address").send_keys(fake.street_address())
	context.utils.select_css("input#mat-input-5").send_keys(fake.city())
	context.utils.select_css("input#mat-input-6").send_keys(fake.country_code())
	context.utils.select_css("button#submitButton").click()
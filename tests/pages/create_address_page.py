from selenium import webdriver
import os
from configparser import ConfigParser
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from faker import Faker
import time

def has_loaded(context):
	return context.utils.check_visible_xpath("//app-address-create")

def enter_random_address(context):
	time.sleep(2)
	fake = Faker()
	country = fake.country()
	name = fake.name()
	number = "1234567890"
	postcode = fake.postcode()
	address = fake.street_address()
	city = fake.city()
	state = fake.country_code()
	
	# Hacky solution, an absolute last resort (nothing else is working)
	context.utils.select_css("mat-icon.mat-search_icon-search").click()
	time.sleep(1)
	element = context.utils.select_css("input#mat-input-0")
	element.click()
	element.send_keys(Keys.TAB)
	element.send_keys(Keys.TAB)
	element.send_keys(Keys.TAB)
	element.send_keys(Keys.TAB)
	element.send_keys(country)
	element.send_keys(Keys.TAB)
	element.send_keys(name)
	element.send_keys(Keys.TAB)
	element.send_keys(number)
	element.send_keys(Keys.TAB)
	element.send_keys(postcode)
	element.send_keys(Keys.TAB)
	element.send_keys(address)
	element.send_keys(Keys.TAB)
	element.send_keys(city)
	element.send_keys(Keys.TAB)
	element.send_keys(state)
	time.sleep(2)
	context.utils.select_css("button#submitButton").click()
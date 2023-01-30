from behave.fixture import use_fixture_by_tag
from selenium import webdriver
import os
from configparser import ConfigParser
from selenium.webdriver.common.keys import Keys
import time
from behave.fixture import use_fixture_by_tag
from tests.utils.utils import UtilityFunctions
 
def before_all(context):
	config = ConfigParser()
	print((os.path.join(os.getcwd(), 'setup.cfg')))
	my_file = (os.path.join(os.getcwd(), 'setup.cfg'))
	config.read(my_file)

	# Browser is read from config and used to initialize utility functions with chosen driver
	browser = config.get('Environment', 'Browser')
	match browser:
		case "chrome":
			driver = webdriver.Chrome()
		case "firefox":
			driver = webdriver.Firefox()
		case other:
			driver = webdriver.Chrome()
	context.utils = UtilityFunctions(driver)
	context.utils.open('https://juice-shop.herokuapp.com/')
	
	# Set other context/environment variables
	context.standard_user_email = config.get('Environment', 'Standard_user_email')
	context.standard_user_password = config.get('Environment', 'Standard_user_password')
 
def after_all(context):
    context.utils.close()
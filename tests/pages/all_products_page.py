from selenium import webdriver
import os
from configparser import ConfigParser
from selenium.webdriver.common.keys import Keys
import time

def has_loaded(context):
	return context.utils.check_visible_xpath("//app-search-result")
	
def find_and_add_to_basket(context, search):
	context.utils.select_xpath("//*[text()[contains(.,'" + search + "')]]//ancestor::mat-card//button").click()
	time.sleep(2)
from selenium import webdriver
import os
from configparser import ConfigParser
from selenium.webdriver.common.keys import Keys

def has_loaded(context):
	return context.utils.check_visible_xpath("//app-search-result")
	
def find_and_add_to_cart(context, search):
	context.utils.select_xpath("//*[text()[contains(.,'" + search + "')]]//ancestor::mat-card//button").click()
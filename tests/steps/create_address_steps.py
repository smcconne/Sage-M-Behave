from selenium import webdriver
import os
from configparser import ConfigParser
from selenium.webdriver.common.keys import Keys
from behave import given, when, then
from tests.pages import create_address_page

@when(u'I enter a new address')
def step_impl(context):
	create_address_page.enter_random_address(context)
from selenium import webdriver
import os
from configparser import ConfigParser
from selenium.webdriver.common.keys import Keys
from behave import given, when, then
from tests.pages import login_page
from tests.pages.banners import site_banner

@when(u'I navigate to the {target_page} page')
def step_impl(context, target_page):
	match target_page:
		case "login":
			site_banner.go_to_login_page(context)
		case "all products":
			site_banner.go_to_all_products_page(context)
		case other:
			context.scenario.skip(reason='page name not recognised - see navigation_steps.py: I navigate to the ' + target_page + ' page')

@then(u'The {target_page} page has loaded')
def step_impl(context, target_page):
	match target_page:
		case "login":
			assert login_page.has_loaded(context)
		case "all products":
			assert login_page.has_loaded(context)
		case other:
			context.scenario.skip(reason='page name not recognised - see navigation_steps.py: The ' + target_page + ' page has loaded')
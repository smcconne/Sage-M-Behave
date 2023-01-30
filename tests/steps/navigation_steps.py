from selenium import webdriver
import os
from configparser import ConfigParser
from selenium.webdriver.common.keys import Keys
from behave import given, when, then
from tests.pages import login_page, registration_page, basket_page, address_select_page, create_address_page
from tests.pages.banners import site_banner

@when(u'I navigate to the {target_page} page')
def step_impl(context, target_page):
	match target_page:
		case "login" | "registration":
			site_banner.go_to_login_page(context)
			if target_page == "registration":
				login_page.go_to_registration_page(context)
		case "all products":
			site_banner.go_to_all_products_page(context)
		case "basket" | "address select" | "create address":
			site_banner.go_to_basket_page(context)
			assert basket_page.has_loaded(context)
			if target_page == "address select":
				basket_page.go_to_address_select_page(context)
				assert address_select_page.has_loaded(context)
				if target_page == "create address":
					address_select_page.go_to_create_address_page(context)
		case other:
			context.scenario.skip(reason='page name not recognised - see navigation_steps.py: When I navigate to the ' + target_page + ' page')

@then(u'The {target_page} page has loaded')
def step_impl(context, target_page):
	match target_page:
		case "login":
			assert login_page.has_loaded(context)
		case "registration":
			assert registration_page.has_loaded(context)
		case "all products":
			assert login_page.has_loaded(context)
		case "basket":
			assert basket_page.has_loaded(context)
		case "address select":
			assert address_select_page.has_loaded(context)
		case "create address":
			assert create_address_page.has_loaded(context)
		case other:
			context.scenario.skip(reason='page name not recognised - see navigation_steps.py: Then the ' + target_page + ' page has loaded')
from selenium import webdriver
import os
from configparser import ConfigParser
from selenium.webdriver.common.keys import Keys
from behave import given, when, then
from tests.pages import login_page
from tests.pages.banners import site_banner, welcome_banner

@given(u'I close the welcome banner')
def step_impl(context):
	if welcome_banner.has_loaded(context):
		welcome_banner.close_welcome_banner(context)

@when(u'I log in as {user_type} user')
def step_impl(context, user_type):
	if user_type == "standard":
		login_page.enter_credentials(context, context.standard_user_email, context.standard_user_password)
	if user_type == "admin":
		context.scenario.skip(reason='admin login not implemented - see login_steps.py: I login as admin user')

@then(u'I should be logged in')
def step_impl(context):
	assert site_banner.check_if_logged_in(context)
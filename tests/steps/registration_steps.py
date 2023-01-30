from selenium import webdriver
import os
from configparser import ConfigParser
from selenium.webdriver.common.keys import Keys
from behave import given, when, then
from tests.pages import login_page
from tests.pages.banners import site_banner, welcome_banner

@when(u'I register as standard user')
def step_impl(context, user_type):
	registration_page.enter_credentials(context, context.standard_user_email, context.standard_user_password)
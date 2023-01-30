from selenium import webdriver
import os
from configparser import ConfigParser
from selenium.webdriver.common.keys import Keys
from behave import given, when, then
from tests.pages import registration_page
from tests.pages.banners import site_banner, welcome_banner
from faker import Faker

@when(u'I register as {user_type} user')
def step_impl(context, user_type):
	if user_type == "standard":
		registration_page.enter_credentials(context, context.standard_user_email, context.standard_user_password)
	elif user_type == "random":
		fake = Faker()
		context.random_user_email = fake.email()
		context.random_user_password = fake.password()
		registration_page.enter_credentials(context, context.random_user_email, context.random_user_password)
from selenium import webdriver
import os
from configparser import ConfigParser
from selenium.webdriver.common.keys import Keys
from behave import given, when, then
from tests.pages import all_products_page
from faker import Faker

@when(u'I add {search} to basket')
def step_impl(context, search):
	all_products_page.find_and_add_to_basket(context, search)
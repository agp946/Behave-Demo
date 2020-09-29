from behave import *
from selene.api import browser
from selene.conditions import *

@Given('user has open the site')
def step_impl(context):
    browser.should(title_containing("My Store"))

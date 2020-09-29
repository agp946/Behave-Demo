from behave import *
from selene.api import browser
from selene.conditions import *
import tests.pages.page_header as this

@when("user in page header clicks link 'Sign up'")
def step_impl(context):
    this.link_sign_in().click()
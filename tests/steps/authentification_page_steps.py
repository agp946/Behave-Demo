from behave import *
import tests.pages.authentification_page as this_page
from selene.conditions import *


@then('system opens \'Authentification\' page')
def step_impl(context):
    this_page.title().should_be(visible)


@when('user on \'Authentification\' page in \'Create an account\' from types \'email\' in input field \'Email address\'')
def step_impl(context):
    import time
    email=str(int(round(time.time() * 1000)))
    this_page.create_account_form_email_input().clear()
    this_page.create_account_form_email_input().type(email+"@example.com")


@when('user on \'Authentification\' page in \'Create an account\' from clicks button \'Create an account\'')
def step_impl(context):
    this_page.create_account_form_create_btn().click()

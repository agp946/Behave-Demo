from behave import *
import tests.pages.my_account_page as this_page
from selene.conditions import *


@then('system opens \'My account\' page')
def step_impl(context):
    this_page.title().should_be(visible)



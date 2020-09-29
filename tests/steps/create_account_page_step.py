from behave import *
from selene.conditions import *

import tests.pages.create_account_page as this_page


@then("system opens 'Create an Account' page")
def step_impl(context):
    this_page.title().should_be(visible)


@when("user on 'Create an Account' page on \"{form_name}\" form chooses \"{btn_name}\" radiobutton")
def step_impl(context, form_name, btn_name):
    if this_page.info_form_mr_radio_button_is_checked(form_name, btn_name).matching(exist):
        this_page.info_form_mr_radio_button(form_name, btn_name).click()
        this_page.info_form_mr_radio_button_is_checked(form_name, btn_name).should(exist)


@when('user on \'Create an Account\' page on "{form_name}" form types "{string}" in input field "{input_name}"')
def step_impl(context, form_name, string, input_name):
    this_page.info_form_input(form_name, input_name).scroll_to()
    this_page.info_form_input(form_name, input_name).clear()
    this_page.info_form_input(form_name, input_name).type(string)

#text area
@when('user on \'Create an Account\' page on "{form_name}" form types "{string}" in text area "{input_name}"')
def step_impl(context, form_name, string, input_name):
    this_page.info_form_textarea(form_name, input_name).type(string)

# combo
@when('user on \'Create an Account\' page on "{form_name}" form in combobox "{name}" choose "{option}"')
def step_impl(context, form_name, name, option):
    context.execute_steps(u'''
    When user on 'Create an Account' page on "{form_name}" form clicks on combobox "{text}"
    Then system on 'Create an Account' page on "{form_name}" form shows content of combobox "{text}"
    When user on 'Create an Account' page on "{form_name}" form in combobox "{text}" clicks on option "{value}"
    Then system on 'Create an Account' page on "{form_name}" form in combobox "{text}" shows selected option "{value}"
    '''.format(form_name=form_name, text=name, value=option))


@step('user on \'Create an Account\' page on "{form_name}" form clicks on combobox "{name}"')
@when('user on \'Create an Account\' page on "{form_name}" form clicks on combobox "{name}"')
def step_impl(context, form_name, name):
    this_page.info_form_combo_control(form_name, name).click()


@then(
    'system on \'Create an Account\' page on "{form_name}" form shows content of combobox "{name}"')
def step_impl(context, form_name, name):
    this_page.info_form_combo_options(form_name, name).should(appear)


@when('user on \'Create an Account\' page on "{form_name}" form in combobox "{name}" clicks on option "{option}"')
def step_impl(context, form_name, name, option):
    this_page.info_form_combo_option(form_name, name, option).click()


@then('system on \'Create an Account\' page on "{form_name}" form hides content of combobox "{name}"')
def step_impl(context, form_name, name):
    this_page.info_form_combo_options(form_name, name).should(disappear)


@then('system on \'Create an Account\' page on "{form_name}" form in combobox "{name}" shows selected option "{option}"')
def step_impl(context, form_name, name, option):
    this_page.info_form_combo_selected_option(form_name, name, option).should(exist)


# --- End combo

# Date part combo
@when('user on \'Create an Account\' page on "{form_name}" form in \'Date of Birth\' parameter '
      'in combobox "{date_part}" choose "{option}"')
def step_impl(context, form_name, date_part, option):
    context.execute_steps(u'''
    When user on 'Create an Account' page on "{form_name}" form in 'Date of Birth' parameter clicks on combobox "{text}"
    Then system on 'Create an Account' page on "{form_name}" form in 'Date of Birth' parameter shows content of combobox "{text}"
    When user on 'Create an Account' page on "{form_name}" form in 'Date of Birth' parameter in combobox "{text}" clicks on option "{value}"
    Then system on 'Create an Account' page on "{form_name}" form in 'Date of Birth' parameter in combobox "{text}" shows selected option "{value}"
    '''.format(form_name=form_name, text=date_part, value=option))

@when(
    'user on \'Create an Account\' page on "{form_name}" form in \'Date of Birth\' parameter clicks on combobox "{date_part}"')
def step_impl(context, form_name, date_part):
    this_page.info_form_combo_date_control(form_name, parse_date_part(date_part)).click()


@then(
    'system on \'Create an Account\' page on "{form_name}" form in \'Date of Birth\' parameter shows content of combobox "{date_part}"')
def step_impl(context, form_name, date_part):
    this_page.info_form_combo_date_options(form_name, parse_date_part(date_part)).should(appear)


@when('user on \'Create an Account\' page on "{form_name}" form in \'Date of Birth\' parameter '
      'in combobox "{date_part}" clicks on option "{option}"')
def step_impl(context, form_name, date_part, option):
    import time
    this_page.info_form_combo_date_option(form_name, parse_date_part(date_part), option).click()


@then('system on \'Create an Account\' page on "{form_name}" form in \'Date of Birth\' parameter '
      'hides content of combobox "{date_part}"')
def step_impl(context, form_name, date_part):
    this_page.info_form_combo_date_options(form_name, parse_date_part(date_part)).should(disappear)


@then('system on \'Create an Account\' page on "{form_name}" form in \'Date of Birth\' parameter '
      'in combobox "{date_part}" shows selected option "{option}"')
def step_impl(context, form_name, date_part, option):
    this_page.info_form_combo_date_selected_option(form_name, parse_date_part(date_part), option).should(exist)


# --- End Date part combo

@step('user on \'Create an Account\' page on "{form_name}" form set checkbox "{name}"')
def step_impl(context, form_name, name):
    if not this_page.info_form_checkbox_is_checked(form_name, name).matching(exist):
        this_page.info_form_checkbox(form_name, name).click()
        this_page.info_form_checkbox_is_checked(form_name, name).should(appear)

# Utils
def parse_date_part(date_part):
    date_parts = {'Day': '1', 'Month': '2', 'Year': '3'}
    try:
        return date_parts[date_part]
    except KeyError:
        raise ConditionMismatchException(
            expected='Data part should be in ["Day","Month","Year"]',
            actual=date_part)

#text area
@when('user on \'Create an Account\' page clicks on button \'Register\'')
def step_impl(context):
    this_page.submit_btn().click()
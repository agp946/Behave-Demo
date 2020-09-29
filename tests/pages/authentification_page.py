from selene.api import s, by


def title():
    return s(by.xpath("//h1[@class='page-heading'][.='Authentication']"))


def create_account_form():
    return s(by.xpath("//form[@id='create-account_form']"))


def create_account_form_email_input():
    return create_account_form().s(by.xpath(".//div[contains(@class,'form-group')][./label[.='Email address']]/input"))


def create_account_form_create_btn():
    return create_account_form().s(by.xpath(".//button[./span[contains(.,'Create an account')]]"))


def login_form():
    return s(by.xpath("//form[@id='login_form']"))


def login_form_email_input():
    return login_form().s(by.xpath(".//div[contains(@class,'form-group')][./label[.='Email address']]/input"))


def login_form_password_input():
    return login_form().s(by.xpath(".//div[contains(@class,'form-group')][./label[.='Password']]//input"))


def login_form_create_signin():
    return create_account_form().s(by.xpath(".//button[./span[contains(.,'Sign in')]]"))

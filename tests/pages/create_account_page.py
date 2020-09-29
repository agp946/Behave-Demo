from selene.api import s, by


def title():
    return s(by.xpath("//h1[@class='page-heading'][.='Create an account']"))


def info_form(name):
    return s(by.xpath("//div[@class='account_creation'][./h3[.='{}']]".format(name)))


def info_form_mr_radio_button(name, btn_name):
    return info_form(name).s(by.xpath(".//div[@class='radio-inline'][./node()[contains(.,'{}')]]".format(btn_name)))


def info_form_mr_radio_button_is_checked(name, btn_name):
    return info_form_mr_radio_button(name, btn_name).s(by.xpath(".//span[@class='checked']".format(btn_name)))


def info_form_mrs_radio_button(name):
    return info_form(name).s(by.xpath(".//div[@class='radio-inline'][./node()[contains(.,'Mrs.')]]"))


def info_form_input(name, caption):
    return info_form(name).s(
        by.xpath("./node()[contains(@class,'form-group')][./label[contains(.,'{}')]]/input".format(caption)))

# TextArea
def info_form_textarea(name, caption):
    return info_form(name).s(
        by.xpath("./node()[contains(@class,'form-group')][./label[contains(.,'{}')]]/textarea".format(caption)))

# Check box
def info_form_checkbox(name, caption):
    return info_form(name).s(
        by.xpath("./node()[contains(@class,'checkbox')][./label[contains(.,'{}')]]//div[contains(@class,'checker')]".format(caption)))

def info_form_checkbox_is_checked(name, caption):
    return info_form_checkbox(name, caption).s("./span[contains(@class,'checked')]")

# Combo
def info_form_combo(name, caption):
    return info_form(name).s(by.xpath("./node()[contains(@class,'form-group')][./label[contains(.,'{}')]]"
                                      "/div[contains(@class,'selector')]".format(caption)))


def info_form_combo_control(name, caption):
    return info_form_combo(name, caption).s(by.xpath("./self::node()"))


def info_form_combo_options(name, caption):
    return info_form_combo(name, caption).s(by.xpath("./self::node()[contains(@class,'focus')]"))


def info_form_combo_option(name, caption, item):
    return info_form_combo_control(name, caption).s(by.xpath("./select/option[contains(.,'{}')]".format(item)))

def info_form_combo_selected_option(name, caption, selected):
    return info_form_combo_control(name, caption).s(by.xpath("./span[contains(.,'{}')]".format(selected)))


# Combo Date
def info_form_combo_date(name, num):
    return info_form(name).s(by.xpath("./node()[contains(@class,'form-group')][./label[contains(.,'Date of Birth')]]"
                                      "/div[@class='row']/div[{}]/div[contains(@class,'selector')]".format(num)))


def info_form_combo_date_control(name, num):
    return info_form_combo_date(name, num).s(by.xpath("./self::node()"))


def info_form_combo_date_options(name, num):
    return info_form_combo_date(name, num).s(by.xpath("./self::node()[contains(@class,'focus')]"))


def info_form_combo_date_option(name, num, item):
    return info_form_combo_date_control(name, num).s(by.xpath("./select/option[contains(.,'{}')]".format(item)))

def info_form_combo_date_selected_option(name, num, selected):
    return info_form_combo_date_control(name, num).s(by.xpath("./span[contains(.,'{}')]".format(selected)))

def submit_btn():
    return s(by.xpath("//button[./span[contains(.,'Register')]]"))

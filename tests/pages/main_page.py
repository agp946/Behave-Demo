from selene.api import s, by
def logo():
    return s(by.xpath("//img[contains(@class.'logo')][contains(@src,'http://automationpractice.com/img/logo.jpg')]"))
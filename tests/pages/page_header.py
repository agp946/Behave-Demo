from selene.api import s, by


def link_sign_in():
    return s(by.xpath("//header//a[contains(.,'Sign in')]"))
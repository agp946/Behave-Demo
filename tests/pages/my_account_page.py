from selene.api import s, by

def title():
    return s(by.xpath("//h1[@class='page-heading'][.='My account']"))
from selene import browser, be, have


def test_find_element():
    browser.open('/')
    non_existent_value = 'erfvrbbtytmntybmbtvmvyfn'

    browser.element('[name="q"]').should(be.blank).type(non_existent_value).press_enter()
    browser.element('.card-section [role=heading]').should(
        have.text(f'{non_existent_value}'))

from selene import browser, be, have


def test_positive():
    browser.open('/')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))

def test_notext ():
    browser.open('https://ya.ru')
    browser.element('[name="text"]').should(be.blank).type('olololo').press_enter()
    browser.element('[id="search"]').should(have.no.text('pumpum'))

def test_find_element():
    browser.open('/')
    non_existent_value = 'erfvrbbtytmntybmbtvmvyfn'

    browser.element('[name="q"]').should(be.blank).type(non_existent_value).press_enter()
    browser.element('.card-section [role=heading]').should(
        have.text(f'No se han encontrado resultados para tu búsqueda ({non_existent_value}).'))

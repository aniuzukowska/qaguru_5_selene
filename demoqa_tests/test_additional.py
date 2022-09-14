from selene import have
from selene.support.shared.jquery_style import s, ss
import time


def test_add_fourth_row(open_and_quit_browser_webtables):
    s('#addNewRecordButton').click()
    s('#firstName').type('Maria')
    s('#lastName').type('Sklodowska')
    s('#userEmail').type('maria-sklodowska@gmail.com')
    s('#age').type('22')
    s('#salary').type('10000')
    s('#department').type('Main Department')
    s('#submit').click()

    ss('.rt-tr-group')[3].ss('.rt-td').should(have.texts(
        'Maria',
        'Sklodowska',
        '22',
        'maria-sklodowska@gmail.com',
        '10000',
        'Main Department',
        ''
    ))


def test_edit_second_row(open_and_quit_browser_webtables):
    s('#edit-record-2').click()
    s('#firstName').clear().type('Maria')
    s('#lastName').clear().type('Sklodowska')
    s('#userEmail').clear().type('maria-sklodowska@gmail.com')
    s('#age').clear().type('22')
    s('#salary').clear().type('10000')
    s('#department').clear().type('Main Department')
    s('#submit').click()

    ss('.rt-tr-group')[1].ss('.rt-td').should(have.texts(
        'Maria',
        'Sklodowska',
        '22',
        'maria-sklodowska@gmail.com',
        '10000',
        'Main Department',
        ''
    ))


def test_delete_third_row(open_and_quit_browser_webtables):
    s('#delete-record-2').click()
    ss('.rt-tr-group')[1].ss('.rt-td').should(have.no.texts(
        'Alden',
        'Cantrell',
        '45',
        'alden@example.com',
        '12000',
        'Compliance',
        ''
    ))








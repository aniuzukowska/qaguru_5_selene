from selene.support.shared.jquery_style import s, ss
from selene import command, have
import files


def test_submit_student_details(open_and_quit_browser_automation_practice_form):
    s('#firstName').type('Maria')
    s('#lastName').type('Sklodowska')
    s('#userEmail').type('maria-sklodowska@gmail.com')
    s('.custom-control-label[for="gender-radio-2"]').click()
    s('#userNumber').type('1234567890')

    s('#dateOfBirthInput').click()

    # Выбираем месяц: февраль
    s('.react-datepicker__month-select').click()
    ss('.react-datepicker__month-select option')[1].click()

    # Выбираем год: 2000
    s('.react-datepicker__year-select').click()
    year = ss('.react-datepicker__year-select option')[100]
    year.perform(command.js.scroll_into_view)
    year.click()

    # Выбираем число: 7
    s('.react-datepicker__day--007').click()

    s('#subjectsInput').type('Physics').press_enter()
    s('.custom-control-label[for="hobbies-checkbox-3"]').click()

    # вставить картинку
    s('#uploadPicture').send_keys(files.abs_path_from_project_root('resources/picture.jpg'))

    s('#currentAddress').type('France, Paris')

    state = s('#state')
    state.perform(command.js.scroll_into_view)
    state.click()
    s('#react-select-3-option-2').click()

    s('#city').click()
    s('#react-select-4-option-0').click()

    s('#submit').perform(command.js.click)

    ss('.table td').should(have.texts(
        'Student Name',
        'Maria Sklodowska',
        'Student Email',
        'maria-sklodowska@gmail.com',
        'Gender',
        'Female',
        'Mobile',
        '1234567890',
        'Date of Birth',
        '07 February,2000',
        'Subjects',
        'Physics',
        'Hobbies',
        'Music',
        'Picture',
        'picture.jpg',
        'Address',
        'France, Paris',
        'State and City',
        'Haryana Karnal'
    ))






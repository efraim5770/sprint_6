import pytest
import allure
from pages.main_page import MainPage
from data import TestData


class TestMainPageFaq:
    @allure.title('Проверка раздела "Вопросы о важном"')
    @allure.description('Проверка появления нужного текста при нажатии на каждую иконку развертывания в разделе')
    @pytest.mark.parametrize('question_number, expected_answer', TestData.test_data_expected_answer_faq)
    def test_click_faq_expand_icons_text_is_expected(self, driver, question_number, expected_answer):
        main_page = MainPage(driver)
        main_page.scroll_to_faq_section()
        main_page.wait_visibility_of_faq_questions(question_number)
        main_page.click_on_faq_question(question_number)
        main_page.wait_visibility_of_faq_answer(question_number)
        displayed_text = main_page.get_displayed_text_from_faq_answer(question_number)
        assert displayed_text == expected_answer
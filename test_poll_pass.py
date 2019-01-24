from pages.poll_page import PollPage
from locators.poll_locators import PollPageLocators

def test_if_poll_can_be_completed():
    poll_page = PollPage()
    poll_page.setup()

    poll_page.submit_continue_click(PollPageLocators.SUBMIT_BUTTON)

    poll_page.select_radio_group_option(PollPageLocators.RADIO_GROUP_Q1, 2)
    poll_page.select_dropdown_option(PollPageLocators.SINGLE_SELECT_Q2, 3)
    poll_page.select_radio_group_option(PollPageLocators.RADIO_IMAGE_GROUP_Q3, 2)
    poll_page.submit_continue_click(PollPageLocators.SUBMIT_BUTTON)

    poll_page.submit_continue_click(PollPageLocators.CONTINUE_BUTTON)

    poll_page.select_checkbox_options(PollPageLocators.CHECKBOX_GROUP_Q4, (1, 3))
    poll_page.select_checkbox_options(PollPageLocators.CHECKBOX_IMAGE_GROUP_Q5, (1, 4))
    poll_page.submit_continue_click(PollPageLocators.SUBMIT_BUTTON)

    poll_page.submit_continue_click(PollPageLocators.CONTINUE_BUTTON)

# Radio rating w/o n/a
    poll_page.select_radio_group_option(PollPageLocators.RATING_RADIO_Q6_ANSWER_A, 1)
    poll_page.select_radio_group_option(PollPageLocators.RATING_RADIO_Q6_ANSWER_B, 2)
    poll_page.select_radio_group_option(PollPageLocators.RATING_RADIO_Q6_ANSWER_C, 10)
    poll_page.select_radio_group_option(PollPageLocators.RATING_RADIO_Q6_ANSWER_D, 5)
# Radio rating w/ n/a
    poll_page.select_radio_group_option(PollPageLocators.RATING_RADIO_Q7_ANSWER_A, 2)
    poll_page.select_radio_group_option(PollPageLocators.RATING_RADIO_Q7_ANSWER_B, 3)
    poll_page.select_radio_group_option(PollPageLocators.RATING_RADIO_Q7_ANSWER_C, 11)
    poll_page.select_radio_group_option(PollPageLocators.RATING_RADIO_Q7_ANSWER_D, 6)
# Dropdown rating w/o n/a
    poll_page.select_dropdown_rating_options(PollPageLocators.RATING_SELECT_Q8, (1, 2, 10, 10))
# Dropdown rating w/ n/a
    poll_page.select_dropdown_rating_options(PollPageLocators.RATING_SELECT_Q9, (1, 2, 11, 11))

    poll_page.submit_continue_click(PollPageLocators.SUBMIT_BUTTON)

    poll_page.submit_continue_click(PollPageLocators.CONTINUE_BUTTON)

    poll_page.set_rating_options_by_drag_and_drop(PollPageLocators.RANKING_SELECT_Q10_LINE_2, PollPageLocators.RANKING_SELECT_Q10_LINE_1)

    poll_page.submit_continue_click(PollPageLocators.SUBMIT_BUTTON)

    poll_page.submit_continue_click(PollPageLocators.CONTINUE_BUTTON)

    poll_page.set_rating_options_by_drag_and_drop(PollPageLocators.RANKING_SELECT_Q11_LINE_2, PollPageLocators.RANKING_SELECT_Q11_LINE_1)
    poll_page.enter_answer_to_text_field(PollPageLocators.TEXT_INPUT_Q12, '1234')

    poll_page.submit_continue_click(PollPageLocators.SUBMIT_BUTTON)

    poll_page.submit_continue_click(PollPageLocators.CONTINUE_BUTTON)

    poll_page.verify_acknowledgement_message(PollPageLocators.ACKNOWLEDGEMENT, 'a really short message -thanks')
    poll_page.teardown()
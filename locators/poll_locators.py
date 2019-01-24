from selenium.webdriver.common.by import By

class PollPageLocators:
# Submit/continue button
    SUBMIT_BUTTON = By.NAME, 'vote_button'
    CONTINUE_BUTTON = By.CLASS_NAME, 'result-continue-button.template_default'
# Question 1 answer
    RADIO_GROUP_Q1 = By.NAME, 'mqp1_answer_id'
# Question 2 answer
    SINGLE_SELECT_Q2 = By.NAME, 'mqp2_answer_id'
# Question 3 answer
    RADIO_IMAGE_GROUP_Q3 = By.NAME, 'mqp3_answer_id'
# Question 4 answer
    CHECKBOX_GROUP_Q4 = By.NAME, 'mqp1_answer_id[]'
# Question 5 answer
    CHECKBOX_IMAGE_GROUP_Q5 = By.NAME, 'mqp2_answer_id[]'
# Question 6 answers    
    RATING_RADIO_Q6_ANSWER_A = By.NAME, '268852_mqp1_answer_id[]'
    RATING_RADIO_Q6_ANSWER_B = By.NAME, '268853_mqp1_answer_id[]'
    RATING_RADIO_Q6_ANSWER_C = By.NAME, '268854_mqp1_answer_id[]'
    RATING_RADIO_Q6_ANSWER_D = By.NAME, '268855_mqp1_answer_id[]'
# Question 7 answers
    RATING_RADIO_Q7_ANSWER_A = By.NAME, '268864_mqp2_answer_id[]'
    RATING_RADIO_Q7_ANSWER_B = By.NAME, '268865_mqp2_answer_id[]'
    RATING_RADIO_Q7_ANSWER_C = By.NAME, '268866_mqp2_answer_id[]'
    RATING_RADIO_Q7_ANSWER_D = By.NAME, '268867_mqp2_answer_id[]'
# Question 8 answers
    RATING_SELECT_Q8 = By.NAME, 'mqp3_answer_id[]'
# Question 9 answers   
    RATING_SELECT_Q9 = By.NAME, 'mqp4_answer_id[]'
# Question 10 answer
    RANKING_SELECT_Q10_LINE_1 = By.ID, 'ans_:268869-1'
    RANKING_SELECT_Q10_LINE_2 = By.ID, 'ans_:268870-1'
# Question 11 answer
    RANKING_SELECT_Q11_LINE_1 = By.ID, 'ans_:268873-1'
    RANKING_SELECT_Q11_LINE_2 = By.ID, 'ans_:268874-1'
# Question 12 answer
    TEXT_INPUT_Q12 = By.NAME, 'mqp2_freeTextAnswer'
# Last page with acknowledgement
    ACKNOWLEDGEMENT = By.CLASS_NAME, 'ps-acknowledgement'
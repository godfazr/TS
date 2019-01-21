from selenium.webdriver.common.by import By

class PollPageLocators:
# Submit/continue button
    VOTE_BUTTON = By.NAME, 'vote_button'
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
    RATING_SELECT_Q8_ANSWER_A = By.ID, 'ps_answer_PSPoll_268860'
    RATING_SELECT_Q8_ANSWER_B = By.ID, 'ps_answer_PSPoll_268861'
    RATING_SELECT_Q8_ANSWER_C = By.ID, 'ps_answer_PSPoll_268862'
    RATING_SELECT_Q8_ANSWER_D = By.ID, 'ps_answer_PSPoll_268863'
# Question 9 answers   
    RATING_SELECT_Q9_ANSWER_A = By.ID, 'ps_answer_PSPoll_268856'
    RATING_SELECT_Q9_ANSWER_B = By.ID, 'ps_answer_PSPoll_268857'
    RATING_SELECT_Q9_ANSWER_C = By.ID, 'ps_answer_PSPoll_268858'
    RATING_SELECT_Q9_ANSWER_D = By.ID, 'ps_answer_PSPoll_268859'
# Question 10 answer
    RANKING_SELECT_Q10_ANSWER_A = By.NAME, 'ans_:268869-1-select'
    RANKING_SELECT_Q10_ANSWER_B = By.NAME, 'ans_:268870-1-select'
    RANKING_SELECT_Q10_ANSWER_C = By.NAME, 'ans_:268871-1-select'
    RANKING_SELECT_Q10_ANSWER_D = By.NAME, 'ans_:268872-1-select'
# Question 11 answer
    RANKING_SELECT_Q11_ANSWER_A = By.NAME, 'ans_:268873-1-select'
    RANKING_SELECT_Q11_ANSWER_B = By.NAME, 'ans_:268874-1-select'
    RANKING_SELECT_Q11_ANSWER_C = By.NAME, 'ans_:268875-1-select'
    RANKING_SELECT_Q11_ANSWER_D = By.NAME, 'ans_:268876-1-select'
# Question 12 answer
    TEXT_INPUT_Q12 = By.NAME, 'mqp2_freeTextAnswer'
# Last page with acknowledgement
    ACKNOWLEDGEMENT = By.NAME, 'ps-acknowledgement'
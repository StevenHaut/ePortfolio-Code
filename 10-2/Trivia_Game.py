# Defines the 'Question' Class.
class Question:
    # The __init__ method initializes the attributes.
    def __init__(self, question):
        # Defines the list 'question_list' as the variable 'question'.
        question_list = question
        self.__question = question_list[0]
        self.__possible_answer_1 = question_list[1]
        self.__possible_answer_2 = question_list[2]
        self.__possible_answer_3 = question_list[3]
        self.__possible_answer_4 = question_list[4]
        self.__correct_answer = question_list[5]

    # The set_question method sets the question.
    def set_question(self, question):
        self.__question = question

    # The set_possible_answer1 method sets possible_answer1.
    def set_possible_answer1(self, answer1):
        self.__possible_answer_1 = answer1

    # The set_possible_answer2 method sets possible_answer2.
    def set_possible_answer2(self, answer2):
        self.__possible_answer_2 = answer2

    # The set_possible_answer3 method sets possible_answer3.
    def set_possible_answer3(self, answer3):
        self.__possible_answer_3 = answer3

    # The set_possible_answer4 method sets possible_answer4.
    def set_possible_answer4(self, answer4):
        self.__possible_answer_4 = answer4

    # The set_correct_answer method sets correct_answer.
    def set_correct_answer(self, answer):
        self.__correct_answer = answer

    # The 'get_question' method returns the question.
    def get_question(self):
        return self.__question

    # The 'get_possible_answer1' method returns 'possible_answer1'.
    def get_possible_answer1(self):
        return self.__possible_answer_1

    # The 'get_possible_answer2' method returns 'possible_answer2'.
    def get_possible_answer2(self):
        return self.__possible_answer_2

    # The 'get_possible_answer3' method returns 'possible_answer3'.
    def get_possible_answer3(self):
        return self.__possible_answer_3

    # The 'get_possible_answer4' method returns 'possible_answer4'.
    def get_possible_answer4(self):
        return self.__possible_answer_4

    # The 'get_correct_answer' method returns the correct answer.
    def get_correct_answer(self):
        return self.__correct_answer

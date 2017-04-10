# Imports the program 'Trivia_Game'.
import Trivia_Game
# Defines the global variable 'player1_points'.
player1_points = 0
# Defines the global variable 'player2_points'.
player2_points = 0

# Creates a dictionary with all the trivia question information.
question_dictionary = {1: ('How many furlongs are there in one mile?', '2', '4', '8', '16', 3),
                       2: ("What's the lifespan of a human red blood cell?", '20 Years', '30 Years', '60 Years', '120 Years', 4),
                       3: ("What is the longest type of cell in the body?", 'Neurons', 'Skin', 'Muscle', 'Bone Tissue', 1),
                       4: ("How much salt does the average human body contain?", '150 grams', '250 grams', '350 grams', '450 grams', 2),
                       5: ("Which is the rarest blood type in humans?", 'O Positive', 'O Negative', 'AB Positive', 'AB Negative', 4),
                       6: ("What is the hardest substance in the human body?", 'Femur Bone', 'Temporal Bone', 'Tooth Enamel', 'Muscle', 3),
                       7: ("How much copper is in sterling silver?", 'None', '2.5%', '7.5%', '10%', 3),
                       8: ("What is the strongest known magnet in the Universe?", 'Neodymium Magnets', 'Horseshoe Magnets', 'Metal Planets', 'Neutron Stars', 4),
                       9: ("How far is the moon away from Earth?", '256,000 km', '376,000 km', '457,000 km', '523,000 km', 2),
                       10: ("How old is our Sun?", '4.5 Billion Years', '6 Billion Years', '7.5 Billion Years', '10 Billion Years', 1)}


# Defines the 'main' function.
def main():
    ask_questions()
    display_results()


# Defines the 'ask_questions' function.
def ask_questions():
    # Calls the global dictionary 'question_dictionary'.
    global question_dictionary
    # Defines the counter variable player1 as equal to zero.
    player1 = 0
    # Defines the counter variable player2 as equal to zero.
    player2 = 0
    # Calls the global variable 'player1_points'.
    global player1_points
    # Calls the global variable 'player2_points'.
    global player2_points
    # Repeats everything below 10 times, for 10 questions.
    for question in range(1, 11):
        # Creates an instance of the Trivia_Game.
        current_question = Trivia_Game.Question(question_dictionary[question])
        # The variable trivia_questions equals the called method 'get_question'.
        trivia_question = current_question.get_question() + "\n"
        # The variable trivia_answers equals the called methods 'get_possible_answer(1-4)'.
        trivia_answers = "#1) " + current_question.get_possible_answer1() + "\n" + \
                         "#2) " + current_question.get_possible_answer2() + "\n" + \
                         "#3) " + current_question.get_possible_answer3() + "\n" + \
                         "#4) " + current_question.get_possible_answer4()
        # If the counter variable 'player1' is less than 5, the current player is equal to 1.
        if player1 < 5:
            current_player = 1
        # If the if command is false, then everything below executes.
        else:
            # If the counter variable 'player2' is less than 5, the current player is equal to 2.
            if player2 < 5:
                current_player = 2
        # Define the variable 'answer' as equal to 0.
        answer = 0
        # While the answer is not 1, 2, 3, or 4, everything below executes.
        while answer not in [1, 2, 3, 4]:
            # Executes a try suite.
            try:
                # The variable 'answer' is equal to the entered value.
                answer = int(input("Question #" + str(question) + " for " + 'player #' + str(current_player) + ": \n"
                                   + trivia_question + trivia_answers + "\nEnter your answer as a number (1-4): "))
                # If the entered value is not 1, 2, 3, or 4, a message is displayed on the screen.
                if answer not in [1, 2, 3, 4]:
                    print("The answer must be 1, 2, 3, or 4. Try Again. \n")
            # The except clause specifies the ValueError exception.
            except ValueError:
                print('The answer must be a number. Try Again. \n')
        print("---------------------------------------------------")
        # If the variable 'current_player' is equal to 1, then everything below executes.
        if current_player == 1:
            # The counter variable 'player1' increases by 1.
            player1 += 1
            # If the answer is equal to the return from the called method 'get_correct_answer'
            # of the instance 'current_question', then the below command executes.
            if answer == int(current_question.get_correct_answer()):
                # The global variable 'player1_points' increases by 1.
                player1_points += 1
            # If the if command is false, then the program continues.
            else:
                continue
        # If the variable 'current_player' is equal to 2, then everything below executes.
        elif current_player == 2:
            # The counter variable 'player2' increases by 1.
            player2 += 1
            # If the answer is equal to the return from the called method 'get_correct_answer'
            # of the instance 'current_question', then the below command executes.
            if answer == int(current_question.get_correct_answer()):
                # The global variable 'player2_points' increases by 1.
                player2_points += 1
            # If the if command is false, then the program continues.
            else:
                continue


# Defines the 'display_results' function.
def display_results():
    # Displays the results of 'player1_points' and 'player2_points' on the screen.
    print("\nPlayer #1 Score: " + str(player1_points) +
          "\nPlayer #2 Score: " + str(player2_points))
# Calls the 'main' function.
main()

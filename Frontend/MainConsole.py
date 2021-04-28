"""
Play a game directly through the console (no Gui). To play simply cd to this directory and run:
    >>> python MainConsole.py

...and follow the prompts 
"""

import sys
from typing import Dict
import os

from Backend.HelperFunctions import get_questions, generate_probabilities, plot_user_data
from Backend.SessionUser import SessionUser
from Backend.Question import Question
from Frontend.DatabaseAPI import DatabaseApi

## DB stuff
FILE_DIR = os.path.dirname(os.path.abspath(__file__)) 
DB_NAME = "TEST.db"
DB_PATH = os.path.normpath(os.path.join(FILE_DIR, "..", "Backend", "database", "db", DB_NAME))


PROBABILITY_OPTIONS = 6

if __name__ == "__main__":
    
    # Connect to DB...
    db = DatabaseApi(DB_PATH)
    
    ## setup user...
    username = input("Username: ")
    user_id = db.get_user_id(username)
    if user_id == -1:
        db.create_new_user(username)
        user_id = db.get_user_id(username)

    session_user = SessionUser(username)


    number_of_questions = int(input("Number of Questions: "))
    score = 0
    
    print("\n")

    ## Fetch questions from API...
    response = get_questions(number_of_questions)
    if response is not None:
        questions: Dict[int, Question] = {i: Question(v) for i, v in enumerate(response)}
    else:
        print("! Error connecting to question API")
        sys.exit(1)

    question_idx = 0
    while question_idx < number_of_questions:
    
        question = questions[question_idx]
        probabilities = generate_probabilities(len(question.awnser_list), PROBABILITY_OPTIONS)

        ## Ask Question
        print("======================")
        print(f"QUESTION {question_idx + 1}: {question.question}")
        awns_str = "\n".join([f"\t{i+1}: {question.awnser_list[i]}" for i in range(len(question.awnser_list))])
        
        selected_awnser = -1
        while selected_awnser not in range(1, len(question.awnser_list)+1):
            selected_awnser = int(input(awns_str + "\n\n"))

        ## Confidence
        print("How confident are you in your awnser: \n")
        conf_level_str = "\n".join([f"\t{i+1}: {probabilities[i]}%" for i in range(PROBABILITY_OPTIONS)])
        
        confidence = -1
        while confidence not in range(1, PROBABILITY_OPTIONS + 1):
            confidence = int(input(conf_level_str  + "\n\n"))

        ## Check Awnser
        chosen_awnser = question.awnser_list[selected_awnser - 1]
        correct = chosen_awnser == question.correct_answer

        ## Update score
        session_user.update(probabilities[confidence - 1], correct)

        #score_change = (10 * (confidence - 1)) * (1 if correct else -1) 
        # conf - 1 since 0-based indexing; no points lost/awarded for pure guess. 
        score_change = 0 if confidence-1 == 0 else (probabilities[confidence-1] * 100) * (1 if correct else -1)
        
        print("\n")
        print
        if correct:
            print("CORRECT!")

        else:
            print(f"INCORRECT! (the correct awnser was: {question.correct_answer})")

        score += score_change

        print(f"Points gained: {score_change}")
        print(f"Current Score: {score}")
        
        question_idx += 1
        
        print("\nMoving on to next question...\n")
        
    
    
    print("GAME OVER!")

    print("-----------------------------------")
    print("Session Stats:")
    print(f"\tFinal Score: {score}")
    print("\t" + str(session_user).replace("\n", "\n\t"))
    print("-----------------------------------")

    ## Plot results
    #session_plot = plot_user_data(session_user, 7)
    #session_plot.show()

    session_id = db.get_next_session_id(user_id)
    db.add_session_data(user_id, session_id, session_user)

    input("Press 'Enter' to exit")
    sys.exit(0)
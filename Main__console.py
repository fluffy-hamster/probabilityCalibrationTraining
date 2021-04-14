import sys
from typing import Dict

import HelperFunctions 
from DataSchema import SessionUser, Question


if __name__ == "__main__":
    
    PROBABILITY_OPTIONS = 6
    
    username = input("Username: ")
    session_user = SessionUser(username)
    
    num_of_questions = int(input("Number of Questions: "))
    score = 0
    
    print("\n")
    

    response = HelperFunctions.get_questions(num_of_questions)
    if response is not None:
        questions: Dict[int, Question] = {i: Question(v) for i, v in enumerate(response)}
    else:
        print("! Error connecting to API")
        sys.exit(1)

    question_idx = 0
    while question_idx < num_of_questions:
    
        question = questions[question_idx]
    
        
        probabilities = HelperFunctions.generate_probabilities(len(question.awnser_list), PROBABILITY_OPTIONS)

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
        
    
    print("-----------------------------------")
    print("GAME OVER!")

    print("Session Stats:")
    print(session_user)

    ## Plot results
    plot_accuracy(session_user, 7)

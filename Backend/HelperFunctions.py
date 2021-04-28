from typing import List, Dict, Any, Optional
from numpy import linspace
import requests
import json
import matplotlib.pyplot as plt

from Backend.SessionUser import SessionUser

MAX_QUESTIONS_PER_API_CALL = 50
GENERAL_KNOWLEDGE = 9

def generate_probabilities(awnser_count:int, num_options:int) -> List[float]:
    return [round(i, 2) for i in linspace(1/awnser_count, 1, num_options)]
    

def get_questions(number_of_questions:int) -> Optional[List[Dict[str, Any]]]:
    """
    Fetch quesions by calling API at https://opentdb.com/
    """

    url = f"https://opentdb.com/api.php?amount={number_of_questions}&category={GENERAL_KNOWLEDGE}&encode=url3986"
    response = requests.get(url)
    
    if response.status_code == 200:
        questions = json.loads(response.text)
        return questions["results"]
    else:
        return None

def plot_user_data(userdata: SessionUser, plot_size:int):
    """
    Returns a plot of userdata. 

    Bars indicate % of correct awnsers.
    Dots indicate "optimal point" 
    Bars below the dots suggests over-confidence bias, bars above dot suggests under-confidence bias.
    """

    fig, ax = plt.subplots(figsize=(plot_size,plot_size))

    x = list(map(str, sorted(userdata.data.keys())))
    y = [round(userdata.data[i][True] / (userdata.data[i][True] + userdata.data[i][False]), 2) for i in sorted(userdata.data.keys())]


    ax.set_ylim([0, 1]) # accuracy as %
    ax.plot(x, [float(i) for i in x], color="red",linestyle="None", marker="o", markersize=plot_size)
    ax.bar(x, y, color="grey")

    plt.title("accuracy of predictions".title())
    ax.set_ylabel("percentage of correct awnsers")
    ax.set_xlabel("probabilities assigned to questions")

    return fig
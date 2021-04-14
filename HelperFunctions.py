from typing import List, Dict, Any, Optional
from numpy import linspace
import requests
import json
import matplotlib.pyplot as plt

from DataSchema import SessionUser

def generate_probabilities(awnser_count:int, num_options:int) -> List[float]:
    return [round(i, 2) for i in linspace(1/awnser_count, 1, num_options)]
    

def get_questions(num_qu:int) -> Optional[List[Dict[str, Any]]]:
    """
    Fetch quesions by calling API at https://opentdb.com/
    """

    GENERAL_KNOWLEDGE = 9
    url = f"https://opentdb.com/api.php?amount={num_qu}&category={GENERAL_KNOWLEDGE}&encode=url3986"
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

    fig = plt.figure(figsize=(plot_size,plot_size))
    ax = fig.add_axes([0,0,1,1])

    #x = ["0.0", "0.1", "0.2", "0.3","0.4","0.5","0.6","0.7", "0.8", "0.9", "1.0" ] 
    x = list(map(str, sorted(userdata.data.keys())))
    y = [round(userdata.data[i][True] / (userdata.data[i][True] + userdata.data[i][False]), 2) for i in sorted(userdata.data.keys())]

    ax.set_ylim([0, 1]) # accuracy as %
    ax.plot(x, [float(i) for i in x], color="red",linewidth=4,linestyle="None", marker="o", markersize=plot_size)
    ax.bar(x, y, color="grey")

    return fig
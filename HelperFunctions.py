from typing import List, Dict, Any, Optional
from numpy import linspace
import requests
import json

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
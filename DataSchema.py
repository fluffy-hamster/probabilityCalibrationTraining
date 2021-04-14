import urllib.parse
from dataclasses import dataclass
from random import shuffle
from typing import Dict, Any, List

#region Question

"""
EXAMPLE DATA:

 {'category': 'Celebrities',
 'type': 'boolean',
 'difficulty': 'hard',
 'question': 'Lady%20Gaga%27s%20real%20name%20is%20Stefani%20Joanne%20Angelina%20Germanotta.',
 'correct_answer': 'True',
 'incorrect_answers': ['False']},
 
 {'category': 'Geography',
  'type': 'multiple',
  'difficulty': 'hard',
  'question': 'When%20does%20Finland%20celebrate%20their%20independence%20day%3F',
  'correct_answer': 'December%206th',
  'incorrect_answers': ['January%202nd', 'November%2012th', 'February%208th']}]
"""

@dataclass
class Question():

    def __init__(self, data: Dict[str, Any]):
        self._data = data

        self._question = urllib.parse.unquote(self._data.get("question", ""))
        self._correct_answer = urllib.parse.unquote(self._data.get("correct_answer", ""))

        ## construct awnser list
        awnser_list = [urllib.parse.unquote(item) for item in self._data.get("incorrect_answers")]
        awnser_list.append(self.correct_answer)
        shuffle(awnser_list)
        self._awnser_list = awnser_list

    @property
    def question(self) -> str:
        return self._question

    @property
    def correct_answer(self) -> str:
        return self._correct_answer

    @property
    def awnser_list(self) -> List[str]:
        return self._awnser_list

#endregion

#region SessionUser

"""
EXAMPLE SessionUser:

    {
    0.1: {True: 1, False: 4},
    0.5: {True: 2, False: 2}, 
    0.6: {True: 4, False: 1}, 
    0.80: {True: 8, False: 2},
    0.99: {True: 99, False: 1}
    }

"""

class SessionUser():

    def __init__(self, username):
        self._username = username
        self._data = dict()

    @property
    def username(self) -> str:
        return self._username

    @property
    def data(self):
        return self._data

    def update(self, probability: float, correct:bool):
        self._data.setdefault(probability, {True: 0, False: 0})
        self._data[probability][correct] += 1

    def __str__(self):
        r = []
        for item in sorted(self._data.keys()):
            correct, incorrect = self._data[item][True], self._data[item][False]
            acc = correct / (correct + incorrect)
            s = f"{item:4} | Accuracy: {acc:.2f}% (diff {"+" if acc-item >=0 else ""}{acc-item:.2f}%) | correct: {correct:2}, incorrect: {incorrect:2}" 
            r.append(s)

        return "\n".join(r)

#endregion

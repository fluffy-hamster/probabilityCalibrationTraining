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

import urllib.parse
from dataclasses import dataclass
from random import shuffle
from typing import Dict, Any, List

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
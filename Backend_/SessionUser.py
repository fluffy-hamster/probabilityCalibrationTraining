from typing import Tuple

class SessionUser():
    """
    Wrapper class,  

    EXAMPLE SessionUser:

        {
        0.1: {True: 1, False: 4},
        0.5: {True: 2, False: 2}, 
        0.6: {True: 4, False: 1}, 
        0.80: {True: 8, False: 2},
        0.99: {True: 99, False: 1}
        }

    """

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
        c = 1 if correct else 0
        w = 1 if not correct else 0

        self.update_with_vals(probability, c, w)
   

    def update_with_vals(self, probability: float, correct: int, incorrect: int):
        self._data.setdefault(probability, {True: 0, False: 0})
        self._data[probability][True] += correct
        self._data[probability][False] += incorrect


    def __str__(self):
        """
        Returns self, with some very basic statistics
        """
        r = []
        for item in sorted(self._data.keys()):
            correct, incorrect = self._data[item][True], self._data[item][False]
            acc = correct / (correct + incorrect)
            s = f"{item:4} | Accuracy: {acc:.2f}% (diff {'+' if acc-item >=0 else ''}{acc-item:.2f}%) | correct: {correct:2}, incorrect: {incorrect:2}" 
            r.append(s)

        return "\n".join(r)

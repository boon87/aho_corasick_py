__author__ = 'boon'

from collections import deque
from collections import defaultdict

class AhoCorasick():
    def __init__(self):
        self.output = defaultdict(set)
        self.goto = defaultdict(dict)
        self.failure = defaultdict(dict)

    def initialize(self, keywords):
        newstate = 0
        for keyword in keywords:
            newstate = self.construct_goto(keyword, newstate)
        self.construct_failure()

    def construct_goto(self, keyword, newstate):
        state = 0
        for char in keyword:
            if self.get_goto_state_for_build(state, char) is not None:
                state = self.get_goto_state_for_build(state, char)
                continue
            else:
                newstate += 1
                self.goto[state][char] = newstate
                state = newstate

        self.output[state].add(keyword)

        return newstate

    def construct_failure(self):
        queue = deque()

        for char, state in self.goto[0].items():
            queue.append(state)
            self.failure[state] = 0

        while queue:
            r = queue.pop()
            for char, state in self.goto.get(r, {})
            for char, state.



    def get_goto_state_for_build(self, state, char):
        """
        Used during the building of state. Does not loop back state 0
        :param state:
        :param char:
        :return:
        """
        if char not in self.goto.get(state, {}):
            return None
        else:
            return self.goto[state][char]

    def get_goto_state(self, state, char):
        """
        Used during normal search_operation. Loops back to state 0
        :param state:
        :param char:
        :return:
        """
        if char not in self.goto.get(state, {}):
            return 0 if state == 0 else None
        else:
            return self.goto[state][char]


def main():
    ac = AhoCorasick()
    ac.initialize(["she", "he", "hers", "his"])

    print("Testing")
    print("Contents in goto:", ac.goto)
    print("Contents in output:", ac.output)

if __name__ == '__main__':
    main()
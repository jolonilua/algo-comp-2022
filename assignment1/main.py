#!usr/bin/env python3
import json
import sys
import os

INPUT_FILE = 'testdata.json' # Constant variables are usually in ALL CAPS

class User:
    def __init__(self, name, gender, preferences, grad_year, responses):
        self.name = name
        self.gender = gender
        self.preferences = preferences
        self.grad_year = grad_year
        self.responses = responses


# Takes in two user objects and outputs a float denoting compatibility
def compute_score(user1, user2):

    # if gender preferences aren't the same, return 0 compatibility 
    if user1.gender not in user2.preferences or user2.gender not in user1.preferences:
        return 0.0

    # initialize the final score to be 4 - absolute value of the grad years such that closer grad years == higher compatiblity
    final_score = 4.0 - abs(user1.grad_year - user2.grad_year)

    # if responses are the same, increase compatibility
    for i in range(len(user1.responses)):
        if user1.responses[i] == user2.responses[i]:
            final_score += 1.0
    # return final score divided by the total number of responses
    return final_score / 20.0

if __name__ == '__main__':
    # Make sure input file is valid
    if not os.path.exists(INPUT_FILE):
        print('Input file not found')
        sys.exit(0)

    users = []
    with open(INPUT_FILE) as json_file:
        data = json.load(json_file)
        for user_obj in data['users']:
            new_user = User(user_obj['name'], user_obj['gender'],
                            user_obj['preferences'], user_obj['gradYear'],
                            user_obj['responses'])
            users.append(new_user)

    for i in range(len(users)-1):
        for j in range(i+1, len(users)):
            user1 = users[i]
            user2 = users[j]
            score = compute_score(user1, user2)
            print('Compatibility between {} and {}: {}'.format(user1.name, user2.name, score))
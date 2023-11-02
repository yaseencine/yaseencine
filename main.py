import json
import re
import random

import randomResponses


# Load JSON data
def load_json(file):
    with open(file) as intent_responses:
        print(f"Loaded '{file}' successfully!")
        return json.load(intent_responses)


# Store JSON data
response_data = load_json("intents.json")


def get_response(input_string):
    split_message = re.split(r'\s+|[,;?!.-]\s*', input_string.lower())
    score_list = []

    # Check all the responses
    for response in response_data:
        response_score = 0
        required_words = response["user_input"]

        # Check if there are any required words
        if required_words:
            for word in required_words:
                if word in split_message:
                    response_score += 1

        score_list.append(response_score)

    # Check if input is empty
    if input_string == "":
        return "Please type something so we can chat :("

    # If there is no good response, return a completely random one from the list of responses
    if max(score_list) > 0:
        response_index = score_list.index(max(score_list))
        responses = response_data[response_index]["bot_response"]

        if isinstance(responses, list):
            return random.choice(responses)
        else:
            return responses

    return randomResponses.random_string()


while True:
    user_input = input("You: ")
    print("Bot:", get_response(user_input))

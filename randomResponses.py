import random


def random_string():
    random_list = [
        "Please try writing something more descriptive.",
        "It appears you wrote something I don't understand yet",
        "Do you mind trying to rephrase that?",
        "I'm sorry, I didn't catch that.",
        "I can't answer that yet, please try asking something else."
    ]

    list_count = len(random_list)
    random_item = random.randrange(list_count)

    return random_list[random_item]

import random
import csv


def main():

    level = get_level()
    score = 0

    dict = {}

    with open("project.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            dict[row["noun"]] = row["translation"]

    if level == 1:

        sample = random.sample(sorted(dict), 5)
        new_val = []
        for i in range(5):
            val = dict[sample[i]]
            new_val.append(val)

        number_of_quest = get_quest_number()

        for _ in range(number_of_quest):
            noun = random.choice(sample)
            translation = random.choice(new_val)

            print(f"Is {noun} = {translation}?")

            while True:
                try:
                    inp = input("Press 'y' or 'n': ")
                    if inp not in("y", "n"):
                        continue
                    break
                except:
                    pass

            answer = dict[noun]

            result = function_level_1(inp, translation, answer)
            print(result)
            if result == "Right!":
                score = score + 1

        print(f"Your score is {score} of {number_of_quest}")

    if level == 2:

        with open("project.csv") as file:
            reader = csv.DictReader(file)
            for row in reader:
                dict[row["noun"]] = row["translation"]

        number_of_quest = get_quest_number()

        for _ in range(number_of_quest):
            noun = random.choice(list(dict.keys()))
            translation = random.choice(list(dict.values()))

            print(f"What is {noun}?")
            inp = input("Type your translation: ")
            answer = dict[noun]

            result = function_level_2(inp, answer)
            print(result)
            if result == "Right!":
                score = score + 1

        print(f"Your score is {score} of {number_of_quest}")

def function_level_1(inp, translation, answer):
    if answer == translation and inp == "y":
        return "Right!"
    elif answer == translation and inp == "n":
        return "Not right!"
    elif answer != translation and inp == "n":
        return "Right!"
    else:
        return "Not right!"


def function_level_2(inp, answer):
    if inp == answer:
        return "Right!"
    else:
        return "Not right!"


def get_level():
    while True:
        try:
            level = int(input("Level (1-2): "))
            if 0 < level < 3:
                return level
        except ValueError:
            pass


def get_quest_number():
    while True:
        try:
            questions = int(input("How many questions? "))
            return questions
        except ValueError:
            pass


if __name__ == "__main__":
    main()

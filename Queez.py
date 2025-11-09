import html
import random
import requests

amountOfQuestions = input("How many questions would you like to answer(enter in numbers): ")
url = f"https://opentdb.com/api.php?amount={amountOfQuestions}"


response = requests.get(url)
data = response.json()
questions = data["results"]


score = 0
for q in questions:
    question = q["question"]
    edited_question = html.unescape(q["question"])
    print("Question:", edited_question)
    options = q["incorrect_answers"] + [q["correct_answer"]]
    random.shuffle(options)
    print("Options:", options)
    user_answer = input("Type the correct answer:  ")
    if user_answer == q["correct_answer"]:
        score+=1
    print("Correct Answer:", q["correct_answer"])

    print("---")

print("You scored --> "+str(score))
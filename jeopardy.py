import requests
import random 

response = requests.get('http://jservice.io/api/clues?category=139').json()

#print(response)
#print(response[0])
score = 0
keepPlaying = "yes"

while keepPlaying == "yes":
    randomNumber = random.randint(0, len(response))
    responseElement = response[randomNumber]
    question = responseElement["question"]

    pointValue = responseElement["value"]
    print("this question is worth " + str(pointValue))

    answer = responseElement["answer"]
    userAnswer = input(question)
    print(userAnswer)

    if userAnswer == answer:
        print("CORRECT")
        score += pointValue
        print(score)
    else:
        print("LOSER")
        score -= pointValue
        print(score)
    print("Your score is " + str(score))
    keepPlaying = input("Enter yes if you want to keep playing!")
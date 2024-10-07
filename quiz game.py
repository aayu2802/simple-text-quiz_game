def new_game():
    guesses=[]
    correct_options=0
    ques_no=1
    for key in questions:
        print(key)
        for i in options[ques_no-1]:
            print(i)
        guess=input("Enter your answer: ")
        guess=guess.upper()
        guesses.append(guess)

        correct_options+=check(questions.get(key),guess)
        ques_no+=1

    display(correct_options,guesses)
    pass
def check(ans,guess):
    if ans == guess:
        print("CORRECT!!!!!!!")
        return 1
    else:
        print("WRONG!!!!!!!!!")
        return 0
def display(correct,guesses):
    print("results")
    print("Answer :",end="")
    for i in questions:
        print(questions.get(i),end="")
    print()
    print("-----------------------------------------------")
    print("guesses :", end="")
    for i in guesses:
        print(i,end="")
    print()
    score=int((correct/len(questions))*10)
    print("Score:"+str(score))

def play_again():
    response=input("If you want to play again?:(Y/N)")
    response=response.upper()
    if response=="Y":
        return True
    else:
        return False

#dictionary for questions
questions={
    "Which Goverment is responsible for demonetization in India?: ":"B",
    "Capital city of New-Zealand :":"B",
    "Who is president of USA:":"C",
    "India is surrounded by which ocean?":"B"
}
#2D List of options
options=[["A.Congress","B.BJP","C.AAP","D.Samaj-Vadi Party"],
         ["A.Auckland","B.Wellington","C. Manukau city","D.ChristChurch"],
        ["A.Donald Trump","B.Brack obama","C. Joe biden","D.beau biden"],
        ["A.Pacific","B.Indian ocean","C. Artic ocean","D.Arabian sea"]]
new_game()
while play_again():
    new_game()

print("Its over")
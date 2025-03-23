prize = 0
Question = [
    {
        "question":"Who is the PM of india?",
        "option":["PM Modi", "Rahul Gandhi", "Amit saha", "Mamta Banerjee"],
        #Answer PM Modi
    },
    {
        "question":"What is the capital of india?",
        "option":["Mumbai", "Kolkata", "Delhi", "Gujrat"],
        #Answer Delhi
    },
    {
        "question": "What is the finicial capital of india",
        "option": ["Kolkata", "Mumbai", "Gujarat", "J&K"],
        #Anser Mumbai
    }
]
Answer = ["PM Modi", "Delhi", "Mumbai"]
for i in range(3):
    print("Question no", i+1,":")
    print(Question[i])
    answers=input("Enter Your anser:")
    if(answers==Answer[i]):
        print("Your answer is right")
        prize=prize+500
        print("Your current amount is", prize)
    else:
        print("Your anser is wrong")
        prize = prize
print("You won total amount of", prize)
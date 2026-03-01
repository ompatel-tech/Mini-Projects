# questions = ("Which wonder of the world is located in India?",
#              "Machu Picchu is located in which country? ",
#              "The Colosseum was primarily used for what purpose in ancient Rome? ",
#              "Petra, famous for its rock-cut architecture, is located in which country? ",
#              "Which wonder is a large statue of Jesus Christ in Brazil?",)

# options =(("A. Petra","B. Taj Mahal","C. Machu Picchu","D. Colosseum"),
#  ("A. Mexico","B. Taj Mahal","C. Machu Picchu","D. Colosseum"),
#  ("A. Religious ceremonies","B. Gladiator contests"," C. Royal residence","D. Library"),
#  ("A. Jordan","B. Egypt"," C. Greece"," D. Turkey"),
#  ("A. Christ the Redeemer","B. Chichen Itza","C. Great Wall","D. Angkor Wat"))


# answers = ("B","C","B","A","A")
# guesses = []
# score = 0
# question_num = 0

# for question in questions:
#     print("-------------------")
#     print(question)
#     for option in options[question_num]:
#         print(option)


#     guess = input("Enter (A,B,C,D): ").upper()
#     guesses.append(guess)

#     if guess == answers[question_num]:
#         score += 1
#         print("CORRECT!!")
#     else: 
#         print("INCORRECT!")
#         print(f"{answers[question_num]} is te correct answer")
#     question_num += 1

# print("==================")
# print("       RESULT     ")
# print("==================")


# print("answers: ", end= " ")
# for answer in answers:
#     print(answer, end = " ")
# print()


# print("gueses: ", end= " ")
# for guess in guesses:
#     print(guess, end = " ")
# print()


# score = int(score/ len(questions)* 100)
# print(f"your score is: {score}%")



nums = [3,1,4,1,5]
nums.remove(1)
nums = nums.sort()
print(nums)
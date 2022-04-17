# question and answer lists
human_space_travel = ["In what year did Neil Armstrong land on the moon?", "Which President cancelled the Apollo program?", "Which President authorized the Apollo program?", "How many space shuttles were built?", "Which space shuttle exploded in 1986?", "What is the name of NASA's first manned spaceflight program?", "Who was the first American in space?", "Which German and former-Nazi rocket scientist led the Apollo program?"]
human_space_answers = ["1969", "Richard Nixon", "John F. Kennedy", "5", "Challenger", "Mercury", "Alan Shepard", "Wernher von Braun"]

unmanned_space_travel = ["What is the name of the first satellite?", "What is the name of the Soviet's space shuttle?", "What was the name of the first dog in space?", "In what year did the James Webb Space Telescope launch?", "Which space probe was the first to closely study Jupiter?", "What was the most recent space probe to Saturn?"]
unmanned_space_answers = ["Sputnik", "Buran", "Laika", "2021", "Galileo", "Cassini"]

solar_system = ["How many planets are there?", "Who discovered Uranus?", "Who discovered Pluto?", "The discovery of which minor planet caused the push to downgrade Pluto?", "What is the name of collection of debris between Mars and Jupiter?", "What is the name of the large torus-shaped collection of debris beyond Neptune?", "How long in Earth days is Mercury's year?", "Which planet is closest in size to Earth?"]
solar_system_answers = ["8", "William Herschel", "Clyde Tombaugh", "Eris", "Asteroid Belt", "Kuiper Belt", "88", "Venus"]

print("Welcome to Connor's Trivia Quiz!")
addQuestion = input("Would you like to add a question? (yes/no): ")

# while loop: as long as addQuestion = yes, the user is asked to select a category and add n questions to that category. 
while addQuestion == "yes":
  category = input("Please select a category: Human Space Travel, Unmanned Space Travel, or Solar System\n")
  n = int(input("How many questions to add?: "))
  for i in range(0,n):
    if category == "Human Space Travel":
      newQuestion = input("Add a question: ")
      newAnswer = input("Add the answer: ")
      human_space_travel.append(newQuestion)
      human_space_answers.append(newAnswer)
    elif category == "Unmanned Space Travel":
      newQuestion = input("Add a question: ")
      newAnswer = input("Add the answer: ")
      unmanned_space_travel.append(newQuestion)
      unmanned_space_answers.append(newAnswer)
    elif category == "Solar System":
      newQuestion = input("Add a question: ")
      newAnswer = input("Add the answer: ")
      solar_system.append(newQuestion)
      solar_system_answers.append(newAnswer)
# The user can stop adding to any category by typing "no"
  addQuestion = input("Would you like to add to another category? (yes/no): ")
print("Done. Starting quiz.")

# User inputs the desired category and number of questions for the quiz
category = input("Please select a category: Human Space Travel, Unmanned Space Travel, or Solar System\n")
num = int(input("Please select the number of questions\n"))

# trivia function that asks questions and calculates score
def trivia(category):
  score = 0
# repeat so that num questions are asked
  for i in range(num):
    if category == "Human Space Travel":
      # x = random.randrange(len(human_space_travel))
      print(human_space_travel[i])
      answer = input("Type your answer: ")
      correct = human_space_answers[i]
      if answer == correct:
        print("Correct!")
        score += 1
      else:
        print("Incorrect, moving on")
    elif category == "Unmanned Space Travel":
      # x = random.randrange(len(unmanned_space_travel))
      print(unmanned_space_travel[i])
      answer = input("Type your answer: ")
      correct = unmanned_space_answers[i]
      if answer == correct:
        print("Correct!")
        score += 1
      else:
        print("Incorrect, moving on")
    elif category == "Solar System":
      # x = random.randrange(len(solar_system))
      print(solar_system[i])
      answer = input("Type your answer: ")
      correct = solar_system_answers[i]
      if answer == correct:
        print("Correct!")
        score += 1
      else:
        print("Incorrect, moving on")
  return score

# calls trivia function and assigns value to score, then prints total
score = trivia(category)
print("Your total score is", str(score), "out of", str(num))


  

  



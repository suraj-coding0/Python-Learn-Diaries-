def display_question(level, questions, options):
  print(f"\nLevel {level + 1}: {questions[level]}")
  for opt in options[level]:
      print(opt)
  
def get_user_answer():
  return input("\nYour answer (A, B, C, D): ").upper()

def handle_answer(level, correctAnswers):
  user_answer = get_user_answer()
  if user_answer == correctAnswers[level]:
      print("Correct! You've moved to the next level.")
      return True
  else:
      print("Incorrect. Game over.")
      return False

def KBC():
 questions = [
      "What is the capital of India?",
      "Which Team Won The 2024 T20 World Cup?",
      "Which city is known as the Pink City of India?",
      "How many states are there in India?"
      "Where is India Gate located?"
      "Which of the following is not a state of India?"
  ]
 options = [
      ["A. Mumbai", "B. Punjab", "C. Banglore", "D. Delhi"],
      ["A. Australia", "B. India", "C. Afganistan", "D. South Africa"],
      ["A. Maysore", "B. Kochi", "C. Jaipur", "D. Banglore"],
      ["A. 26", "B. 28", "C. 31", "D. 29"],
      ["A. Delhi", "B. Agra", "C. Punjab", "D. Mumbai"],
      ["A. Vrindachal", "B. Uttrakhand", "C. Goa", "D. Jharkhand"],
  ]

 correctAnswers = ["D", "B", "C", "B", "A", "A"]

 prize = [1000, 2000, 3000, 5000, 10000, 20000]

 print("Namaskar Deviyo Aur Sajjano. Swagat Hai Aapka Koun Banega Crorepati Me.")
 print("To Chaliye Khel Suru Karte hai!\n")

 level = 0
 score = 0

 while level < len(questions):
      display_question(level, questions, options)

      if handle_answer(level, correctAnswers):
          score += 1
          level += 1
      else:
          break

 if score > 0:
      final_amount = prize[score - 1]
      print(f"Congratulations! You've reached level {score}. Your final amount is ${final_amount}.You'll be taking this amount with you!")
 else:
   print("Game over. You did not win any prize.")

# if _name_ == "_main_":
KBC()
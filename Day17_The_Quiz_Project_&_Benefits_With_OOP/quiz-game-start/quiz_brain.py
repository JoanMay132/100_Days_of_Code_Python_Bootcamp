#TODO: asking the questions
#TODO: checking if the answer was correct
#TODO: checking if we´re the end of the quiz

class QuizBrain:
    def __init__(self, qlist):
        self.qnumber=0 #question number
        self.qlist= qlist 
        self.score=0

    def still_has_question(self):
       if self.qnumber< len(self.qlist):
        return True
       else:
        return False

    def next_question(self):
        current_question= self.qlist[self.qnumber]
        self.qnumber+=1
        user_answer= input(f"Q.{self.qnumber}: {current_question.text} (True/False): ") 
        self.check_answer(user_answer, current_question.answer)
    
    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            self.score+=1

            print("You got it right!")
        else:
            print("That's wrong.!")
        print(f"The correct answer was {correct_answer}")
        print(f"Your current score is: {self.score}/{self.qnumber}")


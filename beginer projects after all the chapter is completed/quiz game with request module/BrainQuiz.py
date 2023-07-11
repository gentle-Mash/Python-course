# from quelist import que_ans
import html

class BrainQuiz:
    def __init__(self, q_list):
        self.que_number = 0
        self.question_list = q_list
        self.score = 0

    def que_left(self):
        return self.que_number < len(self.question_list)

    def next_que(self):
        question = self.question_list[self.que_number].question
        self.answer = self.question_list[self.que_number].answer
        self.que_number +=1
        question = html.unescape(question)
        # print(f"Q/{self.que_number}: {question} ", end="")
        # user_ans = input("True or False? ").lower().strip()
        # self.check_ans(user_ans,answer)
        return f"Q/{self.que_number}: {question}"
    
    def check_ans(self, user_ans):
        if user_ans == self.answer.lower():
            self.score += 1
            return True
        else:
            return False
        # print(f"the correct ans was {self.answer}. your score: {self.score}/{self.que_number}")
        # print("\n")


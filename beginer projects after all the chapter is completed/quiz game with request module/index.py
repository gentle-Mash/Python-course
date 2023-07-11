from datas import question_data
from question_class import MakingQue
from BrainQuiz import BrainQuiz
from ui import Interface


que_ans = []
for data in question_data:
    new_obj = MakingQue(data['question'], data['correct_answer'])
    que_ans.append(new_obj)


quiz = BrainQuiz(que_ans)
quiz_ui = Interface(quiz)


print("the quiz has ended")
print(f"your final score was {quiz.score}/{quiz.que_number}")

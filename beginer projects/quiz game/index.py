from datas import question_data
from question_class import MakingQue
from BrainQuiz import BrainQuiz

que_ans = []
for data in question_data:
    new_obj = MakingQue(data['text'], data['answer'])
    que_ans.append(new_obj)


quiz = BrainQuiz(que_ans)

while quiz.que_left():
    quiz.next_que()

print("the quiz has ended")
print(f"your final score was {quiz.score}/{quiz.que_number}")

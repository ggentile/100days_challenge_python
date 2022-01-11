from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []

def main():

    for lines in question_data:
        question_text = lines['text']
        question_answer = lines['answer']
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)
    
    quiz = QuizBrain(question_bank)

    while quiz.still_has_question() == True:
        quiz.next_question()
    
    print('You have completed the quiz!')
    print(f'Your final score was: {quiz.score}/{len(quiz.question_list)}')


if __name__ == '__main__':
    main()

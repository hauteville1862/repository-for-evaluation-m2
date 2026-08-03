from question_model import Question
from quiz_data import question_data

# 1. 문제 객체들을 담을 빈 리스트를 만듭니다.
question_bank = []

# 2. 반복문을 통해 데이터를 객체로 변환합니다.
for question in question_data:
    q_text = question["text"]
    q_answer = question["answer"]
    
    # 설계도(Question)를 이용해 실제 문제 객체를 생성합니다.
    new_question = Question(q_text, q_answer)
    
    # 생성된 객체를 리스트에 추가합니다.
    question_bank.append(new_question)

# 3. 잘 만들어졌는지 확인해볼까요?
print(f"총 {len(question_bank)}개의 문제가 준비되었습니다!")
print(f"첫 번째 문제 내용: {question_bank[0].text}")
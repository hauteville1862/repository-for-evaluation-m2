import json

# 1. 파일 열기 ("r"은 Read, 읽겠다는 뜻)
file = open("data.json", "r")

# 2. 종이에 적힌 내용을 파이썬이 이해하는 데이터(딕셔너리)로 바꾸기
data = json.load(file)

# 3. 그중에서 "high_score"라는 이름의 숫자를 가져와서 변수에 담기
high_score = data["high_score"]

# 4. 다 읽었으니 파일 닫기
file.close()

print(f"현재 최고 점수는 {high_score}점입니다!")


from question_model import Question
from quiz_data import question_data

# 0. 환영 인사 출력 (여기에 추가!)
print("=" * 50)
print("         📖 세계 문학 거장 퀴즈 📖         ")
print("      정답은 'True' 또는 'False'로 입력하세요.      ")
print("=" * 50)
print() # 한 줄 띄우기


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

from question_model import Question
from quiz_data import question_data
from quiz_brain import QuizBrain # 1. QuizBrain 가져오기

question_bank = []
for question in question_data:
    q_text = question["text"]
    q_answer = question["answer"]
    new_question = Question(q_text, q_answer)
    question_bank.append(new_question)

# 2. 퀴즈 두뇌 객체 생성
quiz = QuizBrain(question_bank)

# 3. 남은 문제가 있다면 계속 퀴즈 내기
while quiz.still_has_questions():
    quiz.next_question()

print("퀴즈가 모두 끝났습니다!")
print(f"최종 점수: {quiz.score}/{quiz.question_number}")

# (게임이 끝난 시점이라고 가정)
current_score = quiz.score 

if current_score > high_score:
    print("최고 기록 경신!")
    
    # 1. 새로 저장할 데이터 만들기
    new_data = {"high_score": current_score}
    
    # 2. 파일 열기 ("w"는 Write, 새로 쓰겠다는 뜻)
    file = open("data.json", "w")
    
    # 3. 파일을 종이에 받아 적기
    json.dump(new_data, file)
    
    # 4. 파일 닫기
    file.close()
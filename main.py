import json
import os
from question_model import Question
from quiz_brain import QuizBrain

# 데이터 파일 경로 설정
DATA_FILE = "data.json"

def load_data():
    """json 파일에서 데이터를 불러옵니다."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    else:
        print("⚠️ 데이터 파일을 찾을 수 없습니다.")
        return None

def save_data(data):
    """최고 점수 등을 json 파일에 저장합니다."""
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def main():
    # 1. 데이터 로드
    data = load_data()
    if not data:
        return

    # 2. Question 객체 리스트 생성
    question_bank = []
    for q_data in data["questions"]:
        new_question = Question(
            text=q_data["text"], 
            choices=q_data["choices"], 
            answer=q_data["answer"]
        )
        question_bank.append(new_question)

    # 3. 퀴즈 브레인 초기화
    quiz = QuizBrain(question_bank)

    # 4. 환영 인사 및 최고 점수 표시
    print("=" * 40)
    print("📚 세계 문학 퀴즈 게임에 오신 것을 환영합니다! 📚")
    print(f"🏆 현재 최고 점수: {data['high_score']}")
    print("=" * 40)

    # 5. 게임 루프 실행
    while quiz.still_has_questions():
        quiz.next_question()

    # 6. 게임 종료 및 결과 발표
    print("\n" + "=" * 40)
    print("🏁 모든 문제를 풀었습니다!")
    print(f"최종 점수: {quiz.score} / {len(quiz.question_list)}")

    # 7. 최고 점수 갱신 및 저장
    if quiz.score > data["high_score"]:
        data["high_score"] = quiz.score
        save_data(data)
        print(f"🎉 축하합니다! 새로운 최고 기록을 달성했습니다: {quiz.score}")
    else:
        print(f"기존 최고 점수({data['high_score']})를 경신하지 못했습니다. 다음에 도전하세요!")
    print("=" * 40)

if __name__ == "__main__":
    main()
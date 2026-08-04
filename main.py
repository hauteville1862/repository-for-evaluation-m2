import json
from question_model import Question
from quiz_brain import QuizBrain
from quiz_data import question_data

def load_data():
    try:
        # 기준: state.json 사용 및 UTF-8 인코딩
        with open("state.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"high_score": 0, "questions": question_data}

def save_data(data):
    with open("state.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def main():
    data = load_data()
    
    while True:
        print("\n=== 📚 세계 문학 퀴즈 프로그램 ===")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 등록")
        print("3. 퀴즈 목록")
        print("4. 최고 점수 확인")
        print("5. 종료")
        choice = input("메뉴를 선택하세요: ")

        if choice == "1":
            # 퀴즈 풀기 로직
            question_bank = [Question(q["text"], q["answer"]) for q in data["questions"]]
            quiz = QuizBrain(question_bank)
            while quiz.still_has_questions():
                quiz.next_question()
            
            print(f"\n게임 종료! 최종 점수: {quiz.score}/{quiz.question_number}")
            if quiz.score > data["high_score"]:
                data["high_score"] = quiz.score
                print(f"🎊 최고 점수 갱신: {data['high_score']}점!")
                save_data(data)

        elif choice == "2":
            # 퀴즈 등록 로직
            text = input("새로운 퀴즈 내용을 입력하세요: ")
            answer = input("정답을 입력하세요 (True/False): ")
            data["questions"].append({"text": text, "answer": answer})
            save_data(data)
            print("✅ 퀴즈가 성공적으로 등록되었습니다.")

        elif choice == "3":
            # 퀴즈 목록 보기
            print("\n--- 등록된 퀴즈 목록 ---")
            for i, q in enumerate(data["questions"], 1):
                print(f"{i}. {q['text']} (정답: {q['answer']})")

        elif choice == "4":
            print(f"\n🏆 현재 최고 점수: {data['high_score']}점")

        elif choice == "5":
            print("프로그램을 종료합니다. 안녕히 가세요!")
            break
        else:
            print("잘못된 선택입니다. 다시 입력해주세요.")

if __name__ == "__main__":
    main()
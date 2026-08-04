# 📖 세계 문학 거장 퀴즈 게임 (Python Quiz Game)

Python의 객체 지향 프로그래밍(OOP) 개념을 활용하여 제작된 **True/False 퀴즈 게임**입니다. 
세계적인 문학 작가와 작품에 대한 상식을 테스트할 수 있으며, 최고 점수 기록 기능을 포함하고 있습니다.

## ✨ 주요 기능
- **퀴즈 진행**: `True` 또는 `False` 입력을 통해 5개의 문학 퀴즈를 풀 수 있습니다.
- **최고 점수 저장 (Data Persistence)**: JSON 파일을 활용하여 프로그램이 종료되어도 최고 점수가 유지됩니다.
- **객체 지향 설계**: 클래스(`Question`, `QuizBrain`)를 분리하여 유지보수가 쉬운 구조로 설계되었습니다.
- **사용자 친화적 UI**: 이모지와 구분선을 사용하여 터미널 환경에서 가독성을 높였습니다.
- **버전 관리**: Git 브랜치(`feature-ui`)를 활용한 기능별 개발 및 병합(Merge) 과정을 거쳐 완성되었습니다.

## 🛠 기술 스택
- **Language**: Python 3.x
- **Data Storage**: JSON
- **Version Control**: Git / GitHub

## 📂 파일 구조
- `main.py`: 게임 실행 및 최고 점수 로직 담당
- `question_model.py`: 퀴즈 문제 객체를 위한 `Question` 클래스
- `quiz_brain.py`: 게임 흐름(문제 출제, 정답 체크, 점수 계산) 관리 클래스
- `quiz_data.py`: 퀴즈 문제 데이터 리스트
- `data.json`: 최고 점수 데이터 저장 파일

## 🚀 실행 방법
1. 저장소를 클론합니다.
   ```bash
   git clone https://github.com/hauteville1862/repository-for-evaluation-m2.git
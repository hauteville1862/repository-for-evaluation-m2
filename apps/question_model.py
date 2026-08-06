class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices  # 보기 리스트 추가
        self.answer = answer    # 정답 (숫자 1~4)
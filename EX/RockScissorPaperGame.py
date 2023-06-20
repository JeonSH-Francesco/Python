import random

def get_user_choice():
    while True:
        user_choice = input("가위, 바위, 보 중에서 선택하세요: ")
        if user_choice in ["가위", "바위", "보"]:
            return user_choice
        else:
            print("잘못된 입력입니다. 다시 입력해주세요.")

def get_computer_choice():
    choices = ["가위", "바위", "보"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "무승부"
    elif (
        (user_choice == "가위" and computer_choice == "보") or
        (user_choice == "바위" and computer_choice == "가위") or
        (user_choice == "보" and computer_choice == "바위")
    ):
        return "인간 승리!"
    else:
        return "컴퓨터 승리!"

# 게임 실행
while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print("인간의 선택:", user_choice)
    print("컴퓨터의 선택:", computer_choice)
    winner = determine_winner(user_choice, computer_choice)
    print("결과:", winner)

    play_again = input("게임을 계속하시겠습니까? (예/아니오): ")
    if play_again.lower() != "예":
        break

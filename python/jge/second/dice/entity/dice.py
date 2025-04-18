import random

#클래스 생성 시 class 키워드를 붙여야 합니다.
#생성하고자 하는 클래스 이름은 Dice 입니다.
#사실상 class를 Domain으로 바라봐야함.
#비즈니스 상에서 주요 항목들

class Dice:
    #보편적으로 대문자만으로 적는 것들 (상수값)
    MAX = 6
    MIN = 1

    #생성자 (클래스 생성)
    def __init__(self): #__private 처리
        #초기 주사위의 눈금은 0
        self.__number = 0

    #주사위를 굴리는 행위
    def rollDice(self):
        self.__number = random.randint(self.MIN, self.MAX)
    #내용 출력
    def printResult(self):
        #f"문자열{}"형식의 경우 내부에 있는 변수 정보를 문자열로 만들어줌
        print(f"dice number: {self.__number}")




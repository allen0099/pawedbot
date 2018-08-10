from random import choice, choices
from ast import literal_eval

class ToS:
    def __init__(self):
        self.__chance_normal = [10, 45, 45, 180, 180, 180, 180, 180]
        self.__chance_double = [25, 100, 100, 155, 155, 155, 155, 155]
        self.__cards = ['浦飯幽助', '藏馬', '飛影', '幻海', '桑原和真', '雷禪', '小閻王', '戶愚呂兄']

    def draw(self):
        result = choices(self.__cards, weights=self.__chance_double, k=1)
        return result
    
class Dinner(object):
    def __init__(self):
        self.__food_list = literal_eval( open('weird_food.txt', 'r').read() )
    
    def draw(self):
        return choice(self.__food_list)

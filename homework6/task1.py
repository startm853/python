from time import sleep
import turtle


class TrafficLight:
    __start_colors = ['red', 'green']
    __rules = {
        'red': {'next': 'red_yellow', 'timer': 7, 'y_coord': 300},
        'red_yellow': {'next': 'green', 'timer': 2},
        'green': {'next': 'yellow', 'timer': 10, 'y_coord': -100},
        'yellow': {'next': 'red', 'timer': 2, 'y_coord': 100},
    }

    def __init__(self, color='red'):
        try:
            self.__color = self.__start_colors[self.__start_colors.index(color)]
        except:
            self.__color = 'red'

    def __items(self, color, start_y, type):
        item = turtle.Turtle()
        item.hideturtle()
        item.speed(0)
        item.penup()
        item.sety(start_y)
        item.setx(-75)
        item.color(color)
        item.pendown()
        if type == 1:
            item.begin_fill()
        for i in range(4):
            item.forward(150)
            item.right(90)
        if type == 1:
            item.end_fill()
        return item

    def __set_colors(self, action):
        """
        self.__process[self.__color] может быть 2 цвета - красный и желтый
        :param action: 1 - создаем закрашенный квадрат, 0 - пустой
        :return:
        """
        if len(self.__process[self.__color]) > 1:
            if action == 0:
                self.__process[self.__color][0].clear()
                self.__process[self.__color][1].clear()
            self.__process[self.__color][0] = self.__items('red', self.__rules['red']['y_coord'], action)
            self.__process[self.__color][1] = self.__items('yellow', self.__rules['yellow']['y_coord'], action)
        else:
            if action == 0:
                self.__process[self.__color][0].clear()
            self.__process[self.__color][0] = self.__items(self.__color, self.__rules[self.__color]['y_coord'], action)

    def running(self):
        window = turtle.Screen()
        window.title('TrafficLight')
        window.setup(width=0.7, height=0.7)
        window.bgcolor("black")

        red = self.__items('red', 300, 0)
        yellow = self.__items('yellow', 100, 0)
        green = self.__items('green', -100, 0)
        self.__process = {'red': [red], 'red_yellow': [red, yellow], 'green': [green], 'yellow': [yellow]}

        while True:
            window.update()
            self.__set_colors(1)
            sleep(self.__rules[self.__color]['timer'])
            self.__set_colors(0)
            self.__color = self.__rules[self.__color]['next']


traffic_light = TrafficLight()
traffic_light.running()

from turtle import Turtle

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.new_snake()
        self.head = self.segments[0]

    def new_snake(self):
        for pos in START_POSITIONS:
            self.add_segm(pos)

    def add_segm(self, pos):
        new_segment = Turtle('square')
        new_segment.penup()
        new_segment.color('green')
        new_segment.goto(pos)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segm(self.segments[-1].position())



    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def move_up(self):
        if self.head.heading() != 270:
            self.head.seth(90)

    def move_down(self):
        if self.head.heading() != 90:
            self.head.seth(270)

    def move_left(self):
        if self.head.heading() != 0:
            self.head.seth(180)

    def move_right(self):
        if self.head.heading() != 180:
            self.head.seth(0)


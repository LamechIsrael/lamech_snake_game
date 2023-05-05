from  turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 280)
        self.color('white')
        self.hideturtle()
        self.score = -1
        self.update_score()   
        
    def update_score(self):
        self.score = self.score +1
        self.clear()
        self.write(arg=(f'Score = {self.score}'), font=FONT, align=ALIGNMENT)
        
    def game_over(self):
        self.goto(0,0)
        self.write(arg='GAME OVER!', align=ALIGNMENT, font=FONT)
import turtle
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet = list(alphabet)
screen = turtle.Screen()
screen.setup(1000,1000)
def coor(x,y):
    print(x,y)
turtle.onscreenclick(coor, 1, add='True')
graphics = turtle.Turtle()
graphics.speed(10)
graphics.hideturtle()
def hanger(t):
    t.penup()
    t.goto(-450, -415)
    t.pendown()
    t.left(90)
    t.forward(50)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(50)
    t.penup()
    t.goto(t.xcor()-250/2, t.ycor()+50)
    t.pendown()
    t.back(600)
    t.left(90)
    t.forward(50)
    t.right(135)
    t.forward(70.7106781187)
    t.left(45)
    t.back(50)
    t.left(90)
    t.forward(200)
    t.right(90)
    t.forward(100)
    t.right(90)
def circle(t):
    t.circle(50)
def face(t):
    t.penup()
    t.goto(t.xcor()-25, t.ycor()-40)
    t.write('.', align='center', font = ('arial', 16, 'bold'))
    t.back(50)
    t.write('.', align='center', font = ('arial', 16, 'bold'))
    t.left(90)
    t.forward(45)
    t.pendown()
    t.left(180)
    t.circle(25, 180)
def body(t):
    t.penup()
    t.goto(t.xcor()+25, t.ycor()-15)
    t.pendown()
    t.forward(200)
def rleg(t):
    t.right(45)
    t.forward(150)
    t.back(150)
def lleg(t):
    t.left(90)
    t.forward(150)
    t.back(150)
def rhand(t):
    t.right(45)
    t.back(150)
    rleg(t)
def lhand(t):
    lleg(t)
functions = [hanger, circle, face, body, rleg, lleg, rhand, lhand]
functions[0](graphics)
writeW = turtle.Turtle()
writeW.speed(10)
writeW.penup()
writeW.hideturtle()
writeW.goto(210, 170)
# go to python shell
word = input("Player 1, what is your word?\n")
# go back to python canvas/screen
W = []
for i in range(len(word)):
    W.append('_ ')
Word = ''
for i in range(len(W)):
    Word = Word + W[i]
writeW.write(Word, align = 'center', font = ('arial', 30, 'normal'))
for i in range(50):
    print('\n') # to make sure that player 2 does not see player 1's word
m = word
Max = 0
letterCount = 0
counter = 1
while Max < 7 and not letterCount >= len(word):
    #go to python shell
    print('You currently have the letters in the following list remaining:')
    print(alphabet)
    guess = input("What is your first/next guess?\n")
    # go back to canvas/screen
    if guess in word:
        for i in range(word.count(guess)):
            letterCount += 1
            x = word.index(guess)
            Guess = guess
            word = list(word)
            word.remove(guess)
            word.insert(x, " ")
            z = word
            word = ''
            for i in range(len(z)):
                word = word + z[i]
            W.pop(x)
            W.insert(x, guess)
            guess = Guess
        Word = ''
        for j in range(len(W)):
            Word = Word + W[j]
        writeW.clear()
        writeW.write(Word, align = 'center', font = ('arial', 30, 'normal'))
        alphabet.remove(guess)
    else:
        functions[counter](graphics)
        Max += 1
        counter += 1
        alphabet.remove(guess)
winLoss = turtle.Turtle()
winLoss.speed(10)
winLoss.color('green')
winLoss.penup()
winLoss.goto(winLoss.xcor(),winLoss.ycor()-250)
winLoss.hideturtle()
if Max>=7:
    winLoss.write('Player 1 wins!!!\nThe word was:\n'+m, align = 'center', font = ('arial', 100, 'normal'))
elif letterCount >= len(word):
    winLoss.write('Player 2 wins!!!\nThe word was \ndiscovered!', align = 'center', font = ('arial', 100, 'normal'))
#USE IN IDLE. DOES NOT WORK IN PYTHON WIDGET OR JUPYTER.ORG
#To get best experience, only use lower and upper case letters. Otherwise, definately do not use spaces

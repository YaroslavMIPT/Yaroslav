import turtle

def zero():
    t.forward(40)
    t.right(90)
    t.forward(80)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(80)
    t.right(90)
    t.forward(40)
    t.penup()
    t.forward(40)
    t.pendown()

def one():
    t.penup()
    t.right(90)
    t.forward(40)
    t.pendown()
    t.right(180 + 45)
    t.forward(40*(2**0.5))
    t.right(45 + 90)
    t.forward(80)
    t.penup()
    t.right(180)
    t.forward(80)
    t.right(90)
    t.forward(40)
    t.pendown()

def two():
    t.forward(40)
    t.right(90)
    t.forward(40)
    t.right(45)
    t.forward(40*(2**0.5))
    t.left(45)
    t.left(90)
    t.forward(40)
    t.penup()
    t.left(90)
    t.forward(80)
    t.right(90)
    t.forward(40)
    t.pendown()

def three():
    t.forward(40)
    t.right(90+45)
    t.forward(40*(2**0.5))
    t.left(45+90)
    t.forward(40)
    t.right(90+45)
    t.forward(40*(2**0.5))

    t.penup()
    t.left(90+45)
    t.forward(40)
    t.left(90)
    t.forward(80)
    t.right(90)
    t.forward(40)
    t.pendown()

def four():
    t.right(90)
    t.forward(40)
    t.left(90)
    t.forward(40)
    t.right(90)
    t.forward(40)
    t.right(180)
    t.forward(80)
    t.penup()
    t.right(90)
    t.forward(40)
    t.pendown()

def five():
    t.forward(40)
    t.right(180)
    t.forward(40)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(40)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(40)

    t.penup()
    t.right(180)
    t.forward(40)
    t.left(90)
    t.forward(80)
    t.right(90)
    t.forward(40)
    t.pendown()

def six():
    t.penup()
    t.forward(40)
    t.pendown()

    t.right(90+45)
    t.forward(40*2**0.5)
    t.left(45)
    t.forward(40)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(40)
    t.left(90)

    t.penup()
    t.forward(40)
    t.left(90)
    t.forward(80)
    t.right(90)
    t.forward(40)
    t.pendown()

def seven():
    t.forward(40)
    t.right(90+45)
    t.forward(40*2**0.5)
    t.left(45)
    t.forward(40)
    t.left(90)

    t.penup()
    t.forward(40)
    t.left(90)
    t.forward(80)
    t.right(90)
    t.forward(40)
    t.pendown()

def eight():
    t.forward(40)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(40)
    t.right(180)
    t.forward(80)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(40)
    t.left(90)

    t.penup()
    t.forward(40)
    t.left(90)
    t.forward(80)
    t.right(90)
    t.forward(40)
    t.pendown()

def nine():
    t.forward(40)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(40)

    t.right(45)
    t.forward(40*2**0.5)
    t.left(45+90)

    t.penup()
    t.forward(40)
    t.left(90)
    t.forward(80)
    t.right(90)
    t.forward(40)
    t.pendown()

t = turtle.Turtle()

t.penup()
t.right(180)
t.forward(200)
t.right(180)
t.pendown()

t.speed(10)
window = turtle.Screen()

s = input()

if len(s) != 6:
    print("Не индекс! Должно быть 6 цифр, а не", len(s), "!")
else:
    for el in s:
        if el == "0":
            zero()
        if el == "1":
            one()
        if el == "2":
            two()
        if el == "3":
            three()
        if el == "4":
            four()
        if el == "5":
            five()
        if el == "6":
            six()
        if el == "7":
            seven()
        if el == "8":
            eight()
        if el == "9":
            nine()

window.mainloop()
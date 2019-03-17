import random
from microbit import*

display.scroll("Do you want to play a game", delay = 100)

while True:
    if pin2.is_touched():
        display.scroll("This is a game where you have to fight enemies", delay = 100)
        display.scroll("You attack by pressing the a button", delay = 100)
        display.scroll("not everything is as it seems tho so be careful", delay = 100)
    elif button_a.is_pressed() or button_b.is_pressed() :
        break

display.scroll("you are walking on a trail and a cow challenges you to a fight", delay = 100)
display.show(Image.COW, delay= 500)

hp = 100
enhp = 20
epwr = 2
pwr = 10
while True:
    while enhp > 0:
        if button_a.is_pressed():
            enhp = enhp-pwr
            enper = random.randint(0,10)
            if enper < 7:
                display.scroll("THE ENEMY MISSED", delay = 100)
            else:
                hp = hp - epwr
                display.scroll("The enemy hit you and you have this much health left", delay = 100)
                display.scroll(str(hp))

    display.scroll("You beat the enemy", delay = 100)
    break

display.scroll("further along the trail you find a chest, you open it for a reward", delay = 100)
thg = random.randint(1,3)

while True:
    if thg >= 3:
        display.scroll("You got a heart which restores your health", delay = 100)
        hp = hp*2
    elif thg >= 2:
        display.scroll("You got a sword which doubles your damage", delay = 100)
        pwr = pwr*2
    else:
        display.scroll("The chest was empty", delay = 100)
    break
display.scroll("You stumble upon a rock who is challenging you to a fight", delay = 100)
enpwr = 10
enhp = 30

while True:
    while enhp > 0:
        yper = random.randint(0, 10)
        enper = random.randint(0, 10)
        if button_a.is_pressed():
            if yper <= 9:
                enhp = enhp - pwr
            else:
                display.scroll("You missed", delay = 100)
            if enper <= 4:
                display.scroll("The enemy hit you", delay = 100)
                hp = hp - enpwr
    display.scroll("The enemy requires you to press the b button 5 timesto beat him", delay = 100)
    sleep(5000)
    lol = button_b.get_presses()
    if lol >= 5 :
        display.scroll("You beat him")
    else:
        display.scroll("game over", loop = True)
    break
display.scroll("further along the trail you find another chest, you open it for a reward", delay = 100)
while True:
    if thg >= 3:
        display.scroll("You got a heart which restores your health", delay = 100)
        hp = hp*2
    elif thg >= 2:
        display.scroll("You got a sword which doubles your damage", delay = 100)
        pwr = pwr*2
    else:
        display.scroll("The chest was empty", delay = 100)
    break
display.scroll("At the end of the trail you encounter the last enemy")
enpwr = 20
enhp = 50
while True:
    while enhp > 0:
        yper = random.randint(0, 10)
        enper = random.randint(0, 10)
        if button_a.is_pressed():
            if yper <= 7:
                enhp = enhp - pwr
            else:
                display.scroll("You missed", delay = 100)
            if enper <= 3:
                display.scroll("The enemy hit you", delay = 100)
                hp = hp - enpwr
    display.scroll("The enemy lies down yet you do not know how to proceed", delay = 100, loop = false)
    gesture = accelerometer.current_gesture()
    if gesture == "face down":
        break
display.scroll("The enemy's back reveals the picture you were looking for. you won. congrats", delay = 100)
display.show(Image.HAPPY)
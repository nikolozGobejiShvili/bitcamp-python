import random

while True:
    try:
     text=int(input("level: "))
     if text < 0:
        continue
    except (ValueError, NameError):
       continue

     
    number=random.randint(1, text)

    guess=int(input("guess: "))

    if guess < 0:
       continue
    elif guess > number:
       print("Too large")
       continue
    elif guess < number:
       print("Too small")
       continue
    elif guess == number:
       print("Just right")
       break

         
      
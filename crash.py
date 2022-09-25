a = "scofield"
b = "kelly"

msg = f"{a} and {b} are brothers"
print(msg)

is_hot =False
is_cold = True

if is_hot:
    print("Drink hot water")
elif is_cold:
    print("Do not bother about going out")
else:
    print("have a great day")

buyer = int(input("please state your credit record: "))
buyer = True


if buyer >= 100:
    print("please sell the book")
 buyer <= 99:
    print("go back home and get more money")
else:
    print("Thank you for coming" )

name = input("please insert name here!: \n")

if len(name) <= 3:
    print("name must be three character long")
elif len(name) > 50:
    print("name can be a maximum of 50 character")
else:
    print("name looks good!")

weight = int(input("Input your figure: "))

Value = input("K or L: ")

if Value.upper() == "K" : 
    V = weight * 100
    print(f" Your weight is {V} kilos")
else:
    D = size * 0.75
    print(f"your mass is {D} Lbs")


Secret_Number = 8
guess_count = 0
Guess_limit = 3

while guess_count < Guess_limit:
    guess = int(input("guess: "))
    guess_count +=1 
    if guess == Secret_Number:
        print("wow, you got it!!!")
        break
else:
    print("You lose")



command = ""
started = False
stopped = False

while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("car already started")
        else:
            started = True
            print("car started")
    elif command == "stop":
        if stopped:
            print("car already stopped")
        else:
            stopped = True
            print("car stopped!!!")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print("text unkown...")

        

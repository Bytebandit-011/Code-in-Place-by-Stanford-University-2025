from karel.stanfordkarel import *

def main():
    while front_is_clear():
        collect_column()
        move_to_next_column()
    collect_column()  # Collect beepers in the last column

def collect_column():
    turn_left()
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()
    turn_around()
    while front_is_clear():
        move()
    turn_left()
def move_to_next_column():
    for i in range(4):  
        move()
def turn_around():
    turn_left()
    turn_left()

if __name__ == '__main__':
    main()
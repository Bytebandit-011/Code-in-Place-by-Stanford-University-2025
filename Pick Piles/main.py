from karel.stanfordkarel import *

# File: piles.py
# -----------------------------
# The warmup program defines a "main"
# function which should make Karel
# pick up all the beepers in the world.
def main():
    move()
    #your code here
    piles()
    move()
    move()
    piles()
    move()
    move()
    piles()
    move()
def piles():
    for i in range(10):
        pick_beeper()
   
   
# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()
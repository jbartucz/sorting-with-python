import pygame as pg
import random
from sys import exit

# this is an extension for the runsort.py assignment - do that part first!

# change this variable to update the display more often
# (smaller numbers will cause the program to run more slowly)
SWAPS_BETWEEN_SCREEN_UPDATES = 100
swap_counter = 0


def dosort():

    # fill in your code here

    if blocks[0] > blocks[1]:
        swap(0, 1)  # example of swapping the first and second block

    return


# ******************************************************************************************************
# You do not need to change any of the code below, but there is no harm in understanding what it does! *
# ******************************************************************************************************

# Set the dimensions of the window and display it
display = pg.display.set_mode((700, 700))

# set the colors to a random selection
colors = ["#%06x" % random.randint(0, 0xFFFFFF) for _ in range(300)]
colors.sort()  # makes a nice visual effect :)

# create a randomly sorted list of blocks from 1-300
blocks = [i for i in range(1, 301)]
random.shuffle(blocks)

# basically just keep the window open until they kill it
def check_events():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

# Swap two blocks (and update the visualization)
def swap(left, right):

    # swap the blocks
    tmp = blocks[left]
    blocks[left] = blocks[right]
    blocks[right] = tmp

    # draw the blocks
    display.fill(pg.Color("#CBC3E3"))  # clear the window
    for i, len in enumerate(blocks):
        # pg.draw.rect(display_window, color_of_rectangle, (left, top, width, height))
        pg.draw.rect(display, colors[len - 1],
                     (50 + i * 2, 650 - 2 * len, 2, 2 * len))

    global swap_counter
    if swap_counter == SWAPS_BETWEEN_SCREEN_UPDATES:
        pg.display.update()
        check_events()
        swap_counter = 0
    else:
        swap_counter += 1

    # pg.time.wait(500)  # slow down the visualization (milliseconds)


if __name__ == "__main__":
    # the program that is run
    try:
        pg.display.init()
        display.fill(pg.Color("#CBC3E3"))  # clear the window
        swap(1, 1)  # draw the randomized blocks
        pg.display.update()
        check_events()
        dosort()  # run the sorting algorithms
        while True:
            check_events()
    except Exception as error:
        print("An exception occurred:", type(error).__name__)
      

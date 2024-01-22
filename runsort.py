import pygame as pg
import random
from sys import exit

# this is your function to fill in!
def dosort():
    # REMEMBER!!! lists start at 0 in python, so the positions here are 0 to 9!
    # REMEMBER!!! If you go off the end of the list, python will crash!

    # this skeleton code makes a variable i go from 0 to 8 once
    # it swaps the block at position i with the next one over
    # essentially, it moves the first block to the end one position at a time.
    for i in range(9):
        swap(i, i + 1)

    # replace the code above with something that moves blocks to their proper positions!

    return  # you don't need to return anything


# ******************************************************************************************************
# You do not need to change any of the code below, but there is no harm in understanding what it does! *
# ******************************************************************************************************

# Set the dimensions of the window and display it
display = pg.display.set_mode((600, 600))

# set the colors to a nice rainbow effect :)
colors = ("#ff0000", "#e88416", "#ffa500", "#faeb36", "#b9d725",
          "#79c314", "#487de7", "#4b369d", "#70369d", "#301934")
# create a randomly sorted list of blocks from 1-10
blocks = [i for i in range(1, 11)]
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
    print(f"before: {blocks} ", end="")  # to help with debugging
    tmp = blocks[left]
    blocks[left] = blocks[right]
    blocks[right] = tmp
    print(f"after: {blocks}")  # to help with debugging

    # draw the blocks
    display.fill(pg.Color("#CBC3E3"))  # clear the window
    for i, len in enumerate(blocks):
        # pg.draw.rect(display_window, color_of_rectangle, (left, top, width, height))
        pg.draw.rect(display, colors[len - 1],
                     (60 + i * 50, 550 - 50 * len, 50, 50 * len))
    pg.display.flip()
    check_events()
    pg.time.wait(500)  # slow down the visualization


if __name__ == "__main__":
    # the program that is run
    try:
        pg.display.init()
        swap(1, 1)  # draw the randomized blocks
        dosort()  # run the sorting algorithms
        while True:
            check_events()
    except Exception as error:
        print("An exception occurred:", type(error).__name__)
        

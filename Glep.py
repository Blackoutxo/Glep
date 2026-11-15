import random
import sys
import textwrap

chaos = 0;

# Glep speak
SOUND = {
    "mrhm", "yah", "grph", "mrp", "hah", "huh", "yeah"
}

# Room
ROOM = {
    "Breakroom" : dict(
        name = "The smiling friends breakroom",
        desc = "Glep is sitting on a bean bag playing with his iPad doing nothing"
               "Charlie and pim and just sitting having a coffee"
               "Alan is looking at the TV about the election of president Jimball and Mr.Frog"
               "Mr.Boss comes in shaking and shivering for being hungry and opens the fridge"
               "He find no snacks and asks glep for help to find snack as the fridge was full JUST NOW",
        exits = ["Alley", "Bus stop"],
        items = [],
        people = ["Alan", "Charlie", "Pim", "Mr.Boss"]
    ),
    "Alley" : dict(
        name = "The smiling friends alley",
        desc = "In the alley, A dumpster, A puddle that reflects a worse version of yourself"
               "And an ominously opened drain gate with a single piece of m&m in its side",
        exits = ["Sewer", "Breakroom-again"],
        items=["A cool rock", "single piece of m&ms"],
        people =["Mr.Boss", "Glep"]
    ),
    "Breakroom-again": dict(
        name="The smiling friends breakroom",
        desc="Glep and Mr.boss went back to the breakroom and suspect something is wrong with the "
             "fridge below......................"
             "They moved the fridge and saw a big gaping hole that seems to lead to a sewer"
             "with a random ancient chinese gold, Charlie's uncle's pill box",
        exits = ["Alley", "Sewer"],
        items =["A random chinese gold coin", "Charlie's uncle's pills"],
        people = ["Mr.Boss", "Glep", "Charlie", "Pim"]
    ),
    "Sewer": dict(
        name="The sewer",
        desc="Knee-high water. Echo. A quarter glints on a dry ledge just past a"
    )
}

def go(destination): 


def eat(item):
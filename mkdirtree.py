#!/usr/bin/python3
#
#
#
#
# i dunno where to start this
#
#
# yo
# monkeys are funky flipping ... lol
#
# ill be kicking..
#
# magicians.. and flip the composition
# im plain im like scarface sniffing cocaine.. holding the m16.. ok ill stop
from os import mkdir

user_input = []
with open("config", "r") as config:
    for line in config:
        user_input += [str(line)[:-1]]


def func(user_input, parent="."):
    arr = []
    for i in user_input:
        if i[0] != ' ':
            if arr != []:
                # call function with previous parent
                func(arr, p)
                arr = []
            p = parent+'/'+i
            # cd parent and create this dir in it
            mkdir(f"{parent}/{i}")
            continue
        if i[0] == ' ':
            # add to the list well call next time
            # we encounter a non idented thing or when were done
            arr += [i[1:]]

    if arr != []:
        # call function with previous parent
        func(arr, p)


func(user_input)

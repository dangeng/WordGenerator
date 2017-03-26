import os
import subprocess
import re

def generateWord():
    words = []
    while len(words) == 0:
        data = subprocess.check_output(["th sample.lua -checkpoint cv/checkpoint_24000.t7 -length 500 -gpu -1"], shell=True)

        p = re.compile(">[A-Z]+<")

        words = p.findall(data.decode("utf-8"))

    return words[0][1:-1]


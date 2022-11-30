#!/usr/bin/env python3

import random
import sys

def generate(): 
    with open("data.csv") as data: 
        lines = data.readlines() 
        number = random.randint(1,19890) 
        target = lines[number].split(",")[0].split('"')[1]
        
        print(f"    \033[1;37m آیت الله {target}")

input("\033[1;31mPress any key to start: ".ljust(10))
print("\033[m\n")

try:
    while True:
        generate()
        input()
except KeyboardInterrupt:
    print("\n")
    sys.exit()
    

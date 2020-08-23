import keyboard
import louis
import sys

def init():
    louis.checkTable([b'./en-ueb-g2.ctb'])
    print('Initialized')

def input():
    input = sys.stdin.readlines()
    translate(input)

def translate(input):
    print('Translating')
    # prints the value of something and combines the ucBrl (64) and noUndefined (128) modes. Outputs as a single word, so a list is necessary to grab individual characters
    dotList = list(louis.charToDots([b'./en-ueb-g2.ctb'],input,mode=192))
    print('Heres the whole thing:')
    print(dotList)
    dispSize = 10
    chunked = list(divide_chunks(dotList, dispSize))
    print(chunked)
    printChunks(chunked)

def divide_chunks(list, number):
    for i in range(0, len(list), number):
        yield list[i:i + number]

def printChunks(chunks):
    n = 0
    print(chunks[n])
    while n<=len(chunks):
        if keyboard.is_pressed('n'):
            print('Printing line of dots')
            print(chunks[n])
            n = n+1

if __name__ == '__main__':
    init()
    input()

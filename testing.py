import louis
import sys

def main():
    print('Testing!')
    print('liblouis version: ' + louis.version())
    # something = input('type something: ')
    something = sys.stdin.readline().strip()
    print("Here's what you typed: " + something)
    braille = louis.translateString([b'./en-ueb-g2.ctb'],something, mode=4)
    print(list(braille))

if __name__ == "__main__":
    main()

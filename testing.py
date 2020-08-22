import louis
import sys

def main():
    print('Testing!')
    print('liblouis version: ' + louis.version())
    print('Table Check passed!')
    louis.checkTable([b'./en-ueb-g2.ctb'])
    # something = input('type something: ')
    something = sys.stdin.readline().strip()
    print("Here's what you typed: " + something)
    # prints the value of something and combines the ucBrl (64) and noUndefined (128) modes. Outputs as a single word, so a list is necessary to grab individual characters
    braille = louis.translateString([b'./en-ueb-g2.ctb'],something,mode=192)
    print(list(braille))
    print("Here it is in dots:")
    dots = louis.charToDots([b'./en-ueb-g2.ctb'],something,mode=192)
    print("Here's a back-translation of what you typed:")
    # Returns typed phrases without contractions, for proper bash interpretation
    backBraille = louis.backTranslateString([b'./en-ueb-g2.ctb'],braille,mode=1)
    print(backBraille)

if __name__ == "__main__":
    main()

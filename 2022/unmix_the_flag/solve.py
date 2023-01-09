import string

# decoded braille
enc = "5a42545a42485a42495a42534253457a6361774253457a797a7561776163"
encASCII = "ZBTZBHZBIZBSBSEzcawBSEzyzuawac"
numShift = "t"

upperFlag = string.ascii_uppercase[:26]
lowerFlag = string.ascii_lowercase[:26]
MIN_LETTER = ord("a")
MIN_CAPLETTER = ord("A")
toSolveOne = ""

def unmix(oneLetter,num):
    if(oneLetter.isupper()):
        word = ord(oneLetter)-MIN_CAPLETTER
        shift = ord(num)-MIN_CAPLETTER
        return upperFlag[(word - shift)%len(upperFlag)]
    if(oneLetter.islower()):
        word = ord(oneLetter)-MIN_LETTER
        shift = ord(num)-MIN_LETTER
        return lowerFlag[(word - shift)%len(upperFlag)]

def unpuzzle (puzzle):
    res = ""
    j=0
    while j<len(puzzle):
        if puzzle[j:j+3] == 'CTF':
            res += '_'
            j+=3

        if (puzzle[j].isupper()):
            binary = ""
            letter = ""
            binary += "{0:05b}".format(ord(puzzle[j])-MIN_CAPLETTER)
            binary += "{0:05b}".format(ord(puzzle[j+1])-MIN_CAPLETTER)
            binary += "{0:05b}".format(ord(puzzle[j+2])-MIN_CAPLETTER)
            j+=3
            letter = chr(int(binary, 2))
            res+=letter

        elif (puzzle[j].islower()):
            six = letter = ""
            six += "{0:01x}".format (ord(puzzle[j])-MIN_LETTER)
            six += "{0:01x}".format (ord(puzzle[j+1])-MIN_LETTER)
            j+=2
            letter = chr(int(six, 16))
            res+=letter
    return res 

unmixed = ""
for count, alpha in enumerate(encASCII):
    unmixed += unmix(alpha, numShift)

flag = unpuzzle(unmixed)
print (flag)
            
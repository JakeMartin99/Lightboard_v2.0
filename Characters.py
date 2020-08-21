# Get the list of pixels for a character, with upper left corner (x,y) of bounding 3x5 box
def char_pts(ch, x, y):
    if ch == 'A':
        return ['A', (x+1, y), (x, y+1), (x+2, y+1), (x, y+2), (x+1, y+2), (x+2, y+2),
                (x, y+3), (x+2, y+3), (x, y+4), (x+2, y+4)]
    elif ch == 'B':
        return ['B', (x,y), (x+1, y), (x, y+1), (x+2, y+1), (x, y+2), (x+1, y+2),
                (x, y+3), (x+2, y+3), (x, y+4), (x+1, y+4)]
    elif ch == 'C':
        return ['C', (x+1, y), (x+2, y), (x, y+1), (x, y+2), (x, y+3), (x+1, y+4),
                (x+2, y+4)]
    elif ch == 'D':
        return ['D', (x, y), (x+1, y), (x, y+1), (x+2, y+1), (x, y+2), (x+2, y+2), (x, y+3),
                (x+2, y+3), (x, y+4), (x+1, y+4)]
    elif ch == 'E':
        return ['E', (x,y), (x+1, y), (x+2, y), (x, y+1), (x, y+2), (x+1, y+2),
                (x, y+3), (x, y+4), (x+1, y+4), (x+2, y+4)]
    elif ch == 'F':
        return ['F', (x,y), (x+1, y), (x+2, y), (x, y+1), (x, y+2), (x+1, y+2),
                (x, y+3), (x, y+4)]
    elif ch == 'G':
        return ['G', (x,y), (x+1, y), (x+2, y), (x, y+1), (x+2, y+1), (x, y+2), (x+1, y+2),
                (x+2, y+2), (x+2, y+3), (x, y+4), (x+1, y+4), (x+2, y+4)]
    elif ch == 'H':
        return ['H', (x, y), (x+2, y), (x, y+1), (x+2, y+1), (x, y+2), (x+1, y+2),
                (x+2, y+2), (x, y+3), (x+2, y+3), (x, y+4), (x+2, y+4)]
    elif ch == 'I':
        return ['I', (x, y), (x+1, y), (x+2, y), (x+1, y+1), (x+1, y+2), (x+1, y+3),
                (x, y+4), (x+1, y+4), (x+2, y+4)]
    elif ch == 'J':
        return ['J', (x+2, y), (x+2, y+1), (x+2, y+2), (x, y+3), (x+2, y+3),
                (x, y+4), (x+1, y+4), (x+2, y+4)]
    elif ch == 'K':
        return ['K', (x, y), (x+2, y), (x, y+1), (x+2, y+1), (x, y+2), (x+1, y+2),
                (x, y+3), (x+2, y+3), (x, y+4), (x+2, y+4)]
    elif ch == 'L':
        return ['L', (x, y), (x, y+1), (x, y+2), (x, y+3), (x, y+4), (x+1, y+4),
                (x+2, y+4)]
    elif ch == 'M':
        return ['M', (x, y), (x+2, y), (x, y+1), (x+1, y+1), (x+2, y+1), (x, y+2),
                (x+1, y+2), (x+2, y+2), (x, y+3), (x+2, y+3), (x, y+4), (x+2, y+4)]
    elif ch == 'N':
        return ['N', (x, y), (x+1, y), (x+2, y), (x, y+1), (x+2, y+1), (x, y+2), (x+2, y+2),
                (x, y+3), (x+2, y+3), (x, y+4), (x+2, y+4)]
    elif ch == 'O':
        return ['O', (x, y), (x+1, y), (x+2, y), (x, y+1), (x+2, y+1), (x, y+2),
                (x+2, y+2), (x, y+3), (x+2, y+3), (x, y+4), (x+1, y+4), (x+2, y+4)]
    elif ch == 'P':
        return ['P', (x, y), (x+1, y), (x, y+1), (x+2, y+1), (x, y+2), (x+1, y+2),
                (x, y+3), (x, y+4)]
    elif ch == 'Q':
        return ['Q', (x, y), (x+1, y), (x+2, y), (x, y+1), (x+2, y+1), (x, y+2),
                (x+2, y+2), (x, y+3), (x+1, y+3), (x+2, y+4)]
    elif ch == 'R':
        return ['R', (x, y), (x+1, y), (x, y+1), (x+2, y+1), (x, y+2), (x+1, y+2),
                (x, y+3), (x+2, y+3), (x, y+4), (x+2, y+4)]
    elif ch == 'S':
        return ['S', (x,y), (x+1, y), (x+2, y), (x, y+1), (x, y+2), (x+1, y+2),
                (x+2, y+2), (x+2, y+3), (x, y+4), (x+1, y+4), (x+2, y+4)]
    elif ch == 'T':
        return ['T', (x, y), (x+1, y), (x+2, y), (x+1, y+1), (x+1, y+2), (x+1, y+3),
                (x+1, y+4)]
    elif ch == 'U':
        return ['U', (x, y), (x+2, y), (x, y+1), (x+2, y+1), (x, y+2), (x+2, y+2),
                (x, y+3), (x+2, y+3), (x, y+4), (x+1, y+4), (x+2, y+4)]
    elif ch == 'V':
        return ['V', (x, y), (x+2, y), (x, y+1), (x+2, y+1), (x, y+2), (x+2, y+2),
                (x, y+3), (x+2, y+3), (x+1, y+4)]
    elif ch == 'W':
        return ['W', (x, y), (x+2, y), (x, y+1), (x+2, y+1), (x, y+2), (x+1, y+2),
                (x+2, y+2), (x, y+3), (x+1, y+3), (x+2, y+3), (x, y+4), (x+2, y+4)]
    elif ch == 'X':
        return ['X', (x, y), (x+2, y), (x, y+1), (x+2, y+1), (x+1, y+2),
                (x, y+3), (x+2, y+3), (x, y+4), (x+2, y+4)]
    elif ch == 'Y':
        return ['Y', (x, y), (x+2, y), (x, y+1), (x+2, y+1), (x, y+2), (x+1, y+2),
                (x+2, y+2), (x+1, y+3), (x+1, y+4)]
    elif ch == 'Z':
        return ['Z', (x,y), (x+1, y), (x+2, y), (x+2, y+1), (x+1, y+2),
                (x, y+3), (x, y+4), (x+1, y+4), (x+2, y+4)]
    elif ch == '0':
        return ['0', (x+1, y), (x, y+1), (x+2, y+1), (x, y+2), (x+2, y+2), (x, y+3),
                (x+2, y+3), (x+1, y+4)]
    elif ch == '1':
        return ['1', (x+1, y), (x, y+1), (x+1, y+1), (x+1, y+2), (x+1, y+3),
                (x, y+4), (x+1, y+4), (x+2, y+4)]
    elif ch == '2':
        return ['2', (x,y), (x+1, y), (x+2, y+1), (x+1, y+2), (x, y+3), (x, y+4),
                (x+1, y+4), (x+2, y+4)]
    elif ch == '3':
        return ['3', (x, y), (x+1, y), (x+2, y+1), (x+1, y+2), (x+2, y+3),
                (x, y+4), (x+1, y+4)]
    elif ch == '4':
        return ['4', (x+2, y), (x+1, y+1), (x+2, y+1), (x, y+2), (x+2, y+2), (x, y+3),
                (x+1, y+3), (x+2, y+3), (x+2, y+4)]
    elif ch == '5':
        return ['5', (x,y), (x+1, y), (x+2, y), (x, y+1), (x, y+2), (x+1, y+2),
                (x+2, y+2), (x+2, y+3), (x, y+4), (x+1, y+4)]
    elif ch == '6':
        return ['6', (x+1, y), (x, y+1), (x, y+2), (x+1, y+2), (x, y+3),
                (x+2, y+3), (x+1, y+4)]
    elif ch == '7':
        return ['7', (x, y), (x+1, y), (x+2, y), (x+2, y+1), (x+1, y+2), (x+1, y+3),
                (x+1, y+4)]
    elif ch == '8':
        return ['8', (x+1, y), (x, y+1), (x+2, y+1), (x+1, y+2), (x, y+3),
                (x+2, y+3), (x+1, y+4)]
    elif ch == '9':
        return ['9', (x+1, y), (x, y+1), (x+2, y+1), (x, y+2), (x+1, y+2), (x+2, y+2),
                (x+2, y+3), (x+1, y+4)]
    elif ch == '<':
        return ['<', (x, y+2), (x+1, y+2), (x+2, y+2), (x+1, y+3)]
    elif ch == '-':
        return ['-', (x, y+2), (x+1, y+2), (x+2, y+2)]
    elif ch == '>':
        return ['>', (x+1, y+1), (x, y+2), (x+1, y+2), (x+2, y+2)]
    elif ch == '.':
        return ['.', (x+1, y+4)]
    elif ch == ' ':
        return [' ',]
    else: # ?
        return ['?', (x, y), (x+1, y), (x+2, y), (x+2, y+1), (x+1, y+2), (x+1, y+4)]

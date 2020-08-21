# Get the list of pixels for a character, with upper left corner (x,y) of bounding 3x5 box
def char_pts(ch, x, y):
    if ch == 'A':
        return [(x+1, y), (x, y+1), (x+2, y+1), (x, y+2), (x+1, y+2), (x+2, y+2),
                (x, y+3), (x+2, y+3), (x, y+4), (x+2, y+4)]
    elif ch == 'B':
        return [(x,y), (x+1, y), (x, y+1), (x+2, y+1), (x, y+2), (x+1, y+2),
                (x, y+3), (x+2, y+3), (x, y+4), (x+1, y+4)]
    elif ch == 'C':
        return [(x+1, y), (x+2, y), (x, y+1), (x, y+2), (x, y+3), (x+1, y+4),
                (x+2, y+4)]
    elif ch == 'D':
        return [(x, y), (x+1, y), (x, y+1), (x+2, y+1), (x, y+2), (x+2, y+2), (x, y+3),
                (x+2, y+3), (x, y+4), (x+1, y+4)]
    elif ch == 'E':
        return [(x,y), (x+1, y), (x+2, y), (x, y+1), (x, y+2), (x+1, y+2),
                (x, y+3), (x, y+4), (x+1, y+4), (x+2, y+4)]
    elif ch == 'F':
        return [(x,y), (x+1, y), (x+2, y), (x, y+1), (x, y+2), (x+1, y+2),
                (x, y+3), (x, y+4)]
    elif ch == 'G':
        return [(x+1, y), (x, y+1), (x+2, y+1), (x+1, y+2), (x+2, y+2), (x+2, y+3),
                (x, y+4), (x+1, y+4)]
    elif ch == 'H':
        return [(x, y), (x+2, y), (x, y+1), (x+2, y+1), (x, y+2), (x+1, y+2),
                (x+2, y+2), (x, y+3), (x+2, y+3), (x, y+4), (x+2, y+4)]
    elif ch == 'I':
        return [(x, y), (x+1, y), (x+2, y), (x+1, y+1), (x+1, y+2), (x+1, y+3),
                (x, y+4), (x+1, y+4), (x+2, y+4)]
    elif ch == 'J':
        return [(x+1, y), (x, y+1), (x+2, y+1), (x, y+2), (x+1, y+2), (x+2, y+2),
                (x, y+3), (x+2, y+3), (x, y+4), (x+2, y+4)]
    elif ch == 'K':
        return [(x+1, y), (x, y+1), (x+2, y+1), (x, y+2), (x+1, y+2), (x+2, y+2),
                (x, y+3), (x+2, y+3), (x, y+4), (x+2, y+4)]
    elif ch == 'L':
        return [(x, y), (x, y+1), (x, y+2), (x, y+3), (x, y+4), (x+1, y+4),
                (x+2, y+4)]
    elif ch == 'M':
        return [(x+1, y), (x, y+1), (x+2, y+1), (x, y+2), (x+1, y+2), (x+2, y+2),
                (x, y+3), (x+2, y+3), (x, y+4), (x+2, y+4)]
    elif ch == 'N':
        return [(x+1, y), (x, y+1), (x+2, y+1), (x, y+2), (x+1, y+2), (x+2, y+2),
                (x, y+3), (x+2, y+3), (x, y+4), (x+2, y+4)]
    elif ch == 'O':
        return [(x+1, y), (x, y+1), (x+2, y+1), (x, y+2), (x+1, y+2), (x+2, y+2),
                (x, y+3), (x+2, y+3), (x, y+4), (x+2, y+4)]
    elif ch == 'P':
        return [(x, y), (x+1, y), (x, y+1), (x+2, y+1), (x, y+2), (x+1, y+2),
                (x, y+3), (x, y+4)]
    elif ch == 'Q':
        return [(x+1, y), (x, y+1), (x+2, y+1), (x, y+2), (x+1, y+2), (x+2, y+2),
                (x, y+3), (x+2, y+3), (x, y+4), (x+2, y+4)]
    elif ch == 'R':
        return [(x+1, y), (x, y+1), (x+2, y+1), (x, y+2), (x+1, y+2), (x+2, y+2),
                (x, y+3), (x+2, y+3), (x, y+4), (x+2, y+4)]
    elif ch == 'S':
        return [(x+1, y), (x, y+1), (x+2, y+1), (x, y+2), (x+1, y+2), (x+2, y+2),
                (x, y+3), (x+2, y+3), (x, y+4), (x+2, y+4)]
    elif ch == 'T':
        return [(x+1, y), (x, y+1), (x+2, y+1), (x, y+2), (x+1, y+2), (x+2, y+2),
                (x, y+3), (x+2, y+3), (x, y+4), (x+2, y+4)]
    elif ch == 'U':
        return [(x+1, y), (x, y+1), (x+2, y+1), (x, y+2), (x+1, y+2), (x+2, y+2),
                (x, y+3), (x+2, y+3), (x, y+4), (x+2, y+4)]
    elif ch == 'V':
        return [(x+1, y), (x, y+1), (x+2, y+1), (x, y+2), (x+1, y+2), (x+2, y+2),
                (x, y+3), (x+2, y+3), (x, y+4), (x+2, y+4)]
    elif ch == 'W':
        return [(x+1, y), (x, y+1), (x+2, y+1), (x, y+2), (x+1, y+2), (x+2, y+2),
                (x, y+3), (x+2, y+3), (x, y+4), (x+2, y+4)]
    elif ch == 'X':
        return [(x+1, y), (x, y+1), (x+2, y+1), (x, y+2), (x+1, y+2), (x+2, y+2),
                (x, y+3), (x+2, y+3), (x, y+4), (x+2, y+4)]
    elif ch == 'Y':
        return [(x+1, y), (x, y+1), (x+2, y+1), (x, y+2), (x+1, y+2), (x+2, y+2),
                (x, y+3), (x+2, y+3), (x, y+4), (x+2, y+4)]
    elif ch == 'Z':
        return [(x+1, y), (x, y+1), (x+2, y+1), (x, y+2), (x+1, y+2), (x+2, y+2),
                (x, y+3), (x+2, y+3), (x, y+4), (x+2, y+4)]
    elif ch == '0':
        return [(x+1, y), (x, y+1), (x+2, y+1), (x, y+2), (x+1, y+2), (x+2, y+2),
                (x, y+3), (x+2, y+3), (x, y+4), (x+2, y+4)]
    elif ch == '1':
        return [(x+1, y), (x, y+1), (x+2, y+1), (x, y+2), (x+1, y+2), (x+2, y+2),
                (x, y+3), (x+2, y+3), (x, y+4), (x+2, y+4)]
    elif ch == '2':
        return [(x+1, y), (x, y+1), (x+2, y+1), (x, y+2), (x+1, y+2), (x+2, y+2),
                (x, y+3), (x+2, y+3), (x, y+4), (x+2, y+4)]
    elif ch == '3':
        return [(x+1, y), (x, y+1), (x+2, y+1), (x, y+2), (x+1, y+2), (x+2, y+2),
                (x, y+3), (x+2, y+3), (x, y+4), (x+2, y+4)]
    elif ch == '4':
        return [(x+1, y), (x, y+1), (x+2, y+1), (x, y+2), (x+1, y+2), (x+2, y+2),
                (x, y+3), (x+2, y+3), (x, y+4), (x+2, y+4)]
    elif ch == '5':
        return [(x+1, y), (x, y+1), (x+2, y+1), (x, y+2), (x+1, y+2), (x+2, y+2),
                (x, y+3), (x+2, y+3), (x, y+4), (x+2, y+4)]
    elif ch == '6':
        return [(x+1, y), (x, y+1), (x+2, y+1), (x, y+2), (x+1, y+2), (x+2, y+2),
                (x, y+3), (x+2, y+3), (x, y+4), (x+2, y+4)]
    elif ch == '7':
        return [(x+1, y), (x, y+1), (x+2, y+1), (x, y+2), (x+1, y+2), (x+2, y+2),
                (x, y+3), (x+2, y+3), (x, y+4), (x+2, y+4)]
    elif ch == '8':
        return [(x+1, y), (x, y+1), (x+2, y+1), (x, y+2), (x+1, y+2), (x+2, y+2),
                (x, y+3), (x+2, y+3), (x, y+4), (x+2, y+4)]
    elif ch == '9':
        return [(x+1, y), (x, y+1), (x+2, y+1), (x, y+2), (x+1, y+2), (x+2, y+2),
                (x, y+3), (x+2, y+3), (x, y+4), (x+2, y+4)]
    elif ch == '<':
        return [(x, y+2), (x+1, y+2), (x+2, y+2), (x+1, y+3)]
    elif ch == '>':
        return [(x+1, y+1), (x, y+2), (x+1, y+2), (x+2, y+2)]
    elif ch == ' ':
        return []
    else: # ?
        return [(x, y), (x+1, y), (x+2, y), (x+2, y+1), (x+1, y+2), (x+1, y+4)]

def split_string(source,splitlist):
    output = []
    atsplit = True# at any split point
    for char in source:
        if char in splitlist:
            atsplit = True

        else:
            if atsplit:
                outpput.append(char)
                atsplit = False
            else:
                # add character to last word
                output[-1] = output[-1] + char
    
    return output

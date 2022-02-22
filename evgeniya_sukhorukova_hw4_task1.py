line = input('Enter any string with more than 4 characters\n')
if len(line) >= 4:
    line1 = line[0] + line[1] + line[-2] + line[-1]
    print(line1)
else:
    print('Your string is too short - %s ' % line)

def telephone_check(tel):
    input = ''

    for t in tel:
        if t.isdigit():
            input += t

    if len(input) == 11 and input[0] == "1":
        input = input.replace(input[0],'')

    if(len(input) != 10):
        return False

    phonebook = [
            input[0:3] + input[3:6] + input[6:10],
            "("  + input[0:3] + ")" + input[3:6] + "-" + input[6:10],
            "("  + input[0:3] + ")" + input[3:6] + " " + input[6:10],
            input[0:3] + " " + input[3:6] + " " + input[6:10],
            input[0:3] + "-" + input[3:6] + "-" + input[6:10],
            "1 " + input[0:3] + "-" + input[3:6] + "-" + input[6:10],
           "1 " + input[0:3] + " " + input[3:6] + " " + input[6:10],
           "1" + "(" + input[0:3] + ")" + input[3:6] + " " + input[6:10],
           "1" + "(" + input[0:3] + ")" + input[3:6] + "-" + input[6:10],
           "1" + " (" + input[0:3] + ") " + input[3:6] + "-" + input[6:10],
           "1 " +  input[0:3] + "-" + input[3:6] + "-" + input[6:10],
           "1 " +  input[0:3] + " " + input[3:6] + " " + input[6:10],

    ]


    for i in range(len(phonebook)):
        if tel == phonebook[i]:
            return True
    return False
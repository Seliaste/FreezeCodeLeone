variableDictionary = {}


def fileReader(filePath):
    file = open(filePath)
    lines = file.readlines()
    file.close()
    for lineNo in range(len(lines)):
        line = lines[lineNo].rstrip('\n')
        returnCode = lexer(line, lineNo)
        if returnCode != 0:
            return returnCode
    return 0


def lexer(command="", lineNo=None):
    tokens = ["j'suis", "fons", "comme", "si",
              "lin", "pendant", "avec", "sans", "par", "s/o", "RIP"]

    orders = command.split(" ")
    for orderIndex in range(len(orders)):
        order = orders[orderIndex]
        if order in tokens:
            if order == "j'suis":
                assert orders[orderIndex+2] == "comme" and orders[orderIndex +
                                                                  1] != None and orders[orderIndex+3] != None, "Invalid command at line "+str(lineNo)
                variableDictionary[str(orders[orderIndex+1])
                                   ] = str(orders[orderIndex+3])
                return 0
            elif order == "s/o":
                assert orders[orderIndex +
                              1] != None, "Invalid command at line "+str(lineNo)
                if orders[orderIndex+1] not in [*variableDictionary]:
                    print(orders[orderIndex+1])
                # elif "\"" in orders[orderIndex+1]: DOES NOT WORK YET
                #     outputstring = ""
                #     for i in range(1,len(orders)):
                #         outputstring += str(i) 
                #     print(outputstring)
                else:
                    print(str(variableDictionary[orders[orderIndex+1]]))
                return 0
            elif order == "avec":
                firstOperator = variableDictionary[orders[orderIndex-1]]
                if type(orders[orderIndex+1]) == int:
                    secondOperator = orders[orderIndex+1]
                else:
                    secondOperator = variableDictionary[orders[orderIndex+1]]
                    del variableDictionary[orders[orderIndex+1]]
                variableDictionary[orders[orderIndex-1]
                                   ] = int(firstOperator) + int(secondOperator)
                return 0
            elif order == "RIP":
                return 2
            else:
                continue


if __name__ == "__main__":
    choice = input("1 for file, 2 for interpreter : ")
    if choice == "1":
        filePrompt = str(input("What is the file path:"))
        if filePrompt.split(".")[len(filePrompt.split("."))-1] != "667":
            print("wrong file extension : please use \".667\" (ekip)")
        else:
            fileReader(filePrompt)
    elif choice == "2":
        lastReturn = 0
        while lastReturn == 0:
            lexer(input("FreezeCodeLeone>"))
    else:
        print("Wrong choice")

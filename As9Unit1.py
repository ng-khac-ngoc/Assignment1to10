import os, sys, magic


def checkCmd(cmd):          # check input in cmd from user
    if len(cmd) < 2:
        print('Not have path of folder/file')
        sys.exit()
    elif len(cmd) > 2:
        print('only 2 arguments')
        sys.exit()


def listFile(path):         # print all file in folder
    print(path, ':')
    for file in os.listdir(path):
        print(file)


def checkFileFolder(cmd):           # check type file
    for i in range(len(cmd)):
        if i > 0:
            input = cmd[i]
            if (os.path.isdir(input)):
                print(input, 'is a directory')
                listFile(input)
            elif (os.path.isfile(input)):
                print(input, ': ', magic.from_file(input))
            else:
                print(input, 'Not exist')


arg = sys.argv
checkCmd(arg)
checkFileFolder(arg)

import sys

from extender import *

# ----------------------------------------------
if __name__ == '__main__':

    # import time
    # start_time = time.time()

    inputFileName = "none"
    if sys.argv[1] == "-f":
        inputFileName = sys.argv[2]
        outputFileName = sys.argv[3]
    elif sys.argv[1] == "-n":
        arrayLen = int(sys.argv[2])
        if arrayLen > 100000 or arrayLen < 1:
            print("Incorrect command line! You must write: -f <inputFileName> <outputFileName>"
                  "or -n <number less than 10000 and larger than 1> outputFileName")
            exit()
        outputFileName = sys.argv[3]
    else:
        print("Incorrect command line! You must write: -f <inputFileName> <outputFileName>"
              "or -n <number> outputFileName")
        exit()

    # Чтение исходного файла, содержащего данные, разделенные пробелами и переводами строки
    if inputFileName != "none":
        ifile = open(inputFileName)
        data = ifile.read()
        ifile.close()
        # Формирование массива строк, содержащего чистые данные в виде массива строк символов.
        strArray = data.replace("\n", " ").split(" ")

    print('==> Start')

    container = Container()

    if inputFileName != "none":
        plantNum = ReadStrArray(container, strArray)
    else:
        plantNum = RandomRead(container, arrayLen)

    container.Print()

    ofile = open(outputFileName, 'w')
    container.Write(ofile)
    ofile.close()

    print('==> Finish')

    # print("--- %s seconds ---" % (time.time() - start_time))

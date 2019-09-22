#!/usr/bin/python3
import os, sys, getopt

# https://stackoverflow.com/questions/11109859/pipe-output-from-shell-command-to-a-python-script/11109920 < todooo

def main(argv):
    baseURL = ''
    fileName = ''
    paths = []

    try:
        opts, args = getopt.getopt(argv,"hb:f:",["baseURL=","fileName="])
    except getopt.GetoptError:
      print ('test.py -b <baseURL> -F <outputfile>')
      sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('test.py -b <baseURL> -f <fileName>')
            sys.exit()
        elif opt in ("-b", "--baseURL"):
            baseURL = arg
        elif opt in ("-f", "--fileName"):
            fileName = arg

    f = open(fileName, "r")
    for x in f:
        paths.append(baseURL+x.rstrip())

    for path in paths:
        print("Trying to snapshot " + path)
        os.system('pageres ' + path + ' 1368x1000 --crop')
        os.system('pageres ' + path + ' 368x1000 --crop')

if __name__ == "__main__":
   main(sys.argv[1:])
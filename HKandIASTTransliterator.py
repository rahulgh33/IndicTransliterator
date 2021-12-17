import csv
import pandas as pd
import numpy as np


def transliterateWord(word, chart):
    hkword = ''
    length = len(word)
    i = 0
    while i < length:
        ch = word[i]
        uCode = ord(ch)
        hCode = str(hex(uCode))
        if(isLetter(uCode)):
            hkLetter = chart.loc[chart.DevanagariCode == hCode, 'HKReal'].values[0]
            if(i + 1 < length ):
                nextCh = word[i + 1]
                nextUCode = ord(nextCh)
                nextHCode = str(hex(nextUCode))
                if(isLetter(nextUCode)):
                    if(isVowel(uCode)):
                        hkword = hkword + hkLetter
                        i+=1
                    elif(isAvagraha(uCode)):
                        hkword = hkword + "'"
                        i+=1
                    else:
                        hkword = hkword + hkLetter + 'a'
                        i+=1
                elif(isMatra(nextUCode)):
                    nextHkLetter = chart.loc[chart.DevanagariCode == nextHCode, 'HKReal'].values[0]
                    hkword = hkword + hkLetter + nextHkLetter
                    if (i+2 < length):
                        secondNextCh = word[i + 2]
                        secondNextUCode = ord(secondNextCh)
                        secondNextHCode = str(hex(secondNextUCode))
                        if(isAyogvah(secondNextUCode)):
                            secondNextHkLetter = chart.loc[chart.DevanagariCode == secondNextHCode, 'HKReal'].values[0]
                            hkword = hkword + secondNextHkLetter
                            i += 2
                        else:
                            i+=2
                    else:
                        i+=1
                elif(isAyogvah(nextUCode)):
                    nextHkLetter = chart.loc[chart.DevanagariCode == nextHCode, 'HKReal'].values[0]
                    hkword = hkword + hkLetter + 'a' + nextHkLetter
                    i+=2
                elif(isHalant(nextUCode)):
                    if(i+2 < length):
                        hkword = hkword + hkLetter
                        i+=2
                    else:
                        hkword = hkword + hkLetter
                        i+=1
            else:
                # Last Character
                hkword = hkword + hkLetter + 'a'
                i += 1
        else:
            i+=1
    return hkword

def iastTransliterateWord(word, chart):
    iastword = ''
    length = len(word)
    i = 0
    while i < length:
        ch = word[i]
        uCode = ord(ch)
        iCode = str(hex(uCode))
        if(isLetter(uCode)):
            iastLetter = chart.loc[chart.Devanagari == iCode, 'IAST'].values[0]
            if(i + 1 < length ):
                nextCh = word[i + 1]
                nextUCode = ord(nextCh)
                nextICode = str(hex(nextUCode))
                if(isLetter(nextUCode)):
                    if(isVowel(uCode)):
                        iastword = iastword + iastLetter
                        i+=1
                    elif (isAvagraha(uCode)):
                        iastword = iastword + "'"
                        i += 1
                    else:
                        iastword = iastword + str(iastLetter) + 'a'
                        i+=1
                elif(isMatra(nextUCode)):
                    nextIastLetter = chart.loc[chart.Devanagari == nextICode, 'IAST'].values[0]
                    iastword = iastword + iastLetter + nextIastLetter
                    # i+=2
                    if (i+2 < length):
                        secondNextCh = word[i + 2]
                        secondNextUCode = ord(secondNextCh)
                        secondNextICode = str(hex(secondNextUCode))
                        if(isAyogvah(secondNextUCode)):
                            secondNextIastLetter = chart.loc[chart.Devanagari == secondNextICode, 'IAST'].values[0]
                            iastword = iastword + secondNextIastLetter
                            i += 2
                        else:
                            i+=2
                    else:
                        i+=1
                elif(isAyogvah(nextUCode)):
                    nextIastLetter = chart.loc[chart.Devanagari == nextICode, 'IAST'].values[0]
                    iastword = iastword + iastLetter + 'a' + nextIastLetter
                    i+=2
                elif(isHalant(nextUCode)):
                    if(i+2 < length):
                        iastword = iastword + iastLetter
                        i+=2
                    else:
                        iastword = iastword + iastLetter
                        i+=1
            else:
                # Last Character
                iastword = iastword + iastLetter + 'a'
                i += 1
        else:
            i+=1
    return iastword

def isLetter(uCode):
    start = int('0905', 16)
    end = int('093D', 16)
    if start <= uCode <= end:
        return True
    else:
        return False

def isVowel(uCode):
    start = int('0905', 16)
    end = int('0914', 16)
    if start <= uCode <= end:
        return True
    else:
        return False
def isAyogvah(uCode):
    start = int('0902', 16)
    end = int('0903', 16)
    if start <= uCode <= end:
        return True
    else:
        return False

def isAvagraha(uCode):
    return uCode == int('093D', 16)

def isMatra(uCode):
    start = int('093E', 16)
    end = int('094C', 16)
    if start <= uCode <= end:
        return True
    else:
        return False

def isHalant(uCode):
    return uCode == int('094D', 16)

def hkCreateMap(filename):
    columnNames = ['DevanagariCode', 'HKReal']
    dict_from_csv = pd.read_csv(filename, header=0, index_col=None, names=columnNames, squeeze=None)
    return dict_from_csv

def iastCreateMap(filename):
    columnNames = ['Devanagari', 'IAST']
    dict_from_csv = pd.read_csv(filename, header=0, index_col=None, names=columnNames, squeeze=None)
    return dict_from_csv

def transliterate(filename):
   inputfile = open(filename, 'r')
   lines = inputfile.readlines()
   devLine = "Devanagari: "
   hkLine = "Harvard Kyoto: "
   iastLine = "IAST: "
   for line in lines:
       words = line.split()
       for word in words:
           devLine = devLine + word + " "
           hkLine = hkLine + transliterateWord(word, HKchart) + " "
           iastLine = iastLine + iastTransliterateWord(word, iastchart) + " "
       devLine = devLine + "\n"
       hkLine = hkLine + "\n"
       iastLine = iastLine + "\n"
   print(devLine)
   print(hkLine)
   print(iastLine)


if __name__ == '__main__':
    HKchart = hkCreateMap('HKChart.csv')
    iastchart = iastCreateMap('IASTChart.csv')
    transliterate('nasadiya.txt')




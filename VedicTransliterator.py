import csv
import pandas as pd
import numpy as np


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
                    elif(isAvagraha(uCode)):
                        iastword = iastword + "'"
                        i+=1
                    else:
                        iastword = iastword + str(iastLetter) + 'a'
                        i+=1
                elif(isPunctuation(nextUCode)):
                    nextIastLetter = chart.loc[chart.Devanagari == nextICode, 'IAST'].values[0]
                    iastword = iastword + iastLetter + 'a' + nextIastLetter
                    i += 2

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
                        elif (isUdatta(secondNextUCode)):
                            if(isa(nextUCode)):
                                iastword = iastword[:-1] + 'á'
                                i += 2
                            elif (isA(nextUCode)):
                                iastword = iastword[:-1] + 'ā́'
                                i += 2
                            elif (isi(nextUCode)):
                                iastword = iastword[:-1] + 'í'
                                i += 2
                            elif (isI(nextUCode)):
                                iastword = iastword[:-1] + 'ī́'
                                i += 2
                            elif (isu(nextUCode)):
                                iastword = iastword[:-1] + 'ú'
                                i += 2
                            elif (isU(nextUCode)):
                                iastword = iastword[:-1] + 'ū́'
                                i += 2
                            elif (ise(nextUCode)):
                                iastword = iastword[:-1] + 'é'
                                i += 2
                            elif (isai(nextUCode)):
                                iastword = iastword[:-1] + 'ái'
                                i += 2
                            elif (iso(nextUCode)):
                                iastword = iastword[:-1] + 'ó'
                                i += 2
                            elif (isau(nextUCode)):
                                iastword = iastword[:-1] + 'áu'
                                i += 2
                            elif (isr(nextUCode)):
                                iastword = iastword[:-1] + 'ṛ́'
                                i += 2
                            elif (isl(nextUCode)):
                                iastword = iastword[:-1] + 'ḷ́'
                                i += 2
                        elif (isAnudatta(secondNextUCode)):
                            if(isa(nextUCode)):
                                iastword = iastword[:-1] + 'à'
                                i+=2
                            elif (isA(nextUCode)):
                                iastword = iastword[:-1] + 'ā̀'
                                i += 2
                            elif (isi(nextUCode)):
                                iastword = iastword[:-1] + 'ì'
                                i += 2
                            elif (isI(nextUCode)):
                                iastword = iastword[:-1] + 'ī̀'
                                i += 2
                            elif (isu(nextUCode)):
                                iastword = iastword[:-1] + 'ù'
                                i += 2
                            elif (isU(nextUCode)):
                                iastword = iastword[:-1] + 'ū̀'
                                i += 2
                            elif (ise(nextUCode)):
                                iastword = iastword[:-1] + 'è'
                                i += 2
                            elif (isai(nextUCode)):
                                iastword = iastword[:-1] + 'ài'
                                i += 2
                            elif (iso(nextUCode)):
                                iastword = iastword[:-1] + 'ò'
                                i += 2
                            elif (isau(nextUCode)):
                                iastword = iastword[-1] + 'àu'
                                i += 2
                            elif (isr(nextUCode)):
                                iastword = iastword[:-1] + 'ṛ̀'
                                i += 2
                            elif (isl(nextUCode)):
                                iastword = iastword[:-1] + 'ḷ̀'
                                i += 2
                        else:
                            i+=2
                    else:
                        i+=1
                elif (isUdatta(nextUCode)):
                    iastword = iastword + iastLetter
                    if (isConsonant(uCode)):
                        iastword += 'á'
                        i += 2
                    if (isa(uCode)):
                        iastword = iastword[:-1] + 'á'
                        i += 2
                    elif (isA(uCode)):
                        iastword = iastword[:-1] + 'ā́'
                        i += 2
                    elif (isi(uCode)):
                        iastword = iastword[:-1] + 'í'
                        i += 2
                    elif (isI(uCode)):
                        iastword = iastword[:-1] + 'ī́'
                        i += 2
                    elif (isu(uCode)):
                        iastword = iastword[:-1] + 'ú'
                        i += 2
                    elif (isU(uCode)):
                        iastword = iastword[:-1] + 'ū́'
                        i += 2
                    elif (ise(uCode)):
                        iastword = iastword[:-1] + 'é'
                        i += 2
                    elif (isai(uCode)):
                        iastword = iastword[:-1] + 'ái'
                        i += 2
                    elif (iso(uCode)):
                        iastword = iastword[:-1] + 'ó'
                        i += 2
                    elif (isau(uCode)):
                        iastword = iastword[:-1] + 'áu'
                        i += 2
                    elif (isr(uCode)):
                        iastword = iastword[:-1] + 'ṛ́'
                        i += 2
                    elif (isl(uCode)):
                        iastword = iastword[:-1] + 'ḷ́'
                        i += 2
                elif (isAnudatta(nextUCode)):
                    iastword = iastword + iastLetter
                    if(isConsonant(uCode)):
                        iastword += 'à'
                        i += 2
                    if (isa(uCode)):
                        iastword = iastword[:-1] + 'à'
                        i += 2
                    elif (isA(uCode)):
                        iastword = iastword[:-1] + 'ā̀'
                        i += 2
                    elif (isi(uCode)):
                        iastword = iastword[-1] + 'ì'
                        i += 2
                    elif (isI(uCode)):
                        iastword = iastword[-1] + 'ī̀'
                        i += 2
                    elif (isu(uCode)):
                        iastword = iastword[-1] + 'ù'
                        i += 2
                    elif (isU(uCode)):
                        iastword = iastword[-1] + 'ū̀'
                        i += 2
                    elif (ise(uCode)):
                        iastword = iastword[-1] + 'è'
                        i += 2
                    elif (isai(uCode)):
                        iastword = iastword[-1] + 'ài'
                        i += 2
                    elif (iso(uCode)):
                        iastword = iastword[-1] + 'ò'
                        i += 2
                    elif (isau(uCode)):
                        iastword = iastword[-1] + 'àu'
                        i += 2
                    elif (isr(uCode)):
                        iastword = iastword[-1] + 'ṛ̀'
                        i += 2
                    elif (isl(uCode)):
                        iastword = iastword[-1] + 'ḷ̀'
                        i += 2

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
        elif(isPunctuation(uCode)):
            iastLetter = chart.loc[chart.Devanagari == iCode, 'IAST'].values[0]
            iastword+=iastLetter
            i+=1
        elif (isOm(uCode)):
            iastLetter = chart.loc[chart.Devanagari == iCode, 'IAST'].values[0]
            iastword += iastLetter
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
def isOm(uCode):
    return uCode == int('0950', 16)

def isVowel(uCode):
    start = int('0905', 16)
    end = int('0914', 16)
    if start <= uCode <= end:
        return True
    else:
        return False
def isAyogvah(uCode):
    start = int('0900', 16)
    end = int('0903', 16)
    if start <= uCode <= end:
        return True
    else:
        return False

def isMatra(uCode):
    start = int('093E', 16)
    end = int('094C', 16)
    if start <= uCode <= end:
        return True
    else:
        return False

def isHalant(uCode):
    return uCode == int('094D', 16)

def isPunctuation(uCode):
    start = int('0964', 16)
    end = int('0971', 16)
    if start <= uCode <= end:
        return True
    else:
        return False

def isa(uCode):
    return uCode == int('0905', 16) or uCode == int('093d', 16)

def isA(uCode):
    return uCode == int('0906', 16) or uCode == int('093e', 16)

def isi(uCode):
    return uCode == int('0907', 16) or uCode == int('093f', 16)

def isI(uCode):
    return uCode == int('0908', 16) or uCode == int('0940', 16)

def isu(uCode):
    return uCode == int('0909', 16) or uCode == int('0941', 16)

def isU(uCode):
    return uCode == int('090a', 16) or uCode == int('0942', 16)

def ise(uCode):
    return uCode == int('090f', 16) or uCode == int('0947', 16)

def isai(uCode):
    return uCode == int('0910', 16) or uCode == int('0948', 16)

def iso(uCode):
    return uCode == int('0913', 16) or uCode == int('094b', 16)

def isau(uCode):
    return uCode == int('0914', 16) or uCode == int('094c', 16)

def isr(uCode):
    return uCode == int('090b', 16) or uCode == int('0943', 16)

def isl(uCode):
    return uCode == int('090c', 16) or uCode == int('0962', 16)
def isConsonant(uCode):
    start = int('0915', 16)
    end = int('093D', 16)
    if start <= uCode <= end:
        return True
    else:
        return False

def isAvagraha(uCode):
    return uCode == int('093D', 16)

def isUdatta(uCode):
    return uCode == int('0951', 16)

def isAnudatta(uCode):
    return uCode == int('0952', 16)

def iastCreateMap(filename):
    columnNames = ['Devanagari', 'IAST']
    dict_from_csv = pd.read_csv(filename, header=0, index_col=None, names=columnNames, squeeze=None)
    return dict_from_csv

def transliterate(filename):
   inputfile = open(filename, 'r')
   lines = inputfile.readlines()
   devLine = "Devanagari: "
   iastLine = "IAST: "
   for line in lines:
       words = line.split()
       for word in words:
           devLine = devLine + word + " "
           iastLine = iastLine + iastTransliterateWord(word, iastchart) + " "
       devLine = devLine + "\n"
       iastLine = iastLine + "\n"
   print(devLine)
   print(iastLine)


if __name__ == '__main__':
    iastchart = iastCreateMap('vedicPitch.csv')
    transliterate('agnimile.txt')




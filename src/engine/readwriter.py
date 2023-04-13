import csv

def readTXTtoString(path):
    """ Lire un fichier au format texte et retourner une chaine de caractère
    """
    filestream =  open(path, 'r', encoding='UTF8')
    lines = filestream.readlines()
    filestream.close()
    data = ""
    for line in lines:
        data += line
    return data

def readTXTtoList(path):
    """ Lire un fichier au format texte et retourner une liste de chaines de caractère
    """
    filestream =  open(path, 'r', encoding='UTF8')
    lines = filestream.readlines()
    filestream.close()
    return lines

def readCSVtoList(path):
    data = []
    f = open(path,'r', encoding='utf8')
    reads = csv.reader(f)
    for row in reads:
        data += [row]
    f.close()
    return data

def writeListtoTXT(path, data):
    f = open(path, 'w', encoding='utf8')
    for line in data :
        f.write(line)
    f.close()

def writeListtoCSV(path, data):
    f = open(path,"w", newline="", encoding="utf8")
    ecrire=csv.writer(f)
    for row in data :
        ecrire.writerow(row)
    f.close()

import csv
import os
import shutil

# initalise
fulltextCSV = 'Round 2 manual matching pdfs.csv'
fullTextFile = 'FullTexts'
maindir = os.path.dirname(os.path.realpath(__file__))
PDFpath = os.path.join(maindir, '05 Feb 21_Autofind rnd 2_YM')
ftFile = os.path.join(maindir, fullTextFile)


def getRefID(ftTitle):
    with open(os.path.join(maindir, fulltextCSV), 'r') as file:
        reader = csv.reader(file)
        refIDList = []
        for row in reader:
            if row[1] == ftTitle:
                refIDList.append(row[0])

        if len(refIDList) == 0:
            refIDList.append('MISSING')

    return refIDList

def main():
    # traverse through PDF
    print('start')
    dupes = []
    missing = []

    PDFdir = os.listdir(PDFpath)
    for refFile in PDFdir:
        if not refFile.startswith('.'):
            print(refFile)
            IDS = getRefID(refFile)
            print(IDS)
            for ID in IDS:
                filename = ID + '_' + refFile
                shutil.copy(os.path.join(PDFpath, refFile), os.path.join(ftFile, filename))

            if len(IDS) > 1:
                IDS.insert(0, refFile)
                dupes.append(IDS)
            
            if IDS[0] == 'MISSING':
                IDS.insert(0, refFile)
                missing.append(IDS)
    
    print(dupes)
    print(missing)
    with open(os.path.join(maindir, 'Duplicates and Missing.csv'), 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['Filename', 'RefID'])

        for entry in dupes:
            writer.writerow(entry)
        
        writer.writerow(['#####', '#####', '#####', '#####', '#####', '#####', '#####', '#####', '#####', '#####'])
        
        for entry in missing:
            writer.writerow(entry)

if __name__ == "__main__":
    main()
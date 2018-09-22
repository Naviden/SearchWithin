# import packages
import PyPDF2
import re
import glob


path = '/Users/Navid/Documents/books'
extention = 'pdf'
query = 'd\.\s+median'

files = glob.glob(path + '/*.' + extention)
for file in files:
    title = file.split('/')[-1].split('.')[0].replace('-', ' ')
    print(f'Title : {title}')
    # print(file)
    try:
        # # open the pdf file
        object = PyPDF2.PdfFileReader(file, strict=False)
        # # get number of pages
        NumPages = object.getNumPages()

        # extract text and do the search
        errs = 0
        fon = 0
        for i in range(0, NumPages):
            PageObj = object.getPage(i)
            try:
                Text = PageObj.extractText()
                ResSearch = re.search(query, Text)
                if ResSearch is not None:
                    fon += 1
            except:
                errs += 1

        un = round(((1 - (errs / NumPages)) * 100), 1)

        print(f'Reachable : {un}%')
        print(f'Found : {fon}')
        print('**********************')
        print()
    except:
        print('Book is not searchable :(')
        print('**********************')
        print()

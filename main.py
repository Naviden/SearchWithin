# import packages
import PyPDF2
import re
import glob


path = '/Users/Navid/Documents/books'
extention = 'pdf'
query = 'python'

files = glob.glob(path + '/*.' + extention)
file = files[0]   # print(file)
print(file)

# # open the pdf file
object = PyPDF2.PdfFileReader(file, strict=False)

# # get number of pages
NumPages = object.getNumPages()


# extract text and do the search
for i in range(0, NumPages):
    PageObj = object.getPage(i)
    try:
        Text = PageObj.extractText()
        ResSearch = re.search(query, Text)
        if ResSearch is not None:
            print(i + 1)
    except:
        print('error')

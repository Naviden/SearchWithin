# import packages
import PyPDF2
import re
import glob

path = '/Users/Navid/Documents/books'
extention = 'pdf'

for file in glob.glob(path + '/*.' + extention):
    print(file)



# # open the pdf file
# object = PyPDF2.PdfFileReader("ISLR.pdf")

# # get number of pages
# NumPages = object.getNumPages()

# # define keyterms
# String = "package"

# # extract text and do the search
# for i in range(0, NumPages):
#     PageObj = object.getPage(i)
#     Text = PageObj.extractText()
#     ResSearch = re.search(String, Text)
#     if ResSearch is not None:
#         print(i + 1)

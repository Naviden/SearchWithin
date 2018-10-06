# import packages

from PyPDF2 import PdfFileReader
import re

path = '/Users/Navid/Documents/books'
book_name = 'All-of-Nonparametric-Statistics'


pdf = PdfFileReader(path + f'/{book_name}.pdf')
# print(pdf)
number_of_pages = pdf.getNumPages()


def prepare(word):
    first_lower = word[0].lower()
    first_upper = first_lower.upper()
    rest = word[1:]
    query = f'\w*({first_lower}|{first_upper}){rest}\w*'
    return query


# define keyterms
String = prepare('install')

# extract text and do the search

i = 0
while i < number_of_pages:
    PageObj = pdf.getPage(i)
    try:
        Text = PageObj.extractText()
        ResSearch = re.search(String, Text)
        if ResSearch is not None:
            print('p: ', i + 1, 'Found!')
        else:
            print('p: ', i + 1, '---')
    except:
        print('p: ', i + 1, '---')

    i += 1

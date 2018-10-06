import glob
from PyPDF2 import PdfFileReader
import re
import time
import argparse

path = '/Users/Navid/Documents/books'
# to_search = 'install'
extention = 'pdf'

ap = argparse.ArgumentParser()
ap.add_argument("-B", "--book", required=True)
args = vars(ap.parse_args())
to_search = args['book']


def prepare(word):
    first_lower = word[0].lower()
    first_upper = first_lower.upper()
    rest = word[1:]
    query = f'\w*({first_lower}|{first_upper}){rest}\w*'
    return query


print(f'Indexing for "{to_search}" ... ')
time.sleep(1)
print(f'{len(glob.glob(path + "/*." + extention))} books has been found')
print('-' * 40)


for file in glob.glob(path + '/*.' + extention):
    title = file.split('/')[-1].split('.')[0].replace('-', ' ')
    print(f'Current book : {title}')

    pdf = PdfFileReader(file, strict=False)
    number_of_pages = pdf.getNumPages()

    # define keyterms
    String = prepare(to_search)

    # extract text and do the search
    p = 0
    err = 0
    found = 0
    while p < number_of_pages:
        PageObj = pdf.getPage(p)
        try:
            Text = PageObj.extractText()
            ResSearch = re.search(String, Text)
            if ResSearch is not None:
                found += 1
        except:
            err += 1

        p += 1
    err_rate = int((err / number_of_pages) * 100)

    print(f'Pages : {number_of_pages}')
    print(f'Found : {found}')
    print(f'Error % : {err_rate}')
    print('-' * 20)

if __name__ == '__main__':
    main()

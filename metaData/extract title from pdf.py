# get_doc_info.py

from PyPDF2 import PdfFileReader


def get_info(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        info = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()

    print(pdf)

    author = info.author
    creator = info.creator
    producer = info.producer
    subject = info.subject
    title = info.title



if __name__ == '__main__':
    path = "E:\\computers\\level 4\\semester 1\\selected 3\\project\\PDFs\\TVEQ_39_1580827.pdf"
    get_info(path)
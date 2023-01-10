import PyPDF2


def readpdf(pdfpath):
    t = " "
    path = open(pdfpath, 'rb')
    pdfReader = PyPDF2.PdfFileReader(path)
    totalpages = pdfReader.numPages
    for i in range(totalpages):
        from_page = pdfReader.getPage(i)
        text = from_page.extractText()
        t = t + text
    txt = t
    return txt

filepath = "E:\\computers\\level 4\\semester 1\\selected 3\\project\\PDFs\\TVEQ_39_1580827.pdf"
pdf1 = readpdf(filepath)
print(pdf1)

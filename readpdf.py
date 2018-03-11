import PyPDF2
pdf_file = open('tmp175n.pdf','rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)



page = read_pdf.getPage(2)
# print(dir(page))
print(page.getContents())


page_content = page.extractText()
print(page_content)
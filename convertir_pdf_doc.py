from pdf2docx import Converter
pdf_file = 'leer.pdf'
docx_file = 'leer.docx'
cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()


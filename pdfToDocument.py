from pdf2docx import Converter

my_pdf = 'demo.pdf'
word_file = 'demo.docx'

#Converting the pdf file to word using Converter
cv = Converter(my_pdf)
cv.convert(word_file, start=0, end=none)
cv.Close()


#Converting the pdf file to word using parse method
parse(my_pdf, word_file, start=0, end=none)
import PyPDF2
import sys


# PDF Watermark
# template = PyPDF2.PdfFileReader(open('combined.pdf', 'rb'))
# watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
# output = PyPDF2.PdfFileWriter()


# for i in range(template.getNumPages()):
# 	page = template.getPage(i)
# 	page.mergePage(watermark.getPage(0))
# 	output.addPage(page)

# with open('watermaked_output.pdf', 'wb') as file:
# 	output.write(file)






# Combine two pdf pages into one pdf
inputs = sys.argv[1:]

def pdf_combine(li):
	merger = PyPDF2.PdfMerger()

	for pdf in li:
		print(pdf)
		merger.append(pdf)
	merger.write('6Months_Statments.pdf')

pdf_combine(inputs)




# PDF Merger
# pdf_1 = sys.argv[1]
# with open(f'{pdf_1}', 'rb') as page:
# 	reader = PyPDF2.PdfFileReader(page)
# 	page = reader.getPage(0)
# 	writer = PyPDF2.PdfFileWriter()
# 	writer.addPage(page)
# 	with open('tilt.pdf', 'wb') as new_file:
# 		writer.write(new_file)


# PDF's With Python
# 'rb' stands for read binary
# with open('dummy.pdf', 'rb') as file:
# 	reader = PyPDF2.PdfFileReader(file)
# 	page = reader.getPage(0)
# 	page.rotateCounterClockwise(90)
# 	writer = PyPDF2.PdfFileWriter()
# 	writer.addPage(page)
# 	with open('tilt.pdf', 'wb') as new_file:
# 		writer.write(new_file)
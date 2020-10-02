import PyPDF2
import os


inputs = os.listdir(r'C:\Users\mayas\PycharmProjects\scripting_with_python\pdf_files')
inputs = inputs[0:3]
print(inputs)

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('super.pdf')

pdf_combiner(inputs)


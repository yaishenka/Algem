from PyPDF2 import PdfFileReader, PdfFileWriter
from PIL import Image
import os
from io import BytesIO
import img2pdf

main_dir = '/Users/daniilgagarinov/Algem/'
sources_dir = '/Users/daniilgagarinov/Algem/sources'
list = os.listdir(sources_dir)

for file in list:
    if '.' in file:
        list.remove(file)

for task_number in list:
    sources = os.listdir(sources_dir + '/' + task_number)
    sources.sort()
    new_task_file = PdfFileWriter()
    for source_file_name in sources:
        buf = BytesIO()
        img = Image.open(sources_dir + '/' + task_number + '/' + source_file_name)
        img.convert("RGB").save(buf, format="pdf")
        # once image is PDF, it can be appended
        new_task_file.addPage(PdfFileReader(buf).getPage(0))
    folder = 'analit/'
    if (int(task_number) > 17):
        task_number = (int(task_number) - 17).__str__()
        folder = 'linal/'
    outputStream = open(main_dir + folder + task_number  + ' билет'+ '.pdf', "wb")
    new_task_file.write(outputStream)
    outputStream.close()







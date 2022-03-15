import os
from PyPDF2 import PdfFileWriter, PdfFileReader

def split_pdf(input_file_path):

    pdf = PdfFileReader(open(input_file_path, 'rb'), strict=False)
     
    if pdf.isEncrypted:
        pdf.decrypt('')

    for page in range(pdf.getNumPages()):
        out = PdfFileWriter()
        out.addPage(pdf.getPage(page))
        output_file_name = f"temp\Page_{page+1}.pdf"
        
        with open(output_file_name, 'wb') as file:
            out.write(file)    

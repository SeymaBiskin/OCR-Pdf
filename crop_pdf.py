from PyPDF2 import PdfFileWriter, PdfFileReader

def crop_pdf(input_file_path, output_file_path, top=125, bottom=220, right=0, left=0):

    pdf = PdfFileReader(open(input_file_path, 'rb'), strict=False)
    out = PdfFileWriter()
    
    if pdf.isEncrypted:
        pdf.decrypt('')


    for page in pdf.pages:
        page.mediaBox.upperRight = (page.mediaBox.getUpperRight_x() - right, page.mediaBox.getUpperRight_y() - top)
        page.mediaBox.lowerLeft  = (page.mediaBox.getLowerLeft_x()  + left,  page.mediaBox.getLowerLeft_y()  + bottom)
        out.addPage(page)    

    ous = open(output_file_path, 'wb')
    out.write(ous)
    ous.close()
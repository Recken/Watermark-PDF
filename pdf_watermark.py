import PyPDF2

def pdf_watermark(original_pdf, stamp_pdf):
    reader = PyPDF2.PdfReader(original_pdf)
    writer = PyPDF2.PdfWriter()

    for index in range(len(reader.pages)):
        page = reader.pages[index]      # we get each page of the original file
        reader_stamp = PyPDF2.PdfReader(stamp_pdf)
        page.merge_page(reader_stamp.pages[0])  # merges each page with the stamp
        # merge_page needs as a parameter a PageObject, that's why we create reader_stamp!
        writer.add_page(page)       # add the merged page into the writer variable

    with open("final.pdf", "wb") as file:
        writer.write(file)      # write the information into the pdf file

pdf_watermark("super.pdf", "wtr.pdf")
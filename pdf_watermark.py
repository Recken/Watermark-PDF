# We want to watermark each page of a pdf
# F.ex. it's used in movies when you give the script to each actor and is watermark with his name

import PyPDF2

def pdf_watermark(original_pdf, stamp_pdf):
    reader = PyPDF2.PdfReader(original_pdf)
    writer = PyPDF2.PdfWriter()
    #writer.add_page(stamp_pdf)

    for index in range(len(reader.pages)):
        print(index)
        page = reader.pages[index]      # we get each page of the original file
        reader_stamp = PyPDF2.PdfReader(stamp_pdf)
        page.merge_page(reader_stamp.pages[0])  # merges each page with the stamp
        # merge_page needs as a parameter a PageObject, that's why we create reader_stamp!
        writer.add_page(page)       # add the merged page into the writer variable

    with open("final.pdf", "wb") as new_file:
        writer.write(new_file)      # write the information into the pdf file

pdf_watermark("super.pdf", "wtr.pdf")
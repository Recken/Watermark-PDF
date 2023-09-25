# Instead of defining a function, we introduce the name of both pdfs at the start
import sys
import PyPDF2

original_pdf = sys.argv[1]
stamp_pdf = sys.argv[2]

template = PyPDF2.PdfReader(open(original_pdf, "rb"))
watermark = PyPDF2.PdfReader(open(stamp_pdf, "rb"))
output = PyPDF2.PdfWriter()

for index in range(len(template.pages)):
    page = template.pages[index]
    page.merge_page(watermark.pages[0])
    output.add_page(page)

    with open("final.pdf", "wb") as file:
        output.write(file)
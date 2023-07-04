import os
import img2pdf
from fpdf import FPDF

with open("output.pdf", "wb") as file:
    file.write(img2pdf.convert([i for i in os.listdir('path to image') if i.endswith(".jpg")]))

Pdf = FPDF()

list_of_images = ["wall.jpg", "nature.jpg","cat.jpg"]
for i in list_of_images:
    Pdf.add_page()
    Pdf.image(i,x,y,w,h)
    Pdf.output("result.pdf", "F")
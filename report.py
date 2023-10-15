import webbrowser
import os
from fpdf import FPDF
from filestack import Client



class PdfReport:
   # """"""  Creating the PDF file that contains
   #    data about the flatemates name  paying
   #    amount and dperiod """"""


    def __init__(self,filename):
        self.filename=filename

    def genertae(self,Flatemate1,Flatemate2,bill):
        Flatemate1_Pay = str(round(Flatemate1.pays(bill, Flatemate2), 2))
        Flatemate2_Pay = str(round(Flatemate2.pays(bill, Flatemate2), 2))

        pdf = FPDF(orientation='p', unit='pt', format='A4')
        pdf.add_page()

        # Add Icon
        pdf.image("files/006 house.png" ,w=30, h=30)

         # Inset title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatemates Bill', border=0, align="C", ln=1)

        # Insert period lable and value
        pdf.set_font(family="Times",size=14 ,style='B')
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        #insert name and due amount first flatemate
        pdf.set_font(family="Times",size=12)
        pdf.cell(w=100, h=25, txt=Flatemate1.name,border=0)
        pdf.cell(w=150, h=25, txt=Flatemate1_Pay, border=0, ln=1)

        #insert name and due  amoount of  second flatemate
        pdf.cell(w=100, h=25, txt=Flatemate2.name, border=0)
        pdf.cell(w=150, txt=Flatemate2_Pay, h=25, border=0, ln=1)

        #change directory to files, generate and open the pdf
        os.chdir("files")
        pdf.output(self.filename)
        webbrowser.open(self.filename)

class Fileshare:
    def __init__(self,filepath,api_key="AxHBbPOpS0ak7l29VPSLQz"):
        self.filepath=filepath
        self.api_key=api_key
    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        print(new_filelink.url)
        return new_filelink.url


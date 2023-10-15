from Flate import Bill, Flatemates
from report import PdfReport
from report import Fileshare


amount=float(input("Hey user, enter the bill price: "))
period=(input("What is the bill period? E.g.December 2022"))
9i
name1=input("What is your name?")
days_in_house1=int(input(f"How many days did {name1} stay in the house during the bill period?"))

name2=input("What is your name?")
days_in_house2=int(input(f"How many days did {name2} stay in the house during the bill period?"))


the_bill= Bill(amount,period)
flatemate1= Flatemates(name1, days_in_house1)
flatemate2= Flatemates(name2, days_in_house2)

print(f"{flatemate1.name}: ",flatemate1.pays(the_bill,flatemate2))
print(f"{flatemate2.name} ", flatemate2.pays(the_bill,flatemate2))

pdf_report= PdfReport(filename=f"{the_bill.period}.pdf")
pdf_report.genertae(flatemate1,flatemate2,bill=the_bill)

file_share=Fileshare(filepath=pdf_report.filename)
print(file_share.share())


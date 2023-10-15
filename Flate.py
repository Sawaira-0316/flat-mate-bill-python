class Bill:

    def __init__(self, amount, period):

        self.amount = amount
        self.period = period


class Flatemates:
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house=days_in_house


    def pays (self,bill,Flatemate2):
        weight=self.days_in_house /( self.days_in_house + Flatemate2.days_in_house)
        to_pay=bill.amount * weight
        return to_pay

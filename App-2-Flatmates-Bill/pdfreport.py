import os
import webbrowser

from bill import Bill
from flatmate import Flatmate
from fpdf import FPDF


class PdfReport:

    def __init__(self, filename_value: str):
        self.filename = filename_value

    # def generate(self, flatmate1: Flatmate, flatmate2: Flatmate, bill_to_pay: Bill) -> None:
    def generate(self, flatmates: dict[str, Flatmate], bill_to_pay: Bill) -> None:
        """
        Creates report showing what each flatmate owes
        flatmates: dict key is flatmate name, value is Flatmate object
        """

        MONEY_FORMAT_STR = "${:.2f}"

        pdf = FPDF(orientation='P', unit='pt', format='Letter')  # 'P' is portrait mode
        # default unit is 'mm', 'pt is [font] points

        pdf.add_page()

        # Add image
        pdf.image("files/house.png", w=30, h=30)  # re-size image to 30x30 pixels

        # add title
        pdf.set_font(family='Times', size=24, style='B')  # 'B' is bold
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C",
                 ln=1)  # w is width in units defined earlier, h is height
        # w=0 means cell occupies entire line
        # "C" means center the text in the cell
        # instructor says "ln=1" ends the current line, so *next* cell will go on new line

        pdf.set_font(family='Times', size=14, style='B')  # 'B' is bold
        pdf.cell(w=170, h=40, txt="Period",
                 border=0)  # default position (ln not specified) is to the right of previous cell
        # default alignment (align not specified) is left-justify text in cell

        pdf.cell(w=170, h=40, txt=bill_to_pay.bill_period_str, border=0, ln=1)

        # What each flatmate pays
        pdf.set_font(family='Times', size=12)
        for name in bill_to_pay.shares:
            pdf.cell(w=170, h=25, txt=name + " pays ", border=0)
            flatmate_share_str = MONEY_FORMAT_STR.format(bill_to_pay.shares[name])
            pdf.cell(w=170, h=25, txt=flatmate_share_str, border=0)
            pdf.cell(w=170, h=25, txt=str(flatmates[name].nbr_days_in_flat) + " days in flat", border=0, ln=1)

        pdf.cell(w=170, h=40, txt="Total bill", border=0)
        pdf.cell(w=170, h=40, txt=MONEY_FORMAT_STR.format(bill_to_pay.amount), border=0, ln=1)

        # Generate PDF file
        pdf.output(self.filename)  # default is same path as source file

        # Display PDF in web browser, if possible
        # Does not work in replit.com 
        webbrowser.open('file://' + os.path.realpath(self.filename))


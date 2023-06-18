from bill import Bill
from filesharer import FileSharer
from flatmate import Flatmate
from pdfreport import PdfReport

FILESTACK_API_KEY = 'your-filestack-api-key-here'   # Need free FileStack account
REPORT_PATH = "output/bill.pdf"
billdata = Bill.input_bill()

flatmates_dict = dict()
userdata = Flatmate.input_flatmate("What is your name? ")
if userdata.nbr_days_in_flat > billdata.bill_period_days:
    userdata.nbr_days_in_flat = billdata.bill_period_days
flatmates_dict[userdata.name] = userdata

flatmatedata = Flatmate.input_flatmate("What is the name of the other flatmate? ")
if flatmatedata.nbr_days_in_flat > billdata.bill_period_days:
    flatmatedata.nbr_days_in_flat = billdata.bill_period_days
flatmates_dict[flatmatedata.name] = flatmatedata

# Calculate how much each flatmate owes
billdata.calc_shares(flatmates_dict)

# Create pretty PDF report
pdf_reporter = PdfReport(REPORT_PATH)
pdf_reporter.generate(flatmates=flatmates_dict, bill_to_pay=billdata)
print("PDF report has been saved as " + REPORT_PATH)

# Upload PDF report to the cloud - requires free FileStack account
if FILESTACK_API_KEY != 'your-filestack-api-key-here':
    api_key = FILESTACK_API_KEY
else:
    api_key = input("Filestack API key (optional): ")
try:
    file_sharer = FileSharer(api_key)
    url = file_sharer.share(REPORT_PATH)
    print("URL of flatmates bill=", url)
except:
    print("No valid API key. Skipped upload of PDF report to cloud.")

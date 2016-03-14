from . .Request import Request
from . .Utilities import RemoveFromJson
from . .Model.Application import Application
from . .Model.Credentials import Credentials
from . .Model.CustomBilling import CustomBilling
from . .Model.Reports import Reports
from . .Model.Transaction import Transaction

class Credit (Request):

    Application = None
    Credentials = None
    CustomBilling = None
    Reports = None
    Transaction = None

    def __init__(self):
        super(Credit, self).__init__("payment", "check", "credit", "POST")
        

    
    
    
    
    
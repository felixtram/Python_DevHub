from . .Request import Request
from . .Utilities import RemoveFromJson
from . .Model.Application import Application
from . .Model.Credentials import Credentials
from . .Model.PayPal import PayPal
from . .Model.Reports import Reports
from . .Model.Transaction import Transaction

class Reversal (Request):

    Application = None
    Credentials = None
    PayPal = None
    Reports = None
    Transaction = None

    def __init__(self):
        super(Reversal, self).__init__("payment", "credit", "reversal", "POST")
        

    
    
    
    
    
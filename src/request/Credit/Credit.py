from . .Request import Request
from . .Utilities import RemoveFromJson
from . .Model.Application import Application
from . .Model.Credentials import Credentials
from . .Model.CustomBilling import CustomBilling
from . .Model.EnhancedData import EnhancedData
from . .Model.PayPal import PayPal
from . .Model.Reports import Reports
from . .Model.Terminal import Terminal
from . .Model.Transaction import Transaction

class Credit (Request):

    Application = None
    Credentials = None
    CustomBilling = None
    EnhancedData = None
    PayPal = None
    Reports = None
    Terminal = None
    Transaction = None

    def __init__(self):
        super(Credit, self).__init__("payment", "credit", "credit", "POST")
        

    
    
    
    
    
    
    
    
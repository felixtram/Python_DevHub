from . .Request import Request
from . .Utilities import RemoveFromJson
from . .Model.Address import Address
from . .Model.Application import Application
from . .Model.Bml import Bml
from . .Model.Card import Card
from . .Model.Credentials import Credentials
from . .Model.CustomBilling import CustomBilling
from . .Model.EnhancedData import EnhancedData
from . .Model.PayPal import PayPal
from . .Model.PaymentAccount import PaymentAccount
from . .Model.Reports import Reports
from . .Model.Terminal import Terminal
from . .Model.Transaction import Transaction

class Return (Request):

    Address = None
    Application = None
    Bml = None
    Card = None
    Credentials = None
    CustomBilling = None
    EnhancedData = None
    PayPal = None
    PaymentAccount = None
    Reports = None
    Terminal = None
    Transaction = None

    def __init__(self):
        super(Return, self).__init__("payment", "credit", "return", "POST")
        

    
    
    
    
    
    
    
    
    
    
    
    
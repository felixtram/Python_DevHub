from . .Request import Request
from . .Utilities import RemoveFromJson
from . .Model.Address import Address
from . .Model.Application import Application
from . .Model.Bml import Bml
from . .Model.Card import Card
from . .Model.Credentials import Credentials
from . .Model.CustomBilling import CustomBilling
from . .Model.EnhancedData import EnhancedData
from . .Model.FraudResult import FraudResult
from . .Model.PaymentAccount import PaymentAccount
from . .Model.Reports import Reports
from . .Model.Terminal import Terminal
from . .Model.Transaction import Transaction
from . .Model.Visa import Visa

class CaptureGivenAuth (Request):

    Address = None
    Application = None
    Bml = None
    Card = None
    Credentials = None
    CustomBilling = None
    EnhancedData = None
    FraudResult = None
    PaymentAccount = None
    Reports = None
    Terminal = None
    Transaction = None
    Visa = None

    def __init__(self):
        super(CaptureGivenAuth, self).__init__("payment", "credit", "captureGivenAuth", "POST")
        

    
    
    
    
    
    
    
    
    
    
    
    
    
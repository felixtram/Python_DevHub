from . .Request import Request
from . .Utilities import RemoveFromJson
from . .Model.Application import Application
from . .Model.Credentials import Credentials
from . .Model.EnhancedData import EnhancedData
from . .Model.PayPal import PayPal
from . .Model.Reports import Reports
from . .Model.Transaction import Transaction

class AuthorizationCompletion (Request):

    Application = None
    Credentials = None
    EnhancedData = None
    PayPal = None
    Reports = None
    Transaction = None

    def __init__(self):
        super(AuthorizationCompletion, self).__init__("payment", "credit", "authorizationCompletion", "POST")
        

    
    
    
    
    
    
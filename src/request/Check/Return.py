from . .Request import Request
from . .Utilities import RemoveFromJson
from . .Model.Address import Address
from . .Model.Application import Application
from . .Model.Credentials import Credentials
from . .Model.CustomBilling import CustomBilling
from . .Model.DemandDepositAccount import DemandDepositAccount
from . .Model.PaymentAccount import PaymentAccount
from . .Model.Reports import Reports
from . .Model.Transaction import Transaction

class Return (Request):

    Address = None
    Application = None
    Credentials = None
    CustomBilling = None
    DemandDepositAccount = None
    PaymentAccount = None
    Reports = None
    Transaction = None

    def __init__(self):
        super(Return, self).__init__("payment", "check", "return", "POST")
        

    
    
    
    
    
    
    
    
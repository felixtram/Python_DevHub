from . .Request import Request
from . .Utilities import RemoveFromJson
from . .Model.Applepay import Applepay
from . .Model.Application import Application
from . .Model.Card import Card
from . .Model.Credentials import Credentials
from . .Model.DemandDepositAccount import DemandDepositAccount
from . .Model.Reports import Reports
from . .Model.Transaction import Transaction

class PaymentAccountCreate (Request):

    Applepay = None
    Application = None
    Card = None
    Credentials = None
    DemandDepositAccount = None
    Reports = None
    Transaction = None

    def __init__(self):
        super(PaymentAccountCreate, self).__init__("payment", "services", "paymentAccountCreate", "POST")
        

    
    
    
    
    
    
    
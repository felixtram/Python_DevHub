from . .Request import Request
from . .Utilities import RemoveFromJson
from . .Model.Application import Application
from . .Model.Card import Card
from . .Model.Credentials import Credentials
from . .Model.PaymentAccount import PaymentAccount
from . .Model.Reports import Reports
from . .Model.Transaction import Transaction

class PaymentAccountUpdate (Request):

    Application = None
    Card = None
    Credentials = None
    PaymentAccount = None
    Reports = None
    Transaction = None

    def __init__(self):
        super(PaymentAccountUpdate, self).__init__("payment", "services", "paymentAccountUpdate", "POST")
        

    
    
    
    
    
    
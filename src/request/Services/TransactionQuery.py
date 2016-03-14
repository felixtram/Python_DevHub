from . .Request import Request
from . .Utilities import RemoveFromJson
from . .Model.Application import Application
from . .Model.Card import Card
from . .Model.Credentials import Credentials
from . .Model.Reports import Reports
from . .Model.Transaction import Transaction

class TransactionQuery (Request):

    Application = None
    Card = None
    Credentials = None
    Reports = None
    Transaction = None

    def __init__(self):
        super(TransactionQuery, self).__init__("payment", "services", "transactionQuery", "POST")
        

    
    
    
    
    
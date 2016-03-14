from . .Request import Request
from . .Utilities import RemoveFromJson
from . .Model.Address import Address
from . .Model.Application import Application
from . .Model.Card import Card
from . .Model.Credentials import Credentials
from . .Model.PaymentAccount import PaymentAccount
from . .Model.Reports import Reports
from . .Model.ScheduledTask import ScheduledTask
from . .Model.Transaction import Transaction

class ScheduledTaskUpdate (Request):

    Address = None
    Application = None
    Card = None
    Credentials = None
    PaymentAccount = None
    Reports = None
    ScheduledTask = None
    Transaction = None

    def __init__(self):
        super(ScheduledTaskUpdate, self).__init__("payment", "services", "scheduledTaskUpdate", "POST")
        

    
    
    
    
    
    
    
    
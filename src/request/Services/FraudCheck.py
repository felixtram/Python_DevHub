from . .Request import Request
from . .Utilities import RemoveFromJson
from . .Model.Address import Address
from . .Model.AdvancedFraudChecks import AdvancedFraudChecks
from . .Model.Application import Application
from . .Model.Credentials import Credentials
from . .Model.Reports import Reports
from . .Model.ScheduledTask import ScheduledTask
from . .Model.Transaction import Transaction

class FraudCheck (Request):

    Address = None
    AdvancedFraudChecks = None
    Application = None
    Credentials = None
    Reports = None
    ScheduledTask = None
    Transaction = None

    def __init__(self):
        super(FraudCheck, self).__init__("payment", "services", "fraudCheck", "POST")
        

    
    
    
    
    
    
    
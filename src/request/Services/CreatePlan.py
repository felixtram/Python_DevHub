from . .Request import Request
from . .Utilities import RemoveFromJson
from . .Model.Application import Application
from . .Model.Credentials import Credentials
from . .Model.Reports import Reports
from . .Model.ScheduledTask import ScheduledTask
from . .Model.Transaction import Transaction

class CreatePlan (Request):

    Application = None
    Credentials = None
    Reports = None
    ScheduledTask = None
    Transaction = None

    def __init__(self):
        super(CreatePlan, self).__init__("payment", "services", "createPlan", "POST")
        

    
    
    
    
    
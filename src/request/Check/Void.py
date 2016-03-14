from . .Request import Request
from . .Utilities import RemoveFromJson
from . .Model.Application import Application
from . .Model.Credentials import Credentials
from . .Model.Reports import Reports
from . .Model.Transaction import Transaction

class Void (Request):

    Application = None
    Credentials = None
    Reports = None
    Transaction = None

    def __init__(self):
        super(Void, self).__init__("payment", "check", "void", "POST")
        

    
    
    
    
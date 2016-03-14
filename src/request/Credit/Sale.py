from . .Request import Request
from . .Utilities import RemoveFromJson
from . .Model.Address import Address
from . .Model.AdvancedFraudChecks import AdvancedFraudChecks
from . .Model.Applepay import Applepay
from . .Model.Application import Application
from . .Model.Bml import Bml
from . .Model.Card import Card
from . .Model.CardholderAuthentication import CardholderAuthentication
from . .Model.Credentials import Credentials
from . .Model.CustomBilling import CustomBilling
from . .Model.EnhancedData import EnhancedData
from . .Model.FraudCheck import FraudCheck
from . .Model.Identification import Identification
from . .Model.PayPal import PayPal
from . .Model.PaymentAccount import PaymentAccount
from . .Model.RecyclingRequest import RecyclingRequest
from . .Model.Reports import Reports
from . .Model.ScheduledTask import ScheduledTask
from . .Model.Terminal import Terminal
from . .Model.Transaction import Transaction
from . .Model.Visa import Visa
from . .Model.Wallet import Wallet

class Sale (Request):

    Address = None
    AdvancedFraudChecks = None
    Applepay = None
    Application = None
    Bml = None
    Card = None
    CardholderAuthentication = None
    Credentials = None
    CustomBilling = None
    EnhancedData = None
    FraudCheck = None
    Identification = None
    PayPal = None
    PaymentAccount = None
    RecyclingRequest = None
    Reports = None
    ScheduledTask = None
    Terminal = None
    Transaction = None
    Visa = None
    Wallet = None

    def __init__(self):
        super(Sale, self).__init__("payment", "credit", "sale", "POST")
        

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
from . .Request import Request
from . .Utilities import RemoveFromJson
from . .Model.Address import Address
from . .Model.Credentials import Credentials
from . .Model.ECheck import ECheck
from . .Model.Merchant import Merchant
from . .Model.PrimaryContact import PrimaryContact
from . .Model.SubMerchantFunding import SubMerchantFunding

class CreateSubMerchant (Request):

    Address = None
    Credentials = None
    ECheck = None
    Merchant = None
    PrimaryContact = None
    SubMerchantFunding = None

    def __init__(self):
        super(CreateSubMerchant, self).__init__("boarding", "services", "createSubMerchant", "POST")
        

    
    
    
    
    
    
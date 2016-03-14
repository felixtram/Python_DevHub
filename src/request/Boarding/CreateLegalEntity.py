from . .Request import Request
from . .Utilities import RemoveFromJson
from . .Model.Address import Address
from . .Model.Credentials import Credentials
from . .Model.LegalEntity import LegalEntity
from . .Model.Principal import Principal

class CreateLegalEntity (Request):

    Address = None
    Credentials = None
    LegalEntity = None
    Principal = None
    PrincipalArray = None

    def __init__(self):
        super(CreateLegalEntity, self).__init__("boarding", "services", "createLegalEntity", "POST")
        

    
    
    
    
    
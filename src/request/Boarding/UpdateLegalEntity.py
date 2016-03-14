from . .Request import Request
from . .Utilities import RemoveFromJson
from . .Model.Address import Address
from . .Model.BackgroundCheckFields import BackgroundCheckFields
from . .Model.Credentials import Credentials
from . .Model.LegalEntity import LegalEntity
from . .Model.Principal import Principal

class UpdateLegalEntity (Request):

    Address = None
    BackgroundCheckFields = None
    Credentials = None
    LegalEntity = None
    Principal = None
    PrincipalArray = None

    def __init__(self):
        super(UpdateLegalEntity, self).__init__("boarding", "services", "updateLegalEntity", "POST")
        

    
    
    
    
    
    
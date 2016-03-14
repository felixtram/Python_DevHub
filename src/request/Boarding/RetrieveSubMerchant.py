from . .Request import Request
from . .Utilities import RemoveFromJson


class RetrieveSubMerchant (Request):

    

    def __init__(self):
        super(RetrieveSubMerchant, self).__init__("boarding", "services", "retrieveSubMerchant", "POST")
        

    
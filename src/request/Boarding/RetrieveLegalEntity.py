from . .Request import Request
from . .Utilities import RemoveFromJson


class RetrieveLegalEntity (Request):

    

    def __init__(self):
        super(RetrieveLegalEntity, self).__init__("boarding", "services", "retrieveLegalEntity", "POST")
        

    
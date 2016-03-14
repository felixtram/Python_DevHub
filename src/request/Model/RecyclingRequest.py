
import sys
from . .Utilities import Frozen

class RecyclingRequest(object):
    RecycleID = None
    RecycleBy = None

    

    class RecycleByEnum(object):
        def __init__(self, value):
            self.value=value
    RecycleByEnum.MERCHANT = RecycleByEnum("Merchant").value
    RecycleByEnum.LITLE = RecycleByEnum("Litle").value
    RecycleByEnum.NONE = RecycleByEnum("None").value
    
    __setattr__=Frozen(object.__setattr__)
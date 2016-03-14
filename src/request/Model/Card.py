
import sys
from . .Utilities import Frozen

class Card(object):
    CardNumber = None
    ExpirationMonth = None
    ExpirationYear = None
    CVV = None
    Track1Data = None
    Track2Data = None
    PaypageRegistrationID = None
    AccountNumber = None
    Type = None

    

    class TypeEnum(object):
        def __init__(self, value):
            self.value=value
    TypeEnum.MC = TypeEnum("MC").value
    TypeEnum.VI = TypeEnum("VI").value
    TypeEnum.AX = TypeEnum("AX").value
    TypeEnum.DC = TypeEnum("DC").value
    TypeEnum.DI = TypeEnum("DI").value
    TypeEnum.PP = TypeEnum("PP").value
    TypeEnum.JC = TypeEnum("JC").value
    TypeEnum.BL = TypeEnum("BL").value
    TypeEnum.EC = TypeEnum("EC").value
    TypeEnum.GC = TypeEnum("GC").value
    TypeEnum.NONE = TypeEnum("").value
    
    __setattr__=Frozen(object.__setattr__)
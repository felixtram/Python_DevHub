
import sys
from . .Utilities import Frozen

class DetailTax(object):
    TaxIncludedInTotal = None
    TaxAmount = None
    TaxRate = None
    AlternateTaxIdentifier = None
    TaxTypeIdentifier = None

    

    class TaxTypeIdentifierEnum(object):
        def __init__(self, value):
            self.value=value
    TaxTypeIdentifierEnum.UNKOWN = TaxTypeIdentifierEnum("00").value
    TaxTypeIdentifierEnum.NATL_SALES = TaxTypeIdentifierEnum("01").value
    TaxTypeIdentifierEnum.ST_SALES = TaxTypeIdentifierEnum("02").value
    TaxTypeIdentifierEnum.CTY_SALES = TaxTypeIdentifierEnum("03").value
    TaxTypeIdentifierEnum.LCL_SALES = TaxTypeIdentifierEnum("04").value
    TaxTypeIdentifierEnum.MUN_SALES = TaxTypeIdentifierEnum("05").value
    TaxTypeIdentifierEnum.OTHER = TaxTypeIdentifierEnum("06").value
    TaxTypeIdentifierEnum.VAT = TaxTypeIdentifierEnum("10").value
    TaxTypeIdentifierEnum.GST = TaxTypeIdentifierEnum("11").value
    TaxTypeIdentifierEnum.PST = TaxTypeIdentifierEnum("12").value
    TaxTypeIdentifierEnum.HST = TaxTypeIdentifierEnum("13").value
    TaxTypeIdentifierEnum.QST = TaxTypeIdentifierEnum("14").value
    TaxTypeIdentifierEnum.ROOM = TaxTypeIdentifierEnum("20").value
    TaxTypeIdentifierEnum.OCCUPANCY = TaxTypeIdentifierEnum("21").value
    TaxTypeIdentifierEnum.ENERGY = TaxTypeIdentifierEnum("22").value
    
    __setattr__=Frozen(object.__setattr__)
import DetailTax
import LineItem
import sys
from . .Utilities import Frozen

class EnhancedData(object):
    PurchaseOrder = None
    TaxAmount = None
    TaxExempt = None
    DiscountAmount = None
    FreightAmount = None
    DutyAmount = None
    ShipFromPostalCode = None
    DestinationPostalCode = None
    DestinationCountryCode = None
    InvoiceReferenceNumber = None
    OrderDate = None
    DetailTaxArray = None
    DetailTax = None
    LineItemArray = None
    LineItem = None
    DeliveryType = None

    

    class DeliveryTypeEnum(object):
        def __init__(self, value):
            self.value=value
    DeliveryTypeEnum.CNC = DeliveryTypeEnum("CNC").value
    DeliveryTypeEnum.DIG = DeliveryTypeEnum("DIG").value
    DeliveryTypeEnum.PHY = DeliveryTypeEnum("PHY").value
    DeliveryTypeEnum.SVC = DeliveryTypeEnum("SVC").value
    DeliveryTypeEnum.TBD = DeliveryTypeEnum("TBD").value
    
    __setattr__=Frozen(object.__setattr__)
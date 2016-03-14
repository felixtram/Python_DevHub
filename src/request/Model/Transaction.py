
import sys
from . .Utilities import Frozen

class Transaction(object):
    CustomerID = None
    PartialCapture = None
    ReferenceNumber = None
    AuthorizationDate = None
    ApprovalNumber = None
    TransactionAmount = None
    TransactionID = None
    ConvenienceFeeAmount = None
    PartialApprovedFlag = None
    FraudFilterOverride = None
    SurchargeFee = None
    ActionReason = None
    Verify = None
    TransactionType = None
    OrderSource = None
    TaxType = None

    
    

    class OrderSourceEnum(object):
        def __init__(self, value):
            self.value=value
    OrderSourceEnum.ECOMMERCE = OrderSourceEnum("ecommerce").value
    OrderSourceEnum.INSTALLMENT = OrderSourceEnum("installment").value
    OrderSourceEnum.MAIL_ORDER = OrderSourceEnum("mailorder").value
    OrderSourceEnum.RECURRING = OrderSourceEnum("recurring").value
    OrderSourceEnum.RETAIL = OrderSourceEnum("retail").value
    OrderSourceEnum.TELEPHONE = OrderSourceEnum("telephone").value
    OrderSourceEnum.AUTH_3DS = OrderSourceEnum("3dsAuthenticated").value
    OrderSourceEnum.ATTEMPTED_3DS = OrderSourceEnum("3dsAttempted").value
    OrderSourceEnum.RECURRING_TEL = OrderSourceEnum("recurringtel").value
    OrderSourceEnum.ECHECK_PPD = OrderSourceEnum("echeckppd").value
    OrderSourceEnum.APPLEPAY = OrderSourceEnum("applepay").value
    class TaxTypeEnum(object):
        def __init__(self, value):
            self.value=value
    TaxTypeEnum.PAYMENT = TaxTypeEnum("payment").value
    TaxTypeEnum.FEE = TaxTypeEnum("fee").value
    
    __setattr__=Frozen(object.__setattr__)
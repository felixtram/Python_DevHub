
import sys
from . .Utilities import Frozen

class Identification(object):
    Ssn = None
    BirthDate = None
    CustomerRegistrationDate = None
    IncomeAmount = None
    CustomerCheckingAccount = None
    CustomerSavingsAccount = None
    EmployerName = None
    CustomerWorkTelephone = None
    YearsAtResidence = None
    YearsAtEmployer = None
    CustomerType = None
    IncomeCurrency = None
    ResidenceStatus = None

    
    
    

    class CustomerTypeEnum(object):
        def __init__(self, value):
            self.value=value
    CustomerTypeEnum.NEW = CustomerTypeEnum("New").value
    CustomerTypeEnum.EXISTING = CustomerTypeEnum("Existing").value
    class IncomeCurrencyEnum(object):
        def __init__(self, value):
            self.value=value
    IncomeCurrencyEnum.AUD = IncomeCurrencyEnum("AUD").value
    IncomeCurrencyEnum.CAD = IncomeCurrencyEnum("CAD").value
    IncomeCurrencyEnum.CHF = IncomeCurrencyEnum("CHF").value
    IncomeCurrencyEnum.DKK = IncomeCurrencyEnum("DKK").value
    IncomeCurrencyEnum.EUR = IncomeCurrencyEnum("EUR").value
    IncomeCurrencyEnum.GBP = IncomeCurrencyEnum("GBP").value
    IncomeCurrencyEnum.HKD = IncomeCurrencyEnum("HKD").value
    IncomeCurrencyEnum.JPY = IncomeCurrencyEnum("JPY").value
    IncomeCurrencyEnum.NOK = IncomeCurrencyEnum("NOK").value
    IncomeCurrencyEnum.NZD = IncomeCurrencyEnum("NZD").value
    IncomeCurrencyEnum.SEK = IncomeCurrencyEnum("SEK").value
    IncomeCurrencyEnum.SGD = IncomeCurrencyEnum("SGD").value
    IncomeCurrencyEnum.USD = IncomeCurrencyEnum("USD").value
    class ResidenceStatusEnum(object):
        def __init__(self, value):
            self.value=value
    ResidenceStatusEnum.OWN = ResidenceStatusEnum("Own").value
    ResidenceStatusEnum.RENT = ResidenceStatusEnum("Rent").value
    ResidenceStatusEnum.OTHER = ResidenceStatusEnum("Other").value
    
    __setattr__=Frozen(object.__setattr__)
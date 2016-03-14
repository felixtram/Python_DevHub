
import sys
from . .Utilities import Frozen

class Terminal(object):
    TerminalID = None
    Capability = None
    EntryMode = None
    CardholderID = None
    CapabilityOfCatTerminal = None

    
    
    
    

    class CapabilityEnum(object):
        def __init__(self, value):
            self.value=value
    CapabilityEnum.NOT_USED = CapabilityEnum("notused").value
    CapabilityEnum.MAG_STRIPE = CapabilityEnum("magstripe").value
    CapabilityEnum.KEYED_ONLY = CapabilityEnum("keyedonly").value
    class EntryModeEnum(object):
        def __init__(self, value):
            self.value=value
    EntryModeEnum.NOT_USED = EntryModeEnum("notused").value
    EntryModeEnum.KEYED = EntryModeEnum("keyed").value
    EntryModeEnum.TRACK1 = EntryModeEnum("track1").value
    EntryModeEnum.TRACK2 = EntryModeEnum("track2").value
    EntryModeEnum.COMPLETE_READ = EntryModeEnum("completeread").value
    class CardholderIDEnum(object):
        def __init__(self, value):
            self.value=value
    CardholderIDEnum.SIGNATURE = CardholderIDEnum("signature").value
    CardholderIDEnum.PIN = CardholderIDEnum("pin").value
    CardholderIDEnum.NO_PIN = CardholderIDEnum("nopin").value
    CardholderIDEnum.DIRECT_MARKET = CardholderIDEnum("directmarket").value
    class CapabilityOfCatTerminalEnum(object):
        def __init__(self, value):
            self.value=value
    CapabilityOfCatTerminalEnum.SELF_SERVICE = CapabilityOfCatTerminalEnum("self service").value
    
    __setattr__=Frozen(object.__setattr__)
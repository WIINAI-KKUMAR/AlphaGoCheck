from enum import Enum, auto

# enum Create for Driver
class BrowserType(Enum):
        CHROME  = auto()
        FIREFOX = auto()
        IE      = auto()
class ResultType(Enum):
        PASS = auto()
        FAIL = auto()
class IdentifierType(Enum):
        id           =auto()
        name         =auto()
        class_name   =auto()
        css_selector =auto()
        xpath        =auto()
        link_text    =auto()
        

class SelectType(Enum):
        _index        =auto()
        _visible_text =auto()
        _by_value     =auto()
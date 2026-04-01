from .santa_cloth import SantaCloth
from .lamp import Lamp
from .sand_house import SandHouse
from .persimmon import Persimmon
from .tree import Tree
from .two_duck import TwoDuck

try:
    from .teaser2_flour import Teaser2Flour
except ImportError:
    pass
try:
    from .teaser2_dough import Teaser2Dough
except ImportError:
    pass
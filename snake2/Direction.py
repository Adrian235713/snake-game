# An enumeration is a set of symbolic names (members) bound to unique, constant values.
# Within an enumeration, the members can be compared by identity,
# and the enumeration itself can be iterated over.
 
 
from enum import Enum
 
class Direction(Enum):
    GORA = 0
    PRAWO = 1
    DOL = 2
    LEWO = 3
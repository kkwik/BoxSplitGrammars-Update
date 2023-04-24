import time # for timing
from math import sqrt, tan, sin, cos, pi, ceil, floor, acos, atan, asin, degrees, radians, log, atan2, acos, asin
from random import *
from numpy import *

import json

from amulet.api.selection import SelectionGroup, SelectionBox
from amulet.api.block import Block

from GrammarBox import BoundingBox  

from MCSplitGrammar import rule, split, reorient, void, fill, start_symbol, Dimension, Direction, Constraint, clearrules

inputs = (
    ("Random Greek Temple Generator", "label"),
    ("Creator: Markus Eger", "label")
    )
    

COLUMNSIZE = 1
COLUMNHEIGHT = 8

clearrules(__file__)

MARBLE = 155

@rule 
def columns():
    with split(Dimension.Z, 
              [1,1,1,1,1,1,1]):
        fill(), void(), fill()
        void()
        fill(), void(), fill()
   
@rule   
def chamber():
    with split(Dimension.Z, [1, -1, 1]):
        fill(), void(), fill()

@rule
def naos():
    with split(Dimension.X, [1, -1, 1]):
        columns(), chamber(), fill()

@rule
def floorplan():
    with split(Dimension.X, 
               [1, 1, -1, 1, 1]):
        columns(),void(),
        naos(),
        void(),columns()

def performOperation(
    world: "BaseLevel",
    dimension,
    selection_group: SelectionGroup,
    options: dict
):
    # Only operate on one selection box at a time. If there are multiple selection boxes in the selection group don't do anything
    if len(selection_group.selection_boxes) == 1:
        selection_box: SelectionBox = selection_group.selection_boxes[0]
        bounding_box: BoundingBox = BoundingBox(selection_box.min, selection_box.shape) # Convert amulet Selection box into GrammarBox BoundingBox
        sc = start_symbol(bounding_box, world)
        floorplan()

export = {
    "name": "Make Floorplan",  # the name of the plugin
    "operation": performOperation,  # the actual function to call when running the plugin
}
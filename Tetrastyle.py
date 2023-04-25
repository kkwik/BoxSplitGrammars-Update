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

MARBLE = 6

@rule 
def level5roof():
    with split(Dimension.Z, [-1, 1, -1]):
        void(),fill(MARBLE)  

@rule 
def temple_roof4():
    with split(Dimension.Y, [1, -1]):
        fill(MARBLE),level5roof()

@rule 
def level4roof():
    with split(Dimension.Z, [1, -1, 1]):
        void(),temple_roof4()  

@rule 
def temple_roof3():
    with split(Dimension.Y, [1, -1]):
        fill(MARBLE),level4roof()

        
@rule 
def level3roof():
    with split(Dimension.Z, [1, -1, 1]):
        void(),temple_roof3()  

@rule 
def temple_roof2():
    with split(Dimension.Y, [1, -1]):
        fill(MARBLE),level3roof()

@rule 
def level2roof():
    with split(Dimension.Z, [1, -1, 1]):
        void(),temple_roof2() 

@rule 
def temple_roof():
    with split(Dimension.Y, [1, -1]):
        fill(MARBLE),level2roof()
        
@rule 
def columns():
    with split(Dimension.Z, [1,COLUMNSIZE,1,COLUMNSIZE,1,COLUMNSIZE,1,COLUMNSIZE,1]):
        void(), fill(MARBLE), void(), fill(MARBLE), void(), fill(MARBLE), void(), fill(MARBLE), void()
   
@rule   
def side_walls():
    with split(Dimension.Z, [1, 1, -1, 1, 1]):
        void(), fill(MARBLE), void(), fill(MARBLE), void()
        
@rule
def back_wall():
    with split(Dimension.Z, [1, -1, 1]):
        void(), fill(MARBLE), void()
        
@rule
def temple_chamber():
    with split(Dimension.X, [1, -1, 1]):
        columns(),side_walls(),back_wall()
        

@rule
def temple_walls():
    with split(Dimension.X, [1, COLUMNSIZE, 1, -1, 1, COLUMNSIZE, 1]):
        void(),columns(),void(),temple_chamber(),void(),columns(),void()

@rule
def temple():
    with split(Dimension.Y, [1, COLUMNHEIGHT, 5]):
        fill(MARBLE),temple_walls(),temple_roof()

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
        temple()

export = {
    "name": "Make Tetrastyle",  # the name of the plugin
    "operation": performOperation,  # the actual function to call when running the plugin
}
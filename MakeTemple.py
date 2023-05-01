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



"""    
@rule 
def columns():
    #fill()
    children = split(Dimension.Z, [1, COLUMNSIZE], repeat=True)
    while children:
        void()
        fill()

    
@rule
def temple_center():
    with split(Dimension.Z, [1, COLUMNSIZE, -1, COLUMNSIZE, 1], x=Dimension.Z, z=Dimension.X):
        void()
        fill() #columns()
        void()
        fill() #columns()
        void()
        
@rule
def temple_center():
    with split(Dimension.Z, [1, COLUMNSIZE, -1, COLUMNSIZE, 1], x=Dimension.Z, z=Dimension.X):
        void()
        columns()
        void()
        columns()
        void()

@rule
def maybe_columns():
    columns()
    
@rule 
def maybe_columns():
    void()


@rule
def temple_layout():
    with split(Dimension.X, [1, COLUMNSIZE, -1, COLUMNSIZE, 1]):
        void()
        columns()
        temple_center()
        maybe_columns()
        void()
    
@rule
def temple():
    with reorient(x=Dimension.LARGEST, y=Dimension.Y):
        temple_layout()
        
"""

@rule 
def level5roof():
    with split(Dimension.Z, [-1, 1, -1]):
        void(),fill(MARBLE) ,void()

@rule 
def temple_roof4():
    with split(Dimension.Y, [1, -1]):
        fill(MARBLE),level5roof()

@rule 
def level4roof():
    with split(Dimension.Z, [1, -1, 1]):
        void(),temple_roof4(),void()

@rule 
def temple_roof3():
    with split(Dimension.Y, [1, -1]):
        fill(MARBLE),level4roof()

        
@rule 
def level3roof():
    with split(Dimension.Z, [1, -1, 1]):
        void(),temple_roof3(),void() 

@rule 
def temple_roof2():
    with split(Dimension.Y, [1, -1]):
        fill(MARBLE),level3roof()

@rule 
def level2roof():
    with split(Dimension.Z, [1, -1, 1]):
        void(),temple_roof2(),void()

@rule 
def temple_roof():
    with split(Dimension.Y, [1, -1]):
        fill(MARBLE),level2roof()
        
@rule 
def level3roof_flat():
    with split(Dimension.Z, [2, -1, 2]):
        void(),fill(MARBLE),void()
        
@rule 
def temple_roof2_flat():
    with split(Dimension.Y, [1, -1]):
        fill(MARBLE),level3roof_flat()

@rule 
def level2roof_flat():
    with split(Dimension.Z, [2, -1, 2]):
        void(),temple_roof2_flat(),void() 

@rule 
def temple_roof_flat():
    with split(Dimension.Y, [1, -1]):
        fill(MARBLE),level2roof_flat()
        
@rule 
def columns():
    with split(Dimension.Z, [1,COLUMNSIZE,1,COLUMNSIZE,1,COLUMNSIZE,1,COLUMNSIZE,1]):
        void(), fill(MARBLE), void(), fill(MARBLE), void(), fill(MARBLE), void(), fill(MARBLE), void()
   
@rule   
def chamber():
    with split(Dimension.Z, [1, 1, -1, 1, 1]):
        void(), fill(MARBLE), void(), fill(MARBLE), void()
        
@rule
def back_wall():
    with split(Dimension.Z, [1, -1, 1]):
        void(), fill(MARBLE), void()
        
@rule
def naos():
    with split(Dimension.X, [1, -1, 1]):
        columns(),chamber(),back_wall()

@rule
def floorplan():
    with split(Dimension.X, [1, COLUMNSIZE, 1, -1, 1, COLUMNSIZE, 1]):
        void(),columns(),void(),naos(),void(),columns(),void()

@rule
def temple():
    with split(Dimension.Y, [1, COLUMNHEIGHT, 5]):
        fill(MARBLE),floorplan(),temple_roof()
        
@rule
def temple1():
    with split(Dimension.Y, [1, COLUMNHEIGHT, 1,-1]):
        fill(MARBLE),floorplan(),fill(MARBLE),void()
        
@rule
def temple2():
    with split(Dimension.Y, [1, COLUMNHEIGHT, -1]):
        fill(MARBLE),floorplan(),void()
        
@rule
def temple3():
    with split(Dimension.Y, [1, COLUMNHEIGHT, 3]):
        fill(MARBLE),floorplan(),temple_roof_flat()
        
@rule
def temples():
    with split(Dimension.Z, [9, -1, 9, -1, 9, -1, 9]):
        temple2()
        void()
        temple1()
        void()
        temple()
        void()
        temple3()

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
        sc = start_symbol(bounding_box, world, dimension)
        temples()
        f = open("temple.json", "w")
        json.dump(sc.to_json(True), f, indent=4)
        f.close()

export = {
    "name": "Make Temple",  # the name of the plugin
    "operation": performOperation,  # the actual function to call when running the plugin
}
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
    ("Random Castle Generator", "label"),
    ("Creator: Markus Eger", "label")
    )
    
    
LARGETOWER = 9
SMALLTOWER = 5
GREATHALL = 13
WALLHEIGHT = 5
WALLWIDTH = 3
TOWERHEIGHT = 8


clearrules(__file__)

@rule 
def mid_crennels():
    with split(Dimension.Z, [1,-1,1], z=Dimension.X):
        gapcrennels()
        void()
        gapcrennels()

@rule 
def tower_crennels():
    with split(Dimension.X, [1,-1,1]):
        crennels()
        mid_crennels()
        crennels()

@rule
def large_tower():
    with split(Dimension.Y, [TOWERHEIGHT, 1, -1]):
        fill()
        tower_crennels()
        void()
        
@rule(constraint=(Dimension.Z%2 == 0))
def gapcrennels():
    items = split(Dimension.Z, [1,1], repeat=True)
    while items:
        void()
        fill()

@rule(constraint=Constraint.ELSE)
def gapcrennels():
    with split(Dimension.Z, [-1,1]):
        gapcrennels() 
        void()
    
@rule(constraint=(Dimension.Z%2 == 0))
def crennels():
    items = split(Dimension.Z, [1,1], repeat=True)
    while items:
        fill()
        void()

@rule(constraint=Constraint.ELSE)
def crennels():
    with split(Dimension.Z, [-1,1]):
        crennels() 
        fill()
        
@rule(constraint=Dimension.X<3)
def wallcrennels():
    crennels()
    
@rule(constraint=Constraint.ELSE)
def wallcrennels():
    with split(Dimension.X, [1,-1,1]):
        crennels()
        void()
        crennels()

@rule 
def wall():
    with split(Dimension.Y, [WALLHEIGHT, 1, -1]):
        fill()
        wallcrennels()
        void()
        
@rule
def carve_wall():
    with split(Dimension.X, [-1, WALLWIDTH]):
        void()
        wall()

@rule(constraint=Dimension.Z > 2*LARGETOWER+1)
def side_wall():
    with split(Dimension.Z, [LARGETOWER, -1, LARGETOWER]):
        large_tower()
        carve_wall()
        large_tower()
        
@rule
def carve_wallr():
    with split(Dimension.X, [WALLWIDTH, -1]):
        wall()
        void()

@rule(constraint=Dimension.Z > 2*LARGETOWER+1)
def side_wallr():
    with split(Dimension.Z, [LARGETOWER, -1, LARGETOWER]):
        large_tower()
        carve_wallr()
        large_tower()

@rule
def castle_center():
    with split(Dimension.Z, [LARGETOWER, -1, LARGETOWER]):
        with reorient(x=Dimension.Z):
            carve_wall()
        void()
        with reorient(x=Dimension.Z):
            carve_wallr()
    
@rule(constraint=Dimension.X > 2*LARGETOWER+GREATHALL+4)
def castle_layout():
    with split(Dimension.X, [LARGETOWER,-1,LARGETOWER]):
        side_wall()
        castle_center()
        side_wallr()

@rule(constraint=Constraint.ELSE)
def castle_layout():
    with split(Dimension.X, [SMALLTOWER, -1, SMALLTOWER]): 
        side_wall()
        castle_center()
        side_wallr()
    
@rule
def castle():
    with reorient(x=Dimension.LARGEST, y=Dimension.Y):
        castle_layout()

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
        castle()
        f = open("parsetree.json", "w")
        json.dump(sc.to_json(), f, indent=4)
        f.close()

export = {
    "name": "Make Castle",  # the name of the plugin
    "operation": performOperation,  # the actual function to call when running the plugin
}
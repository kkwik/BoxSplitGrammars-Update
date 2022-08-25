import time # for timing
from math import sqrt, tan, sin, cos, pi, ceil, floor, acos, atan, asin, degrees, radians, log, atan2, acos, asin
from random import *
from numpy import *
from pymclevel import alphaMaterials, MCSchematic, MCLevel, BoundingBox
from mcplatform import *
import json

import utilityFunctions as uf

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
        
        
def perform(level, box, options):
    sc = start_symbol(box, level)
    floorplan()
    
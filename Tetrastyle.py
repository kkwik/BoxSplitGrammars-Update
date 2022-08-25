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
    
def perform(level, box, options):
    sc = start_symbol(box, level)
    temple()
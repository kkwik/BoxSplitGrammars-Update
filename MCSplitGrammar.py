from SplitGrammar import rule, split, reorient, void, fill, Dimension, Direction, Constraint, Scope, clearrules
import utilityFunctions as uf
from pymclevel import alphaMaterials, MCSchematic, MCLevel
import SplitGrammar



class MCScope(Scope):
    def __init__(self, level, box, **kwargs):
        super(MCScope, self).__init__(box, **kwargs)
        self.level = level 
    def make_child(self, box, **kwargs):
        return MCScope(self.level, box, **kwargs)
        
    def set_material(self, material):
        for (x,y,z) in self.box.positions:
            uf.setBlock(self.level, (material,0), x, y, z)
            
def start_symbol(box, level):
    scope = MCScope(level, box, source="Root")
    return SplitGrammar.start_symbol(scope)
    
SplitGrammar.register_material(-1, alphaMaterials.Cobblestone.ID)
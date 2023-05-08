from SplitGrammar import rule, split, reorient, void, fill, Dimension, Direction, Constraint, Scope, clearrules
import SplitGrammar

from amulet.api.block import Block
from amulet.api.selection import SelectionGroup


class MCScope(Scope):
    def __init__(self, level, box, dimension, **kwargs):
        super(MCScope, self).__init__(box, **kwargs)
        self.level = level
        self.dimension = dimension
        self.platform_version = (level.level_wrapper.platform, level.level_wrapper.version)

    def make_child(self, box, **kwargs):
        return MCScope(self.level, box, self.dimension, **kwargs)
        
    def set_material(self, material):
        for (x,y,z) in self.box.positions:
            if isinstance(material, str):
                material = Block.from_string_blockstate(material)
            self.level.set_version_block(x, y, z, self.dimension, self.platform_version, material) # set block


def start_symbol(box: SelectionGroup, level: "BaseLevel", dimension):
    scope = MCScope(level=level, box=box, dimension=dimension, source="Root")
    return SplitGrammar.start_symbol(scope)

    
SplitGrammar.register_material(-1 ,Block.from_string_blockstate("minecraft:stone"))
SplitGrammar.register_material(0, Block.from_string_blockstate("minecraft:air"))
SplitGrammar.register_material(1, Block.from_string_blockstate("minecraft:cobblestone"))
SplitGrammar.register_material(2, Block.from_string_blockstate("minecraft:dirt"))
SplitGrammar.register_material(3, Block.from_string_blockstate("minecraft:granite"))
SplitGrammar.register_material(4, Block.from_string_blockstate("minecraft:diorite"))
SplitGrammar.register_material(5, Block.from_string_blockstate("minecraft:andesite"))
SplitGrammar.register_material(6, Block.from_string_blockstate("minecraft:quartz_block"))
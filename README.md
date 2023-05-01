# Readme

This repository contains Box Split Grammars as presented in Eger, M. "Instant Architecture in Minecraft using Box-Split Grammars", presented at FDG 2022. The grammar system is written in Python 2.7, for compatibility with MCEdit, but it also allows other backends and should be convertible to Python 3, if necessary.

## Setup

To run the grammar system, you will need python 2.7, as stated above. For the Minecraft-Backend you will additionally need [this version](https://github.com/mcgreentn/GDMC) of MCEdit (in particular some of the utility functions). The grammar system can be dropped somewhere in your python path, or just directly into MCEdit's `stock-filter` directory and then be used from any filter. Some demo filters you can find are `MakeCastle.py`, `MakeTemple.py`, `MakeFloorplan.py` and `Tetrastyle.py`, corresponding to various examples shown in the paper (more examples coming soon). `makePattern.py` requires Pillow, and shows how the grammar system can be used with the PNG backend. 

# Amulet Update

## Installation / Usage

1. Download Amulet, can be done through Github releases for exact versioning. [Amulet Releases](https://github.com/Amulet-Team/Amulet-Map-Editor/releases)
2. Place relevant Box-Split Grammar files in `Amulet/plugins/operations/`. NOTE: Do not include PNGSplitGrammar in this or any other non-MCSplitGrammar file as they can override the registered materials in MCSplitGrammar.
3. Run Amulet and open a world. Select a section of land, switch to the Operation tool, select the relevant Operation and run it.

## Notes on implementation

- Amulet passes a SelectionGroup into an operation, which is a collection of one or more SelectionBoxes. This allows operations to work on more complex selection shapes. The current implementation of the Box-Split grammar only works on a SelectionGroup with a single SelectionBox and pass if more than one SelectionBox is present

## Helpful Documentation

- General Documentation on Amulet. [link](https://amulet-map-editor.readthedocs.io/en/develop/api.html)
- Documentation on Amulet Core (Much more helpful). [link](https://amulet-core.readthedocs.io/en/stable/getting_started/index.html)
    - Documentation on the BaseLevel object passed into an operation. [link](https://amulet-core.readthedocs.io/en/stable/api_reference/api/level/base_level/index.html)
    - Documentation on the SelectionGroup object passed into an operation. [link](https://amulet-core.readthedocs.io/en/stable/api_reference/api/selection/group.html)
    - Documentation on the SelectionBox object which is contained by SelectionGroups. [link](https://amulet-core.readthedocs.io/en/stable/api_reference/api/selection/box.html)
- Documentation on MCEdit's BoundingBox. [link](https://github.com/mcedit/mcedit2/blob/4bb98da521447b6cf43d923cea9f00acf2f427e9/src/mceditlib/selection/__init__.py#L430)
- Valid blockstates. [link](https://minecraft.fandom.com/wiki/Block_states)
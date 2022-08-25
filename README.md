# Readme

This repository contains Box Split Grammars as presented in Eger, M. "Instant Architecture in Minecraft using Box-Split Grammars", presented at FDG 2022. The grammar system is written in Python 2.7, for compatibility with MCEdit, but it also allows other backends and should be convertible to Python 3, if necessary.

## Setup

To run the grammar system, you will need python 2.7, as stated above. For the Minecraft-Backend you will additionally need [this version](https://github.com/mcgreentn/GDMC) of MCEdit (in particular some of the utility functions). The grammar system can be dropped somewhere in your python path, or just directly into MCEdit's `stock-filter` directory and then be used from any filter. Some demo filters you can find are `MakeCastle.py`, `MakeTemple.py`, `MakeFloorplan.py` and `Tetrastyle.py`, corresponding to various examples shown in the paper (more examples coming soon). `makePattern.py` requires Pillow, and shows how the grammar system can be used with the PNG backend. 
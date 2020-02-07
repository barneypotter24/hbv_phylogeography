# HBV-D Phylogeography

## BEAST run3
Run using command:
```bash
beast \
  -beagle_gpu \
  -overwrite \
  -seed 888 \
  -save_every 100000 \
  -save_state checkpoint.state \
  D_with_ancient_aligned.xml
```

Ran for approx. 750,000 iterations using TitanV gpu between 5 November and 6 November 2019.

Originally started to test fixing skygrid issue that was initially present in all runs except number 1.
This issue specified a particular starting tree from one of the posterior trees from run1 (process below).
Canceled to start using HMC with new geographic locations.
Seemed to run normally.
Ended at approx. 3.1 hours/million states.


## Starting from a set tree
1. Copied the contents of the `.trees` output file from run1 to `TREES-MODIFIED.txt` and added `END;` to the end of the file so that it could be read into FigTree.
2. Loaded that file into FigTree and set Current Tree to the last posterior tree (number 318 at the time).
3. Selected the tree (mouse over) and copied/pasted into a new FigTree window.
4. Exported that tree as a Newick to `just-one-tree.nwk`
5. Replaced the random starting tree in the XML with the Newick as follows:

Replace:
```xml
<!-- Generate a random starting tree under the coalescent process            -->
<coalescentSimulator id="startingTree">
  <taxa idref="taxa"/>
  <constantSize idref="initialDemo"/>
</coalescentSimulator>
```
With:
```xml
<!-- Specify the starting tree with a Newick -->
<newick id="startingTree">
  THE COPIED CONTENTS OF `just-one-tree.txt`
</newick>
```

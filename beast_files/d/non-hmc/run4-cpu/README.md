# HBV-D Phylogeography

## BEAST run4
Run using command:
```bash
beast \
  -beagle_cpu \
  -overwrite \
  -seed 999 \
  -save_every 100000 \
  -save_state checkpoint.state \
  D_with_ancient_aligned.xml
```

Ran for approx. 97,400,000 iterations using Intel Xeon Gold 5215 cpu (40 available threads) between 1 November and 6 November 2019.

Canceled because the skygrid estimation was not sampling correctly.
Ended at approx. 1.47 hours/million states.

# HBV-D Phylogeography

## BEAST run1
Run using command:
```bash
beast \
  -beagle_gpu \
  -overwrite \
  -seed 666 \
  -save_every 100000 \
  -save_state checkpoint.state \
  D_with_ancient_aligned.xml
```

Ran for approx. 95,040,000 iterations using TitanV gpu between 28 October and 6 November 2019.

Canceled to start using HMC with new geographic locations.
Seemed to run normally.
Ended at approx. 2.26 hours/million states.

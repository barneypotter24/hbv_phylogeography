# HBV-D Phylogeography

## BEAST run2
Run using command:
```bash
beast \
  -beagle_gpu \
  -overwrite \
  -seed 777 \
  -save_every 100000 \
  -save_state checkpoint.state \
  D_with_ancient_aligned.xml
```

Ran for approx. 60,250,000 iterations using TitanV gpu between 1 November and 6 November 2019.

Canceled because the skygrid estimation was not sampling correctly.
Ended at approx. 2.8 hours/million states.

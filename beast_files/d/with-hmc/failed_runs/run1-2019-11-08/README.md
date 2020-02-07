# HBV-D Phylogeography with HMC and Updated Locations

# Beast run1

Started on 8 November 2019 as a GPU replicate of the HBV-D phylogeography analysis.

This run contained ancestral node date sampling.

```bash
java   -jar ~/IdeaProjects/beast-mcmc/build/dist/beast.jar   -beagle_cpu   -overwrite   -seed 666   -save_every 100000   -save_state checkpoint.state   HBV-D_ancientDNA_HMCskygrid_geo.xml
```

Failed after approx. 24,960,000 states (1.5 days) with the following error:
```
24960000	-131711.8585	-18447.8517 	-113264.0068	-177.958    	5.92252E-4  	1.41478E-3  	11    	1.47 hours/million states
Exception in thread "Thread-0" java.lang.ArrayIndexOutOfBoundsException: Index 1537 out of bounds for length 1537
	at dr.evolution.coalescent.TreeIntervals.getIntervalTime(Unknown Source)
	at dr.evomodel.coalescent.GMRFMultilocusSkyrideLikelihood.moveToNextTimeIndex(Unknown Source)
	at dr.evomodel.coalescent.GMRFMultilocusSkyrideLikelihood.setupSufficientStatistics(Unknown Source)
	at dr.evomodel.coalescent.GMRFMultilocusSkyrideLikelihood.checkIntervals(Unknown Source)
	at dr.evomodel.coalescent.GMRFMultilocusSkyrideLikelihood.calculateLogCoalescentLikelihood(Unknown Source)
	at dr.evomodel.coalescent.GMRFMultilocusSkyrideLikelihood.getLogLikelihood(Unknown Source)
	at dr.inference.model.CompoundLikelihood.evaluateLikelihoods(Unknown Source)
	at dr.inference.model.CompoundLikelihood.getLogLikelihood(Unknown Source)
	at dr.inference.model.CompoundLikelihood.evaluateLikelihoods(Unknown Source)
	at dr.inference.model.CompoundLikelihood.getLogLikelihood(Unknown Source)
	at dr.inference.markovchain.MarkovChain.evaluate(Unknown Source)
	at dr.inference.markovchain.MarkovChain.runChain(Unknown Source)
	at dr.inference.mcmc.MCMC.chain(Unknown Source)
	at dr.inference.mcmc.MCMC.run(Unknown Source)
	at java.base/java.lang.Thread.run(Thread.java:834)
1.5250056018518519 days
```

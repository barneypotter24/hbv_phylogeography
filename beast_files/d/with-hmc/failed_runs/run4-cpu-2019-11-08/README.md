# HBV-D Phylogeography with HMC and Updated Locations

# Beast run4

Started on 8 November 2019 as a CPU replicate of the HBV-D phylogeography analysis.

This run contained ancestral node date sampling.

```bash
java   -jar ~/IdeaProjects/beast-mcmc/build/dist/beast.jar   -beagle_cpu   -overwrite   -seed 121212   -save_every 100000   -save_state checkpoint.state   HBV-D_ancientDNA_HMCskygrid_geo.xml
```

Failed after approx. 3,940,000 states (4.6 hours) with the following error:
```
3940000	-136226.6531	-17758.7602 	-118467.8928	-236.906    	3.06528E-3  	4.57611E-3  	13    	1.16 hours/million states
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
4.574026666666667 hours
```

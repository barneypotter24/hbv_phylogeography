# HBV-D Phylogeography with HMC and Updated Locations

# Beast run5

Started on 8 November 2019 as a CPU replicate of the HBV-D phylogeography analysis.

This run contained ancestral node date sampling.

```bash
java   -jar ~/IdeaProjects/beast-mcmc/build/dist/beast.jar   -beagle_cpu   -overwrite   -seed 141414   -save_every 100000   -save_state checkpoint.state   HBV-D_ancientDNA_HMCskygrid_geo.xml
```

Failed after approx. 104,800,000 states (12.8 hours) with the following error:
```
10480000	-132636.1162	-17547.4442 	-115088.6720	-264.574    	4.28479E-3  	5.91077E-3  	10    	1.22 hours/million states
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
12.79496638888889 hours
```

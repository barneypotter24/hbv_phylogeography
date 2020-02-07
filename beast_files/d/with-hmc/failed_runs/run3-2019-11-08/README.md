# HBV-D Phylogeography with HMC and Updated Locations

# Beast run3

Started on 8 November 2019 as a CPU replicate of the HBV-D phylogeography analysis

```bash
java   -jar ~/IdeaProjects/beast-mcmc/build/dist/beast.jar   -beagle_cpu   -overwrite   -seed 151515   -save_every 100000   -save_state checkpoint.state   HBV-D_ancientDNA_HMCskygrid_geo.xml
```

Failed after approx. 13,680,000 states (16.6 hours) with the following error:
```
13680000	-132199.1291	-18309.2843 	-113889.8448	-193.712    	1.08121E-3  	2.1229E-3   	10    	1.21 hours/million states
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
16.60729027777778 hours
```

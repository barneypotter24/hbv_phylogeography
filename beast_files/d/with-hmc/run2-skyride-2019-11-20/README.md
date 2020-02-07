# HBV-D Phylogeography with HMC and Updated Locations

# Beast run2-2019-11-20

Started on 18 November 2019 as a CPU replicate of the HBV-D phylogeography analysis.

This run was started using a Bayesian SkyRide model, since all SkyGrid models errored out and SkyRide run1 seems to be working after 2 days.

Using BEAST version 1.10.4 and BEAGLE CPU.

```bash
beast -beagle_cpu -overwrite -seed 777 -save_every 100000 -save_state checkpoint.state HBV-D_ancientDNA_skyride_geo.xml
```

Starting output:
```
BEAST v1.10.4 Prerelease #bc6cbd9, 2002-2018
Bayesian Evolutionary Analysis Sampling Trees
				 Designed and developed by
Alexei J. Drummond, Andrew Rambaut and Marc A. Suchard

			 Department of Computer Science
					 University of Auckland
					alexei@cs.auckland.ac.nz

		 Institute of Evolutionary Biology
					University of Edinburgh
						 a.rambaut@ed.ac.uk

			David Geffen School of Medicine
	 University of California, Los Angeles
						 msuchard@ucla.edu

				Downloads, Help & Resources:
						http://beast.community

Source code distributed under the GNU Lesser General Public License:
		http://github.com/beast-dev/beast-mcmc

						 BEAST developers:
Alex Alekseyenko, Guy Baele, Trevor Bedford, Filip Bielejec, Erik Bloomquist, Matthew Hall,
Joseph Heled, Sebastian Hoehna, Denise Kuehnert, Philippe Lemey, Wai Lok Sibon Li,
Gerton Lunter, Sidney Markowitz, Vladimir Minin, Michael Defoin Platel,
		Oliver Pybus, Chieh-Hsi Wu, Walter Xie

								 Thanks to:
Roald Forsberg, Beth Shapiro and Korbinian Strimmer

Using BEAGLE library v3.2.0 (PRE-RELEASE) for accelerated, parallel likelihood evaluation
2009-, BEAGLE Working Group - https://beagle-dev.github.io/
Citation: Ayres et al (2012) Systematic Biology 61: 170-173 | doi:10.1093/sysbio/syr100


Random number seed: 777


Loading additional development parsers from development_parsers.properties, which is additional set of parsers only available for development version ...
Parsing XML file: HBV-D_ancientDNA_skyride_geo.xml
File encoding: UTF8
Looking for plugins in /home/luna.kuleuven.be/r0787607/projects/hbv_phylogeography/beast_files/d/with-hmc/run2-skyride-2019-11-20/plugins

Read alignment: alignment
Sequences = 769
Sites = 3188
Datatype = nucleotide
Site patterns 'patterns' created from positions 1-3188 of alignment 'alignment'
unique pattern count = 2104
Read attribute patterns, 'location.pattern' for attribute, location

Creating the tree model, 'treeModel'
taxon count = 769
tree height = 2208.454782650104
The gmrfSkyrideLikelihood has time aware smoothing
Creating a GMRF smoothed skyride model:
Population sizes: 768
If you publish results using this model, please reference: Minin, Bloomquist and Suchard (2008) Molecular Biology and Evolution, 25, 1459-1471.

Using discretized relaxed clock model.
over sampling = 1
parametric model = logNormalDistributionModel
rate categories = 1

Using strict molecular clock model.

Creating state frequencies model 'frequencies': Initial frequencies = {0.25, 0.25, 0.25, 0.25}

Creating HKY substitution model. Initial kappa = 2.0

Creating site rate model:
4 category discrete gamma with initial shape = 0.5

Using BEAGLE DataLikelihood Delegate
Using BEAGLE resource 0: CPU
with instance flags:  PRECISION_DOUBLE COMPUTATION_SYNCH EIGEN_REAL SCALING_MANUAL SCALERS_RAW VECTOR_SSE THREADING_CPP PROCESSOR_CPU FRAMEWORK_CPU
Ignoring ambiguities in tree likelihood.
With 2104 unique site patterns.
Using rescaling scheme : dynamic (rescaling every 100 evaluations, delay rescaling until first overflow)

Using TreeDataLikelihood
Branch rate model used: discretizedBranchRates

Creating state frequencies model 'location.frequencies': Initial frequencies = {0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125}
General Substitution Model (stateCount=8)
Using BSSVS General Substitution Model

Creating site rate model.

Using BEAGLE TreeLikelihood
Branch rate model used: strictClockBranchRates
Using BEAGLE resource 0: CPU
with instance flags:  PRECISION_DOUBLE COMPUTATION_SYNCH EIGEN_REAL SCALING_MANUAL SCALERS_RAW VECTOR_NONE THREADING_CPP PROCESSOR_CPU FRAMEWORK_CPU
Ignoring ambiguities in tree likelihood.
With 1 unique site patterns.
Using rescaling scheme : delayed (delay rescaling until first overflow)
Creating swap operator for parameter default.branchRates.categories (weight=10.0)
Optimization Schedule: log
Creating CTMC Scale Reference Prior model.
Acting on subtree of size 769
Creating CTMC Scale Reference Prior model.
Acting on subtree of size 769
Constructing a cache around likelihood 'null', signal = location.rates

Likelihood computation is using an auto sizing thread pool.

Creating the MCMC chain:
chain length = 500000000
operator adaption = true
adaptation delayed for 5000000 steps
WARNING: Likelihood component, null, created but not used in the MCMC
Underflow calculating likelihood. Attempting a rescaling...
Underflow calculating likelihood. Attempting a rescaling... (patterns)

Citations for this analysis:

FRAMEWORK
BEAST primary citation:
Suchard MA, Lemey P, Baele G, Ayres DL, Drummond AJ, Rambaut A (2018) Bayesian phylogenetic and phylodynamic data integration using BEAST 1.10. Virus Evolution. vey016. DOI:10.1093/ve/vey016
Using BEAGLE likelihood calculation library:
Ayres et al  (2012) BEAGLE: a common application programming inferface and high-performance computing library for statistical phylogenetics. Syst Biol. 61, 170-173. DOI:10.1093/sysbio/syr100

TREE DENSITY MODELS
Skyride coalescent:
Minin VN, Bloomquist EW, Suchard MA (2008) Smooth skyride through a rough skyline: Bayesian coalescent-based inference of population dynamics. Mol Biol Evol. 25, 1459-1471. DOI:10.1093/molbev/msn090

MOLECULAR CLOCK MODELS
Uncorrelated relaxed clock:
Drummond AJ, Ho SYW, Phillips MJ, Rambaut A (2006) Relaxed Phylogenetics and Dating with Confidence. PLoS Biology. 4: e88. DOI:10.1371/journal.pbio.0040088

SUBSTITUTION MODELS
HKY nucleotide substitution model:
Hasegawa M, Kishino H, Yano T (1985) Dating the human-ape splitting by a molecular clock of mitochondrial DNA. J. Mol. Evol.. 22, 160-174
Discrete gamma-distributed rate heterogeneity model:
Yang Z (1994) Maximum likelihood phylogenetic estimation from DNA sequences with variable rates over sites: approximate methods. J. Mol. Evol.. 39, 306-314
Stochastic search variable selection, reversible substitution model:
Lemey P, Rambaut A, Drummond AJ, Suchard MA (2009) Bayesian phylogeography finds its roots. PLoS Computational Biology. e1000520

PRIOR MODELS
CTMC Scale Reference Prior model:
Ferreira MAR, Suchard MA (2008) Bayesian analysis of elapsed times in continuous-time Markov chains. Canadian Journal of Statistics. 36, 355-368


# BEAST v1.10.4 Prerelease #bc6cbd9
# Generated Wed Nov 20 10:30:24 CET 2019 [seed=777]
# -beagle_cpu -overwrite -seed 777 -save_every 100000 -save_state checkpoint.state HBV-D_ancientDNA_skyride_geo.xml
# keywords: skyride discretized_branch_rates
state	Joint       	Prior       	Likelihood  	age(root)   	default.ucld.mean	location.clock.rate	location.nonZeroRates
0	-494252.1315	-50374.7963 	-443877.3352	-196.455    	1.00000     	1.00000     	28    	-
10000	-236324.0680	-21178.0613 	-215146.0067	-1573.98    	4.54011E-3  	1.06233E-2  	10    	-
20000	-224880.4772	-20878.2548 	-204002.2224	-725.454    	6.34225E-3  	1.40107E-2  	12    	1.68 hours/million states
30000	-216573.4296	-20341.7736 	-196231.6559	-640.408    	6.60244E-3  	1.49385E-2  	11    	1.56 hours/million states
40000	-212158.1308	-20722.3630 	-191435.7678	-639.415    	6.40154E-3  	1.52423E-2  	12    	1.52 hours/million states
50000	-208156.3141	-20689.3822 	-187466.9320	-610.639    	6.4802E-3   	1.50006E-2  	12    	1.52 hours/million states
60000	-204679.6217	-20445.7579 	-184233.8638	-592.707    	6.45899E-3  	1.62585E-2  	12    	1.5 hours/million states
70000	-201683.6885	-20711.1282 	-180972.5603	-592.300    	6.49999E-3  	1.30999E-2  	10    	1.49 hours/million states
80000	-199156.4548	-20392.2185 	-178764.2364	-592.663    	6.31751E-3  	1.33979E-2  	11    	1.48 hours/million states
90000	-197112.5660	-20655.3681 	-176457.1979	-589.548    	6.48045E-3  	1.327E-2    	10    	1.48 hours/million states
100000	-195205.1194	-20606.9220 	-174598.1975	-579.713    	6.41998E-3  	1.30192E-2  	10    	1.48 hours/million states
110000	-193030.7522	-20514.2276 	-172516.5246	-579.961    	6.76494E-3  	1.28875E-2  	12    	1.48 hours/million states
120000	-190944.8474	-20411.0350 	-170533.8125	-579.720    	6.54588E-3  	1.34308E-2  	10    	1.49 hours/million states
130000	-189775.6067	-20463.2229 	-169312.3838	-579.704    	6.6563E-3   	1.19365E-2  	13    	1.49 hours/million states
140000	-188768.0693	-20612.2948 	-168155.7745	-579.816    	6.39647E-3  	1.20202E-2  	11    	1.5 hours/million states
150000	-187071.4243	-20280.6436 	-166790.7807	-580.184    	6.43799E-3  	1.25652E-2  	11    	1.5 hours/million states
160000	-186265.6920	-20613.2739 	-165652.4181	-579.637    	6.38098E-3  	1.2454E-2   	11    	1.5 hours/million states
170000	-185129.8937	-20658.1926 	-164471.7011	-580.206    	6.37677E-3  	1.22794E-2  	12    	1.5 hours/million states
180000	-183806.6378	-20476.8102 	-163329.8277	-580.602    	6.61227E-3  	1.15089E-2  	12    	1.5 hours/million states
190000	-183068.4711	-20448.5533 	-162619.9178	-584.423    	6.53523E-3  	1.16055E-2  	11    	1.5 hours/million states
200000	-182325.5780	-20718.5215 	-161607.0565	-586.857    	6.91344E-3  	1.11354E-2  	12    	1.51 hours/million states

```

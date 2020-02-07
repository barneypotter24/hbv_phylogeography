# HBV-D Phylogeography with HMC and Updated Locations

# Beast run1-2019-11-18

Started on 20 November 2019 as a CPU replicate of the HBV-D phylogeography analysis.

This run was started using a Bayesian SkyRide model, since all SkyGrid models errored out.

Using BEAST version 1.10.4 and BEAGLE CPU on

```bash
beast -beagle_cpu -overwrite -seed 666 -save_every 100000 -save_state checkpoint.state HBV-D_ancientDNA_skyride_geo.xml
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


Random number seed: 666


Loading additional development parsers from development_parsers.properties, which is additional set of parsers only available for development version ...
Parsing XML file: HBV-D_ancientDNA_skyride_geo.xml
File encoding: UTF8
Looking for plugins in /home/luna.kuleuven.be/r0787607/projects/hbv_phylogeography/beast_files/d/with-hmc/run1-skyride-2019-11-18/plugins

Read alignment: alignment
Sequences = 769
Sites = 3188
Datatype = nucleotide
Site patterns 'patterns' created from positions 1-3188 of alignment 'alignment'
unique pattern count = 2104
Read attribute patterns, 'location.pattern' for attribute, location

Creating the tree model, 'treeModel'
taxon count = 769
tree height = 2246.873306134997
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
# Generated Mon Nov 18 14:45:58 CET 2019 [seed=666]
# -beagle_cpu -overwrite -seed 666 -save_every 100000 -save_state checkpoint.state HBV-D_ancientDNA_skyride_geo.xml
# keywords: skyride discretized_branch_rates
state	Joint       	Prior       	Likelihood  	age(root)   	default.ucld.mean	location.clock.rate	location.nonZeroRates
0	-496809.6833	-54469.8579 	-442339.8254	-234.873    	1.00000     	1.00000     	28    	-
10000	-236650.0422	-21611.2356 	-215038.8066	-2239.82    	3.50076E-3  	8.3269E-3   	11    	-
20000	-225489.1132	-21138.7176 	-204350.3957	-1951.01    	3.35505E-3  	7.57843E-3  	12    	1.47 hours/million states
30000	-217846.5333	-21210.5868 	-196635.9465	-1703.79    	3.789E-3    	7.87753E-3  	11    	1.47 hours/million states
40000	-212881.0450	-21054.2455 	-191826.7994	-1660.98    	3.97366E-3  	8.44006E-3  	9     	1.47 hours/million states
50000	-209110.1712	-21220.3001 	-187889.8711	-1656.62    	4.1154E-3   	9.03262E-3  	10    	1.46 hours/million states
60000	-206021.6583	-21143.7132 	-184877.9452	-1678.37    	3.9999E-3   	8.23204E-3  	10    	1.44 hours/million states
70000	-203180.7633	-21259.3842 	-181921.3791	-1647.27    	4.15983E-3  	8.07015E-3  	10    	1.43 hours/million states
80000	-200930.6563	-21242.1747 	-179688.4816	-1644.66    	4.09973E-3  	8.16415E-3  	12    	1.42 hours/million states
90000	-198658.1756	-21242.4567 	-177415.7189	-1644.17    	4.16169E-3  	8.23411E-3  	10    	1.41 hours/million states
100000	-196148.6161	-21063.2696 	-175085.3464	-1641.79    	4.11424E-3  	7.81654E-3  	12    	1.4 hours/million states
110000	-194546.4877	-20947.7509 	-173598.7367	-1674.43    	4.10838E-3  	7.14444E-3  	14    	1.4 hours/million states
120000	-193040.2586	-21237.0510 	-171803.2075	-1675.25    	4.03157E-3  	7.77493E-3  	13    	1.39 hours/million states
130000	-191587.5181	-21270.6208 	-170316.8974	-1673.79    	3.92938E-3  	7.54027E-3  	13    	1.38 hours/million states
140000	-190199.7201	-21135.7359 	-169063.9842	-1675.15    	3.85295E-3  	7.88504E-3  	15    	1.38 hours/million states
150000	-188995.1166	-21125.1125 	-167870.0041	-1676.93    	3.85863E-3  	6.67018E-3  	15    	1.37 hours/million states
160000	-187365.4366	-21108.2112 	-166257.2254	-1657.46    	3.84327E-3  	6.90063E-3  	14    	1.37 hours/million states
170000	-186202.1257	-21098.5995 	-165103.5261	-1665.91    	3.85739E-3  	6.74425E-3  	13    	1.36 hours/million states
180000	-185551.4264	-21345.4816 	-164205.9448	-1678.68    	3.77293E-3  	6.58241E-3  	14    	1.36 hours/million states
190000	-184285.5364	-21088.4361 	-163197.1003	-1709.88    	3.77593E-3  	5.63585E-3  	14    	1.36 hours/million states
200000	-183210.9516	-20999.6216 	-162211.3300	-1691.58    	3.77296E-3  	6.43138E-3  	14    	1.36 hours/million states
```

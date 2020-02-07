# HBV-D Phylogeography with HMC and Updated Locations

# Beast run3-2019-11-20

Started on 20 November 2019 as a CPU replicate of the HBV-D phylogeography analysis.

This run was started using a Bayesian SkyRide model, since all SkyGrid models errored out and SkyRide run1 seems to be working after 2 days.

Using BEAST version 1.10.4 and BEAGLE CPU.

```bash
beast -beagle_cpu -overwrite -seed 888 -save_every 100000 -save_state checkpoint.state HBV-D_ancientDNA_skyride_geo.xml
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


Random number seed: 888


Loading additional development parsers from development_parsers.properties, which is additional set of parsers only available for development version ...
Parsing XML file: HBV-D_ancientDNA_skyride_geo.xml
File encoding: UTF8
Looking for plugins in /home/luna.kuleuven.be/r0787607/projects/hbv_phylogeography/beast_files/d/with-hmc/run3-skyride-2019-11-20/plugins

Read alignment: alignment
Sequences = 769
Sites = 3188
Datatype = nucleotide
Site patterns 'patterns' created from positions 1-3188 of alignment 'alignment'
unique pattern count = 2104
Read attribute patterns, 'location.pattern' for attribute, location

Creating the tree model, 'treeModel'
taxon count = 769
tree height = 2234.2228058357387
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
# Generated Wed Nov 20 10:30:46 CET 2019 [seed=888]
# -beagle_cpu -overwrite -seed 888 -save_every 100000 -save_state checkpoint.state HBV-D_ancientDNA_skyride_geo.xml
# keywords: skyride discretized_branch_rates
state	Joint       	Prior       	Likelihood  	age(root)   	default.ucld.mean	location.clock.rate	location.nonZeroRates
0	-483844.5879	-51280.2882 	-432564.2997	-222.223    	1.00000     	1.00000     	28    	-
10000	-234819.8900	-21056.9860 	-213762.9040	-1321.84    	7.09338E-3  	1.46726E-2  	12    	-
20000	-222795.1560	-20985.8119 	-201809.3441	-196.853    	7.18566E-3  	1.74144E-2  	12    	1.46 hours/million states
30000	-216215.2298	-20916.4842 	-195298.7456	-193.627    	7.12794E-3  	1.57492E-2  	14    	1.43 hours/million states
40000	-210696.2767	-20875.8308 	-189820.4458	-188.949    	7.17308E-3  	1.73758E-2  	12    	1.42 hours/million states
50000	-207122.5469	-20888.2737 	-186234.2732	-188.776    	7.18443E-3  	1.86752E-2  	11    	1.41 hours/million states
60000	-203830.7845	-20865.8383 	-182964.9463	-188.460    	7.0584E-3   	1.59522E-2  	11    	1.41 hours/million states
70000	-200991.8008	-20880.7512 	-180111.0496	-188.481    	6.98397E-3  	1.66649E-2  	12    	1.41 hours/million states
80000	-198875.2652	-20870.1848 	-178005.0804	-189.178    	6.75396E-3  	1.63525E-2  	11    	1.41 hours/million states
90000	-196407.0893	-20894.9879 	-175512.1014	-188.245    	6.74384E-3  	1.88006E-2  	12    	1.41 hours/million states
100000	-194912.9833	-20887.8655 	-174025.1178	-188.397    	6.59076E-3  	1.61871E-2  	11    	1.41 hours/million states
110000	-192872.7689	-20870.5856 	-172002.1832	-188.270    	6.63372E-3  	1.50821E-2  	13    	1.4 hours/million states
120000	-191410.1623	-20899.2483 	-170510.9141	-189.332    	6.68032E-3  	1.62823E-2  	12    	1.4 hours/million states
130000	-190116.1309	-20881.7135 	-169234.4174	-188.164    	6.79105E-3  	1.43122E-2  	13    	1.39 hours/million states
140000	-189299.9066	-20897.7057 	-168402.2010	-188.859    	6.71174E-3  	1.63743E-2  	13    	1.39 hours/million states
150000	-188417.4689	-20868.4242 	-167549.0446	-188.282    	6.89499E-3  	1.41908E-2  	13    	1.39 hours/million states
160000	-187150.3365	-20870.1777 	-166280.1588	-188.041    	6.72054E-3  	1.5079E-2   	12    	1.38 hours/million states
170000	-185839.8214	-20852.3260 	-164987.4954	-191.137    	6.77967E-3  	1.37129E-2  	13    	1.38 hours/million states
180000	-184949.0158	-20877.5925 	-164071.4233	-193.896    	6.85942E-3  	1.43473E-2  	13    	1.38 hours/million states
190000	-184100.5509	-20851.0287 	-163249.5222	-190.459    	6.99729E-3  	1.3134E-2   	13    	1.38 hours/million states
200000	-183334.0657	-20840.6546 	-162493.4111	-189.206    	6.8294E-3   	1.39027E-2  	14    	1.37 hours/million states
```

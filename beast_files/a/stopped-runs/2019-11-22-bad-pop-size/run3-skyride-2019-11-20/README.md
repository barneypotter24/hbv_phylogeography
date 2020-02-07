# HBV-A Phylogeography with HMC and Updated Locations

# Beast run3-2019-11-20

Started on 20 November 2019 as a GPU replicate of the HBV-A phylogeography analysis.


Using BEAST version 1.10.4 and BEAGLE GPU on NVIDIA Titan V.

```bash
beast1.10.5pre -beagle_gpu -overwrite -seed 888 -save_every 100000 -save_state checkpoint.state HBV-A_ancientDNA_skyride_geo.xml
```

Starting output:
```
BEAST v1.10.5 Prerelease #23570d1, 2002-2019
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

Parsing XML file: HBV-A_ancientDNA_skyride_geo.xml
File encoding: UTF8
Looking for plugins in /home/luna.kuleuven.be/r0787607/projects/hbv_phylogeography/beast_files/a/run3-skyride-2019-11-20/plugins

Read alignment: alignment
Sequences = 587
Sites = 3222
Datatype = nucleotide
Site patterns 'patterns' created from positions 1-3222 of alignment 'alignment'
unique pattern count = 1937
Read attribute patterns, 'location.pattern' for attribute, location

Creating the tree model, 'treeModel'
taxon count = 587
tree height = 4503.923932439754
The gmrfSkyrideLikelihood has time aware smoothing
Creating a GMRF smoothed skyride model:
Population sizes: 586
If you publish results using this model, please reference: Minin, Bloomquist and Suchard (2008) Molecular Biology and Evolution, 25, 1459-1471.

Using discretized relaxed clock model.
over sampling = 1
parametric model = logNormalDistributionModel
rate categories = 1

Using strict molecular clock model.

Creating state frequencies model 'frequencies': Initial frequencies = {0.25, 0.25, 0.25, 0.25}

Creating HKY substitution model. Initial kappa = 2.0

Creating site rate model.

Using BEAGLE DataLikelihood Delegate
Using BEAGLE resource 1: TITAN V
Global memory (MB): 12037
Clock speed (Ghz): 1.46
Number of cores: 10240
with instance flags:  PRECISION_DOUBLE COMPUTATION_SYNCH EIGEN_REAL SCALING_MANUAL SCALERS_RAW VECTOR_NONE THREADING_NONE PROCESSOR_GPU FRAMEWORK_CUDA
Ignoring preOrder partials in tree likelihood.
Ignoring ambiguities in tree likelihood.
With 1937 unique site patterns.
Using rescaling scheme : dynamic (rescaling every 100 evaluations, delay rescaling until first overflow)

Using TreeDataLikelihood
Branch rate model used: discretizedBranchRates

Creating state frequencies model 'location.frequencies': Initial frequencies = {0.2, 0.2, 0.2, 0.2, 0.2}
General Substitution Model (stateCount=5)
Using BSSVS General Substitution Model

Creating site rate model.

Using BEAGLE TreeLikelihood
Branch rate model used: strictClockBranchRates
Using BEAGLE resource 1: TITAN V
Global memory (MB): 12037
Clock speed (Ghz): 1.46
Number of cores: 10240
with instance flags:  PRECISION_DOUBLE COMPUTATION_SYNCH EIGEN_REAL SCALING_MANUAL SCALERS_RAW VECTOR_NONE THREADING_NONE PROCESSOR_GPU FRAMEWORK_CUDA
Ignoring ambiguities in tree likelihood.
With 1 unique site patterns.
Using rescaling scheme : delayed (delay rescaling until first overflow)
Creating swap operator for parameter default.branchRates.categories (weight=10.0)
Optimization Schedule: log
Creating CTMC Scale Reference Prior model.
Acting on subtree of size 587
Creating CTMC Scale Reference Prior model.
Acting on subtree of size 587
Constructing a cache around likelihood 'null', signal = location.rates

Likelihood computation is using an auto sizing thread pool.

Creating the MCMC chain:
chain length = 500000000
operator adaption = true
adaptation delayed for 5000000 steps
WARNING: Likelihood component, null, created but not used in the MCMC
Underflow calculating likelihood. Attempting a rescaling... (patterns)
Underflow calculating likelihood. Attempting a rescaling...

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
Stochastic search variable selection, reversible substitution model:
Lemey P, Rambaut A, Drummond AJ, Suchard MA (2009) Bayesian phylogeography finds its roots. PLoS Computational Biology. e1000520

PRIOR MODELS
CTMC Scale Reference Prior model:
Ferreira MAR, Suchard MA (2008) Bayesian analysis of elapsed times in continuous-time Markov chains. Canadian Journal of Statistics. 36, 355-368


# BEAST v1.10.5 Prerelease #23570d1
# Generated Wed Nov 20 10:51:43 CET 2019 [seed=888]
# -beagle_gpu -overwrite -seed 888 -save_every 100000 -save_state checkpoint.state HBV-A_ancientDNA_skyride_geo.xml
# keywords: skyride discretized_branch_rates
state	Joint       	Prior       	Likelihood  	age(root)   	default.ucld.meanlocation.clock.rate	location.nonZeroRates
0	-2134334.0698	-43168.5832 	-2091165.4866	-2489.92    	1.00000     	1.00000     	10    	-
10000	-199672.5892	-14136.3800 	-185536.2092	-2276.70    	6.3234E-3   	1.88865E-2  	7     	-
20000	-177208.0881	-14394.2507 	-162813.8374	-2281.65    	6.00884E-3  	2.3651E-2   	8     	1.47 hours/million states
30000	-164529.6892	-14414.7554 	-150114.9338	-2270.57    	6.28797E-3  	2.55059E-2  	6     	1.52 hours/million states
40000	-157659.0260	-14416.3153 	-143242.7107	-2266.57    	6.30717E-3  	2.10788E-2  	6     	1.52 hours/million states
50000	-152813.2471	-14465.3887 	-138347.8584	-2273.91    	6.54358E-3  	1.48604E-2  	6     	1.51 hours/million states
60000	-149190.4698	-14567.6274 	-134622.8424	-2267.77    	6.4945E-3   	1.42133E-2  	6     	1.51 hours/million states
70000	-146431.5699	-14451.1240 	-131980.4459	-2285.84    	6.58426E-3  	1.26001E-2  	6     	1.5 hours/million states
80000	-144299.0816	-14552.6972 	-129746.3845	-2308.86    	6.74264E-3  	1.44419E-2  	6     	1.5 hours/million states
90000	-140722.5885	-14356.8804 	-126365.7080	-2278.45    	6.85113E-3  	1.49815E-2  	6     	1.49 hours/million states
100000	-137699.5307	-14134.4056 	-123565.1251	-2290.62    	6.84828E-3  	1.39293E-2  	6     	1.5 hours/million states
110000	-135643.4287	-14262.2265 	-121381.2022	-2282.03    	6.78782E-3  	1.65498E-2  	6     	1.5 hours/million states
120000	-134707.6595	-14751.0679 	-119956.5916	-2278.45    	6.80815E-3  	1.33902E-2  	7     	1.5 hours/million states
130000	-133185.2389	-14550.1430 	-118635.0959	-2267.95    	6.75116E-3  	1.503E-2    	6     	1.49 hours/million states
140000	-130102.1466	-14506.1522 	-115595.9944	-2273.29    	6.70082E-3  	1.59779E-2  	7     	1.49 hours/million states
150000	-128562.0401	-14661.4343 	-113900.6059	-2264.38    	6.79365E-3  	1.44144E-2  	6     	1.49 hours/million states
160000	-127756.6028	-14669.5471 	-113087.0557	-2266.52    	6.75152E-3  	1.49578E-2  	6     	1.49 hours/million states
170000	-126525.3536	-14330.5470 	-112194.8066	-2264.46    	6.75347E-3  	1.26486E-2  	6     	1.49 hours/million states
180000	-125386.0404	-14505.3270 	-110880.7133	-2265.85    	6.65455E-3  	1.35309E-2  	6     	1.48 hours/million states
190000	-124832.4394	-14675.6607 	-110156.7787	-2270.36    	6.60812E-3  	9.73508E-3  	6     	1.48 hours/million states
200000	-123295.2115	-14591.6614 	-108703.5501	-2274.72    	6.68274E-3  	1.04761E-2  	7     	1.48 hours/million states
```

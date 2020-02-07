# HBV-D Phylogeography with HMC and Updated Locations

# Beast run4-2019-11-20

Started on 20 November 2019 as a CPU replicate of the HBV-D phylogeography analysis.

This run was started using a Bayesian SkyRide model, since all SkyGrid models errored out and SkyRide run1 seems to be working after 2 days.

Using BEAST version 1.10.4 and BEAGLE CPU.

```bash
beast -beagle_cpu -overwrite -seed 999 -save_every 100000 -save_state checkpoint.state HBV-D_ancientDNA_skyride_geo.xml
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


Random number seed: 999


Loading additional development parsers from development_parsers.properties, which is additional set of parsers only available for development version ...
Parsing XML file: HBV-D_ancientDNA_skyride_geo.xml
File encoding: UTF8
Looking for plugins in /home/luna.kuleuven.be/r0787607/projects/hbv_phylogeography/beast_files/d/with-hmc/run4-skyride-2019-11-20/plugins

Read alignment: alignment
Sequences = 769
Sites = 3188
Datatype = nucleotide
Site patterns 'patterns' created from positions 1-3188 of alignment 'alignment'
unique pattern count = 2104
Read attribute patterns, 'location.pattern' for attribute, location

Creating the tree model, 'treeModel'
taxon count = 769
tree height = 2229.147091402372
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
# Generated Wed Nov 20 14:16:56 CET 2019 [seed=999]
# -beagle_cpu -overwrite -seed 999 -save_every 100000 -save_state checkpoint.state HBV-D_ancientDNA_skyride_geo.xml
# keywords: skyride discretized_branch_rates
state	Joint       	Prior       	Likelihood  	age(root)   	default.ucld.mean	location.clock.rate	location.nonZeroRates
0	-476308.9981	-49316.2144 	-426992.7837	-217.147    	1.00000     	1.00000     	28    	-
10000	-235828.3523	-20747.5967 	-215080.7556	-1135.81    	8.02666E-3  	1.66044E-2  	12    	-
20000	-225182.0065	-20794.8368 	-204387.1697	-198.982    	8.20224E-3  	1.92523E-2  	13    	2.04 hours/million states
30000	-217796.9524	-20768.4711 	-197028.4813	-190.421    	7.81954E-3  	1.92341E-2  	13    	2.03 hours/million states
40000	-211917.6253	-20763.4284 	-191154.1970	-188.506    	7.52738E-3  	1.81318E-2  	13    	2.03 hours/million states
50000	-208303.2511	-20748.4774 	-187554.7737	-188.239    	7.51121E-3  	1.74879E-2  	11    	2.02 hours/million states
60000	-205166.6199	-20782.4270 	-184384.1929	-188.750    	7.33552E-3  	2.00745E-2  	14    	2.03 hours/million states
70000	-202830.4919	-20745.1608 	-182085.3311	-189.152    	7.06524E-3  	1.7197E-2   	12    	2.05 hours/million states
80000	-200013.1300	-20744.1443 	-179268.9858	-190.510    	7.0487E-3   	1.67962E-2  	12    	2.04 hours/million states
90000	-197880.4020	-20746.3923 	-177134.0097	-189.560    	6.84198E-3  	1.53728E-2  	12    	2.03 hours/million states
100000	-195612.9396	-20716.4413 	-174896.4982	-188.375    	6.82687E-3  	1.61112E-2  	12    	2.03 hours/million states
110000	-193676.5244	-20724.6853 	-172951.8392	-188.731    	6.67934E-3  	1.54039E-2  	16    	2.02 hours/million states
120000	-191753.8254	-20767.4694 	-170986.3560	-188.109    	6.76654E-3  	1.77311E-2  	14    	2.02 hours/million states
130000	-190179.2848	-20701.4954 	-169477.7894	-188.143    	6.62069E-3  	1.50166E-2  	13    	2.02 hours/million states
140000	-189028.9224	-20714.9738 	-168313.9486	-188.555    	6.62768E-3  	1.57511E-2  	11    	2.02 hours/million states
150000	-188219.5998	-20725.6505 	-167493.9493	-188.036    	6.58044E-3  	1.66915E-2  	13    	2.01 hours/million states
160000	-187391.6164	-20692.6829 	-166698.9335	-188.048    	6.58044E-3  	1.5669E-2   	11    	2.01 hours/million states
170000	-186010.9742	-20703.1432 	-165307.8310	-188.097    	6.60798E-3  	1.55406E-2  	12    	2.02 hours/million states
180000	-184823.2046	-20668.7613 	-164154.4433	-188.082    	6.65941E-3  	1.45849E-2  	12    	2.02 hours/million states
190000	-183241.8844	-20718.5114 	-162523.3730	-188.084    	6.91271E-3  	1.68414E-2  	14    	2.02 hours/million states
200000	-181941.7114	-20719.3248 	-161222.3867	-188.038    	6.70983E-3  	1.58092E-2  	15    	2.03 hours/million states
```

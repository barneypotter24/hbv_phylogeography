# HBV-A Phylogeography with HMC and Updated Locations

# Beast run2-2019-11-20

Started on 20 November 2019 as a GPU replicate of the HBV-A phylogeography analysis.

Using BEAST version 1.10.5pre and BEAGLE CPU.

```bash
beast1.10.5pre -beagle_cpu -overwrite -seed 777 -save_every 100000 -save_state checkpoint.state HBV-A_ancientDNA_skyride_geo.xml
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


Random number seed: 777


Loading additional development parsers from development_parsers.properties, which is additional set of parsers only available for development version ...

Parsing XML file: HBV-A_ancientDNA_skyride_geo.xml
File encoding: UTF8
Looking for plugins in /home/luna.kuleuven.be/r0787607/projects/hbv_phylogeography/beast_files/a/run2-skyride-2019-11-20/plugins

Read alignment: alignment
Sequences = 587
Sites = 3222
Datatype = nucleotide
Site patterns 'patterns' created from positions 1-3222 of alignment 'alignment'
unique pattern count = 1937
Read attribute patterns, 'location.pattern' for attribute, location

Creating the tree model, 'treeModel'
taxon count = 587
tree height = 4296.089909726406
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
Using BEAGLE resource 0: CPU
with instance flags:  PRECISION_DOUBLE COMPUTATION_SYNCH EIGEN_REAL SCALING_MANUAL SCALERS_RAW VECTOR_SSE THREADING_CPP PROCESSOR_CPU FRAMEWORK_CPU
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
Using BEAGLE resource 0: CPU
with instance flags:  PRECISION_DOUBLE COMPUTATION_SYNCH EIGEN_REAL SCALING_MANUAL SCALERS_RAW VECTOR_NONE THREADING_CPP PROCESSOR_CPU FRAMEWORK_CPU
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
Stochastic search variable selection, reversible substitution model:
Lemey P, Rambaut A, Drummond AJ, Suchard MA (2009) Bayesian phylogeography finds its roots. PLoS Computational Biology. e1000520

PRIOR MODELS
CTMC Scale Reference Prior model:
Ferreira MAR, Suchard MA (2008) Bayesian analysis of elapsed times in continuous-time Markov chains. Canadian Journal of Statistics. 36, 355-368


# BEAST v1.10.5 Prerelease #23570d1
# Generated Wed Nov 20 10:51:12 CET 2019 [seed=777]
# -beagle_cpu -overwrite -seed 777 -save_every 100000 -save_state checkpoint.state HBV-A_ancientDNA_skyride_geo.xml
# keywords: skyride discretized_branch_rates
state	Joint       	Prior       	Likelihood  	age(root)   	default.ucld.meanlocation.clock.rate	location.nonZeroRates
0	-2110376.4494	-43585.6951 	-2066790.7543	-2282.09    	1.00000     	1.00000     	10    	-
10000	-210254.8813	-13133.1622 	-197121.7190	-2264.12    	1.56595E-2  	2.41585E-2  	7     	-
20000	-181010.6514	-13740.4592 	-167270.1921	-2266.68    	1.01659E-2  	1.85839E-2  	6     	0.76 hours/million states
30000	-169241.7430	-14196.7974 	-155044.9456	-2264.17    	1.00692E-2  	1.90013E-2  	6     	0.76 hours/million states
40000	-161177.8739	-14490.6235 	-146687.2504	-2264.02    	1.03794E-2  	2.06425E-2  	7     	0.75 hours/million states
50000	-156148.7586	-14365.5706 	-141783.1880	-2264.02    	1.04656E-2  	1.88379E-2  	7     	0.75 hours/million states
60000	-153465.2824	-14718.5749 	-138746.7075	-2264.10    	1.06338E-2  	1.60912E-2  	7     	0.75 hours/million states
70000	-150081.4590	-14587.8872 	-135493.5718	-2264.08    	1.05695E-2  	1.612E-2    	7     	0.74 hours/million states
80000	-147770.4406	-14527.0495 	-133243.3911	-2264.02    	1.10913E-2  	1.58052E-2  	7     	0.74 hours/million states
90000	-145135.2284	-14799.5236 	-130335.7048	-2264.00    	1.11175E-2  	1.34076E-2  	8     	0.74 hours/million states
100000	-142735.7829	-14412.2425 	-128323.5405	-2264.00    	1.10069E-2  	1.48357E-2  	7     	0.74 hours/million states
110000	-141060.4134	-14745.8559 	-126314.5575	-2264.00    	1.0952E-2   	1.72609E-2  	7     	0.74 hours/million states
120000	-139065.4518	-14239.1267 	-124826.3251	-2264.00    	1.08708E-2  	1.47872E-2  	7     	0.75 hours/million states
130000	-137406.4308	-14086.3737 	-123320.0571	-2264.00    	1.07647E-2  	1.32871E-2  	6     	0.75 hours/million states
140000	-136058.0668	-14462.4837 	-121595.5831	-2264.00    	1.07048E-2  	1.50984E-2  	6     	0.75 hours/million states
150000	-135562.9157	-14659.1750 	-120903.7407	-2264.00    	1.09785E-2  	1.24508E-2  	6     	0.74 hours/million states
160000	-134556.7765	-14681.3072 	-119875.4693	-2264.00    	1.10006E-2  	1.39336E-2  	6     	0.74 hours/million states
170000	-133578.7030	-14539.8084 	-119038.8947	-2264.00    	1.11523E-2  	1.27087E-2  	6     	0.74 hours/million states
180000	-133146.1957	-14605.5257 	-118540.6699	-2264.00    	1.11796E-2  	1.22055E-2  	6     	0.74 hours/million states
190000	-132754.0806	-14802.2693 	-117951.8113	-2264.00    	1.11578E-2  	1.23338E-2  	6     	0.74 hours/million states
200000	-131521.0417	-14341.7275 	-117179.3142	-2264.23    	1.09399E-2  	1.29654E-2  	7     	0.74 hours/million states
```

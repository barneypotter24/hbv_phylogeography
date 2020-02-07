# HBV-A Phylogeography with HMC and Updated Locations

# Beast run1-2019-11-20

Started on 20 November 2019 as a CPU replicate of the HBV-A phylogeography analysis.

Using BEAST version 1.10.5pre and BEAGLE CPU.

```bash
beast1.10.5pre -beagle_cpu -overwrite -seed 666 -save_every 100000 -save_state checkpoint.state HBV-A_ancientDNA_skyride_geo.xml
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


Random number seed: 666


Loading additional development parsers from development_parsers.properties, which is additional set of parsers only available for development version ...

Parsing XML file: HBV-A_ancientDNA_skyride_geo.xml
File encoding: UTF8
Looking for plugins in /home/luna.kuleuven.be/r0787607/projects/hbv_phylogeography/beast_files/a/run1-skyride-2019-11-20/plugins

Read alignment: alignment
Sequences = 587
Sites = 3222
Datatype = nucleotide
Site patterns 'patterns' created from positions 1-3222 of alignment 'alignment'
unique pattern count = 1937
Read attribute patterns, 'location.pattern' for attribute, location

Creating the tree model, 'treeModel'
taxon count = 587
tree height = 4279.361568160566
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
# Generated Wed Nov 20 10:50:44 CET 2019 [seed=666]
# -beagle_cpu -overwrite -seed 666 -save_every 100000 -save_state checkpoint.state HBV-A_ancientDNA_skyride_geo.xml
# keywords: skyride discretized_branch_rates
state	Joint       	Prior       	Likelihood  	age(root)   	default.ucld.meanlocation.clock.rate	location.nonZeroRates
0	-2148183.9672	-43762.4472 	-2104421.5200	-2265.36    	1.00000     	1.00000     	10    	-
10000	-210772.9894	-14662.6656 	-196110.3238	-2363.85    	6.05582E-3  	2.22136E-2  	6     	-
20000	-184170.2975	-14580.5592 	-169589.7383	-2340.29    	5.83806E-3  	1.71586E-2  	6     	0.79 hours/million states
30000	-172550.9237	-14744.3664 	-157806.5573	-2340.78    	6.42146E-3  	1.63771E-2  	6     	0.78 hours/million states
40000	-164533.8263	-14915.9484 	-149617.8779	-2341.48    	6.93798E-3  	1.34158E-2  	6     	0.78 hours/million states
50000	-158622.6809	-14768.6425 	-143854.0384	-2339.47    	7.12751E-3  	1.5683E-2   	6     	0.77 hours/million states
60000	-154688.9487	-14997.6442 	-139691.3045	-2342.76    	7.26962E-3  	1.37828E-2  	6     	0.78 hours/million states
70000	-152125.1905	-14982.2955 	-137142.8950	-2345.29    	7.39618E-3  	1.35682E-2  	5     	0.78 hours/million states
80000	-149231.5571	-14712.5946 	-134518.9625	-2346.07    	7.55639E-3  	1.36349E-2  	6     	0.78 hours/million states
90000	-147525.9306	-14858.8138 	-132667.1168	-2344.24    	7.38631E-3  	1.55511E-2  	6     	0.79 hours/million states
100000	-145174.3453	-14592.8922 	-130581.4532	-2346.45    	7.45138E-3  	1.38222E-2  	6     	0.79 hours/million states
110000	-142690.1099	-14698.8348 	-127991.2751	-2343.16    	7.38288E-3  	1.36913E-2  	6     	0.8 hours/million states
120000	-140339.5989	-14806.1268 	-125533.4721	-2344.86    	7.42931E-3  	1.34562E-2  	6     	0.8 hours/million states
130000	-138468.4688	-14683.6353 	-123784.8335	-2343.71    	7.41454E-3  	1.2447E-2   	6     	0.79 hours/million states
140000	-137616.1875	-14705.9987 	-122910.1888	-2344.27    	7.34812E-3  	1.54299E-2  	6     	0.79 hours/million states
150000	-135846.4450	-14728.0959 	-121118.3490	-2343.64    	7.58637E-3  	1.58686E-2  	6     	0.79 hours/million states
160000	-134231.8927	-14696.3563 	-119535.5364	-2344.33    	7.56155E-3  	1.3326E-2   	7     	0.79 hours/million states
170000	-133786.2864	-14722.3525 	-119063.9339	-2341.60    	7.52274E-3  	1.37579E-2  	6     	0.79 hours/million states
180000	-132921.1367	-14840.8780 	-118080.2587	-2344.79    	7.30047E-3  	1.04802E-2  	6     	0.79 hours/million states
190000	-131384.7401	-14453.3920 	-116931.3481	-2341.64    	7.31253E-3  	1.10905E-2  	8     	0.79 hours/million states
200000	-130092.8411	-14177.6911 	-115915.1500	-2341.14    	7.05915E-3  	1.19113E-2  	7     	0.79 hours/million states
210000	-129163.8136	-14587.8150 	-114575.9987	-2338.69    	6.96236E-3  	1.1647E-2   	6     	0.79 hours/million states
220000	-128364.3182	-14558.3030 	-113806.0152	-2338.94    	6.95297E-3  	1.02263E-2  	6     	0.79 hours/million states
```

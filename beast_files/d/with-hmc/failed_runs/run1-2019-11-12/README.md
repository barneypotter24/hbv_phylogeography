# HBV-D Phylogeography with HMC and Updated Locations

# Beast run1-2019-11-12

Started on 12 November 2019 as a CPU replicate of the HBV-D phylogeography analysis.

This run has removed the ancestral node date estimation that was present in the prior runs, which all failed with an identical message.

```bash
java   -jar ~/IdeaProjects/beast-mcmc/build/dist/beast.jar   -beagle_cpu   -overwrite   -seed 666   -save_every 100000   -save_state checkpoint.state   HBV-D_ancientDNA_HMCskygrid_geo.xml
```
```
java   -jar ~/IdeaProjects/beast-mcmc/build/dist/beast.jar   -beagle_cpu   -overwrite   -seed 666   -save_every 100000   -save_state checkpoint.state   HBV-D_ancientDNA_HMCskygrid_geo.xml

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



Failed to load parser: dr.inference.trace.DnDsPerSiteAnalysis
line = dr.inference.trace.DnDsPerSiteAnalysis


Failed to load parser: dr.inference.trace.CnCsPerSiteAnalysis
line = dr.inference.trace.CnCsPerSiteAnalysis


Failed to load parser: dr.inference.trace.CnCsToDnDsPerSiteAnalysis
line = dr.inference.trace.CnCsToDnDsPerSiteAnalysis

Loading additional development parsers from development_parsers.properties, which is additional set of parsers only available for development version ...

Parsing XML file: HBV-D_ancientDNA_HMCskygrid_geo.xml
  File encoding: UTF8
Looking for plugins in /home/luna.kuleuven.be/r0787607/projects/grad_school/HBV-Phylogeography/beast_files/d/with-hmc/run1-2019-11-12/plugins

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
Creating a GMRF smoothed skyride model for multiple loci (SkyGrid)
	Population sizes: 50
skygrid(-31890.455306481817).logPopulationSizes
Gradient
analytic: [ 29570.335854317385, 379.6210410437168, 95.5405841521826, 2.190804879327777, 0.0, 0.0, 0.0, 0.0, 0.0, 0.6547317199151561, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 15.758754020793024, 17.267810503965666, 17.267810503965624, 17.26781050396571, 17.267810503965666, 17.26781050396558, 3.552043149410575, 17.267810503965666, 17.267810503965666, 17.267810503965666, 9.703642847703275, 0.0, 0.0, 0.0, 0.0, 0.0, 0.683204676461262, 17.267810503965666, 3.3193041940648325, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.252323109212902, 13.991402557587795, 0.0, 0.0]
numeric : [ 29570.335815429688, 379.62103271484375, 95.54058837890625, 2.1907958984375, 0.0, 0.0, 0.0, 0.0, 0.0, 0.65472412109375, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 15.7587890625, 17.267822265625, 17.267822265625, 17.267822265625, 17.267822265625, 17.267822265625, 3.55206298828125, 17.267822265625, 17.267822265625, 17.267822265625, 9.70361328125, 0.0, 0.0, 0.0, 0.0, 0.0, 0.6832275390625, 17.267822265625, 3.3193359375, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.2523193359375, 13.99139404296875, 0.0, 0.0]
Hessian
analytic: [ -30323.435854317384, -384.8210410437168, -99.7405841521826, -3.390804879327777, -0.2, -0.2, -0.2, -0.2, -0.2, -1.854731719915156, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -15.958754020793023, -17.467810503965666, -17.467810503965623, -17.46781050396571, -17.467810503965666, -17.46781050396558, -4.752043149410575, -17.467810503965666, -17.467810503965666, -17.467810503965666, -10.903642847703274, -0.2, -0.2, -0.2, -0.2, -0.2, -0.883204676461262, -17.467810503965666, -4.519304194064833, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -2.452323109212902, -15.191402557587795, -0.2, -0.1]
numeric : [ -30323.436155550182, -384.82104486459866, -99.74058514105855, -3.390804911025043, -0.2, -0.2, -0.2, -0.2, -0.2, -1.8547317363531874, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -15.95875417733987, -17.467810675501823, -17.467810675501823, -17.4678106755091, -17.467810675501823, -17.467810675501823, -4.752043194632279, -17.467810675501823, -17.467810675501823, -17.467810675501823, -10.903642954031966, -0.2, -0.2, -0.2, -0.2, -0.2, -0.8832046832483229, -17.467810675501823, -4.519304236973767, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -2.452323131588855, -15.191402706510416, -0.2, -0.1]

skygrid(-31890.455306481817).precision
Gradient
analytic: [ 245.0]
numeric : [ 244.99999999999997]
Hessian
analytic: [ -2449.9999999999995]
numeric : [ -2450.004417457279]

compoundGradient.hmc
Gradient
analytic: [ 235.00900000000001, 29570.335854317385, 379.6210410437168, 95.5405841521826, 2.190804879327777, 0.0, 0.0, 0.0, 0.0, 0.0, 0.6547317199151561, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 15.758754020793024, 17.267810503965666, 17.267810503965624, 17.26781050396571, 17.267810503965666, 17.26781050396558, 3.552043149410575, 17.267810503965666, 17.267810503965666, 17.267810503965666, 9.703642847703275, 0.0, 0.0, 0.0, 0.0, 0.0, 0.683204676461262, 17.267810503965666, 3.3193041940648325, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.252323109212902, 13.991402557587795, 0.0, 0.0]
numeric : [ 235.00898881392044, 29570.335815429688, 379.62103271484375, 95.54058837890625, 2.1907958984375, 0.0, 0.0, 0.0, 0.0, 0.0, 0.65472412109375, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 15.7587890625, 17.267822265625, 17.267822265625, 17.267822265625, 17.267822265625, 17.267822265625, 3.55206298828125, 17.267822265625, 17.267822265625, 17.267822265625, 9.70361328125, 0.0, 0.0, 0.0, 0.0, 0.0, 0.6832275390625, 17.267822265625, 3.3193359375, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.2523193359375, 13.99139404296875, 0.0, 0.0]


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
    with instance flags:  PRECISION_DOUBLE COMPUTATION_SYNCH EIGEN_REAL SCALING_MANUAL SCALERS_RAW VECTOR_SSE THREADING_CPP PROCESSOR_CPU FRAMEWORK_CPU PREORDER_TRANSPOSE_MANUAL
  Ignoring preOrder partials in tree likelihood.
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
    with instance flags:  PRECISION_DOUBLE COMPUTATION_SYNCH EIGEN_REAL SCALING_MANUAL SCALERS_RAW VECTOR_NONE THREADING_CPP PROCESSOR_CPU FRAMEWORK_CPU PREORDER_TRANSPOSE_MANUAL
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
WARNING: Likelihood component, skygrid.precision.prior, created but not used in the MCMC
WARNING: Likelihood component, null, created but not used in the MCMC
Underflow calculating likelihood. Attempting a rescaling...
Underflow calculating likelihood. Attempting a rescaling... (patterns)

Citations for this analysis:

FRAMEWORK
BEAST primary citation:
	Suchard MA, Lemey P, Baele G, Ayres DL, Drummond AJ, Rambaut A (2018) Bayesian phylogenetic and phylodynamic data integration using BEAST 1.10. Virus Evolution. vey016. DOI:10.1093/ve/vey016
BEAGLE likelihood calculation library:
	Ayres et al  (2012) BEAGLE: a common application programming inferface and high-performance computing library for statistical phylogenetics. Syst Biol. 61, 170-173. DOI:10.1093/sysbio/syr100
Using BEAGLE likelihood calculation library:
	Ayres et al  (2012) BEAGLE: a common application programming inferface and high-performance computing library for statistical phylogenetics. Syst Biol. 61, 170-173. DOI:10.1093/sysbio/syr100

TREE DENSITY MODELS
Skygrid coalescent:
	Gill MS, Lemey P, Faria NR, Rambaut A, Shapiro B, Suchard MA (2013) Improving Bayesian population dynamics inference: a coalescent-based model for multiple loci. Mol Biol Evol. 30, 713-724
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


# BEAST v1.10.5 Prerelease #23570d1
# Generated Tue Nov 12 13:48:20 CET 2019 [seed=666]
# -beagle_cpu -overwrite -seed 666 -save_every 100000 -save_state checkpoint.state HBV-D_ancientDNA_HMCskygrid_geo.xml
# keywords: skygrid discretized_branch_rates

```

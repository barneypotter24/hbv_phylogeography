#!/bin/bash
#SBATCH --clusters=genius
#SBATCH --account="lp_phylogeo_inf_gpu"
#SBATCH --chdir="/data/leuven/332/vsc33218/hbv_phylogeography/phylogeography/e/HBV-E_updated_geo_priors"
#SBATCH --mail-type="END,FAIL,TIME_LIMIT"
#SBATCH --mail-user="barneyisaksen.potter@kuleuven.be"
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --partition=batch
#SBATCH --time="24:00:00"

####################################
##### Run a beast analysis ######
####################################

#### How to run: ####
# sbatch --export=ALL,ARGS='' gpu_example.slurm

# write a function that catches any errors
abort()
{
    echo >&2 '
***************
*** ABORTED ***
***************
'
    echo "An error occurred. Exiting..." >&2
    exit 1
}

set -e
trap 'abort' 0

# activate the appropriate conda environment
module purge
module load cluster/genius/batch
module load Java/13.0.2

export BEAGLE_LIB=$HOME/lib/:/apps/leuven/skylake/2018a/software/GCCcore/6.4.0/lib64/
export LD_LIBRARY_PATH=$BEAGLE_LIB

# write some cluster metadata to the error and output files
hostname >&2
echo $0 >&2
printf START >&2; uptime >&2
date >&2

# run the analysis,
java -jar $VSC_HOME/beast_hmc-clock.jar -beagle_double HBV-E_updated_geo_priors_completeHistory_posterior_run2.xml

# write some cluster metadata to the error and output files
printf END >&2; uptime >&2

trap : 0

echo >&2 '
************
*** DONE ***
************
'

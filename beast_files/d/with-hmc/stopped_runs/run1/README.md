# HBV-D Phylogeography with HMC and Updated Locations

# Beast run1

Started on 6 November 2019 to test if my addition of the HMC portion of the XML.
Run from the `hmc-clock` branch of `beast-mcmc` using IntelliJ.
The following command was copied from the IntelliJ stdout window.

```bash
/usr/lib/jvm/java-1.11.0-openjdk-amd64/bin/java \
  -Dparsers=development \
  -javaagent:/home/luna.kuleuven.be/r0787607/Tools/idea-IC-192.6817.14/lib/idea_rt.jar=40297:/home/luna.kuleuven.be/r0787607/Tools/idea-IC-192.6817.14/bin \
  -Dfile.encoding=UTF-8 \
  -classpath /home/luna.kuleuven.be/r0787607/projects/beast-mcmc/out/production/beast-mcmc:/home/luna.kuleuven.be/r0787607/projects/beast-mcmc/lib/colt.jar:/home/luna.kuleuven.be/r0787607/projects/beast-mcmc/lib/mtj.jar:/home/luna.kuleuven.be/r0787607/projects/beast-mcmc/lib/freemarker.jar:/home/luna.kuleuven.be/r0787607/projects/beast-mcmc/lib/figtreepanel.jar:/home/luna.kuleuven.be/r0787607/projects/beast-mcmc/lib/jdom.jar:/home/luna.kuleuven.be/r0787607/projects/beast-mcmc/lib/javax.json.jar:/home/luna.kuleuven.be/r0787607/projects/beast-mcmc/lib/lbfgs4j-0.2.1.jar:/home/luna.kuleuven.be/r0787607/projects/beast-mcmc/lib/beagle.jar:/home/luna.kuleuven.be/r0787607/projects/beast-mcmc/lib/jebl.jar:/home/luna.kuleuven.be/r0787607/projects/beast-mcmc/lib/EJML-core-0.30.jar:/home/luna.kuleuven.be/r0787607/projects/beast-mcmc/lib/jam.jar:/home/luna.kuleuven.be/r0787607/projects/beast-mcmc/lib/commons-cli-1.4.jar:/home/luna.kuleuven.be/r0787607/projects/beast-mcmc/lib/junit-4.4.jar:/home/luna.kuleuven.be/r0787607/projects/beast-mcmc/lib/org.boehn.kmlframework_20090320.jar:/home/luna.kuleuven.be/r0787607/projects/beast-mcmc/lib/itext-1.4.5.jar:/home/luna.kuleuven.be/r0787607/projects/beast-mcmc/lib/EJML-dense64-0.30.jar:/home/luna.kuleuven.be/r0787607/projects/beast-mcmc/lib/commons-math-2.2.jar:/home/luna.kuleuven.be/r0787607/projects/beast-mcmc/lib/mpj.jar:/home/luna.kuleuven.be/r0787607/projects/beast-mcmc/lib/JRI.jar:/home/luna.kuleuven.be/r0787607/projects/beast-mcmc/lib/options.jar:/home/luna.kuleuven.be/r0787607/projects/beast-mcmc/release_phylogeography/common/lib/phylogeography.jar dr.app.beast.BeastMain \
  -beagle_gpu \
  -overwrite \
  -seed 666 \
  -save_every 100000 \
  -save_state checkpoint.state \
  /home/luna.kuleuven.be/r0787607/projects/grad_school/HBV-Phylogeography/beast_files/d/with-hmc/run1/HBV-D_ancientDNA_HMCskygrid_geo.xml
```

After 80,000 states it seems to be running correctly.
Sitting at around 1.5 hours/million states.
I am stopping the run to install a UPS, then restarting with the above command from the terminal.


## Creating a new BEAST build from IntelliJ
1. View -> Tool Windows -> ANT
2. Hit `+` and navigate to `~/IdeaProjects/beast-mcmc/build.xml` which creates a BEAST option
3. Right click that option and it Run Build
4. Wait until it successfully completes; the jar file is in `~/IdeaProjects/beast-mcmc/build/dist`.
5. Run using that.

E.g.(from the correct working directory)
```bash
java \
  -jar ~/IdeaProjects/beast-mcmc/build/dist/beast.jar \
  -beagle_gpu \
  -overwrite \
  -seed 666 \
  -save_every 100000 \
  -save_state checkpoint.state \
  HBV-D_ancientDNA_HMCskygrid_geo.xml
```

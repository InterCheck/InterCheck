# Reproducibility Package for EMSOFT '25 Submission #39

This repository contains the code, benchmark instances,  executables and instructions to reproduce the experimental results in submission #39 to EMSOFT '25.



## Environment

All experiments in the paper are conducted on a workstation (Intel Core i5-12500 CPU 3.4GHz, 16 GB RAM, and UBUNTU 20.04). The time limit for experiments is set to 1000 s, and the memory usage limit is set to 4 GB. Note that cases where time limit is exceed will be recorded as out of time ('OOT'), and cases where memory limit is exceed will be recorded as out of memory ('OOM').
All experiments will take about 5 hours.

Finally, please note that the executables provided here are available solely for the purpose of reproducing the experiments of the above paper.



## Instructions

For reproducing the results of the paper, the script "run.py" should be run *FROM this directory* using the command::

```
python3 run.py
```

Before running run.py you have to make sure "Python" and "runlim" are installed.
If not, use the following command to install:

```
sudo apt-get install runlim python3
```



## Directory Structure 

The directory structure is as follows:

```
InterCheck 
    the executable of our CLHA bounded reachability checker, InterCheck

lib/
    contains the library files needed to run InterCheck

benchmarks/
    contains the benchmark instances for CLHA in SpaceEx formats

run.py 
    the script to run the experiment

results/ 
    the output directory with experimental results of running the benchmarks, including both reachable and unreachable cases
```




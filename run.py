import os
import os.path
import sys

current_directory = os.getcwd()
os.environ['LD_LIBRARY_PATH'] += os.pathsep + current_directory + '/lib'

cmd = "cd benchmarks/svbenchmarks; python3 run.py "
print(cmd)
os.system(cmd)
os.system("cp -f benchmarks/svbenchmarks/result/*_result.txt results/")

cmd = "cd benchmarks/slbenchmarks; python3 run.py "
print(cmd)
os.system(cmd)
os.system("cp -f benchmarks/slbenchmarks/result/*_result.txt results/")
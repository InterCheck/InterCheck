import os
import os.path
import time

timelimit = 1000
runlim	= '''runlim -s 4096 -t ''' +str(timelimit)+''' -r '''+str(timelimit)
intercheck	= ''' ../../InterCheck -t -p -solver cmsat '''
resultdir = "result/"

def mkdir(path):
	folder = os.path.exists(path)
	if not folder:
		os.makedirs(path)
		print("new folder "+path)

def test(benchmarkname, benchmarkpath, size ,flagmap):
	res={}
	for flag in flagmap:
		cost = []
		occ = False
		for i, _n in size:
			if occ:
				cost.append(timelimit)
				continue

			stri = str(i)
			model_name = benchmarkname+stri
			n = str(_n)
			runlimdir = resultdir+benchmarkpath
			runlimlog = runlimdir+model_name+"_"+n+"_"+flag+".runlim"
			logdir = runlimdir+'''log/'''
			logname = logdir+model_name+"_"+n+"_"+flag+".log"
			model_path = benchmarkpath+model_name
		
			mkdir(runlimdir)
			mkdir(logdir)
			
			cmd = runlim+" -o "+runlimlog+intercheck+flagmap[flag]+model_path+".xml "+model_path+".cfg "+n+" > "+logname
			print (cmd)
			t = time.time()

			rtn = os.system(cmd)
			t = time.time() - t
			if t > 0.95*timelimit:
				occ = True
			if rtn != 0:
				t = timelimit
				print("----------------------------------")
			cost.append(t)
			
			
		res[flag] = cost

	with open(resultdir+benchmarkname+"_result.txt","a") as f:
		f.write(benchmarkpath+"\n")
		f.write("Number of Components:\n")
		for i,n in size:
			f.write(str(i)+",")
		f.write("\n")
		f.write("Bound:\n")
		for i,n in size:
			f.write(str(n)+",")
		f.write("\n")
		for flag in flagmap:
			f.write("Time cost of ")
			f.write(flag)
			f.write(" (s):\n")
			for t in res[flag]:
				if t > 0.999 * timelimit:
					f.write("OOT")
					f.write(",")
				else:
					f.write(str(round(t,2)))
					f.write(",")
			f.write("\n\n")
		f.write("-----------------------------------------------------------\n")

os.system("rm -f " + resultdir+"*_result.txt")

dic = {'InterCheck': ' -interaction -nspread ',  'InterCheck-trg': ' -trg -nspread '}

map=[]
for i in [2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20]:
	map.append((i, 6))
test("lynch_", '''Lynch/unreachable/''', map, dic)
test("lynch_", '''Lynch/reachable/''', map, dic)

map=[]
for i in [2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20]:
	map.append((i, 2))
test("acc_", '''ACC/unreachable/''', map, dic)
test("acc_", '''ACC/reachable/''', map, dic)

map=[]
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
	map.append((i, 7))
test("ETCS_", '''ETCS/reachable/''', map, dic)

map=[]
for i in [1, 2, 3, 4, 5, 6]:
	map.append((i, 10))
test("ETCS_", '''ETCS/unreachable/''', map, dic)

map=[]
for i in [2, 3, 4, 5, 6, 7, 8]:
	map.append((i, 6))
test("fischer_", '''fischer/unreachable/''', map, dic)
test("fischer_", '''fischer/reachable/''', map, dic)

map=[]
for i in [3,4,5,6,7,8,9,10,11,12]:
	map.append((i, 13))
test("fischer_ring_", '''fischer_ring/unreachable/''', map, dic)
test("fischer_ring_", '''fischer_ring/reachable/''', map, dic)

map=[]
for i in [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]:
	map.append((i, 2))
test("temp_", '''temperature/unreachable/''', map, dic)
test("temp_", '''temperature/reachable/''', map, dic)

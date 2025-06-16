import os
import os.path
import time

timelimit = 1000
runlim	= '''runlim -s 4096 -t ''' +str(timelimit)+''' -r '''+str(timelimit)
intercheck	= ''' ../../InterCheck -t -p -v2 -solver cmsat '''
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
			if rtn != 0:
				t = timelimit
				print("-------------------------------")
			cost.append(t)
			if t > 0.99*timelimit:
				occ = True
			
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

dic = {'InterCheck': ' -interaction -nspread ', 'InterCheck-trg': ' -trg -nspread '}

map=[]
for i in [2, 4, 6, 8, 10, 15, 20, 25, 30, 35, 40, 45, 50]:
	map.append((i, 2))

test("FDDI_", '''case/FDDI/reachable/''', map, dic)
test("FDDI_", '''case/FDDI/unreachable/''', map, dic)

map=[]
for i in [2, 3, 4, 6, 8, 10, 12, 14, 16, 18, 20]:
	map.append((i, 7))

test("motorcycle_", '''case/motorcycle/reachable/''', map, dic)

map=[]
for i in [2, 4, 6, 8, 10, 12, 14]:
	map.append((i, 7))

test("motorcycle_", '''case/motorcycle/unreachable/''', map, dic)

map=[]
for i in [2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20, 25, 30]:
	map.append((i, 2*i))

test("NRS_", '''case/NRS/reachable/''', map, dic)

map=[]
for i in [2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25]:
	map.append((i, 2*i))

test("NRS_", '''case/NRS/unreachable/''', map, dic)
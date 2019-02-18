"""Genetic Algorithm implementation to find proofs for Reo connectors
get_Fitness is for the fitness function
display is for the display
uco= uniform crossover
spc = single point crossover
mpc = multi point crossover
mutate = standard mutation operator
pimutate =  pairwise interchange mutation
PVS proof steps from which initial population is generated is included in guru99.txt
txt.txt file contains the proof steps for theorem and lemmas for the properties of Reo connectors in PVS
crossover operators works by randomly generating child solutions and then perform the crossover operation to obtain parent solution
parent solution then goes through mutation operator.  """

import random
import statistics
import time
import gc
import psutil
import numpy

def Fitness(guess):
    fitness = 0
    for i in range(len(guess)):
        if guess[i] == proof[i]:
            fitness+=1
    return fitness


def Results(guess, timings):
    timeD = time.time() - sTime
    fit = Fitness(guess)
    print(guess, fit, timeD)
    timings.append(timeD)
    #return timings[-1]

def uco(i1, i2, prob):
#    g1 = []
#    g2 = []
#    while len(g1) < length:
#        sSize = min(length - len(g1), len(gSet))
#        g1.extend(random.sample(gSet, sSize))
#    g2.extend(random.sample(gSet, sSize))
#    print(g1)
#    print(g2)
#   i1 = list(g1)
#    i2 = list(g2)
    size = min(len(i1), len(i2))
    for i in range(size):
        if random.random() < prob:
            i1[i], i2[i] = i2[i], i1[i]
    if Fitness(i1) > Fitness(i2):
        return (i1, Fitness(i1))
    else:
        return (i2, Fitness(i2))


def spc(i1, i2):
    #g1 = []  #g2 = [] #while len(g1) < length: #    sSize = min(length - len(g1), len(gSet)) #    g1.extend(random.sample(gSet, sSize)) #    g2.extend(random.sample(gSet, sSize))
    #i1= list(g1) #i2 = list(g2)
    #print("PARENT 1:", i1)
    #print("PARENT 2:", i2)
    size = min(len(i1), len(i2))
    cop = random.randint(1, size - 1)
    i1[cop:], i2[cop:] = i2[cop:], i1[cop:]
    #print("First Child", i1)
    #print("Seoond Second Child", i2)
    if Fitness(i1) > Fitness(i2):
        return (i1, Fitness(i1))
    else:
        return (i2, Fitness(i2))


def mpc(i1, i2):
    #print("MPC")
    size = min(len(i1), len(i2))
    cop1 = random.randint(1, size)
    cop2 = random.randint(1, size - 1)
    if cop1 > cop2:
        m = cop1
        cop1 = cop2
        cop2 = m
    if cop1 != cop2:
            #cop1, cop2 = cop2, cop1
        i1[cop1:cop2], i2[cop1:cop2] = i2[cop1:cop2], i1[cop1:cop2]
    if Fitness(i1) > Fitness(i2):
        return (i1, Fitness(i1))
    else:
        return (i2, Fitness(i2))


def mutate(parent):
    #print("Muttion PARENT :", parent)
    #print("PARENT 2:", i2)
    ind = random.randint(0, len(parent) - 1)
    cGenes = list(parent)
    ng, alter = random.sample(gSet, 2) #print("DFGH", nGene, alter) #x = []#while nGene == cGenes[ind]:
    if ng == cGenes[ind]:
        cGenes[ind] = alter
    #print("Muated:", cGenes)
    ite.append(+1)
    z1 = len(ite)
    print("ITER:", z1) #print("CHILD:", cGenes)
    return (cGenes)



def pmutate(parent):
    ind1 = random.randint(0, len(parent) -1)
    ind2 = random.randint(0, len(parent) - 1)
    cGenes = list(parent)
    #print(cGenes)
    idx= range(len(cGenes))
    nGene, alter = random.sample(gSet, 2)
    cGenes[ind1] = nGene
    cGenes[ind2] = alter
    #print("Mut", cGenes)
    ite.append(+1)
    z1 = len(ite)
    #print("PRINT PIM:", cGenes)
    print("ITER:", z1) #print("CHILD:", cGenes)
    return (cGenes)


def pimutate(targe):
    g1 =[]
    target = list(targe)
    cxp1 = random.randint(0, len(targe) - 1)
    cxp2 = random.randint(0, len(targe) - 1)
    if cxp2 >= cxp1:
        cxp2 += 1
    else:  # Swap the two cx points
        cxp1, cxp2 = cxp2, cxp1
    #    i1[cop1:cop2], i2[cop1:cop2] \ #    = i2[cop1:cop2], i1[cop1:cop2]#if cxp1 > cxp2:#    m = cxp1 #    cxp1 = cxp2#    cxp2 = m # y = abs(cxp1-cxp2)# while len(g1) < len(y):  #     sSize = min(len(y) - len(g1), len(gSet))   #     g1.extend(random.sample(gSet, sSize))   # g2.extend(random.sample(gSet, sSize))   # i1= list(g1)   # i2 = list(g2)    #print(y)    #print(cxp2)
    if cxp1 != cxp2:
            sublist = target[cxp1:cxp2]
            sublist.reverse()
            target[cxp1:cxp2] = sublist
            ite.append(+1)
            z1 = len(ite)
            #print("ITER:", z1)#   print("FINAL:", target)
    return (target)


#pid = psutil.Process(os.getpgid())
#print(pid.memory_info().rss)# str(os.getpgid())
#status = os.system('cat /proc' +pid + 'status')
#print(status)
random.seed()
#pst = time.time()
timee = time.process_time()
fits = []
lastt = []

ite = []
with open("guru99.txt", 'r') as f:
    p = f.read()
    gSet = p.split()

with open("proofs.txt", 'r') as f:
    for line in f:
        timee += timee
        timings = []
        for i in range(1):
            proof = line.split()
            length = len(proof)
            sTime = time.time()
            g1 = []
            g2 = []

            while len(g1) < len(proof):
                sSize = min(length - len(g1), len(gSet))
                g1.extend(random.sample(gSet, sSize))
                g2.extend(random.sample(gSet, sSize))
                i1 = list(g1)
                i2 = list(g2)

                leni1 = sum(1 for exp, act in zip(proof, i1)
                    if exp == act)

                leni2 = sum(1 for exp, act in zip(proof, i1)
                           if exp == act)
                #print(i1)
                #print(i2)
                #print(proof)
                #print(len1)
                #print(len2)
                if leni1 == len(proof): #i in (Fitness(i1), Fitness(proof)):
                   bParent = i1
                   bFitness = Fitness(i1)
                elif leni2 == len(proof): #in (Fitness(i2), Fitness(proof)):
                    bParent = i2
                    bFitness = Fitness(i2)
                else:
                    #print("PARENT 1:", i1)
                    #print("PARENT 2:", i2)
                    sTime = time.time()
                    bParent, bFitness = spc(i1, i2)
                    #bParent, bFitness = uco(i1, i2, 0.5)
                #    #bestFitness = get_fitness(bestParent)
                    Results(bParent, timings)
                while True:
                    child = mutate(bParent)
                    cFitness = Fitness(child)

                    if bFitness >= cFitness:
                        continue
                    res = Results(child, timings)
                    # print("TIMINGS1:", timings)
                    mea = timings
                    #lt = mea[-1]
                   # print("LT:", mea)
                    #lastt.append(lt)
                    #lasttt = numpy.array(lastt)
                    print("Time:", mea)
                    ##tm = numpy.array(mea)
                    ##abc=numpy.mean(tm)
                    #print("M:", mea)
                    ##mean = statistics.mean(mea)
                    ##print("MeanSta", mean)
                    ##print("MeanNumpy", abc)
                    ##sta= statistics.stdev(timings, mean)
                    ##cba= numpy.std(tm)
                    ##print("Standard DeviationSta:", sta)
                    #print("Standard DeviationNumpy:",cba)
                    ## total = sum(timings)
                    ## print("TTTTTT:", total)
                    #fits.append(cFitness)#fits.append(cFitness)
                    #print("Overall Fitness:", cFitness)
                    ##mem = psutil.virtual_memory()#.total / (1024.0 ** 2)
                    ##print("Memory Used in Mb:", mem.used >> 20)
                    gc.collect()
                    if cFitness >= len(bParent):
                        #print("FITNESS:", cFitness)
                        #print("TIMINGS:", timings)
                        #meas = timings
                        #lt = meas[-1]
                        #print("LT:", lt)
                        #lastt.append(lt)
                        #lasttt = numpy.array(lastt)
                        #print("Time:", lasttt)
                        #xzz = numpy.mean(lasttt)  # , dtype=numpy.float64)
                        #yyz = numpy.std(lasttt)  # statistics.stdev(fitss, mean)
                        #print("SDT is s", yyz, xzz)
                        fits.append(cFitness)
                        fitss = numpy.array(fits)
                        print("FITNESS:", fitss)
                        total = sum(timings)
                        lastt.append(total)
                        lasttt = numpy.array(lastt)
                        print("Time:", lasttt)
                        xzz = numpy.mean(lasttt)  # , dtype=numpy.float64)
                        yyz = numpy.std(lasttt)  # statistics.stdev(fitss, mean)
                        print("SDT and MeanT is:", yyz, xzz)
                        total1 = sum(lasttt)
                        print("Total Time:", total1)
                        #Fit = [2, 10, 3, 4, 8, 8, 3, 12, 10, 13, 11, 23, 25, 16, 5, 19, 11, 16, 23, 26, 3, 4, 14, 8, 8, 5, 6]
                        #yzx = fits.mean
                        #xyz= fitss.std()
                        #print("Mean is ", yzx)
                        #print("SD is ", xyz) # % (fitss.stdev()))
                        xuz= numpy.mean(fitss)#, dtype=numpy.float64)
                        xyz = numpy.std(fitss)# statistics.stdev(fitss, mean)
                        print("SDF and MeanF is:", xuz, xyz)#(statistics.men(fitss)))
                        ##fme = statistics.mean(fits)
                        #print("FITNESSMEAN", fme)
                        #fsta = statistics.stdev(fits, xbar=fme)
                        #print("Standard Deviation fITNeSS:", fsta)
                        mem = psutil.virtual_memory()  # .total / (1024.0 ** 2)
                        print("Memory Used in Mb:", mem.used >> 20)
                        break
                    bFitness = cFitness
                    bParent = child
                    #print("Overall Fitness:", cFitness)#time.process_time() - timee)
                    #total = sum(timings)
                    #print("TTTTTT:", total)
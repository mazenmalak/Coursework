import numpy as np
import matplotlib.pyplot as plt

Nevents=1000 #number of sims
N=np.array([4,8,16,32,64,128,256,512,1024]) #number of events per sim
prob=0.5   #probability of heads

all_events_av=np.zeros(N.size)      #for each N
all_events_var=np.zeros(N.size)     #  ^^^
all_events_stderr=np.zeros(N.size)  #  ^^^

for x in range(N.size):
    ind=N[x]                        
    av=0
    var=0
    stderr=0
    for i in range(Nevents):
        current_run=0               ##assumed heads
        current_run_tails=0         ##tails
        longest_run=0           
        for j in range(ind):
            if(np.random.random()<prob):    # if heads
                current_run+=1
                if(current_run_tails>=longest_run): #has longest run of heads or been beat?
                    longest_run=current_run_tails
                current_run_tails=0         #reset tails run
            else:                           #if tails
                current_run_tails+=1        
                if(current_run>=longest_run):
                    longest_run=current_run
                current_run=0               #reset heads run
        av+=longest_run
        var+=longest_run**2
    av/=Nevents
    var/=Nevents
    var=(var-av**2)
    all_events_av[x]=av
    all_events_var[x]=var
    all_events_stderr[x]=np.sqrt(var/Nevents)


predicted=np.array([np.log2(k) for k in N])
plt.errorbar(N, all_events_av, yerr=all_events_stderr, fmt='.', color="r")
plt.plot(N, predicted)
plt.xlabel("N")
plt.ylabel("n=average # of consecutiver heads or tails")
plt.title("prediction versus simmulated longest run")
plt.legend(['Predicted', 'Simmulated'], loc="best")
plt.show()

for i in range(N.size):
    print("For N=", N[i], ": the average longest run is ", all_events_av[i], " and the variance ", all_events_var[i])
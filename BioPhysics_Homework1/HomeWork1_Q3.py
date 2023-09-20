import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as scipy
import ROOT 

#4.11 a)
loaded_array=np.load("londonIncidents.npz")
x=np.zeros(loaded_array['all'].size)
y=np.zeros(loaded_array['all'].size)
for i in range(int(loaded_array['all'].size/2)):
    x[i]=loaded_array['all'][i][0]
    y[i]=loaded_array['all'][i][1]

#plt.scatter(x,y)

x_max=np.max(x)
y_min=np.min(y)
for i in range(int(loaded_array['all'].size/2)):
    x[i]=x_max*np.random.random_sample()
    y[i]=y_min*np.random.random_sample()
plt.scatter(x,y)

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Coordinates from NPZ")

#4.11 b)
spacing=14
N=np.linspace((np.min(x)), (np.max(x)), num=spacing)
M=np.linspace((np.min(y)), (np.max(y)), num=spacing)
for i in range(M.size):
    plt.axhline(y=M[i], color='r', linestyle='-')
    plt.axvline(x=N[i], color='r', linestyle='-')
plt.show()

#4.11 c)
##Create a 2D histogram that bins the quadrents
c1=ROOT.TCanvas()
h2=ROOT.TH2D("h2","h2",N.size,np.min(x), np.max(x), M.size, np.min(y), np.max(y))
for i in range(x.size):
    h2.Fill(x[i],y[i])
h2.Draw("colz")
h2.GetXaxis().SetTitle("X")
h2.GetYaxis().SetTitle("Y")
h2.SetTitle("Counts in each quandrent")
h2.Draw()
c1.Draw()

#get counts per cell
counts=np.zeros(20) ##array will store from 0 - 20 with each index counting how many times l occured
for i in range(1,N.size+1):
    for j in range(1,M.size+1):
        l=int(h2.GetBinContent(i,j))
        counts[l]+=1
print(counts)

#4.11 d) find distributiuon
points=[]
for i in range(counts.size): #count possible l points
    if(counts[i]!=0):           #if 0, this is not possible
        points.append(i)
av=np.sum(points)/len(points)   #get average
std=np.std(points)                      #calculated standard deviation

Gauss=scipy.norm.pdf(points, av, std)   #get gaussian dist

x_calls=np.arange(0,counts.size, 1)
plt.bar(x_calls, counts/(N.size*M.size))    #plot P_est
plt.scatter(points, Gauss, color='r')      #plot Gaussian
plt.xlabel("l=counts of counts per cell")
plt.ylabel("P(l)")
plt.title("4.11.d Different Distributions")
plt.legend(["P_est(l)=Gauss_l(av,l,std)", "P_est(l)=F(l)/NM"], loc="best")
plt.show()





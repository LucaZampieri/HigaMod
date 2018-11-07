##################################
from numpy import *
from numpy import linalg as LA
import numpy as np
from numpy.linalg.linalg import inv
import matplotlib.pyplot as plt
from pylab import cm, clabel, contour, imshow, colorbar, title, show
import os, sys
#################################
archi_full = open('./input/Full2D.out','r')
ptosx = int(archi_full.readline(30))
ptosy = int(archi_full.readline(30))
ptos = ptosx*ptosy

Full = zeros((4,ptos))
xfull = zeros((ptosx))
yfull = zeros((ptosy))
ufemfull = zeros((ptosx,ptosy))

for i in range(ptos):
   	archi_full.read(7)
   	Full[0,i] = archi_full.read(15)
	archi_full.read(5)
	Full[1,i] = archi_full.read(15)
	archi_full.read(5)
	Full[2,i] = archi_full.readline() 
for i in range(ptosy):
         yfull[i]=Full[1,i]
for j in range(ptosx):
        xfull[j]=Full[0,j*ptosy]
for i in range(ptosx):
	ufemfull[i]= Full[2,ptosy*i:ptosy+ptosy*i]
archi_full.close()
Yfull,Xfull = np.meshgrid(yfull,xfull)
##########################################################################

archi_U2d = open('./input/Krpo2D.out','r')
archi_U1d = open('./input/matrice.out','r')
archi_x1d = open('./input/xcoordinate.out','r')
archi_y1d = open('./input/ycoordinate.out','r')
# Convenzione: vengono passati il numero di vertici nelle due direzioni
ptosx2d = int(archi_U2d.readline(30))
ptosy2d = int(archi_U2d.readline(30))
ptos = (ptosx2d)*(ptosy2d)
F = zeros((4,ptos))
# Modifica qui per griglia 1D diversa
ptosx1d = 301
ptosy1d = 100
F1d = zeros((ptosx1d,ptosy1d))
# Per fare il plot fuso assumiamo di utilizzare lo stesso numero di vertici
# nelle direzione Y. Nella direzione x vengono sovrapposti due vertici.
x = zeros(ptosx2d+ptosx1d-1)
y = zeros(ptosy2d)

x1d = zeros(ptosx1d)
y1d = zeros(ptosy1d)

x2d = zeros(ptosx2d)
y2d = zeros(ptosy2d)

ufem1d = zeros((ptosx1d,ptosy1d))
ufem2d = zeros((ptosx2d,ptosy2d))
ufem   = zeros((ptosx2d + ptosx1d - 1,ptosy2d))

# Salvo temporanemante i valori della soluzione 2d
for i in range(ptos):
   	archi_U2d.read(7)
	F[0,i] = archi_U2d.read(13)
	archi_U2d.read(7)
	F[1,i] = archi_U2d.read(13)
	archi_U2d.read(7)
	F[2,i] = archi_U2d.readline() 

# Salvo il pezzo di soluzione 2D nella soluzione totale e in quella solo 2D
for i in range(ptosx2d):
	ufem[i]= F[2,ptosy2d*i:ptosy2d+ptosy2d*i]
	ufem2d[i] = F[2,ptosy2d*i:ptosy2d+ptosy2d*i]

# salvo la soluzione 1d sia in ufem che in ufem1d
for j in range(ptosy1d):
	archi_U1d.read(2)
	for i in range(ptosx1d-3):
		ufem[ptosx2d+i,j] = archi_U1d.read(6)
		ufem1d[i,j] = ufem[ptosx2d+i,j]
		archi_U1d.read(3)
	ufem[ptosx2d+ptosx1d-2,j]=archi_U1d.read(6)
	ufem1d[ptosx1d-1,j]=ufem[ptosx2d+ptosx1d-2,j]
	archi_U1d.readline()


# salvo la mesh in direzione y (prima meta')
for i in range(50):
	archi_y1d.read(1)
#	print(archi_y1d.readline())
	y1d[i]=float(archi_y1d.readline())

# salvo la mesh in direzione y (seconda meta')
for i in range(50):
	archi_y1d.read(2)
	y1d[50+i]=float(archi_y1d.readline()) 

# salvo la mesh in y dal 2D
for i in range(ptosy2d):
	y[i]=F[1,i]

# salvo la mesh in x del 2D in entrambi i posti
for j in range(ptosx2d):
	x[j]=F[0,j*ptosy2d]
	x2d[j]=F[0,j*ptosy2d]

# salvo la mesh in x del 1D in entrambi i posti
for i in range(ptosx1d-1):
	archi_x1d.read(2)
	x[ptosx2d+i]=archi_x1d.readline()

archi_U2d.close()
archi_U1d.close()
archi_x1d.close()
archi_y1d.close()

Y,X = np.meshgrid(y,x)
#########################################################################

archi_x  = open('./input/himo51.out','r')
archi_x1 = open('./input/himo31.out','r')

ptosx = int(archi_x.readline(30))
ptosy = int(archi_x.readline(30))

archi_x1.readline(30);
archi_x1.readline(30);

ptos = ptosx*ptosy

A = zeros((4,ptos))
A1 = zeros((4,ptos))

nos = int(sqrt(ptos))

xx = zeros((ptosx,ptosy))
yy = zeros((ptosx,ptosy))
ua = zeros((ptosx,ptosy))
ua1= zeros((ptosx,ptosy))

for i in range(ptos):
    archi_x.read(7)
    A[0,i] = archi_x.read(15)
    archi_x.read(5)
    A[1,i] = archi_x.read(15)
    archi_x.read(5)
    A[2,i] = archi_x.readline()

for i in range(ptos):
    archi_x1.read(7)
    A1[0,i] = archi_x1.read(15)
    archi_x1.read(5)
    A1[1,i] = archi_x1.read(15)
    archi_x1.read(5)
    A1[2,i] = archi_x1.readline()
      
for i in range(ptosx):
	xx[i] = A[0,ptosy*i:ptosy+ptosy*i]    
	yy[i] = A[1,ptosy*i:ptosy+ptosy*i]
	ua[i] = A[2,ptosy*i:ptosy+ptosy*i]
	ua1[i]= A1[2,ptosy*i:ptosy+ptosy*i]

archi_x.close()
archi_x1.close()
########################################################################

vm=0.05
vM=0.15


CBt=np.linspace(0.0,vM,16)
CB=np.linspace(vm,vM,16)

plt.subplot(4,4,(1,2))
C2=plt.contourf(Xfull,Yfull,ufemfull, CB)
#plt.ylabel('FreeFem++')
plt.colorbar(C2,use_gridspec=True,ticks=CBt[::3])
plt.grid()

#Figura completa
plt.subplot(4,4,(3,4))
C1=plt.contourf(X,Y,ufem,CB)
plt.plot([3,3],[0.0,1.0],color='black',lw=1)
#plt.ylabel('1D-reduced model')
plt.colorbar(C1,use_gridspec=True,ticks=CBt[::3])
plt.grid()

#HiMod53
plt.subplot(4,4,(5,6))
C1=plt.contourf(xx,yy,ua1,CB)
plt.plot([3.,3.],[0.0,1.0],color='black',lw=1)
#plt.ylabel('HiMod, m=3,1')
plt.colorbar(C1,use_gridspec=True,ticks=CBt[::3])
plt.grid()

#HiMod51
plt.subplot(4,4,(7,8))
C1=plt.contourf(xx,yy,ua,CB)
plt.plot([3.,3.],[0.0,1.0],color='black',lw=1)
#plt.ylabel('HiMod, m=5,1')
plt.colorbar(C1,use_gridspec=True,ticks=CBt[::3])
plt.grid()

plt.tight_layout()
plt.savefig('./fotoprova/Figura4.eps',format='eps',transparent='true')
plt.savefig('./fotoprova/Figura4.png',format='png',transparent='true')

#epstool --copy --bbox Figura4.eps Figura4c.eps
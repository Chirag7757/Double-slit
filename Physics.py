import streamlit as st 
import numpy as np 
import matplotlib.pyplot as plt


st.title("Double Slit Experiment Simulator")
col1,col2=st.columns(2)
d1= 0.0003
d3= 0.0003
L=2
x=np.linspace(-L,L,10000)
lamb=0.00006
list=[]

with col1:
    N=st.number_input("Enter no of photon particles",min_value=1,max_value=100000)
    

psi1=np.sqrt(d1/(lamb*L))*np.sinc(np.pi*d1*x/(lamb*L))
psi12=psi1**2
psi2=np.sqrt(d1/(lamb*L))*np.sinc(np.pi*d1*x/(lamb*L))
psi22=psi2**2

psi3=2*np.sqrt(d3/(lamb*L))*np.sinc(np.pi*d3*x/(lamb*L))
y=abs(psi12+psi22+psi3)
y2=y/np.sum(y)
x1 = np.random.choice(x, size=N, p=y2)
y3 = np.random.rand(N) * np.max(y)

fig, ax = plt.subplots()
ax.scatter(x1,y3,label="Interference Pattern")
ax.set_xlabel("Screen Position (m)")
ax.set_ylabel("Intensity")
ax.set_title("Double Slit Interference Pattern")
ax.legend()
ax.grid()
with col2:
    st.pyplot(fig) 

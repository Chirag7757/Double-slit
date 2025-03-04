import streamlit as st 
import numpy as np 
import matplotlib.pyplot as plt


st.title("Double Slit Experiment Simulator")

d1= 0.0003
d3= 0.0003
L=2
x=np.linspace(-0.25,0.25,1000)
lamb=0.00006
list=[]

N=st.number_input("Enter no of photon particles",min_value=1,max_value=1000)
    

psi1=np.sqrt(d1/(lamb*L))*np.sinc(np.pi*d1*x/(lamb*L))
psi12=psi1**2
psi2=np.sqrt(d1/(lamb*L))*np.sinc(np.pi*d1*x/(lamb*L))
psi22=psi2**2

psi3=2*np.sqrt(d3/(lamb*L))*np.sinc(np.pi*d3*x/(lamb*L))
y=abs(psi12+psi22+psi3)
y2=y/np.sum(y)
x1 = np.random.choice(x, size=N, p=y2)
y3 = np.random.rand(N) * np.max(y)
fig, ax = plt.subplots(figsize=(8, 4))
ax.scatter(x1, y3, s=10, alpha=0.5, label="Sampled Photons")
ax.plot(x, y / np.max(y) * np.max(y3), 'r-', label="Interference Pattern")

ax.set_xlabel("Screen Position (x)")
ax.set_ylabel("Intensity")
ax.legend()
st.pyplot(fig)

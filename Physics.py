pip install matplotlib
import streamlit as st 
import numpy as np 
import matplotlib.pyplot as plt


st.title("Double Slit Experiment Simulator")
col1,col2=st.columns(2)

with col1:
    d1= (st.slider("slit 1 and 2 width in cm", 0.01,0.1))/100
    d3= (st.slider("distnce between slit in cm", 0.05, 0.5))/100
    L=(st.slider("distance between screen and slit in cm", 5, 100))/100
    x=np.linspace(-L,L,50)
    la=st.slider("wavelength of photon",4000,7000)
    lamb=la*1e-10

psi1=np.sqrt(d1/(lamb*L))*np.sinc(np.pi*d1*x/(lamb*L))
psi12=psi1**2
psi2=np.sqrt(d1/(lamb*L))*np.sinc(np.pi*d1*x/(lamb*L))
psi22=psi2**2

psi3=2*np.sqrt(d3/(lamb*L))*np.sinc(np.pi*d3*x/(lamb*L))
y=abs(psi12+psi22+psi3)

fig, ax = plt.subplots()
ax.plot(x, y, label="Interference Pattern")
ax.set_xlabel("Screen Position (m)")
ax.set_ylabel("Intensity")
ax.set_title("Double Slit Interference Pattern")
ax.legend()
ax.grid()
with col2:
    st.pyplot(fig) 

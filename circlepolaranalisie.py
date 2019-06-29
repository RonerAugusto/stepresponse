import control as con 
import matplotlib.pyplot as plt 
import numpy as np 

num = np.array([ 1, 2])
den = np.array([ 1 , 1 ])

sys = con.TransferFunction(num,den)
time_simulation = np.arange(0,15,0.5,  dtype = float)

[xout,yout]=con.step_response(sys,time_simulation)
information=con.step_info(sys)


print(information)
plt.figure()
plt.plot(xout,yout)
plt.show()


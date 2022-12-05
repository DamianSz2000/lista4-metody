import numpy as np
for i in np.arange(0, len(np.roots( [1, (5 + 1j), -(8 -5j), (30 -14j), -84]))):
    print("Piewiastek nr:", i+1)
    print(np.real( np.round( np.roots( [1, (5 + 1j), -(8 -5j), (30 -14j), -84 ] )[i], 5 ) ), " ", np.imag( np.round( np.roots( [1, (5 + 1j), -(8 -5j), (30 -14j), -84 ] )[i], 5 ) ), "j", sep="" )
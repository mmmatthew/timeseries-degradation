import tsdeg
import matplotlib.pyplot as plt
import pandas as pd

data = pd.DataFrame(dict(vals=[1, 2, 30, 40,45,46,48]))

noisy, cor = tsdeg.noisify(data, 'vals', 'normal', 0.2, normalize=True)

noisy.plot()
plt.show()
print(cor)
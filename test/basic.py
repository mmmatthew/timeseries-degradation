import tsdeg
import pandas as pd

data = pd.DataFrame(dict(vals=[1, 2, 3, 4]))

noisy = tsdeg.noisify(data, 'vals', 'normal', 0.2, True)

print(noisy.head())
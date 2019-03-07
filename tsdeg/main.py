import pandas as pd
import os
from functions import random_iid


def noisify(data, signal_col, noise_type, intensity, noisy_signal_col='degraded', normalize=False):
    """Adds noise to signal
    :param noisy_signal_col: name of column that should be created to save noisy data in
    :param data: Pandas Dataframe
    :param signal_col: name of column in which noise should be added
    :param noise_type: "normal"
    :param intensity: Standard deviation or equivalent
    :param normalize: Data column will be normalized before adding noise
    :return: Dataframe with noisy signal
    """
    if not type(data) == type(pd.DataFrame()):
        raise Exception('Data is not in pandas DataFrame format')
    if not signal_col in data.columns:
        raise Exception('Data does not have column ' + signal_col)
    if noisy_signal_col == signal_col:
        raise Exception('Columns have identical names')

    df_copy = data.copy()

    if normalize:
        df_copy[signal_col] = df_copy[signal_col] / df_copy[signal_col].max()

    if noise_type == 'normal':
        noise = random_iid.normal(length=df_copy.shape[0], std_dev=intensity)
    else:
        raise Exception('noise type not recognized')

    # Add noise to signal, scaling to signal size
    df_copy[noisy_signal_col] = df_copy[signal_col] + df_copy[signal_col]*noise

    # Measure correlation
    correlation = df_copy.corr(method='spearman')
    return df_copy, correlation[signal_col][noisy_signal_col]

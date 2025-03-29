import pandas as pd
import numpy  as np
from scipy.optimize import curve_fit

def pdTime_to_decYear(pdTime):
    """
    Convert a pandas datetime object to decimal year.
    """
    return ((pdTime.dt.year + (pdTime.dt.dayofyear - 1) / 365.25 + (pdTime.dt.hour * 3600 + pdTime.dt.minute * 60 + pdTime.dt.second) / (86400 * 365.25))).values

def fourier4_model_series(x, a0, a1, b1, a2, b2, a3, b3, a4, b4, p_value):
    """
    Fourier series model with 4 terms.
    """
    return (
        a0 +
        a1 * np.cos(1 * p_value * x) + b1 * np.sin(1 * p_value * x) +
        a2 * np.cos(2 * p_value * x) + b2 * np.sin(2 * p_value * x) +
        a3 * np.cos(3 * p_value * x) + b3 * np.sin(3 * p_value * x) +
        a4 * np.cos(4 * p_value * x) + b4 * np.sin(4 * p_value * x)
    )
    
def lineal_model_series(x, a, b):
    """
    Lineal model.
    """
    return a + b * x
    
def fit_data(x_data, y_data, intialParams, model):
    """
    Fit the data with the selected model - initialParams not used.
    """

    xdata_norm = (x_data - np.min(x_data)) / (np.max(x_data) - np.min(x_data))
    ydata_norm = (y_data - np.min(y_data)) / (np.max(y_data) - np.min(y_data))
    
    match model:
        case "fourier4":
            params, _ = curve_fit(fourier4_model_series, xdata_norm, ydata_norm, method="trf")
            return fourier4_model_series(xdata_norm, *params) * (np.max(y_data) - np.min(y_data)) + np.min(y_data)
        
        case "lineal":
            params, _ = curve_fit(lineal_model_series, xdata_norm, ydata_norm, method="trf")
            return lineal_model_series(xdata_norm, *params) * (np.max(y_data) - np.min(y_data)) + np.min(y_data)
        
def find_local_max_min(data):
    """
    Find the local max and min of the fitted prices.
    """
    return (np.diff(np.sign(np.diff(data))) != 0).nonzero()[0] + 1

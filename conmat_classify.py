import xarray as xr
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
import math

    
def mat_rain_classifier(flt):
        if flt >= 0.0 and flt < 10.0:
            return 14
        elif flt >= 10.0 and flt < 20.0:
            return 13
        elif flt >= 20.0 and flt < 30.0:
            return 12
        elif flt >= 30.0 and flt < 40.0:
            return 11
        elif flt >= 40.0 and flt < 50.0:
            return 10
        elif flt >= 50.0 and flt < 60.0:
            return 9
        elif flt >= 60.0 and flt < 70.0:
            return 8
        elif flt >= 70.0 and flt < 80.0:
            return 7
        elif flt >= 80.0 and flt < 90.0:
            return 6
        elif flt >= 90.0 and flt < 100.0:
            return 5
        elif flt >= 100.0 and flt < 110.0:
            return 4
        elif flt >= 110.0 and flt < 120.0:
            return 3
        elif flt >= 120.0 and flt < 130.0:
            return 2
        elif flt >= 130.0 and flt < 140.0:
            return 1
        elif flt >= 140.0:
            return 0
        else:
            return("Error")
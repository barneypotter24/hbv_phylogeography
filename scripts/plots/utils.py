import numpy as np
import pandas as pd
from matplotlib.patches import Polygon
import datetime as dt
import math
from scipy.special import binom
import matplotlib as mpl
import colorsys

def load_geojson_to_polygons(gjs_file):
    '''Given a geojson, return a dictionary of polygons keyed by country name.

    Adapted from https://github.com/ebov/space-time/blob/master/Scripts/notebooks/auxiliaries/ebov_data.py#L352
    '''
    polygons = {}
    location_points = {}
    locations = []
    handle=pd.read_json(open(gjs_file,'r')) ## load data
    features=handle['features']

    for loc in features: ## iterate through features (locations)
    	poly = np.array(loc['geometry']['coordinates']) ## get coordinates
    	location=loc['properties']['name'] ## standardised location name

    	locations.append(location)

    	polygons[location]=[]
    	location_points[location]=[]
    	if loc['geometry']['type']=='MultiPolygon': ## multiple parts detected
    		for part in poly:
    			for coords in part:
    				xs=column(coords,0)
    				ys=column(coords,1)
    				location_points[location].append(np.vstack(zip(xs,ys)))
    	if loc['geometry']['type']=='Polygon': ## location is single part
    		for coords in poly:
    			xs=column(coords,0)
    			ys=column(coords,1)
    			location_points[location].append(np.vstack(zip(xs,ys)))

    	complete_location=[]
    	for part in location_points[location]:
    		complete_location.append(Polygon(part,True))

    	polygons[location]=complete_location

    return polygons, locations

def convert_partial_year(number):
    year = int(number)
    d = timedelta(days=(number - year)*(365 + is_leap(year)))
    if year > 0:
        day_one = datetime(year,1,1)
        date = d + day_one
        return date.date().isoformat()
    else:
        day_one = datetime(-year,1,1)
        date = d + day_one
        return '-' +date.date().isoformat()

def is_leap(x):
    if int(x) % 4 == 0:
        return True
    else:
        return False

def create_log_normalization(l,n_min,n_max):
    lc = [ math.log10(v) for v in l ]
    l_max=max(lc)
    l_min=min(lc)

    oldRange = (l_max-l_min)
    newRange = (n_max-n_min)

    def normalize(value):
        return (((math.log10(value)-l_min)*newRange)/float(oldRange)) + n_min
    return normalize

def create_normalization(l,n_min,n_max):
    l_max=max(l)
    l_min=min(l)

    oldRange = (l_max-l_min)
    newRange = (n_max-n_min)

    def normalize(value):
        return (((value-l_min)*newRange)/float(oldRange)) + n_min
    return normalize

def findTimeDelta(date1,date2):
    """Returns number of days separating two decimal dates
    """
    delta = date2-date1
    years = int(delta)
    days = (delta - years)*365
    return (365*years+days)

def Bezier(points,start,end,num=10):
    """Build Bezier curve from points.
    """
    N = len(points)
    t = np.linspace(start, end, num)
    curve = np.zeros((num, 2))
    for ii in range(N):
        curve += np.outer(Bernstein(N - 1, ii)(t), points[ii])

    return curve

def Bezier_control(pointA,pointB,height):
    """
    Given a line defined by 2 points A & B,
    find a third point at a given distance that defines a line perpendicular to line AB which intercepts AB at its midpoint.
    Equation derived by Luiz Max Fagundes de Carvalho (University of Edinburgh).
    """
    x1,y1=pointA
    x2,y2=pointB

    sign=1
    if x1>x2:
        sign=-1

    slope = (y2-y1) / (x2-x1)
    d=np.sqrt((y2-y1)**2 + (x2-x1)**2)

    h=np.sqrt(height**2+(d**2)/4.0)

    n1=x1+h*np.cos(np.arctan(2*height/float(d))+np.arctan(slope))*sign
    n2=y1+h*np.sin(np.arctan(2*height/float(d))+np.arctan(slope))*sign

    return (n1,n2)

def Bernstein(n, k):
    """Bernstein polynomial.
    """
    coeff = binom(n, k)

    def _bpoly(x):
        return coeff * x ** k * (1 - x) ** (n - k)

    return _bpoly

def column(data,col):
    return [row [col] for row in data]

#### code stolen from seaborn to desaturate colours
def desaturate(color, prop):
    """Decrease the saturation channel of a color by some percent.
    Parameters
    ----------
    color : matplotlib color
        hex, rgb-tuple, or html color name
    prop : float
        saturation channel of color will be multiplied by this value
    Returns
    -------
    new_color : rgb tuple
        desaturated color code in RGB tuple representation
    """
    # Check inputs
    if not 0 <= prop <= 1:
        raise ValueError("prop must be between 0 and 1")

    # Get rgb tuple rep
    rgb = mpl.colors.colorConverter.to_rgb(color)

    # Convert to hls
    h, l, s = colorsys.rgb_to_hls(*rgb)

    # Desaturate the saturation channel
    s *= prop

    # Convert back to rgb
    new_color = colorsys.hls_to_rgb(h, l, s)

    return new_color

def decimalDate(date,fmt="%Y-%m-%d"):
    """ Converts calendar dates in specified format to decimal date. """
    is_neg=date.startswith('-')
    if is_neg:
        date=date[1:]
    adatetime=dt.datetime.strptime(date,fmt)
    year = adatetime.year
    boy = dt.datetime(year, 1, 1)
    eoy = dt.datetime(year + 1, 1, 1)
    if is_neg:
        return -1*(year + ((adatetime - boy).total_seconds() / ((eoy - boy).total_seconds())))
    else:
        return year + ((adatetime - boy).total_seconds() / ((eoy - boy).total_seconds()))

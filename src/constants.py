
from pathlib import Path

parent_folder = Path.cwd().parent  
CSV_FOLDER = Path.cwd().parent / "StatsForecast" / "results_norm"  
# SRC = Path.cwd().parent / "StatsForecast" / "data"
DATA_PATH = Path.cwd().parent / "StatsForecast" / "data" / "ETTh.csv"
# DATA_PATH = Path.cwd().parent / "StatsForecast" / "data" / "volatility_Europe_garch_1_1.csv"

EVAL_HORIZONS = [
    24, 
    # 7, 
    # 1
]

# size of test df (and forecast) in months
TEST_SIZE = 1

valid_metrics = ['mae', 'mape', 'rmse', 'smape', "norm_mae"]

LOW_QUANTILE = 0.025
UP_QUANTILE = 0.975

COLORS = {
    'HoltWinters': '#98df8a', 
    'Croston': '#ff7f0e', 
    'ARIMA': '#1f77b4',
    'AutoARIMA': '#2ca02c',
    'DOT_sl7': '#d62728', 
    'SeasonalNaive': '#9467bd', 
    'Naive': '#8c564b',
    'AutoETS': '#e377c2', 
    'HistoricAverage': '#7f7f7f',
    'DOT_sl1': '#bcbd22', 
    'GARCH(1,1)': '#17becf',
    'GARCH(2,1)': '#aec7e8', 
    'GARCH(2,2)': '#ffbb78'
}

DARK_STYLE = {
    'style': 'fivethirtyeight',  
    'rcParams': {
        'lines.linewidth': 3,  
        'figure.facecolor': '#1a1c38',
        'axes.facecolor': '#1a1c38',
        'savefig.facecolor': '#1a1c38',
        'axes.grid': True,
        'axes.grid.which': 'both',
        'axes.spines.left': False,
        'axes.spines.right': False,
        'axes.spines.top': False,
        'axes.spines.bottom': False,
        'grid.color': '#2A3459',
        'grid.linewidth': 1,
        'text.color': '0.9',
        'axes.labelcolor': '0.9',
        'xtick.color': '0.9',
        'ytick.color': '0.9',
        'font.size': 20
    }
}




import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Consts:
    pi = 3.141592
    c = 3e8
    e = 1.6e-19
    mu_B = 5.788 * 10**-9  # eV / Gauss
    hbar = 6.58 * 10**-16  # eV * s

class Setup:
    dummy = 0
    probe_d = 14.3          # mm
    probe_d_err = 0.1       # mm
    probe_N = 49            # turns
    freq = 50               # Hz
    freq_err = 1            # Hz

def read_calibration_data(file_path):
    calibration_data = pd.read_excel(file_path)
    column_names = calibration_data.columns
    units_row = calibration_data.iloc[0]
    multi_index = pd.MultiIndex.from_tuples(zip(column_names, units_row), names=('Variable', 'Unit'))
    calibration_data = pd.read_excel(file_path, header=None, skiprows=2)
    calibration_data.columns = multi_index
    return calibration_data

def format_calibration_data(calibration_data):
    if isinstance(calibration_data, pd.Series):
        # If it's a Series, convert it to a DataFrame with a single column
        calibration_data = pd.DataFrame(calibration_data)

    if isinstance(calibration_data.columns, pd.MultiIndex):
        # If it already has a MultiIndex, rename columns directly
        fmt = {'V_r, mV': 'V', 'V_probe, mV': 'V_probe', 'Main coils': 'Calibration'}
        calibration_data.columns = calibration_data.columns.set_levels(
            calibration_data.columns.levels[0].map(fmt).fillna(calibration_data.columns.levels[0]), level=0
        )
    else:
        # If it's a regular DataFrame, assume the first row contains the header
        fmt = {'V_r, mV': 'V', 'V_probe, mV': 'V_probe', 'Main coils': 'Calibration'}
        calibration_data.columns = pd.MultiIndex.from_frame(calibration_data.iloc[:1])
        calibration_data = calibration_data.iloc[1:]
        calibration_data.columns = calibration_data.columns.set_levels(
            calibration_data.columns.levels[0].map(fmt).fillna(calibration_data.columns.levels[0]), level=0
        )

    return calibration_data

def convert_to_magnetic_induction(calibration_data):
    V = 0.001 * calibration_data['Calibration', 'V_probe']
    S = 1/4 * Consts.pi * (Setup.probe_d / 1000)**2
    omega = 2 * Consts.pi * Setup.freq
    calibration_data['Calibration', 'B'] = 10000 * V / (Setup.probe_N * S * omega)
    return calibration_data

def plot_calibration_data(calibration_data):
    d = calibration_data['Calibration']
    x, y, _ = plt.errorbar(d['V'], d['B'], xerr=0, fmt='o', label='Calibration')
    plt.xlabel('V, мВ')
    plt.ylabel('B, Гс')
    plt.grid()
    plt.savefig('gen/calibration.pdf')
    return x, y

def perform_linear_regression(x, y):
    mnk_coefficients = np.polyfit(x, y, 1)
    a, b = mnk_coefficients
    print(f'MNK Coefficients: a = {a:.4f}, b = {b:.4f}')
    return a, b

def calculate_B_for_V10(V2B):
    V10_B = V2B(10)
    print(f'V=10 corresponds to B={V10_B:.4f} Gauss')
    return V10_B

def prepare_calibration_table(calibration_data):
    calibration_table_data = calibration_data['Calibration'].dropna()
    calibration_table_fmt = {'V': [r'$V$, мВ', '{:.2f}'], 'V_probe': [r'$V_{probe}$, мВ', '{:.2f}'],
                             'B': [r'$B$, Гс', '{:.1f}']}
    calibration_table = pd.DataFrame(calibration_table_data, columns=calibration_table_fmt.keys())
    return calibration_table.rename(columns=calibration_table_fmt)

def save_calibration_table_to_latex(calibration_table):
    calibration_table.to_latex('gen/calibration.tex')

def read_epr_data(file_path):
    return pd.read_excel(file_path, usecols=('A', 'B', 'C', 'D'), header=(0)).dropna()

def format_epr_data(epr_data):
    epr_fmt = {'f, MHz': 'f', 'V, mV': 'V', 'V_left, mV': 'V_left', 'V_right, mV': 'V_right', 'Width, 10*cell': 'width'}
    return epr_data.rename(columns=epr_fmt)

def plot_epr_data(epr_data):
    x, y, _ = plt.errorbar(epr_data['B'], epr_data['f'], xerr=epr_data['B'] * 0.01, fmt='o', label='EPR')
    plt.grid()
    plt.xlabel('$B$, Гс')
    plt.ylabel('$f$, МГц')
    plt.savefig('gen/epr.pdf')
    return x, y

def perform_linear_regression_epr(x, y):
    mnk_coefficients = np.polyfit(x, 2 * np.pi * y * 1e6, 1)
    mnk_a, _ = mnk_coefficients
    print(f'MNK Coefficient for EPR: a = {mnk_a:.4f}')
    return mnk_a

def calculate_lande_factor(mnk_a):
    g = mnk_a * Consts.hbar / (0.5 * Consts.mu_B)
    print(f'g = {g:.4f}')
    return g

def prepare_epr_table(epr_data):
    epr_table_data = epr_data.dropna()
    epr_table_fmt = {'f': [r'$f$, МГц', '{:.3f}'], 'V': [r'$V$, мВ', '{:.2f}'],
                     'V_left': [r'$V_{left}$, мВ', '{:.2f}'], 'V_right': [r'$V_{right}$, мВ', '{:.2f}'],
                     'B': [r'$B$, Гс', '{:.1f}'], 'B_left': [r'$B_{left}$, Гс', '{:.1f}'],
                     'B_right': [r'$B_{right}$, Гс', '{:.1f}']}
    return pd.DataFrame(epr_table_data, columns=epr_table_fmt.keys()).rename(columns=epr_table_fmt)

# Usage of the functions
calibration_data = read_calibration_data(r'C:\\Users\\evgen\\Downloads\\10.1.xlsx')
calibration_data = format_calibration_data(calibration_data)
calibration_data = convert_to_magnetic_induction(calibration_data)
x, y = plot_calibration_data(calibration_data)
a, b = perform_linear_regression(x, y)
V10_B = calculate_B_for_V10(lambda v: 10000 * v / (Setup.probe_N * (1/4 * Consts.pi * (Setup.probe_d / 1000)**2) * (2 * Consts.pi * Setup.freq)))
calibration_table = prepare_calibration_table(calibration_data)
save_calibration_table_to_latex(calibration_table)

epr_data = read_epr_data(r'C:\\Users\\evgen\\Downloads\\10.1.xlsx')
epr_data = format_epr_data(epr_data)
x, y = plot_epr_data(epr_data)
mnk_a = perform_linear_regression_epr(x, y)
calculate_lande_factor(mnk_a)
epr_table = prepare_epr_table(epr_data)

#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

from IPython.display import display

from kplot import kFit

# N個のガウシアンを合成する関数
def Gaussian(x, *params):
	Length = len(params)//3 # gaussは3つのパラメータ
	Y = np.zeros_like(x)
	for i in range(Length):
		Amp = params[3*i]
		Mu = params[3*i + 1]
		Sigma = params[3*i + 2]
		Y += Amp*np.exp(-0.5*(x-Mu)**2/Sigma**2)
	Y += params[-1]
	return Y

# --- fitting ---------------
fit = kFitting()
df = pd.read_csv('./test.csv')
# display(df)

xData = df['Energy']
yData = df['Count']

xLower = 1.74
xUpper = 2.5

xFitData, yFitData = fit.SetXRange(df, 'Energy', 'Count',  xLower, xUpper)
x = fit.GetSampleXarray()

p0 = [25000, 2.013, 0.1, 600.0]
fit.Fit(Gaussian, xFitData, yFitData, p0=p0)
# fit.EchoParamTable()

p1 = p0[:-1] + [5000, 2.042, 0.04] + p0[-1:]
# Mu だけを制限（例：2.00〜2.02）
# LowBound = [-np.inf, 2.03, 0.02]
# UpBound  = [ np.inf, 2.05, 0.05]
# Limits = (LowBound, UpBound)

# Params1, Conv1 = curve_fit(Gaussian, xFitData, yFitData, p0=p1, bounds=Limits)
ParamsAll, Conv = fit.Fit(Gaussian, xFitData, yFitData, p0=p1)
fit.EchoParamTable()
fit.SaveParamTable('./test.csv')
# plt.plot(x, Gaussian(x, *Params1), color='red')

# print(ParamsAll)
LabelL = ParamsAll[3:6].tolist()+[ParamsAll[6]]
LabelR = ParamsAll[:3].tolist() +[ParamsAll[6]]


# --- plot ---------------
fig, ax = plt.subplots(2, 1, sharex=True, gridspec_kw={'height_ratios':[3,1], 'hspace': 0.0}, tight_layout=True)

ax[0].step(xData, yData, where='mid', color='black', label='data')
ax[0].plot(x, Gaussian(x, *LabelL), color='blue', linestyle='--', label='2.01 keV')
ax[0].plot(x, Gaussian(x, *LabelR), color='green', linestyle='--', label='2.04 keV')
ax[0].plot(x, Gaussian(x, *ParamsAll), color='red', label='all fit')
ax[0].set_ylabel('Events', loc='top')
ax[0].set_ylim(-2000, max(yFitData)*1.1)
ax[0].set_xlim(xLower, xUpper)
ax[0].legend()

Delta = fit.GetResidual(yFitData, Gaussian(xFitData, *ParamsAll))
DeltaErr = np.sqrt(yFitData) # 本当は誤差伝播シなくちゃだめ
ax[1].axhline(y=0, color='red', linestyle='--', linewidth=1)
ax[1].errorbar(xFitData, Delta, yerr=DeltaErr, xerr=None, marker='o', color='black', capsize=2, elinewidth=1, linestyle='')
Range = max(max(Delta), abs(min(Delta)))*1.5
ax[1].set_ylim(-Range, Range)
ax[1].set_xlabel('Energy [keV]', loc='right')

plt.savefig('./plot.pdf')
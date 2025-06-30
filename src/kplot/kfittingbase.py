#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# import kplot.common

from IPython.display import display

# 作りかけ
class kFittingBase:
	fDataFrameStyle = True
	xDef = None
	p0 = None
	Func = None
	Nsamples = 500 # サンプル点数
	Params = None
	ParamErrors = None
	Conv = None
	dfParamTable = None
	def __init__(self):
		pass
	def SetPointN(self, val):
		self.Nsamples = val

	def GetSampleXarray(self):
		return self.x

	def SetXRange(self, df, xcolname, ycolname, xlow, xup):
		self.x = np.linspace(xlow, xup, self.Nsamples)
		Mask = (df[xcolname] >= xlow) & (df[xcolname] <= xup)
		xApplyData = df.loc[Mask, xcolname]
		yApplyData = df.loc[Mask, ycolname]
		return xApplyData, yApplyData

	def GetParamsInfo(self, params=None, conv=None):
		if params is not None: self.Params = params
		if conv is not None: self.Conv = conv
  
		self.ParamErrors = np.sqrt(np.diag(self.Conv))
		if len(self.ParamErrors) != len(self.Params):
			print('Parameter table error')

		ParamInfo = {}
		if self.fDataFrameStyle:
			ParamInfo['Parameter'] = []
			ParamInfo['Error']	   = []
			for i in range(len(self.Params)):
				ParamInfo['Parameter'].append(self.Params[i])
				ParamInfo[	  'Error'].append(self.ParamErrors[i])
		else:
			for i, param in enumerate(self.Params):
				ParamInfo[f'p{i}'] = param
				ParamInfo[f'p{i}Err'] = self.ParamErrors[i]
		return ParamInfo

	def EchoParamTable(self, params=None, conv=None):
		ParamInfo = self.GetParamsInfo(params, conv)
		if self.fDataFrameStyle:
			self.dfParamTable = pd.DataFrame(ParamInfo)
		else:
			self.dfParamTable = pd.DataFrame([ParamInfo])
		# print(df)
		display(self.dfParamTable)
		return self.dfParamTable

	def SaveParamTable(self, path='./fit-params.csv', encoding='utf-8'):
		self.dfParamTable.to_csv(path, encoding=encoding)

	def SetParameter(self, index, param):
		if (len(self.p0)>index+1):
			self.p0 = []
			while len(self.p0)==index:
				self.p0.append(0)

	def SetParameters(self, params):
		self.p0 = params

	def SetParLimits(self, index, low, up):
		pass

	def Fit(self, func, x, y, p0=None, xlim=None, ylim=None):
		self.Func = func
		if p0 is not None: self.p0 = p0
		if self.p0 == None:
			self.Params, self.Conv = curve_fit(self.Func, x, y)
		else:
			self.Params, self.Conv = curve_fit(self.Func, x, y, p0=self.p0)

		return self.Params, self.Conv

	def GetResidual(self, ydata=None, yfit=None):
		return ydata-yfit
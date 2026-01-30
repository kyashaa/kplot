#%%
"""kplot.pltstyle

* Optimizing default parameters in matplotlib for kplot.

"""
import platform
import matplotlib as mpl 

def SetDefaultFont(font='auto', font_size=18):
	"""Font settings

	Set font type and size. default font set 'sans-serif'.
	You can set to be serif-font, using 'paper' or 'auto' parameter.

	Args:
		font (str): Set font type or tag ['paper', 'auto'].
		font_size (int): Font size
	"""

	Font='sans-serif'
	System = platform.system()

	if font == 'paper': font = 'auto'

	if font!='': 
		if font=='auto':
			if System in ("Windows", "Darwin"):
				Font='Times New Roman'
			else: Font='Nimbus Roman'
			mpl.rcParams['mathtext.fontset'] = 'stix' 
		else: Font=font

	# print(Font)
	mpl.rcParams["font.family"] = Font
	mpl.rcParams["font.size"] = font_size

def SetLoadLatex(flag=True):
	"""LoadLatex 
		If this flag set to be True, This function load Installed LaTeX system. 
	"""
	mpl.rcParams["text.usetex"] = flag


def SetDefaultFigSize(tag:str='default', fig_size:list=[], x=8, y=6, dpi=350):
	"""SetDefaultFigSize

	Settings for default figure size. Default set a figure size to 8 inch x 6 inch.

	Args:
		tag (str): set figure size using tag: 'default', 'A4', 'a4', 'B5', 'b5'.
		fig_size (list): set figure size using list: [x, y]
		x, y (float): set figure size
		dpi (float): set figure resolution (dpi).
	"""
	FigSize=[8, 6]
	if x != 8: FigSize[0]=x
	if y != 6: FigSize[1]=y
	if fig_size != []:
		if len(fig_size) != 2:
			print('[WARNING:SetDefaultFigSize] List length of figure size parameters can set to be 2.')
			print(f'[WARNING:SetDefaultFigSize] You set {fig_size}. It\'s ignored.')
		else: FigSize=fig_size
	if tag in ['A4', 'a4']: FigSize = [11.69, 8.27]
	if tag in ['B5', 'b5']: FigSize = [10.10, 7.20]

	mpl.rcParams["figure.figsize"] = FigSize
	mpl.rcParams["savefig.dpi"] = dpi
	# mpl.rcParams["legend.fontsize"] = "small"
	mpl.rcParams["legend.fontsize"] = 14
	mpl.rcParams["legend.title_fontsize"] = 14

def SetDefaultSettings():
	"""SetDefaultSettings
	Load and set to default figure setting parameters.
	"""
	SetDefaultFont(font='auto', font_size=18)

	SetDefaultFigSize('default', dpi=350)

	# axis
	mpl.rcParams["xtick.direction"] = 'in'
	mpl.rcParams["ytick.direction"] = 'in'
	mpl.rcParams["xtick.top"] = True
	mpl.rcParams["ytick.right"] = True

	mpl.rcParams["xtick.minor.visible"] = True
	mpl.rcParams["ytick.minor.visible"] = True

	mpl.rcParams["xtick.major.width"] = 1.0
	mpl.rcParams["ytick.major.width"] = 1.0

	mpl.rcParams["xtick.major.size"] = 10
	mpl.rcParams["ytick.major.size"] = 10

	mpl.rcParams["xtick.minor.width"] = 1.0
	mpl.rcParams["ytick.minor.width"] = 1.0

	mpl.rcParams["xtick.minor.size"] = 5
	mpl.rcParams["ytick.minor.size"] = 5

	mpl.rcParams["xaxis.labellocation"] = 'right'
	mpl.rcParams["yaxis.labellocation"] = 'top'

	# ticks
	mpl.rcParams['xtick.top'] 	= False
	mpl.rcParams['ytick.right'] = False

	# Frame
	mpl.rcParams["axes.linewidth"] = 1.0

	mpl.rcParams["lines.marker"] = 'o'
	mpl.rcParams["lines.color"] = 'black'

	mpl.rcParams["savefig.bbox"] = "tight"
	mpl.rcParams["savefig.pad_inches"] = 0.05


import os
if os.getenv("KLPLOT_AUTOLOAD", "0") == "1":
    SetDefaultSettings()
# mpl.rcParamsDefault.keys()
# SetDefaultSettings()


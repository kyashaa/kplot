#%%
"""kplot.pltstyle

* Optimizing default parameters in matplotlib for kplot.

"""
import platform
import matplotlib as plt

def SetDefaultFont(font='auto', font_size=20):
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
		else: Font=font

	# print(Font)
	plt.rcParams["font.family"] = Font
	plt.rcParams["font.size"] = font_size

def SetLoadLatex(flag=True):
	"""LoadLatex 
		If this flag set to be True, This function load Installed LaTeX system. 
	"""
	plt.rcParams["text.usetex"] = flag


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

	plt.rcParams["figure.figsize"] = FigSize
	plt.rcParams["savefig.dpi"] = dpi

def SetDefaultSettings():
	"""SetDefaultSettings
	Load and set to default figure setting parameters.
	"""
	SetDefaultFont(font='auto', font_size=20)

	SetDefaultFigSize('A4', dpi=350)

	# axis
	plt.rcParams["xtick.direction"] = 'in'
	plt.rcParams["ytick.direction"] = 'in'

	plt.rcParams["xtick.minor.visible"] = True
	plt.rcParams["ytick.minor.visible"] = True

	plt.rcParams["xtick.major.width"] = 1.0
	plt.rcParams["ytick.major.width"] = 1.0

	plt.rcParams["xtick.major.size"] = 10
	plt.rcParams["ytick.major.size"] = 10

	plt.rcParams["xtick.minor.width"] = 1.0
	plt.rcParams["ytick.minor.width"] = 1.0

	plt.rcParams["xtick.minor.size"] = 5
	plt.rcParams["ytick.minor.size"] = 5

	# ticks
	plt.rcParams['xtick.top'] 	= False
	plt.rcParams['ytick.right'] = False

	# Frame
	plt.rcParams["axes.linewidth"] = 1.0

	# plt.rcParams["lines.marker"] = 'o'
	plt.rcParams["lines.color"] = 'black'

# plt.rcParamsDefault.keys()
SetDefaultSettings()


#%%
"""kplot.hist

* The histogram and graph module using matplotlib.
It's beta version. We will add the ability to manage common parameters.

"""

import matplotlib
import matplotlib.pyplot as plt

class hist:
    """kplot.hist class

    Create a one or two dimension graph/histogram.

    """
    HistXRange = None
    uHistYRange = None
    bHistYRange = None
    Titles = ""
    TitleLabel = ""
    xAxisLabel = "x"
    yAxisLabel = "y"
    y2AxisLabel = "y2"

    Fig = None
    FigSize=(11.69,8.27)
    Axs = []

    def __init__(self, titles, xBin=10, xMin=0, xMax=1, yBin=0, yMin=0, yMax=0):
        """default constructor

        default constructor

        Args:
            titles (str): The titles of the graph. "Graph title;x-axis label;y-axis label".
            xBim (int): Bin for x-axis.
            xMin (float): Minimum of graph/histogram for x-axis.
            xMaz (float): Maximum of graph/histogram for x-axis.
            yBim (int): Bin for y-axis.
            yMin (float): Minimum of graph/histogram for y-axis.
            yMaz (float): Maximum of graph/histogram for y-axis.
        """
        self.Titles = titles
        self.SplitTitle()
        self.HistXRange = (xBin, xMin, xMax)
        self.HistYRange = (yBin, yMin, yMax)
        # print(self.HistXRange)

    def SplitTitle(self):
        """SplitTitle

        Analysis function for graph labels. It is automatically called when the title labels is set.

        Args:
            None.
        """
        Buf = self.Titles.split(sep=';')
        # print(Buf)
        if len(Buf) >= 3:
            self.TitleLabel = Buf[0]
            self.xAxisLabel = Buf[1]
            self.yAxisLabel = Buf[2]
            if len(Buf) == 4: self.y2AxisLabel = Buf[3]
            
    def DrawCanv(self, figsize: tuple=None):
        """DrawCanv

        Draw a canvas.
        
        Note:
            If the canvas already exists, redraw it.
        """

        if figsize is not None: self.FigSize=figsize
        if self.Fig is not None: self.Fig = None
        self.Fig = plt.figure(figsize=self.FigSize)

    def Draw1D(self, data):
        """Draw1D

        Draw a 1-Dim histogram. 

        Args:
            data (array): value of data.
        """
        self.DrawCanv()
        if len(self.Axs) > 0: self.Axs.clear()
        self.Axs.append(self.Fig.add_subplot(1,1,1))
        # print(self.Axs)
        # print(len(self.Axs))
        # print(self.HistXRange)
        # print(self.xAxisLabel)
        
        self.Axs[0].hist(data, bins=self.HistXRange[0], range=self.HistXRange[1:], histtype='step')
        self.Axs[0].set_xlim(self.HistXRange[1:])
        self.Axs[0].set_title(self.TitleLabel)
        self.Axs[0].set_xlabel(self.xAxisLabel, loc='right')
        self.Axs[0].set_ylabel(self.yAxisLabel, loc='top')

        return self.Axs[0]

    def Draw2D(self, x, y):
        """Draw2D

        Draw a 2-Dim histogram. Automatic generation of color bars.

        Args:
            x (array): value of data for x-axis hist.
            y (array): value of data for y-axis hist.
        """
        self.DrawCanv()
        self.Axs.append(self.Fig.add_subplot(1,1,1))
        Hist = self.Axs[0].hist2d(x, y,
                                bins=(self.HistXRange[0], self.HistYRange[0]), 
                                range=(self.HistXRange[1:],self.HistYRange[1:]))
        self.Fig.colorbar(Hist[3], ax=self.Axs[0])
        
        self.Axs[0].set_title(self.TitleLabel)
        self.Axs[0].set_xlabel(self.xAxisLabel, loc='right')
        self.Axs[0].set_ylabel(self.yAxisLabel, loc='top')
        pass
    
    def DrawSep2(self, x, ax0_y, ax1_y, ratio=0.8, val_hline=None):
        """DrawSep2

        Draw a graphs with the canvas divided into two parts by an division ratio; the x-axis is shared.

        Args:
            x (array): value of data for x-axis hist.
            ax0_y (array): value of data for upper graph y-axis.
            ax1_y (array): value of data for lower graph y-axis.
            ratio (float): division ratio to the y length of the canvas. (default: 0.8)
            val_hline (bool): To enable flag for y=0 horizontal line in the lower graph.

        Examples:
            The function has been implemented to show the variance of the data with respect to the fitted graph and the fitted curve
        """
        self.DrawCanv()
        if len(self.Axs) > 0: self.Axs.clear()
        self.Axs = self.Fig.subplots(2, 1)
        plt.subplots_adjust(wspace=0, hspace=0)
        
        self.Axs[0].plot(x, ax0_y, marker='o', linestyle='', color='black')
        self.Axs[1].plot(x, ax1_y, marker='o', linestyle='', color='black')
        
        if val_hline is not None:
            self.Axs[1].axhline(y=val_hline, linestyle='--', color='red')

        self.Axs[0].set_title(self.TitleLabel)
        self.Axs[1].set_xlabel(self.xAxisLabel, loc='right')
        self.Axs[0].set_ylabel(self.yAxisLabel, loc='top')
        self.Axs[1].set_ylabel(self.y2AxisLabel, loc='top')
        
        self.Fig.align_labels()
        return self.Axs

    def SetxLimit(self, lower, upper):
        """SetxLimit

        Set the viewing range for the x-axis from lower val. to upper val.

        Args:
            index (int): index of graph. index 0 is upper, 1 is lower.
            lower (float): lower limit val.
            upper (float): upper limit val.
        Note:
            If an out-of-range index is used, this function is ignored.
        """
        for ax in self.Axs:
            ax.set_xlim(lower, upper)
            
    def SetyLimit(self, index, lower, upper):
        """SetyLimit

        Set the viewing range for the y-axis from lower val. to upper val.

        Args:
            index (int): index of graph. index 0 is upper, 1 is lower.
            lower (float): lower limit val.
            upper (float): upper limit val.
        Note:
            If an out-of-range index is used, this function is ignored.
        """
        if index < len(self.Axs):
            self.Axs[index].set_ylim(lower, upper)
        else:
            print('index is out of range.')
    
    def Print(self, path='./plot.pdf', dpi=350, pad_inches=0.5):
        """Print

        Save the graph.

        Args:
            path (str): path to file.
            dpi (int): DPI.
            pad_inches (float): pad inches.
        """
        plt.savefig(path, dpi=dpi, bbox_inches='tight', pad_inches=pad_inches)

    def Clear(self):
        """Clear

        Clear the pad.
        """
        plt.cla()
        plt.clf()
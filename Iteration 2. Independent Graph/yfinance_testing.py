
import yfinance as yf
import pyqtgraph as pg
import pandas as pd
from PyQt5 import QtCore, QtWidgets
from pyqtgraph import DateAxisItem


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        stock = 'TSLA'
        start = '2020-11-01'

        df = yf.download(stock, start=start)

        X = df.index
        Y = df.Close

        self.plot_graph = pg.PlotWidget()
        self.setCentralWidget(self.plot_graph)

        self.plot_graph.setBackground("w")
        pen = pg.mkPen(color=(255, 0, 0))
        self.plot_graph.setTitle("Tesla stock", color="b", size="20pt")
        styles = {"color": "red", "font-size": "18px"}
        self.plot_graph.setLabel("right", "Price", **styles)
        self.plot_graph.setLabel("bottom", "Time", **styles)

        self.plot_graph.showGrid(x=True, y=True)
        # print(X)
        # print(Y)
        try:
            x_axis = DateAxisItem
            self.plot_graph.setAxisItems({"bottom":x_axis})
            self.line = self.plot_graph.plot(X, Y, name="Tesla", pen=pen, symbol=None,)
        except Exception as e:
            print(type(e).__name__, "-", e)


if __name__ in "__main__":
    app = QtWidgets.QApplication([])
    main = MainWindow()
    main.show()
    app.exec()


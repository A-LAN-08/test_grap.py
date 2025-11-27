
import pyqtgraph as pg
from PyQt5 import QtWidgets

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Temperature vs time plot
        time = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]
        time2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        temperature2 = [32, 29, 30, 33, 30, 29, 35, 40, 31, 27]

        self.plot_graph = pg.PlotWidget()
        self.setCentralWidget(self.plot_graph)

        self.plot_graph.addLegend()

        self.plot_graph.setBackground("#adadad")
        pen = pg.mkPen(color=(255, 0, 0), width=5)

        self.plot_graph.plot(time, temperature, name="Temp 1", pen=pen, symbol="x", symbolSize=20, symbolBrush="b")
        self.plot_graph.plot(time2, temperature2, name="Temp 2", pen=pen, symbol="x", symbolSize=20, symbolBrush="b")
        self.plot_graph.setTitle("Temperature vs Time", color="b", size="20pt")

        styles = {"color": "red", "font-size": "18px"}
        self.plot_graph.setLabel("left", "Temperature / °C", **styles)
        self.plot_graph.setLabel("bottom", "Time / min", **styles)

        self.plot_graph.showGrid(x=True, y=True)

        self.plot_graph.setXRange(1, 10)
        self.plot_graph.setYRange(20, 40)


app = QtWidgets.QApplication([])
main = MainWindow()
main.show()
app.exec()




import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPalette, QPainter, QPixmap, QPainterPath
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout,
    QLabel, QPushButton, QFrame
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dashboard Layout Example")
        self.setGeometry(100, 100, 1500, 900)

        # --- Main container ---
        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QHBoxLayout()
        central.setLayout(main_layout)

        # --- Left sidebar ---
        left_bar = self.coloured_frame("lightgray")
        left_layout = QVBoxLayout(left_bar)
        left_layout.addStretch()

        # --- Center area (graph + top bar) ---
        center_frame = QFrame()
        center_layout = QVBoxLayout(center_frame)

        # Top bar
        top_bar = self.coloured_frame("whitesmoke")
        top_layout = QHBoxLayout(top_bar)
        top_layout.addStretch()

        # Graph area
        graph_frame = self.coloured_frame("white")
        graph_label = QLabel("Graph Area")
        graph_label.setAlignment(Qt.AlignCenter)
        graph_frame.layout().addWidget(graph_label)

        center_layout.addWidget(top_bar, 1)
        center_layout.addWidget(graph_frame, 10)

        # --- Right sidebar ---
        right_frame = QFrame()
        right_layout = QVBoxLayout(right_frame)

        # Profile screen
        profile_bar = QWidget()
        profile_bar.setStyleSheet("background-color: lightgray;")
        # profile_bar.setFixedWidth(150)

        circle_label = QLabel()
        pixmap = QPixmap("Test.png")
        circle_pixmap = self.circle_bitmap(pixmap, 100)
        circle_label.setPixmap(circle_pixmap)
        circle_label.setAlignment(Qt.AlignCenter)

        right_bar_profile_layout = QVBoxLayout(profile_bar)
        right_bar_profile_layout.addStretch()
        right_bar_profile_layout.addWidget(circle_label, alignment=Qt.AlignCenter)
        right_bar_profile_layout.addStretch()


        # Prediction settings
        right_bar_prediction_settings = self.coloured_frame("red")

        # Prediction result
        right_bar_prediction = self.coloured_frame("lightgray")
        right_bar_label = QLabel("Prediciton result")
        right_bar_label.setAlignment(Qt.AlignCenter)
        right_bar_prediction.layout().addWidget(right_bar_label)


        right_layout.addWidget(profile_bar, 1)
        right_layout.addWidget(right_bar_prediction_settings, 10)
        right_layout.addWidget(right_bar_prediction, 10)

        # --- Add sections to main layout ---
        main_layout.addWidget(left_bar, 1)
        main_layout.addWidget(center_frame, 15)
        main_layout.addWidget(right_frame, 3)

    def coloured_frame(self, colour, min_height=None):
        frame = QFrame()
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setAutoFillBackground(True)
        palette = frame.palette()
        palette.setColor(QPalette.Window, QColor(colour))
        frame.setPalette(palette)
        if min_height:
            frame.setMinimumHeight(min_height)
        layout = QVBoxLayout(frame)
        layout.setContentsMargins(5, 5, 5, 5)
        return frame

    def circle_bitmap(self, pixmap, diameter):
        size = min(pixmap.width(), pixmap.height())
        pixmap = pixmap.scaled(diameter, diameter, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)

        mask = QPixmap(diameter, diameter)
        mask.fill(Qt.transparent)

        painter = QPainter(mask)
        path = QPainterPath()
        path.addEllipse(0, 0, diameter, diameter)
        painter.setClipPath(path)
        painter.drawPixmap(0, 0, pixmap)
        painter.end()
        return mask

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
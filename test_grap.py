

import sys
import os

from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QColor, QPalette, QPainter, QPixmap, QPainterPath, QBrush
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout,
    QLabel, QPushButton, QFrame
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dashboard Layout Example")
        self.setGeometry(100, 100, 1500, 900)
        self.btns = {}

        ##### --- Main alignment --- #####
        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QHBoxLayout()
        central.setLayout(main_layout)

        ##### --- Left area --- #####
        left_frame = QFrame()
        left_frame.setStyleSheet("border: 1px solid black;")
        left_layout = QVBoxLayout(left_frame)
        left_layout.setContentsMargins(0,0,0,0)
        left_layout.setSpacing(0)

        left_btn_heights = 100
        self.btns["left_btns"] = []

        mouse_btn = self.make_btn("mouse_tool", "left_btns", "img_src/mouse_icon_scaled.png", height=left_btn_heights)
        line_tool_btn = self.make_btn("line_tool", "left_btns", "img_src/line_icon_scaled.png", height=left_btn_heights)
        notes_tool_btn = self.make_btn("notes_tool", "left_btns", "img_src/notes_icon_scaled.png", height=left_btn_heights)

        left_layout.addWidget(mouse_btn)
        left_layout.addWidget(line_tool_btn)
        left_layout.addWidget(notes_tool_btn)
        left_layout.addStretch()

        ##### --- Center area --- #####
        center_frame = QFrame()
        center_layout = QVBoxLayout(center_frame)

        # Top bar
        top_frame = QFrame()
        top_frame.setStyleSheet("border: 1px solid black")
        top_layout = QHBoxLayout(top_frame)
        top_layout.setContentsMargins(0,0,0,0)
        top_layout.setSpacing(0)

        top_btn_widths = 100
        self.btns["top_btns"] = []

        graph_type_icon = QPushButton()
        graph_type_icon.setCheckable(True)
        graph_type_icon.setFixedWidth(top_btn_widths)

        graph_type_icon.setStyleSheet(f"""
        QPushButton {{background-image: url('img_src/candlestick_icon_scaled.png'); background-repeat: no-repeat; background-position: center; background-color: #e3e3e3}}
        QPushButton:hover {{background-color: #adadad}}
        QPushButton:pressed {{background-image: url('img_src/line_graph_icon_scaled.png'); background-repeat: no-repeat; background-position: center; background-color: #e3e3e3}}
        """)
        graph_type_icon.clicked.connect(lambda checked, n="graph_type": self.testfunc(n))
        self.btns["top_btns"].append(graph_type_icon)

        top_layout.addWidget(graph_type_icon)
        top_layout.addStretch()
        # top_centre = self.coloured_frame("transparent")
        # top_centre_layout = QHBoxLayout(top_centre)
        # top_centre_layout.addStretch()

        # Graph area
        graph_frame = self.coloured_frame("transparent")
        graph_label = QLabel("Graph Area")
        graph_label.setAlignment(Qt.AlignCenter)
        graph_frame.layout().addWidget(graph_label)

        center_layout.addWidget(top_frame, 1)
        center_layout.addWidget(graph_frame, 10)

        ##### --- Right sidebar --- #####
        right_frame = QFrame()
        right_layout = QVBoxLayout(right_frame)

        # Profile screen
        profile_frame = QWidget()
        profile_frame.setStyleSheet("background-color: None;")
        profile_frame_layout = QVBoxLayout(profile_frame)
        profile_frame_layout.setAlignment(Qt.AlignCenter)

        circle_label = QLabel()
        pixmap = QPixmap("img_src/person_icon.jpg")
        if pixmap.isNull():
            pixmap = QPixmap(200, 200)
            pixmap.fill(Qt.gray)
        circle_pixmap = self.circle_bitmap(pixmap, 120)
        circle_label.setPixmap(circle_pixmap)
        circle_label.setAlignment(Qt.AlignCenter)

        profile_frame_layout.addWidget(circle_label, alignment=Qt.AlignCenter)

        # Prediction settings frame
        prediction_settings_frame = self.coloured_frame("transparent")

        # Prediction result
        prediction_result_frame = self.coloured_frame("transparent")
        prediction_result_label = QLabel("Prediction result")
        prediction_result_label.setAlignment(Qt.AlignCenter)
        prediction_result_frame.layout().addWidget(prediction_result_label)


        right_layout.addWidget(profile_frame, 1)
        right_layout.addWidget(prediction_settings_frame, 10)
        right_layout.addWidget(prediction_result_frame, 10)

        ##### --- Add to layout --- #####
        main_layout.addWidget(left_frame, 1)
        main_layout.addWidget(center_frame, 15)
        main_layout.addWidget(right_frame, 3)

    def testfunc(self, tool):
        print("testfunc", tool)

    def make_btn(self, name, group, icon_img, width = None, height = None):
        btn = QPushButton()
        btn.setCheckable(True)
        if height and width:
            btn.setFixedSize(width, height)
        elif height and not width:
            btn.setFixedHeight(height)
        elif width and not height:
            btn.setFixedWidth(width)

        btn.normal_img = icon_img

        btn.setStyleSheet(f"""
        QPushButton {{background-image: url('{btn.normal_img}'); background-repeat: no-repeat; background-position: center; background-color: #e3e3e3}}
        QPushButton:hover {{background-color: #adadad}} 
        """)

        btn.clicked.connect(lambda checked, b=btn, n=name: self.handle_click(b, n))
        self.btns[group].append(btn)
        return btn

    def handle_click(self, clicked_btn, name):
        for btn_arr in self.btns.values():
            for btn in btn_arr:
                if btn == clicked_btn:
                    btn.setStyleSheet(f"""QPushButton {{background-image: url('{btn.normal_img}'); background-repeat: no-repeat; background-position: center; background-color: #8a8a8a}}""")
                    self.testfunc(name)
                else:
                    btn.setChecked(False)
                    btn.setStyleSheet(f"""QPushButton {{background-image: url('{btn.normal_img}'); background-repeat: no-repeat; background-position: center; background-color: #e3e3e3}}
                                          QPushButton:hover {{background-color: #adadad}} """)



    @classmethod
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

    @classmethod
    def circle_bitmap(self, pixmap, diameter):
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

    def closeEvent(self, event) -> None:
        # for created_path in created_paths:
        #     os.remove(created_path)
        event.accept()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())

from PyQt5 import *

class xFsygGgnabP8GO5b6BFtInHswOzyg4X(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self) 
        self.setWindowTitle('Synthesizing')
    def setupUi(self, synthesizing_widget):
        synthesizing_widget.setObjectName("synthesizing_widget")
        synthesizing_widget.resize(1000, 722)
        synthesizing_widget.setMinimumSize(QtCore.QSize(0, 0))
        synthesizing_widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        synthesizing_widget.setStyleSheet("")
        self.gridLayout = QtWidgets.QGridLayout(synthesizing_widget)
        self.gridLayout.setSpacing(20)
        self.gridLayout.setContentsMargins(20, 20, 20, 20)
        self.gridLayout.setObjectName("gridLayout")
        self.boxplot_window = QtWidgets.QWidget(synthesizing_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boxplot_window.sizePolicy().hasHeightForWidth())
        self.boxplot_window.setSizePolicy(sizePolicy)
        self.boxplot_window.setMinimumSize(QtCore.QSize(0, 0))
        self.boxplot_window.setStyleSheet("QWidget#boxplot_content {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #606060, stop: 1 #B8B8B8);;\n"
"    border: 1px solid #484848;\n"
"    border-top: none;\n"
"}\n"
"")
        self.boxplot_window.setObjectName("boxplot_window")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.boxplot_window)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.resultstitle = QtWidgets.QLabel(self.boxplot_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resultstitle.sizePolicy().hasHeightForWidth())
        self.resultstitle.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.resultstitle.setFont(font)
        self.resultstitle.setStyleSheet("padding: 10px;\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #A8A8A8, stop: 1 #505050);\n"
"border: 1px solid #484848;")
        self.resultstitle.setObjectName("resultstitle")
        self.gridLayout_4.addWidget(self.resultstitle, 0, 0, 1, 1)
        self.boxplot_content = QtWidgets.QWidget(self.boxplot_window)
        self.boxplot_content.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    padding: 5px;\n"
"}")
        self.boxplot_content.setObjectName("boxplot_content")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.boxplot_content)
        self.gridLayout_5.setSpacing(10)
        self.gridLayout_5.setContentsMargins(15, 15, 15, 15)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self._gmLjkWzGXQfc4b4hF20WeFOmmm1roV = QtWidgets.QDoubleSpinBox(self.boxplot_content)
        self._gmLjkWzGXQfc4b4hF20WeFOmmm1roV.setAlignment(QtCore.Qt.AlignCenter)
        self._gmLjkWzGXQfc4b4hF20WeFOmmm1roV.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self._gmLjkWzGXQfc4b4hF20WeFOmmm1roV.setDecimals(5)
        self._gmLjkWzGXQfc4b4hF20WeFOmmm1roV.setMinimum(-99999999999.0)
        self._gmLjkWzGXQfc4b4hF20WeFOmmm1roV.setMaximum(99999999999.0)
        self._gmLjkWzGXQfc4b4hF20WeFOmmm1roV.setObjectName("plot_lowerlimit")
        self.gridLayout_5.addWidget(self._gmLjkWzGXQfc4b4hF20WeFOmmm1roV, 2, 1, 1, 1)
        self.set_limits_label = QtWidgets.QLabel(self.boxplot_content)
        self.set_limits_label.setObjectName("set_limits_label")
        self.gridLayout_5.addWidget(self.set_limits_label, 1, 0, 1, 1)
        self._QNxJCD4T7LkrmSEMyIXkWLEDGFHn0R = QtWidgets.QDoubleSpinBox(self.boxplot_content)
        self._QNxJCD4T7LkrmSEMyIXkWLEDGFHn0R.setAlignment(QtCore.Qt.AlignCenter)
        self._QNxJCD4T7LkrmSEMyIXkWLEDGFHn0R.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self._QNxJCD4T7LkrmSEMyIXkWLEDGFHn0R.setDecimals(5)
        self._QNxJCD4T7LkrmSEMyIXkWLEDGFHn0R.setMinimum(-99999999999.0)
        self._QNxJCD4T7LkrmSEMyIXkWLEDGFHn0R.setMaximum(99999999999.0)
        self._QNxJCD4T7LkrmSEMyIXkWLEDGFHn0R.setObjectName("plot_upperlimit")
        self.gridLayout_5.addWidget(self._QNxJCD4T7LkrmSEMyIXkWLEDGFHn0R, 2, 2, 1, 1)
        self._s2wIbCheVOpnbL6KIfXAyehxsbbiKV = QtWidgets.QPushButton(self.boxplot_content)
        self._s2wIbCheVOpnbL6KIfXAyehxsbbiKV.setObjectName("updateplot_button")
        self.gridLayout_5.addWidget(self._s2wIbCheVOpnbL6KIfXAyehxsbbiKV, 2, 0, 1, 1)
        self.upper_limit_label = QtWidgets.QLabel(self.boxplot_content)
        self.upper_limit_label.setObjectName("upper_limit_label")
        self.gridLayout_5.addWidget(self.upper_limit_label, 1, 2, 1, 1)
        self.lower_limit_label = QtWidgets.QLabel(self.boxplot_content)
        self.lower_limit_label.setObjectName("lower_limit_label")
        self.gridLayout_5.addWidget(self.lower_limit_label, 1, 1, 1, 1)
        self.plotwidget = QtWidgets.QWidget(self.boxplot_content)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotwidget.sizePolicy().hasHeightForWidth())
        self.plotwidget.setSizePolicy(sizePolicy)
        self.plotwidget.setStyleSheet("background: white;\n"
"border: 1px solid #484848;")
        self.plotwidget.setObjectName("plotwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.plotwidget)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_5.addWidget(self.plotwidget, 0, 0, 1, 4)
        self.se_yscale_label = QtWidgets.QLabel(self.boxplot_content)
        self.se_yscale_label.setObjectName("se_yscale_label")
        self.gridLayout_5.addWidget(self.se_yscale_label, 1, 3, 1, 1)
        self.plot_scale = QtWidgets.QComboBox(self.boxplot_content)
        self.plot_scale.setObjectName("plot_scale")
        self.plot_scale.addItem("")
        self.plot_scale.addItem("")
        self.plot_scale.addItem("")
        self.gridLayout_5.addWidget(self.plot_scale, 2, 3, 1, 1)
        self.gridLayout_4.addWidget(self.boxplot_content, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.boxplot_window, 1, 1, 2, 1)
        self.choosefile_widget = QtWidgets.QWidget(synthesizing_widget)
        self.choosefile_widget.setMinimumSize(QtCore.QSize(0, 90))
        self.choosefile_widget.setMaximumSize(QtCore.QSize(16777215, 90))
        self.choosefile_widget.setStyleSheet("QWidget#choosefile_content{\n"
"    background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #606060, stop: 1 #B8B8B8);\n"
"    border: 1px solid #484848;\n"
"    border-top: none;\n"
"}\n"
"")
        self.choosefile_widget.setObjectName("choosefile_widget")
        self.choosefile_widget_layout = QtWidgets.QGridLayout(self.choosefile_widget)
        self.choosefile_widget_layout.setSpacing(0)
        self.choosefile_widget_layout.setContentsMargins(0, 0, 0, 0)
        self.choosefile_widget_layout.setObjectName("choosefile_widget_layout")
        self.choosefile_content = QtWidgets.QWidget(self.choosefile_widget)
        self.choosefile_content.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #E0E0E0;\n"
"    padding: 5px 9px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"background-color: #C0C0C0;\n"
"}\n"
"\n"
"QComboBox{\n"
"    border: 0px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #E0E0E0, stop: 1 #FFFFFF);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView{\n"
"    padding: 2px;\n"
"    border: 1px solid black;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #E0E0E0, stop: 1 #FFFFFF);\n"
"}\n"
"\n"
"QSpinBox{\n"
"    border: 1px solid #E0E0E0;\n"
"    background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #E0E0E0, stop: 1 #FFFFFF);\n"
"}\n"
"")
        self.choosefile_content.setObjectName("choosefile_content")
        self.chosefile_content_layout = QtWidgets.QHBoxLayout(self.choosefile_content)
        self.chosefile_content_layout.setSpacing(6)
        self.chosefile_content_layout.setContentsMargins(20, 9, 20, 9)
        self.chosefile_content_layout.setObjectName("chosefile_content_layout")
        self._vRzOYIiAkEAo30sLk9ckj6Xhh791xW = QtWidgets.QLineEdit(self.choosefile_content)
        self._vRzOYIiAkEAo30sLk9ckj6Xhh791xW.setMinimumSize(QtCore.QSize(600, 0))
        self._vRzOYIiAkEAo30sLk9ckj6Xhh791xW.setMaximumSize(QtCore.QSize(450, 16777215))
        self._vRzOYIiAkEAo30sLk9ckj6Xhh791xW.setStyleSheet("")
        self._vRzOYIiAkEAo30sLk9ckj6Xhh791xW.setObjectName("filepath_label")
        self.chosefile_content_layout.addWidget(self._vRzOYIiAkEAo30sLk9ckj6Xhh791xW)
        self._Pr9TYkngN2vla6VXbLwmMkeXSZPbvh = QtWidgets.QPushButton(self.choosefile_content)
        self._Pr9TYkngN2vla6VXbLwmMkeXSZPbvh.setMinimumSize(QtCore.QSize(60, 0))
        self._Pr9TYkngN2vla6VXbLwmMkeXSZPbvh.setStyleSheet("")
        self._Pr9TYkngN2vla6VXbLwmMkeXSZPbvh.setObjectName("file_explorerbutton")
        self.chosefile_content_layout.addWidget(self._Pr9TYkngN2vla6VXbLwmMkeXSZPbvh)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.chosefile_content_layout.addItem(spacerItem)
        self._ooRZTw2PuOcqrCBLtnFhSB1NXBtAmQ = QtWidgets.QPushButton(self.choosefile_content)
        self._ooRZTw2PuOcqrCBLtnFhSB1NXBtAmQ.setMinimumSize(QtCore.QSize(100, 0))
        self._ooRZTw2PuOcqrCBLtnFhSB1NXBtAmQ.setStyleSheet("")
        self._ooRZTw2PuOcqrCBLtnFhSB1NXBtAmQ.setObjectName("startbutton")
        self.chosefile_content_layout.addWidget(self._ooRZTw2PuOcqrCBLtnFhSB1NXBtAmQ)
        self.choosefile_widget_layout.addWidget(self.choosefile_content, 2, 0, 1, 1)
        self.choosefile_titlelabel = QtWidgets.QLabel(self.choosefile_widget)
        self.choosefile_titlelabel.setMinimumSize(QtCore.QSize(0, 40))
        self.choosefile_titlelabel.setMaximumSize(QtCore.QSize(16777215, 40))
        self.choosefile_titlelabel.setStyleSheet("padding: 10px;\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #A8A8A8, stop: 1 #505050);\n"
"border: 1px solid #484848;")
        self.choosefile_titlelabel.setTextFormat(QtCore.Qt.RichText)
        self.choosefile_titlelabel.setObjectName("choosefile_titlelabel")
        self.choosefile_widget_layout.addWidget(self.choosefile_titlelabel, 0, 0, 1, 5)
        self.gridLayout.addWidget(self.choosefile_widget, 0, 0, 1, 2)
        self.resultswindow = QtWidgets.QWidget(synthesizing_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resultswindow.sizePolicy().hasHeightForWidth())
        self.resultswindow.setSizePolicy(sizePolicy)
        self.resultswindow.setMinimumSize(QtCore.QSize(0, 0))
        self.resultswindow.setStyleSheet("QWidget#results_content{\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #606060, stop: 1 #B8B8B8);;\n"
"    border: 1px solid #484848;\n"
"    border-top: none;\n"
"}\n"
"")
        self.resultswindow.setObjectName("resultswindow")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.resultswindow)
        self.gridLayout_12.setSpacing(0)
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.results_title = QtWidgets.QLabel(self.resultswindow)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.results_title.setFont(font)
        self.results_title.setStyleSheet("padding: 10px;\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #A8A8A8, stop: 1 #505050);\n"
"border: 1px solid #484848;")
        self.results_title.setObjectName("results_title")
        self.gridLayout_12.addWidget(self.results_title, 1, 0, 1, 1)
        self.results_content = QtWidgets.QWidget(self.resultswindow)
        self.results_content.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    padding: 5px;\n"
"}")
        self.results_content.setObjectName("results_content")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.results_content)
        self.gridLayout_13.setSpacing(10)
        self.gridLayout_13.setContentsMargins(15, 15, 15, 15)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self._0or7mF4jsCmc4wNpxEqPFgo9wZrGlF = QtWidgets.QTableWidget(self.results_content)
        self._0or7mF4jsCmc4wNpxEqPFgo9wZrGlF.setMinimumSize(QtCore.QSize(0, 0))
        self._0or7mF4jsCmc4wNpxEqPFgo9wZrGlF.setStyleSheet("background-color: #C0C0C0;")
        self._0or7mF4jsCmc4wNpxEqPFgo9wZrGlF.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self._0or7mF4jsCmc4wNpxEqPFgo9wZrGlF.setObjectName("results_table")
        self._0or7mF4jsCmc4wNpxEqPFgo9wZrGlF.setColumnCount(3)
        self._0or7mF4jsCmc4wNpxEqPFgo9wZrGlF.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self._0or7mF4jsCmc4wNpxEqPFgo9wZrGlF.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self._0or7mF4jsCmc4wNpxEqPFgo9wZrGlF.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self._0or7mF4jsCmc4wNpxEqPFgo9wZrGlF.setHorizontalHeaderItem(2, item)
        self._0or7mF4jsCmc4wNpxEqPFgo9wZrGlF.horizontalHeader().setCascadingSectionResizes(True)
        self._0or7mF4jsCmc4wNpxEqPFgo9wZrGlF.horizontalHeader().setDefaultSectionSize(150)
        self._0or7mF4jsCmc4wNpxEqPFgo9wZrGlF.horizontalHeader().setHighlightSections(True)
        self._0or7mF4jsCmc4wNpxEqPFgo9wZrGlF.horizontalHeader().setMinimumSectionSize(50)
        self._0or7mF4jsCmc4wNpxEqPFgo9wZrGlF.horizontalHeader().setSortIndicatorShown(True)
        self._0or7mF4jsCmc4wNpxEqPFgo9wZrGlF.horizontalHeader().setStretchLastSection(True)
        self._0or7mF4jsCmc4wNpxEqPFgo9wZrGlF.verticalHeader().setVisible(False)
        self.gridLayout_13.addWidget(self._0or7mF4jsCmc4wNpxEqPFgo9wZrGlF, 2, 1, 1, 2)
        self.gridLayout_12.addWidget(self.results_content, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.resultswindow, 2, 0, 1, 1)
        self._25hWqsf4uybsR4T3X2DGjzoZBPzb7M_widget = QtWidgets.QWidget(synthesizing_widget)
        self._25hWqsf4uybsR4T3X2DGjzoZBPzb7M_widget.setMinimumSize(QtCore.QSize(0, 90))
        self._25hWqsf4uybsR4T3X2DGjzoZBPzb7M_widget.setMaximumSize(QtCore.QSize(16777215, 90))
        self._25hWqsf4uybsR4T3X2DGjzoZBPzb7M_widget.setStyleSheet("QWidget#runtime_content{\n"
"    background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #606060, stop: 1 #B8B8B8);\n"
"    border: 1px solid #484848;\n"
"    border-top: none;\n"
"}\n"
"")
        self._25hWqsf4uybsR4T3X2DGjzoZBPzb7M_widget.setObjectName("runtime_widget")
        self.choosefile_widget_layout_2 = QtWidgets.QGridLayout(self._25hWqsf4uybsR4T3X2DGjzoZBPzb7M_widget)
        self.choosefile_widget_layout_2.setSpacing(0)
        self.choosefile_widget_layout_2.setContentsMargins(0, 0, 0, 0)
        self.choosefile_widget_layout_2.setObjectName("choosefile_widget_layout_2")
        self._25hWqsf4uybsR4T3X2DGjzoZBPzb7M_title_label = QtWidgets.QLabel(self._25hWqsf4uybsR4T3X2DGjzoZBPzb7M_widget)
        self._25hWqsf4uybsR4T3X2DGjzoZBPzb7M_title_label.setMinimumSize(QtCore.QSize(0, 40))
        self._25hWqsf4uybsR4T3X2DGjzoZBPzb7M_title_label.setMaximumSize(QtCore.QSize(16777215, 40))
        self._25hWqsf4uybsR4T3X2DGjzoZBPzb7M_title_label.setStyleSheet("padding: 10px;\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #A8A8A8, stop: 1 #505050);\n"
"border: 1px solid #484848;")
        self._25hWqsf4uybsR4T3X2DGjzoZBPzb7M_title_label.setTextFormat(QtCore.Qt.RichText)
        self._25hWqsf4uybsR4T3X2DGjzoZBPzb7M_title_label.setObjectName("runtime_title_label")
        self.choosefile_widget_layout_2.addWidget(self._25hWqsf4uybsR4T3X2DGjzoZBPzb7M_title_label, 0, 0, 1, 5)
        self._25hWqsf4uybsR4T3X2DGjzoZBPzb7M_content = QtWidgets.QWidget(self._25hWqsf4uybsR4T3X2DGjzoZBPzb7M_widget)
        self._25hWqsf4uybsR4T3X2DGjzoZBPzb7M_content.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    padding: 5px;\n"
"}")
        self._25hWqsf4uybsR4T3X2DGjzoZBPzb7M_content.setObjectName("runtime_content")
        self.chosefile_content_layout_2 = QtWidgets.QHBoxLayout(self._25hWqsf4uybsR4T3X2DGjzoZBPzb7M_content)
        self.chosefile_content_layout_2.setSpacing(6)
        self.chosefile_content_layout_2.setContentsMargins(20, 9, 20, 9)
        self.chosefile_content_layout_2.setObjectName("chosefile_content_layout_2")
        self._25hWqsf4uybsR4T3X2DGjzoZBPzb7M = QtWidgets.QLabel(self._25hWqsf4uybsR4T3X2DGjzoZBPzb7M_content)
        self._25hWqsf4uybsR4T3X2DGjzoZBPzb7M.setStyleSheet("QLabel{\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #E0E0E0, stop: 1 #FFFFFF);\n"
"    border: 1px solid black;\n"
"}")
        self._25hWqsf4uybsR4T3X2DGjzoZBPzb7M.setText("")
        self._25hWqsf4uybsR4T3X2DGjzoZBPzb7M.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self._25hWqsf4uybsR4T3X2DGjzoZBPzb7M.setObjectName("runtime")
        self.chosefile_content_layout_2.addWidget(self._25hWqsf4uybsR4T3X2DGjzoZBPzb7M)
        self.choosefile_widget_layout_2.addWidget(self._25hWqsf4uybsR4T3X2DGjzoZBPzb7M_content, 2, 0, 1, 5)
        self.gridLayout.addWidget(self._25hWqsf4uybsR4T3X2DGjzoZBPzb7M_widget, 1, 0, 1, 1)

        self.retranslateUi(synthesizing_widget)
        QtCore.QMetaObject.connectSlotsByName(synthesizing_widget)

    def retranslateUi(self, synthesizing_widget):
        _translate = QtCore.QCoreApplication.translate
        synthesizing_widget.setWindowTitle(_translate("synthesizing_widget", "Form"))
        self.resultstitle.setText(_translate("synthesizing_widget", "<html><head/><body><p><span style=\" font-weight:600;\">Box Plot</span></p></body></html>"))
        self.set_limits_label.setText(_translate("synthesizing_widget", "Set Limits"))
        self._s2wIbCheVOpnbL6KIfXAyehxsbbiKV.setText(_translate("synthesizing_widget", "Update"))
        self.upper_limit_label.setText(_translate("synthesizing_widget", "Upper Limit"))
        self.lower_limit_label.setText(_translate("synthesizing_widget", "Lower Limit"))
        self.se_yscale_label.setText(_translate("synthesizing_widget", "Set Y-Scale"))
        self.plot_scale.setItemText(0, _translate("synthesizing_widget", "Linear"))
        self.plot_scale.setItemText(1, _translate("synthesizing_widget", "Logarithmic"))
        self.plot_scale.setItemText(2, _translate("synthesizing_widget", "Symmetrical Log"))
        self._Pr9TYkngN2vla6VXbLwmMkeXSZPbvh.setText(_translate("synthesizing_widget", "Browse"))
        self._ooRZTw2PuOcqrCBLtnFhSB1NXBtAmQ.setText(_translate("synthesizing_widget", "Start"))
        self.choosefile_titlelabel.setText(_translate("synthesizing_widget", "<html><head/><body><p><span style=\" font-weight:600;\">Choose File</span></p></body></html>"))
        self.results_title.setText(_translate("synthesizing_widget", "<html><head/><body><p><span style=\" font-weight:600;\">Final Results</span></p></body></html>"))
        item = self._0or7mF4jsCmc4wNpxEqPFgo9wZrGlF.horizontalHeaderItem(0)
        item.setText(_translate("synthesizing_widget", "Node"))
        item = self._0or7mF4jsCmc4wNpxEqPFgo9wZrGlF.horizontalHeaderItem(1)
        item.setText(_translate("synthesizing_widget", "Total Items"))
        item = self._0or7mF4jsCmc4wNpxEqPFgo9wZrGlF.horizontalHeaderItem(2)
        item.setText(_translate("synthesizing_widget", "Mean"))
        self._25hWqsf4uybsR4T3X2DGjzoZBPzb7M_title_label.setText(_translate("synthesizing_widget", "<html><head/><body><p><span style=\" font-weight:600;\">Run Time</span></p></body></html>"))


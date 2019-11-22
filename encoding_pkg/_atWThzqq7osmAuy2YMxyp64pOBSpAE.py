from PyQt5 import QtCore, QtGui, QtWidgets

class E3ENNvUgGSKO5hnmfBaEfiabzrE3LO(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self




















                                                                                                                                                                                    )
        self.setupUi(self) 
        self.setWindowTitle('Encoding'




















                                                                                                                                                                                    )
    def setupUi(self, encoding_widget):
        encoding_widget.setObjectName("encoding_widget"




















                                                                                                                                                                                    )
        encoding_widget.resize(940, 669




















                                                                                                                                                                                    )
        encoding_widget.setMinimumSize(QtCore.QSize(0, 0)




















                                                                                                                                                                                    )
        encoding_widget.setMaximumSize(QtCore.QSize(16777215, 16777215)




















                                                                                                                                                                                    )
        self.gridLayout = QtWidgets.QGridLayout(encoding_widget




















                                                                                                                                                                                    )
        self.gridLayout.setSpacing(20




















                                                                                                                                                                                    )
        self.gridLayout.setContentsMargins(20, 20, 20, 20




















                                                                                                                                                                                    )
        self.gridLayout.setObjectName("gridLayout"




















                                                                                                                                                                                    )
        self.resultswindow = QtWidgets.QWidget(encoding_widget




















                                                                                                                                                                                    )
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred




















                                                                                                                                                                                    )
        sizePolicy.setHorizontalStretch(3




















                                                                                                                                                                                    )
        sizePolicy.setVerticalStretch(0




















                                                                                                                                                                                    )
        sizePolicy.setHeightForWidth(self.resultswindow.sizePolicy().hasHeightForWidth()




















                                                                                                                                                                                    )
        self.resultswindow.setSizePolicy(sizePolicy




















                                                                                                                                                                                    )
        self.resultswindow.setMinimumSize(QtCore.QSize(400, 0)




















                                                                                                                                                                                    )
        self.resultswindow.setMaximumSize(QtCore.QSize(16777215, 16777215)




















                                                                                                                                                                                    )
        self.resultswindow.setStyleSheet("QWidget#resultscontent {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #606060, stop: 1 #B8B8B8);;\n"
"    border: 1px solid #484848;\n"
"    border-top: none;\n"
"}\n"
""




                                                                                                        















                                                                                                                                                                        )
        self.resultswindow.setObjectName("resultswindow"




















                                                                                                                                                                                    )
        self.gridLayout_4 = QtWidgets.QGridLayout(self.resultswindow




















                                                                                                                                                                                    )
        self.gridLayout_4.setSpacing(0




















                                                                                                                                                                                    )
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0




















                                                                                                                                                                                    )
        self.gridLayout_4.setObjectName("gridLayout_4"




















                                                                                                                                                                                    )
        self.resultstitle = QtWidgets.QLabel(self.resultswindow




















                                                                                                                                                                                    )
        self.resultstitle.setMinimumSize(QtCore.QSize(0, 36)




















                                                                                                                                                                                    )
        self.resultstitle.setMaximumSize(QtCore.QSize(16777215, 36)




















                                                                                                                                                                                    )
        font = QtGui.QFont(




















                                                                                                                                                                                    )
        font.setFamily("Arial"




















                                                                                                                                                                                    )
        self.resultstitle.setFont(font




















                                                                                                                                                                                    )
        self.resultstitle.setStyleSheet("padding: 10px;\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #A8A8A8, stop: 1 #505050);\n"
"border: 1px solid #484848;"




                                                                                                        















                                                                                                                                                                        )
        self.resultstitle.setObjectName("resultstitle"




















                                                                                                                                                                                    )
        self.gridLayout_4.addWidget(self.resultstitle, 0, 0, 1, 1




















                                                                                                                                                                                    )
        self.resultscontent = QtWidgets.QWidget(self.resultswindow




















                                                                                                                                                                                    )
        self.resultscontent.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    padding: 5px;\n"
"}"




                                                                                                        















                                                                                                                                                                        )
        self.resultscontent.setObjectName("resultscontent"




















                                                                                                                                                                                    )
        self.gridLayout_5 = QtWidgets.QGridLayout(self.resultscontent




















                                                                                                                                                                                    )
        self.gridLayout_5.setSpacing(10




















                                                                                                                                                                                    )
        self.gridLayout_5.setContentsMargins(15, 15, 15, 15




















                                                                                                                                                                                    )
        self.gridLayout_5.setObjectName("gridLayout_5"




















                                                                                                                                                                                    )
        self.legendwidget = QtWidgets.QWidget(self.resultscontent




















                                                                                                                                                                                    )
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred




















                                                                                                                                                                                    )
        sizePolicy.setHorizontalStretch(0




















                                                                                                                                                                                    )
        sizePolicy.setVerticalStretch(0




















                                                                                                                                                                                    )
        sizePolicy.setHeightForWidth(self.legendwidget.sizePolicy().hasHeightForWidth()




















                                                                                                                                                                                    )
        self.legendwidget.setSizePolicy(sizePolicy




















                                                                                                                                                                                    )
        self.legendwidget.setStyleSheet("QWidget {\n"
"    background: transparent;\n"
"}\n"
"QLabel{\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #E0E0E0, stop: 1 #FFFFFF);\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QWidget#legendwidget{\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #B8B8B8, stop: 1 #606060);;\n"
"    border: 1px solid #606060;\n"
"}"




                                                                                                        















                                                                                                                                                                        )
        self.legendwidget.setObjectName("legendwidget"




















                                                                                                                                                                                    )
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.legendwidget




















                                                                                                                                                                                    )
        self.horizontalLayout.setSpacing(0




















                                                                                                                                                                                    )
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1




















                                                                                                                                                                                    )
        self.horizontalLayout.setObjectName("horizontalLayout"




















                                                                                                                                                                                    )
        self.legend_label = QtWidgets.QLabel(self.legendwidget




















                                                                                                                                                                                    )
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred




















                                                                                                                                                                                    )
        sizePolicy.setHorizontalStretch(0




















                                                                                                                                                                                    )
        sizePolicy.setVerticalStretch(0




















                                                                                                                                                                                    )
        sizePolicy.setHeightForWidth(self.legend_label.sizePolicy().hasHeightForWidth()




















                                                                                                                                                                                    )
        self.legend_label.setSizePolicy(sizePolicy




















                                                                                                                                                                                    )
        font = QtGui.QFont(




















                                                                                                                                                                                    )
        font.setFamily("Arial"




















                                                                                                                                                                                    )
        self.legend_label.setFont(font




















                                                                                                                                                                                    )
        self.legend_label.setStyleSheet("background: transparent;\n"
"border: 0px;"




                                                                                                        















                                                                                                                                                                        )
        self.legend_label.setObjectName("legend_label"




















                                                                                                                                                                                    )
        self.horizontalLayout.addWidget(self.legend_label




















                                                                                                                                                                                    )
        self.a_legendlabel = QtWidgets.QLabel(self.legendwidget




















                                                                                                                                                                                    )
        self.a_legendlabel.setStyleSheet("border-right: 0px;\n"
""




                                                                                                        















                                                                                                                                                                        )
        self.a_legendlabel.setObjectName("a_legendlabel"




















                                                                                                                                                                                    )
        self.horizontalLayout.addWidget(self.a_legendlabel




















                                                                                                                                                                                    )
        self.a_legendbounds = QtWidgets.QLabel(self.legendwidget




















                                                                                                                                                                                    )
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred




















                                                                                                                                                                                    )
        sizePolicy.setHorizontalStretch(0




















                                                                                                                                                                                    )
        sizePolicy.setVerticalStretch(0




















                                                                                                                                                                                    )
        sizePolicy.setHeightForWidth(self.a_legendbounds.sizePolicy().hasHeightForWidth()




















                                                                                                                                                                                    )
        self.a_legendbounds.setSizePolicy(sizePolicy




















                                                                                                                                                                                    )
        self.a_legendbounds.setStyleSheet(""




















                                                                                                                                                                                    )
        self.a_legendbounds.setObjectName("a_legendbounds"




















                                                                                                                                                                                    )
        self.horizontalLayout.addWidget(self.a_legendbounds




















                                                                                                                                                                                    )
        self.b_legendlabel = QtWidgets.QLabel(self.legendwidget




















                                                                                                                                                                                    )
        self.b_legendlabel.setStyleSheet("border-right: 0px;\n"
"margin-left: 9px;"




                                                                                                        















                                                                                                                                                                        )
        self.b_legendlabel.setObjectName("b_legendlabel"




















                                                                                                                                                                                    )
        self.horizontalLayout.addWidget(self.b_legendlabel




















                                                                                                                                                                                    )
        self.b_legendbounds = QtWidgets.QLabel(self.legendwidget




















                                                                                                                                                                                    )
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred




















                                                                                                                                                                                    )
        sizePolicy.setHorizontalStretch(0




















                                                                                                                                                                                    )
        sizePolicy.setVerticalStretch(0




















                                                                                                                                                                                    )
        sizePolicy.setHeightForWidth(self.b_legendbounds.sizePolicy().hasHeightForWidth()




















                                                                                                                                                                                    )
        self.b_legendbounds.setSizePolicy(sizePolicy




















                                                                                                                                                                                    )
        self.b_legendbounds.setObjectName("b_legendbounds"




















                                                                                                                                                                                    )
        self.horizontalLayout.addWidget(self.b_legendbounds




















                                                                                                                                                                                    )
        self.c_legendlabel = QtWidgets.QLabel(self.legendwidget




















                                                                                                                                                                                    )
        self.c_legendlabel.setStyleSheet("border-right: 0px;\n"
"margin-left: 9px;"




                                                                                                        















                                                                                                                                                                        )
        self.c_legendlabel.setObjectName("c_legendlabel"




















                                                                                                                                                                                    )
        self.horizontalLayout.addWidget(self.c_legendlabel




















                                                                                                                                                                                    )
        self.c_legendbounds = QtWidgets.QLabel(self.legendwidget




















                                                                                                                                                                                    )
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred




















                                                                                                                                                                                    )
        sizePolicy.setHorizontalStretch(0




















                                                                                                                                                                                    )
        sizePolicy.setVerticalStretch(0




















                                                                                                                                                                                    )
        sizePolicy.setHeightForWidth(self.c_legendbounds.sizePolicy().hasHeightForWidth()




















                                                                                                                                                                                    )
        self.c_legendbounds.setSizePolicy(sizePolicy




















                                                                                                                                                                                    )
        self.c_legendbounds.setObjectName("c_legendbounds"




















                                                                                                                                                                                    )
        self.horizontalLayout.addWidget(self.c_legendbounds




















                                                                                                                                                                                    )
        self.d_legendlabel = QtWidgets.QLabel(self.legendwidget




















                                                                                                                                                                                    )
        self.d_legendlabel.setStyleSheet("border-right: 0px;\n"
"margin-left: 9px;"




                                                                                                        















                                                                                                                                                                        )
        self.d_legendlabel.setObjectName("d_legendlabel"




















                                                                                                                                                                                    )
        self.horizontalLayout.addWidget(self.d_legendlabel




















                                                                                                                                                                                    )
        self.d_legendbounds = QtWidgets.QLabel(self.legendwidget




















                                                                                                                                                                                    )
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred




















                                                                                                                                                                                    )
        sizePolicy.setHorizontalStretch(0




















                                                                                                                                                                                    )
        sizePolicy.setVerticalStretch(0




















                                                                                                                                                                                    )
        sizePolicy.setHeightForWidth(self.d_legendbounds.sizePolicy().hasHeightForWidth()




















                                                                                                                                                                                    )
        self.d_legendbounds.setSizePolicy(sizePolicy




















                                                                                                                                                                                    )
        self.d_legendbounds.setObjectName("d_legendbounds"




















                                                                                                                                                                                    )
        self.horizontalLayout.addWidget(self.d_legendbounds




















                                                                                                                                                                                    )
        self.e_legendlabel = QtWidgets.QLabel(self.legendwidget




















                                                                                                                                                                                    )
        self.e_legendlabel.setStyleSheet("border-right: 0px;\n"
"margin-left: 9px;"




                                                                                                        















                                                                                                                                                                        )
        self.e_legendlabel.setObjectName("e_legendlabel"




















                                                                                                                                                                                    )
        self.horizontalLayout.addWidget(self.e_legendlabel




















                                                                                                                                                                                    )
        self.e_legendbounds = QtWidgets.QLabel(self.legendwidget




















                                                                                                                                                                                    )
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred




















                                                                                                                                                                                    )
        sizePolicy.setHorizontalStretch(0




















                                                                                                                                                                                    )
        sizePolicy.setVerticalStretch(0




















                                                                                                                                                                                    )
        sizePolicy.setHeightForWidth(self.e_legendbounds.sizePolicy().hasHeightForWidth()




















                                                                                                                                                                                    )
        self.e_legendbounds.setSizePolicy(sizePolicy




















                                                                                                                                                                                    )
        self.e_legendbounds.setStyleSheet(""




















                                                                                                                                                                                    )
        self.e_legendbounds.setObjectName("e_legendbounds"




















                                                                                                                                                                                    )
        self.horizontalLayout.addWidget(self.e_legendbounds




















                                                                                                                                                                                    )
        self.gridLayout_5.addWidget(self.legendwidget, 0, 1, 1, 2




















                                                                                                                                                                                    )
        self._Q2eFZefYli03STJlToHLvxnTRDWIut_widget = QtWidgets.QWidget(self.resultscontent




















                                                                                                                                                                                    )
        self._Q2eFZefYli03STJlToHLvxnTRDWIut_widget.setStyleSheet("QWidget {\n"
"    background: transparent;\n"
"}\n"
"QLabel{\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #E0E0E0, stop: 1 #FFFFFF);\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QWidget#runtime_widget{\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #B8B8B8, stop: 1 #606060);;\n"
"    border: 1px solid #606060;\n"
"}"




                                                                                                        















                                                                                                                                                                        )
        self._Q2eFZefYli03STJlToHLvxnTRDWIut_widget.setObjectName("runtime_widget"




















                                                                                                                                                                                    )
        self.gridLayout_10 = QtWidgets.QGridLayout(self._Q2eFZefYli03STJlToHLvxnTRDWIut_widget




















                                                                                                                                                                                    )
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0




















                                                                                                                                                                                    )
        self.gridLayout_10.setObjectName("gridLayout_10"




















                                                                                                                                                                                    )
        self._Q2eFZefYli03STJlToHLvxnTRDWIut_label = QtWidgets.QLabel(self._Q2eFZefYli03STJlToHLvxnTRDWIut_widget




















                                                                                                                                                                                    )
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred




















                                                                                                                                                                                    )
        sizePolicy.setHorizontalStretch(0




















                                                                                                                                                                                    )
        sizePolicy.setVerticalStretch(0




















                                                                                                                                                                                    )
        sizePolicy.setHeightForWidth(self._Q2eFZefYli03STJlToHLvxnTRDWIut_label.sizePolicy().hasHeightForWidth()




















                                                                                                                                                                                    )
        self._Q2eFZefYli03STJlToHLvxnTRDWIut_label.setSizePolicy(sizePolicy




















                                                                                                                                                                                    )
        self._Q2eFZefYli03STJlToHLvxnTRDWIut_label.setStyleSheet("background: transparent;\n"
"border: 0px;"




                                                                                                        















                                                                                                                                                                        )
        self._Q2eFZefYli03STJlToHLvxnTRDWIut_label.setObjectName("runtime_label"




















                                                                                                                                                                                    )
        self.gridLayout_10.addWidget(self._Q2eFZefYli03STJlToHLvxnTRDWIut_label, 0, 0, 1, 1




















                                                                                                                                                                                    )
        self._Q2eFZefYli03STJlToHLvxnTRDWIut = QtWidgets.QLabel(self._Q2eFZefYli03STJlToHLvxnTRDWIut_widget




















                                                                                                                                                                                    )
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred




















                                                                                                                                                                                    )
        sizePolicy.setHorizontalStretch(0




















                                                                                                                                                                                    )
        sizePolicy.setVerticalStretch(0




















                                                                                                                                                                                    )
        sizePolicy.setHeightForWidth(self._Q2eFZefYli03STJlToHLvxnTRDWIut.sizePolicy().hasHeightForWidth()




















                                                                                                                                                                                    )
        self._Q2eFZefYli03STJlToHLvxnTRDWIut.setSizePolicy(sizePolicy




















                                                                                                                                                                                    )
        self._Q2eFZefYli03STJlToHLvxnTRDWIut.setText(""




















                                                                                                                                                                                    )
        self._Q2eFZefYli03STJlToHLvxnTRDWIut.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse




















                                                                                                                                                                                    )
        self._Q2eFZefYli03STJlToHLvxnTRDWIut.setObjectName("runtime"




















                                                                                                                                                                                    )
        self.gridLayout_10.addWidget(self._Q2eFZefYli03STJlToHLvxnTRDWIut, 0, 1, 1, 1




















                                                                                                                                                                                    )
        self.gridLayout_5.addWidget(self._Q2eFZefYli03STJlToHLvxnTRDWIut_widget, 1, 1, 1, 2




















                                                                                                                                                                                    )
        self.results_table = QtWidgets.QTableWidget(self.resultscontent




















                                                                                                                                                                                    )
        self.results_table.setMinimumSize(QtCore.QSize(0, 0)




















                                                                                                                                                                                    )
        self.results_table.setStyleSheet("background-color: #C0C0C0;"




















                                                                                                                                                                                    )
        self.results_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers




















                                                                                                                                                                                    )
        self.results_table.setObjectName("results_table"




















                                                                                                                                                                                    )
        self.results_table.setColumnCount(1




















                                                                                                                                                                                    )
        self.results_table.setRowCount(0




















                                                                                                                                                                                    )
        item = QtWidgets.QTableWidgetItem(




















                                                                                                                                                                                    )
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter




















                                                                                                                                                                                    )
        self.results_table.setHorizontalHeaderItem(0, item




















                                                                                                                                                                                    )
        self.results_table.horizontalHeader().setCascadingSectionResizes(True




















                                                                                                                                                                                    )
        self.results_table.horizontalHeader().setDefaultSectionSize(200




















                                                                                                                                                                                    )
        self.results_table.horizontalHeader().setHighlightSections(True




















                                                                                                                                                                                    )
        self.results_table.horizontalHeader().setMinimumSectionSize(50




















                                                                                                                                                                                    )
        self.results_table.horizontalHeader().setSortIndicatorShown(True




















                                                                                                                                                                                    )
        self.results_table.horizontalHeader().setStretchLastSection(True




















                                                                                                                                                                                    )
        self.results_table.verticalHeader().setVisible(False




















                                                                                                                                                                                    )
        self.gridLayout_5.addWidget(self.results_table, 3, 1, 1, 2




















                                                                                                                                                                                    )
        self.gridLayout_4.addWidget(self.resultscontent, 1, 0, 1, 1




















                                                                                                                                                                                    )
        self.gridLayout.addWidget(self.resultswindow, 0, 1, 4, 1




















                                                                                                                                                                                    )
        self.frequencieswindow = QtWidgets.QWidget(encoding_widget




















                                                                                                                                                                                    )
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred




















                                                                                                                                                                                    )
        sizePolicy.setHorizontalStretch(2




















                                                                                                                                                                                    )
        sizePolicy.setVerticalStretch(0




















                                                                                                                                                                                    )
        sizePolicy.setHeightForWidth(self.frequencieswindow.sizePolicy().hasHeightForWidth()




















                                                                                                                                                                                    )
        self.frequencieswindow.setSizePolicy(sizePolicy




















                                                                                                                                                                                    )
        self.frequencieswindow.setStyleSheet("QWidget#frequenciescontent {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #606060, stop: 1 #B8B8B8);;\n"
"    border: 1px solid #484848;\n"
"    border-top: none;\n"
"}\n"
""




                                                                                                        















                                                                                                                                                                        )
        self.frequencieswindow.setObjectName("frequencieswindow"




















                                                                                                                                                                                    )
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frequencieswindow




















                                                                                                                                                                                    )
        self.gridLayout_3.setSpacing(0




















                                                                                                                                                                                    )
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0




















                                                                                                                                                                                    )
        self.gridLayout_3.setObjectName("gridLayout_3"




















                                                                                                                                                                                    )
        self.frequenciescontent = QtWidgets.QWidget(self.frequencieswindow




















                                                                                                                                                                                    )
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum




















                                                                                                                                                                                    )
        sizePolicy.setHorizontalStretch(0




















                                                                                                                                                                                    )
        sizePolicy.setVerticalStretch(1




















                                                                                                                                                                                    )
        sizePolicy.setHeightForWidth(self.frequenciescontent.sizePolicy().hasHeightForWidth()




















                                                                                                                                                                                    )
        self.frequenciescontent.setSizePolicy(sizePolicy




















                                                                                                                                                                                    )
        self.frequenciescontent.setMinimumSize(QtCore.QSize(200, 200)




















                                                                                                                                                                                    )
        self.frequenciescontent.setMaximumSize(QtCore.QSize(16777215, 16777215)




















                                                                                                                                                                                    )
        self.frequenciescontent.setObjectName("frequenciescontent"




















                                                                                                                                                                                    )
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frequenciescontent




















                                                                                                                                                                                    )
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0




















                                                                                                                                                                                    )
        self.gridLayout_7.setObjectName("gridLayout_7"




















                                                                                                                                                                                    )
        self.gridLayout_3.addWidget(self.frequenciescontent, 2, 0, 1, 1




















                                                                                                                                                                                    )
        self.frequenciestitle = QtWidgets.QLabel(self.frequencieswindow




















                                                                                                                                                                                    )
        self.frequenciestitle.setMinimumSize(QtCore.QSize(0, 36)




















                                                                                                                                                                                    )
        self.frequenciestitle.setMaximumSize(QtCore.QSize(16777215, 36)




















                                                                                                                                                                                    )
        font = QtGui.QFont(




















                                                                                                                                                                                    )
        font.setFamily("Arial"




















                                                                                                                                                                                    )
        self.frequenciestitle.setFont(font




















                                                                                                                                                                                    )
        self.frequenciestitle.setStyleSheet("padding: 10px;\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #A8A8A8, stop: 1 #505050);\n"
"border: 1px solid #484848;"




                                                                                                        















                                                                                                                                                                        )
        self.frequenciestitle.setObjectName("frequenciestitle"




















                                                                                                                                                                                    )
        self.gridLayout_3.addWidget(self.frequenciestitle, 1, 0, 1, 1




















                                                                                                                                                                                    )
        self.gridLayout.addWidget(self.frequencieswindow, 2, 0, 2, 1




















                                                                                                                                                                                    )
        self.settingswindow = QtWidgets.QWidget(encoding_widget




















                                                                                                                                                                                    )
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred




















                                                                                                                                                                                    )
        sizePolicy.setHorizontalStretch(2




















                                                                                                                                                                                    )
        sizePolicy.setVerticalStretch(0




















                                                                                                                                                                                    )
        sizePolicy.setHeightForWidth(self.settingswindow.sizePolicy().hasHeightForWidth()




















                                                                                                                                                                                    )
        self.settingswindow.setSizePolicy(sizePolicy




















                                                                                                                                                                                    )
        self.settingswindow.setMaximumSize(QtCore.QSize(16777215, 16777215)




















                                                                                                                                                                                    )
        self.settingswindow.setStyleSheet("QWidget#settingscontent {\n"
"    background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #606060, stop: 1 #B8B8B8);\n"
"    border: 1px solid #484848;\n"
"    border-top: none;\n"
"}\n"
""




                                                                                                        















                                                                                                                                                                        )
        self.settingswindow.setObjectName("settingswindow"




















                                                                                                                                                                                    )
        self.gridLayout_2 = QtWidgets.QGridLayout(self.settingswindow




















                                                                                                                                                                                    )
        self.gridLayout_2.setSpacing(0




















                                                                                                                                                                                    )
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0




















                                                                                                                                                                                    )
        self.gridLayout_2.setObjectName("gridLayout_2"




















                                                                                                                                                                                    )
        self.settingstitle = QtWidgets.QLabel(self.settingswindow




















                                                                                                                                                                                    )
        self.settingstitle.setMinimumSize(QtCore.QSize(0, 36)




















                                                                                                                                                                                    )
        self.settingstitle.setMaximumSize(QtCore.QSize(16777215, 36)




















                                                                                                                                                                                    )
        font = QtGui.QFont(




















                                                                                                                                                                                    )
        font.setFamily("Arial"




















                                                                                                                                                                                    )
        self.settingstitle.setFont(font




















                                                                                                                                                                                    )
        self.settingstitle.setStyleSheet("padding: 10px;\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #A8A8A8, stop: 1 #505050);\n"
"border: 1px solid #484848;"




                                                                                                        















                                                                                                                                                                        )
        self.settingstitle.setObjectName("settingstitle"




















                                                                                                                                                                                    )
        self.gridLayout_2.addWidget(self.settingstitle, 0, 0, 1, 1




















                                                                                                                                                                                    )
        self.settingscontent = QtWidgets.QWidget(self.settingswindow




















                                                                                                                                                                                    )
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred




















                                                                                                                                                                                    )
        sizePolicy.setHorizontalStretch(0




















                                                                                                                                                                                    )
        sizePolicy.setVerticalStretch(1




















                                                                                                                                                                                    )
        sizePolicy.setHeightForWidth(self.settingscontent.sizePolicy().hasHeightForWidth()




















                                                                                                                                                                                    )
        self.settingscontent.setSizePolicy(sizePolicy




















                                                                                                                                                                                    )
        self.settingscontent.setMinimumSize(QtCore.QSize(0, 0)




















                                                                                                                                                                                    )
        self.settingscontent.setMaximumSize(QtCore.QSize(16777215, 16777215)




















                                                                                                                                                                                    )
        self.settingscontent.setStyleSheet("QLabel {\n"
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
""




                                                                                                        















                                                                                                                                                                        )
        self.settingscontent.setObjectName("settingscontent"




















                                                                                                                                                                                    )
        self.gridLayout_8 = QtWidgets.QGridLayout(self.settingscontent




















                                                                                                                                                                                    )
        self.gridLayout_8.setContentsMargins(15, 10, 15, 15




















                                                                                                                                                                                    )
        self.gridLayout_8.setHorizontalSpacing(9




















                                                                                                                                                                                    )
        self.gridLayout_8.setVerticalSpacing(2




















                                                                                                                                                                                    )
        self.gridLayout_8.setObjectName("gridLayout_8"




















                                                                                                                                                                                    )
        self.inputfile = QtWidgets.QLineEdit(self.settingscontent




















                                                                                                                                                                                    )
        self.inputfile.setMinimumSize(QtCore.QSize(100, 25)




















                                                                                                                                                                                    )
        self.inputfile.setMaximumSize(QtCore.QSize(16777215, 25)




















                                                                                                                                                                                    )
        self.inputfile.setMouseTracking(False




















                                                                                                                                                                                    )
        self.inputfile.setStyleSheet("padding-left: 2px;\n"
"padding-right: 2px;"




                                                                                                        















                                                                                                                                                                        )
        self.inputfile.setReadOnly(True




















                                                                                                                                                                                    )
        self.inputfile.setObjectName("inputfile"




















                                                                                                                                                                                    )
        self.gridLayout_8.addWidget(self.inputfile, 1, 0, 1, 3




















                                                                                                                                                                                    )
        self.inputfile_label = QtWidgets.QLabel(self.settingscontent




















                                                                                                                                                                                    )
        font = QtGui.QFont(




















                                                                                                                                                                                    )
        font.setFamily("Arial"




















                                                                                                                                                                                    )
        self.inputfile_label.setFont(font




















                                                                                                                                                                                    )
        self.inputfile_label.setObjectName("inputfile_label"




















                                                                                                                                                                                    )
        self.gridLayout_8.addWidget(self.inputfile_label, 0, 0, 1, 4




















                                                                                                                                                                                    )
        self._tLnkLDZWQwYUeBDgoEFeYq0AjRpzQh = QtWidgets.QComboBox(self.settingscontent




















                                                                                                                                                                                    )
        self._tLnkLDZWQwYUeBDgoEFeYq0AjRpzQh.setMinimumSize(QtCore.QSize(166, 25)




















                                                                                                                                                                                    )
        self._tLnkLDZWQwYUeBDgoEFeYq0AjRpzQh.setMaximumSize(QtCore.QSize(16777215, 25)




















                                                                                                                                                                                    )
        self._tLnkLDZWQwYUeBDgoEFeYq0AjRpzQh.setObjectName("datatype"




















                                                                                                                                                                                    )
        self._tLnkLDZWQwYUeBDgoEFeYq0AjRpzQh.addItem(""




















                                                                                                                                                                                    )
        self._tLnkLDZWQwYUeBDgoEFeYq0AjRpzQh.addItem(""




















                                                                                                                                                                                    )
        self.gridLayout_8.addWidget(self._tLnkLDZWQwYUeBDgoEFeYq0AjRpzQh, 7, 0, 1, 2




















                                                                                                                                                                                    )
        self._tLnkLDZWQwYUeBDgoEFeYq0AjRpzQh_label = QtWidgets.QLabel(self.settingscontent




















                                                                                                                                                                                    )
        self._tLnkLDZWQwYUeBDgoEFeYq0AjRpzQh_label.setMinimumSize(QtCore.QSize(166, 0)




















                                                                                                                                                                                    )
        self._tLnkLDZWQwYUeBDgoEFeYq0AjRpzQh_label.setMaximumSize(QtCore.QSize(166, 16777215)




















                                                                                                                                                                                    )
        font = QtGui.QFont(




















                                                                                                                                                                                    )
        font.setFamily("Arial"




















                                                                                                                                                                                    )
        self._tLnkLDZWQwYUeBDgoEFeYq0AjRpzQh_label.setFont(font




















                                                                                                                                                                                    )
        self._tLnkLDZWQwYUeBDgoEFeYq0AjRpzQh_label.setObjectName("datatype_label"




















                                                                                                                                                                                    )
        self.gridLayout_8.addWidget(self._tLnkLDZWQwYUeBDgoEFeYq0AjRpzQh_label, 6, 0, 1, 2




















                                                                                                                                                                                    )
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding




















                                                                                                                                                                                    )
        self.gridLayout_8.addItem(spacerItem, 9, 0, 1, 1




















                                                                                                                                                                                    )
        self._Z6ukXiaZPRay7FWBzVwZbfPw3308Gk = QtWidgets.QPushButton(self.settingscontent




















                                                                                                                                                                                    )
        self._Z6ukXiaZPRay7FWBzVwZbfPw3308Gk.setMinimumSize(QtCore.QSize(166, 25)




















                                                                                                                                                                                    )
        self._Z6ukXiaZPRay7FWBzVwZbfPw3308Gk.setMaximumSize(QtCore.QSize(16777215, 25)




















                                                                                                                                                                                    )
        self._Z6ukXiaZPRay7FWBzVwZbfPw3308Gk.setStyleSheet("margin-top: 4px;"




















                                                                                                                                                                                    )
        self._Z6ukXiaZPRay7FWBzVwZbfPw3308Gk.setObjectName("startbutton"




















                                                                                                                                                                                    )
        self.gridLayout_8.addWidget(self._Z6ukXiaZPRay7FWBzVwZbfPw3308Gk, 11, 0, 1, 2




















                                                                                                                                                                                    )
        self._lA0iZhCGslvE1JMm7gfhC6nWQyCmkj = QtWidgets.QWidget(self.settingscontent




















                                                                                                                                                                                    )
        self._lA0iZhCGslvE1JMm7gfhC6nWQyCmkj.setEnabled(True




















                                                                                                                                                                                    )
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding




















                                                                                                                                                                                    )
        sizePolicy.setHorizontalStretch(0




















                                                                                                                                                                                    )
        sizePolicy.setVerticalStretch(0




















                                                                                                                                                                                    )
        sizePolicy.setHeightForWidth(self._lA0iZhCGslvE1JMm7gfhC6nWQyCmkj.sizePolicy().hasHeightForWidth()




















                                                                                                                                                                                    )
        self._lA0iZhCGslvE1JMm7gfhC6nWQyCmkj.setSizePolicy(sizePolicy




















                                                                                                                                                                                    )
        self._lA0iZhCGslvE1JMm7gfhC6nWQyCmkj.setMinimumSize(QtCore.QSize(225, 233)




















                                                                                                                                                                                    )
        self._lA0iZhCGslvE1JMm7gfhC6nWQyCmkj.setStyleSheet("QWidget#noncategoricalsettings {\n"
"    background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #606060, stop: 1 #B8B8B8);\n"
"    border: 1px solid #606060;\n"
"    margin-top: 5px;\n"
"}"




                                                                                                        















                                                                                                                                                                        )
        self._lA0iZhCGslvE1JMm7gfhC6nWQyCmkj.setObjectName("noncategoricalsettings"




















                                                                                                                                                                                    )
        self.gridLayout_6 = QtWidgets.QGridLayout(self._lA0iZhCGslvE1JMm7gfhC6nWQyCmkj




















                                                                                                                                                                                    )
        self.gridLayout_6.setContentsMargins(-1, 15, -1, -1




















                                                                                                                                                                                    )
        self.gridLayout_6.setObjectName("gridLayout_6"




















                                                                                                                                                                                    )
        self._MJLzbvu0qucO8F83zmecRbni5ufH9L_label = QtWidgets.QLabel(self._lA0iZhCGslvE1JMm7gfhC6nWQyCmkj




















                                                                                                                                                                                    )
        self._MJLzbvu0qucO8F83zmecRbni5ufH9L_label.setObjectName("discretizations_label"




















                                                                                                                                                                                    )
        self.gridLayout_6.addWidget(self._MJLzbvu0qucO8F83zmecRbni5ufH9L_label, 0, 0, 1, 1




















                                                                                                                                                                                    )
        self._MJLzbvu0qucO8F83zmecRbni5ufH9L = QtWidgets.QComboBox(self._lA0iZhCGslvE1JMm7gfhC6nWQyCmkj




















                                                                                                                                                                                    )
        self._MJLzbvu0qucO8F83zmecRbni5ufH9L.setStyleSheet("padding: 3px;"




















                                                                                                                                                                                    )
        self._MJLzbvu0qucO8F83zmecRbni5ufH9L.setObjectName("discretizations"




















                                                                                                                                                                                    )
        self._MJLzbvu0qucO8F83zmecRbni5ufH9L.addItem(""




















                                                                                                                                                                                    )
        self._MJLzbvu0qucO8F83zmecRbni5ufH9L.addItem(""




















                                                                                                                                                                                    )
        self._MJLzbvu0qucO8F83zmecRbni5ufH9L.addItem(""




















                                                                                                                                                                                    )
        self._MJLzbvu0qucO8F83zmecRbni5ufH9L.addItem(""




















                                                                                                                                                                                    )
        self._MJLzbvu0qucO8F83zmecRbni5ufH9L.addItem(""




















                                                                                                                                                                                    )
        self.gridLayout_6.addWidget(self._MJLzbvu0qucO8F83zmecRbni5ufH9L, 0, 1, 1, 1




















                                                                                                                                                                                    )
        self._sg4YrXPMPQn3hELetTQOQcopanxwsc = QtWidgets.QWidget(self._lA0iZhCGslvE1JMm7gfhC6nWQyCmkj




















                                                                                                                                                                                    )
        self._sg4YrXPMPQn3hELetTQOQcopanxwsc.setMinimumSize(QtCore.QSize(100, 100)




















                                                                                                                                                                                    )
        self._sg4YrXPMPQn3hELetTQOQcopanxwsc.setStyleSheet("QWidget#expertsettings{\n"
"    background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #606060, stop: 1 #B8B8B8);\n"
"    border: 1px solid #606060;\n"
"}"




                                                                                                        















                                                                                                                                                                        )
        self._sg4YrXPMPQn3hELetTQOQcopanxwsc.setObjectName("expertsettings"




















                                                                                                                                                                                    )
        self.gridLayout_9 = QtWidgets.QGridLayout(self._sg4YrXPMPQn3hELetTQOQcopanxwsc




















                                                                                                                                                                                    )
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0




















                                                                                                                                                                                    )
        self.gridLayout_9.setObjectName("gridLayout_9"




















                                                                                                                                                                                    )
        self.b_label = QtWidgets.QLabel(self._sg4YrXPMPQn3hELetTQOQcopanxwsc




















                                                                                                                                                                                    )
        self.b_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter




















                                                                                                                                                                                    )
        self.b_label.setObjectName("b_label"




















                                                                                                                                                                                    )
        self.gridLayout_9.addWidget(self.b_label, 3, 0, 1, 1




















                                                                                                                                                                                    )
        self.c_label = QtWidgets.QLabel(self._sg4YrXPMPQn3hELetTQOQcopanxwsc




















                                                                                                                                                                                    )
        self.c_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter




















                                                                                                                                                                                    )
        self.c_label.setObjectName("c_label"




















                                                                                                                                                                                    )
        self.gridLayout_9.addWidget(self.c_label, 5, 0, 1, 1




















                                                                                                                                                                                    )
        self.d_label = QtWidgets.QLabel(self._sg4YrXPMPQn3hELetTQOQcopanxwsc




















                                                                                                                                                                                    )
        self.d_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter




















                                                                                                                                                                                    )
        self.d_label.setObjectName("d_label"




















                                                                                                                                                                                    )
        self.gridLayout_9.addWidget(self.d_label, 6, 0, 1, 1




















                                                                                                                                                                                    )
        self.a_label = QtWidgets.QLabel(self._sg4YrXPMPQn3hELetTQOQcopanxwsc




















                                                                                                                                                                                    )
        self.a_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter




















                                                                                                                                                                                    )
        self.a_label.setWordWrap(False




















                                                                                                                                                                                    )
        self.a_label.setObjectName("a_label"




















                                                                                                                                                                                    )
        self.gridLayout_9.addWidget(self.a_label, 1, 0, 1, 1




















                                                                                                                                                                                    )
        self.e_label = QtWidgets.QLabel(self._sg4YrXPMPQn3hELetTQOQcopanxwsc




















                                                                                                                                                                                    )
        self.e_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter




















                                                                                                                                                                                    )
        self.e_label.setObjectName("e_label"




















                                                                                                                                                                                    )
        self.gridLayout_9.addWidget(self.e_label, 7, 0, 1, 1




















                                                                                                                                                                                    )
        self.upperbound_label = QtWidgets.QLabel(self._sg4YrXPMPQn3hELetTQOQcopanxwsc




















                                                                                                                                                                                    )
        self.upperbound_label.setObjectName("upperbound_label"




















                                                                                                                                                                                    )
        self.gridLayout_9.addWidget(self.upperbound_label, 0, 2, 1, 1




















                                                                                                                                                                                    )
        self.lowerbound_label = QtWidgets.QLabel(self._sg4YrXPMPQn3hELetTQOQcopanxwsc




















                                                                                                                                                                                    )
        self.lowerbound_label.setObjectName("lowerbound_label"




















                                                                                                                                                                                    )
        self.gridLayout_9.addWidget(self.lowerbound_label, 0, 1, 1, 1




















                                                                                                                                                                                    )
        self.a_lowerbound = QtWidgets.QSpinBox(self._sg4YrXPMPQn3hELetTQOQcopanxwsc




















                                                                                                                                                                                    )
        self.a_lowerbound.setAlignment(QtCore.Qt.AlignCenter




















                                                                                                                                                                                    )
        self.a_lowerbound.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons




















                                                                                                                                                                                    )
        self.a_lowerbound.setMaximum(999999999




















                                                                                                                                                                                    )
        self.a_lowerbound.setProperty("value", 0




















                                                                                                                                                                                    )
        self.a_lowerbound.setObjectName("a_lowerbound"




















                                                                                                                                                                                    )
        self.gridLayout_9.addWidget(self.a_lowerbound, 1, 1, 1, 1




















                                                                                                                                                                                    )
        self.a_upperbound = QtWidgets.QSpinBox(self._sg4YrXPMPQn3hELetTQOQcopanxwsc




















                                                                                                                                                                                    )
        self.a_upperbound.setAlignment(QtCore.Qt.AlignCenter




















                                                                                                                                                                                    )
        self.a_upperbound.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons




















                                                                                                                                                                                    )
        self.a_upperbound.setMaximum(999999999




















                                                                                                                                                                                    )
        self.a_upperbound.setObjectName("a_upperbound"




















                                                                                                                                                                                    )
        self.gridLayout_9.addWidget(self.a_upperbound, 1, 2, 1, 1




















                                                                                                                                                                                    )
        self.b_upperbound = QtWidgets.QSpinBox(self._sg4YrXPMPQn3hELetTQOQcopanxwsc




















                                                                                                                                                                                    )
        self.b_upperbound.setAlignment(QtCore.Qt.AlignCenter




















                                                                                                                                                                                    )
        self.b_upperbound.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons




















                                                                                                                                                                                    )
        self.b_upperbound.setMaximum(999999999




















                                                                                                                                                                                    )
        self.b_upperbound.setObjectName("b_upperbound"




















                                                                                                                                                                                    )
        self.gridLayout_9.addWidget(self.b_upperbound, 3, 2, 1, 1




















                                                                                                                                                                                    )
        self.b_lowerbound = QtWidgets.QSpinBox(self._sg4YrXPMPQn3hELetTQOQcopanxwsc




















                                                                                                                                                                                    )
        self.b_lowerbound.setAlignment(QtCore.Qt.AlignCenter




















                                                                                                                                                                                    )
        self.b_lowerbound.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons




















                                                                                                                                                                                    )
        self.b_lowerbound.setMaximum(999999999




















                                                                                                                                                                                    )
        self.b_lowerbound.setObjectName("b_lowerbound"




















                                                                                                                                                                                    )
        self.gridLayout_9.addWidget(self.b_lowerbound, 3, 1, 1, 1




















                                                                                                                                                                                    )
        self.c_upperbound = QtWidgets.QSpinBox(self._sg4YrXPMPQn3hELetTQOQcopanxwsc




















                                                                                                                                                                                    )
        self.c_upperbound.setAlignment(QtCore.Qt.AlignCenter




















                                                                                                                                                                                    )
        self.c_upperbound.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons




















                                                                                                                                                                                    )
        self.c_upperbound.setMaximum(999999999




















                                                                                                                                                                                    )
        self.c_upperbound.setObjectName("c_upperbound"




















                                                                                                                                                                                    )
        self.gridLayout_9.addWidget(self.c_upperbound, 5, 2, 1, 1




















                                                                                                                                                                                    )
        self.d_lowerbound = QtWidgets.QSpinBox(self._sg4YrXPMPQn3hELetTQOQcopanxwsc




















                                                                                                                                                                                    )
        self.d_lowerbound.setAlignment(QtCore.Qt.AlignCenter




















                                                                                                                                                                                    )
        self.d_lowerbound.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons




















                                                                                                                                                                                    )
        self.d_lowerbound.setMaximum(999999999




















                                                                                                                                                                                    )
        self.d_lowerbound.setObjectName("d_lowerbound"




















                                                                                                                                                                                    )
        self.gridLayout_9.addWidget(self.d_lowerbound, 6, 1, 1, 1




















                                                                                                                                                                                    )
        self.d_upperbound = QtWidgets.QSpinBox(self._sg4YrXPMPQn3hELetTQOQcopanxwsc




















                                                                                                                                                                                    )
        self.d_upperbound.setAlignment(QtCore.Qt.AlignCenter




















                                                                                                                                                                                    )
        self.d_upperbound.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons




















                                                                                                                                                                                    )
        self.d_upperbound.setMaximum(999999999




















                                                                                                                                                                                    )
        self.d_upperbound.setObjectName("d_upperbound"




















                                                                                                                                                                                    )
        self.gridLayout_9.addWidget(self.d_upperbound, 6, 2, 1, 1




















                                                                                                                                                                                    )
        self.e_lowerbound = QtWidgets.QSpinBox(self._sg4YrXPMPQn3hELetTQOQcopanxwsc




















                                                                                                                                                                                    )
        self.e_lowerbound.setAlignment(QtCore.Qt.AlignCenter




















                                                                                                                                                                                    )
        self.e_lowerbound.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons




















                                                                                                                                                                                    )
        self.e_lowerbound.setMaximum(999999999




















                                                                                                                                                                                    )
        self.e_lowerbound.setObjectName("e_lowerbound"




















                                                                                                                                                                                    )
        self.gridLayout_9.addWidget(self.e_lowerbound, 7, 1, 1, 1




















                                                                                                                                                                                    )
        self.e_upperbound = QtWidgets.QSpinBox(self._sg4YrXPMPQn3hELetTQOQcopanxwsc




















                                                                                                                                                                                    )
        self.e_upperbound.setAlignment(QtCore.Qt.AlignCenter




















                                                                                                                                                                                    )
        self.e_upperbound.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons




















                                                                                                                                                                                    )
        self.e_upperbound.setMaximum(999999999




















                                                                                                                                                                                    )
        self.e_upperbound.setObjectName("e_upperbound"




















                                                                                                                                                                                    )
        self.gridLayout_9.addWidget(self.e_upperbound, 7, 2, 1, 1




















                                                                                                                                                                                    )
        self.c_lowerbound = QtWidgets.QSpinBox(self._sg4YrXPMPQn3hELetTQOQcopanxwsc




















                                                                                                                                                                                    )
        self.c_lowerbound.setAlignment(QtCore.Qt.AlignCenter




















                                                                                                                                                                                    )
        self.c_lowerbound.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons




















                                                                                                                                                                                    )
        self.c_lowerbound.setMaximum(999999999




















                                                                                                                                                                                    )
        self.c_lowerbound.setObjectName("c_lowerbound"




















                                                                                                                                                                                    )
        self.gridLayout_9.addWidget(self.c_lowerbound, 5, 1, 1, 1




















                                                                                                                                                                                    )
        self.gridLayout_6.addWidget(self._sg4YrXPMPQn3hELetTQOQcopanxwsc, 1, 0, 1, 2




















                                                                                                                                                                                    )
        self.gridLayout_8.addWidget(self._lA0iZhCGslvE1JMm7gfhC6nWQyCmkj, 4, 2, 8, 3




















                                                                                                                                                                                    )
        self._LjSNqBco1zsObpjEmgU3vBsD7tkSua = QtWidgets.QPushButton(self.settingscontent




















                                                                                                                                                                                    )
        self._LjSNqBco1zsObpjEmgU3vBsD7tkSua.setMinimumSize(QtCore.QSize(55, 25)




















                                                                                                                                                                                    )
        self._LjSNqBco1zsObpjEmgU3vBsD7tkSua.setMaximumSize(QtCore.QSize(55, 25)




















                                                                                                                                                                                    )
        self._LjSNqBco1zsObpjEmgU3vBsD7tkSua.setObjectName("browsebutton"




















                                                                                                                                                                                    )
        self.gridLayout_8.addWidget(self._LjSNqBco1zsObpjEmgU3vBsD7tkSua, 1, 4, 1, 1




















                                                                                                                                                                                    )
        self.gridLayout_2.addWidget(self.settingscontent, 1, 0, 1, 1




















                                                                                                                                                                                    )
        self.gridLayout.addWidget(self.settingswindow, 0, 0, 2, 1




















                                                                                                                                                                                    )

        self.retranslateUi(encoding_widget




















                                                                                                                                                                                    )
        QtCore.QMetaObject.connectSlotsByName(encoding_widget




















                                                                                                                                                                                    )

    def retranslateUi(self, encoding_widget):
        _translate = QtCore.QCoreApplication.translate
        encoding_widget.setWindowTitle(_translate("encoding_widget", "Form")




















                                                                                                                                                                                    )
        self.resultstitle.setText(_translate("encoding_widget", "<html><head/><body><p><span style=\" font-weight:600;\">Results</span></p></body></html>")




















                                                                                                                                                                                    )
        self.legend_label.setText(_translate("encoding_widget", "Legend")




















                                                                                                                                                                                    )
        self.a_legendlabel.setText(_translate("encoding_widget", "<html><head/><body><p><span style=\" font-weight:600;\">A</span></p></body></html>")




















                                                                                                                                                                                    )
        self.a_legendbounds.setText(_translate("encoding_widget", "<html><head/><body><p><span style=\" font-style:italic;\">n/a</span></p></body></html>")




















                                                                                                                                                                                    )
        self.b_legendlabel.setText(_translate("encoding_widget", "<html><head/><body><p><span style=\" font-weight:600;\">B</span></p></body></html>")




















                                                                                                                                                                                    )
        self.b_legendbounds.setText(_translate("encoding_widget", "<html><head/><body><p><span style=\" font-style:italic;\">n/a</span></p></body></html>")




















                                                                                                                                                                                    )
        self.c_legendlabel.setText(_translate("encoding_widget", "<html><head/><body><p><span style=\" font-weight:600;\">C</span></p></body></html>")




















                                                                                                                                                                                    )
        self.c_legendbounds.setText(_translate("encoding_widget", "<html><head/><body><p><span style=\" font-style:italic;\">n/a</span></p></body></html>")




















                                                                                                                                                                                    )
        self.d_legendlabel.setText(_translate("encoding_widget", "<html><head/><body><p><span style=\" font-weight:600;\">D</span></p></body></html>")




















                                                                                                                                                                                    )
        self.d_legendbounds.setText(_translate("encoding_widget", "<html><head/><body><p><span style=\" font-style:italic;\">n/a</span></p></body></html>")




















                                                                                                                                                                                    )
        self.e_legendlabel.setText(_translate("encoding_widget", "<html><head/><body><p><span style=\" font-weight:600;\">E</span></p></body></html>")




















                                                                                                                                                                                    )
        self.e_legendbounds.setText(_translate("encoding_widget", "<html><head/><body><p><span style=\" font-style:italic;\">n/a</span></p></body></html>")




















                                                                                                                                                                                    )
        self._Q2eFZefYli03STJlToHLvxnTRDWIut_label.setText(_translate("encoding_widget", "Run Time")




















                                                                                                                                                                                    )
        item = self.results_table.horizontalHeaderItem(0




















                                                                                                                                                                                    )
        item.setText(_translate("encoding_widget", "Encoded Expression")




















                                                                                                                                                                                    )
        self.frequenciestitle.setText(_translate("encoding_widget", "<html><head/><body><p><span style=\" font-weight:600;\">Frequencies</span></p></body></html>")




















                                                                                                                                                                                    )
        self.settingstitle.setText(_translate("encoding_widget", "<html><head/><body><p><span style=\" font-weight:600;\">Settings</span></p></body></html>")




















                                                                                                                                                                                    )
        self.inputfile_label.setText(_translate("encoding_widget", "Input File")




















                                                                                                                                                                                    )
        self._tLnkLDZWQwYUeBDgoEFeYq0AjRpzQh.setItemText(0, _translate("encoding_widget", "Non-Categorical")




















                                                                                                                                                                                    )
        self._tLnkLDZWQwYUeBDgoEFeYq0AjRpzQh.setItemText(1, _translate("encoding_widget", "Categorical")




















                                                                                                                                                                                    )
        self._tLnkLDZWQwYUeBDgoEFeYq0AjRpzQh_label.setText(_translate("encoding_widget", "Data Type")




















                                                                                                                                                                                    )
        self._Z6ukXiaZPRay7FWBzVwZbfPw3308Gk.setText(_translate("encoding_widget", "Start")




















                                                                                                                                                                                    )
        self._MJLzbvu0qucO8F83zmecRbni5ufH9L_label.setText(_translate("encoding_widget", "Discretizations")




















                                                                                                                                                                                    )
        self._MJLzbvu0qucO8F83zmecRbni5ufH9L.setItemText(0, _translate("encoding_widget", "2")




















                                                                                                                                                                                    )
        self._MJLzbvu0qucO8F83zmecRbni5ufH9L.setItemText(1, _translate("encoding_widget", "3")




















                                                                                                                                                                                    )
        self._MJLzbvu0qucO8F83zmecRbni5ufH9L.setItemText(2, _translate("encoding_widget", "4")




















                                                                                                                                                                                    )
        self._MJLzbvu0qucO8F83zmecRbni5ufH9L.setItemText(3, _translate("encoding_widget", "5")




















                                                                                                                                                                                    )
        self._MJLzbvu0qucO8F83zmecRbni5ufH9L.setItemText(4, _translate("encoding_widget", "Expert")




















                                                                                                                                                                                    )
        self.b_label.setText(_translate("encoding_widget", "B")




















                                                                                                                                                                                    )
        self.c_label.setText(_translate("encoding_widget", "C")




















                                                                                                                                                                                    )
        self.d_label.setText(_translate("encoding_widget", "D")




















                                                                                                                                                                                    )
        self.a_label.setText(_translate("encoding_widget", "A")




















                                                                                                                                                                                    )
        self.e_label.setText(_translate("encoding_widget", "E")




















                                                                                                                                                                                    )
        self.upperbound_label.setText(_translate("encoding_widget", "Upperbound")




















                                                                                                                                                                                    )
        self.lowerbound_label.setText(_translate("encoding_widget", "Lowerbound")




















                                                                                                                                                                                    )
        self._LjSNqBco1zsObpjEmgU3vBsD7tkSua.setText(_translate("encoding_widget", "Browse")




















                                                                                                                                                                                    )


from PyQt5 import *

class xNuznGpiYaw6qrLaVeTAuxsgPY4BOgO(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self) 
        self.setWindowTitle('Categorization')
    def setupUi(self, categorization_widget):
        categorization_widget.setObjectName("categorization_widget")
        categorization_widget.resize(1000, 722)
        categorization_widget.setMinimumSize(QtCore.QSize(0, 0))
        categorization_widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        categorization_widget.setStyleSheet("")
        self.gridLayout = QtWidgets.QGridLayout(categorization_widget)
        self.gridLayout.setSpacing(20)
        self.gridLayout.setContentsMargins(20, 20, 20, 20)
        self.gridLayout.setObjectName("gridLayout")
        self.artificial_nodes_window = QtWidgets.QWidget(categorization_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.artificial_nodes_window.sizePolicy().hasHeightForWidth())
        self.artificial_nodes_window.setSizePolicy(sizePolicy)
        self.artificial_nodes_window.setMinimumSize(QtCore.QSize(0, 0))
        self.artificial_nodes_window.setStyleSheet("QWidget#artificial_nodes_content {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #606060, stop: 1 #B8B8B8);;\n"
"    border: 1px solid #484848;\n"
"    border-top: none;\n"
"}\n"
"")
        self.artificial_nodes_window.setObjectName("artificial_nodes_window")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.artificial_nodes_window)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.artifical_nodes_title = QtWidgets.QLabel(self.artificial_nodes_window)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.artifical_nodes_title.setFont(font)
        self.artifical_nodes_title.setStyleSheet("padding: 10px;\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #A8A8A8, stop: 1 #505050);\n"
"border: 1px solid #484848;")
        self.artifical_nodes_title.setObjectName("artifical_nodes_title")
        self.gridLayout_4.addWidget(self.artifical_nodes_title, 0, 0, 1, 1)
        self.artificial_nodes_content = QtWidgets.QWidget(self.artificial_nodes_window)
        self.artificial_nodes_content.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    padding: 5px;\n"
"}")
        self.artificial_nodes_content.setObjectName("artificial_nodes_content")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.artificial_nodes_content)
        self.gridLayout_5.setSpacing(10)
        self.gridLayout_5.setContentsMargins(15, 15, 15, 15)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self._9sFzevNYeAJq045IX3LNXSxE2Tok0r = QtWidgets.QTableWidget(self.artificial_nodes_content)
        self._9sFzevNYeAJq045IX3LNXSxE2Tok0r.setMinimumSize(QtCore.QSize(0, 0))
        self._9sFzevNYeAJq045IX3LNXSxE2Tok0r.setStyleSheet("background-color: #C0C0C0;")
        self._9sFzevNYeAJq045IX3LNXSxE2Tok0r.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self._9sFzevNYeAJq045IX3LNXSxE2Tok0r.setObjectName("artificial_nodes_table")
        self._9sFzevNYeAJq045IX3LNXSxE2Tok0r.setColumnCount(1)
        self._9sFzevNYeAJq045IX3LNXSxE2Tok0r.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self._9sFzevNYeAJq045IX3LNXSxE2Tok0r.setHorizontalHeaderItem(0, item)
        self._9sFzevNYeAJq045IX3LNXSxE2Tok0r.horizontalHeader().setCascadingSectionResizes(True)
        self._9sFzevNYeAJq045IX3LNXSxE2Tok0r.horizontalHeader().setDefaultSectionSize(300)
        self._9sFzevNYeAJq045IX3LNXSxE2Tok0r.horizontalHeader().setHighlightSections(True)
        self._9sFzevNYeAJq045IX3LNXSxE2Tok0r.horizontalHeader().setMinimumSectionSize(50)
        self._9sFzevNYeAJq045IX3LNXSxE2Tok0r.horizontalHeader().setSortIndicatorShown(True)
        self._9sFzevNYeAJq045IX3LNXSxE2Tok0r.horizontalHeader().setStretchLastSection(True)
        self._9sFzevNYeAJq045IX3LNXSxE2Tok0r.verticalHeader().setVisible(False)
        self.gridLayout_5.addWidget(self._9sFzevNYeAJq045IX3LNXSxE2Tok0r, 2, 1, 1, 2)
        self.gridLayout_4.addWidget(self.artificial_nodes_content, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.artificial_nodes_window, 2, 1, 1, 1)
        self.runtime_widget = QtWidgets.QWidget(categorization_widget)
        self.runtime_widget.setMinimumSize(QtCore.QSize(0, 0))
        self.runtime_widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.runtime_widget.setStyleSheet("QWidget#runtime_content{\n"
"    background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #606060, stop: 1 #B8B8B8);\n"
"    border: 1px solid #484848;\n"
"    border-top: none;\n"
"}\n"
"")
        self.runtime_widget.setObjectName("runtime_widget")
        self.choosefile_widget_layout_2 = QtWidgets.QGridLayout(self.runtime_widget)
        self.choosefile_widget_layout_2.setSpacing(0)
        self.choosefile_widget_layout_2.setContentsMargins(0, 0, 0, 0)
        self.choosefile_widget_layout_2.setObjectName("choosefile_widget_layout_2")
        self.runtime_title_label = QtWidgets.QLabel(self.runtime_widget)
        self.runtime_title_label.setMinimumSize(QtCore.QSize(0, 40))
        self.runtime_title_label.setMaximumSize(QtCore.QSize(16777215, 40))
        self.runtime_title_label.setStyleSheet("padding: 10px;\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #A8A8A8, stop: 1 #505050);\n"
"border: 1px solid #484848;")
        self.runtime_title_label.setTextFormat(QtCore.Qt.RichText)
        self.runtime_title_label.setObjectName("runtime_title_label")
        self.choosefile_widget_layout_2.addWidget(self.runtime_title_label, 0, 0, 1, 4)
        self.runtime_content = QtWidgets.QWidget(self.runtime_widget)
        self.runtime_content.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    padding: 5px;\n"
"}")
        self.runtime_content.setObjectName("runtime_content")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.runtime_content)
        self.gridLayout_2.setContentsMargins(20, 9, 20, 9)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self._UXuEeGCFJgBY8hxMA7ZDg9mqM2RDUp = QtWidgets.QLabel(self.runtime_content)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._UXuEeGCFJgBY8hxMA7ZDg9mqM2RDUp.sizePolicy().hasHeightForWidth())
        self._UXuEeGCFJgBY8hxMA7ZDg9mqM2RDUp.setSizePolicy(sizePolicy)
        self._UXuEeGCFJgBY8hxMA7ZDg9mqM2RDUp.setStyleSheet("QLabel{\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #E0E0E0, stop: 1 #FFFFFF);\n"
"    border: 1px solid black;\n"
"}")
        self._UXuEeGCFJgBY8hxMA7ZDg9mqM2RDUp.setText("")
        self._UXuEeGCFJgBY8hxMA7ZDg9mqM2RDUp.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self._UXuEeGCFJgBY8hxMA7ZDg9mqM2RDUp.setObjectName("categorization_runtime")
        self.gridLayout_2.addWidget(self._UXuEeGCFJgBY8hxMA7ZDg9mqM2RDUp, 1, 1, 1, 1)
        self._UXuEeGCFJgBY8hxMA7ZDg9mqM2RDUp_label = QtWidgets.QLabel(self.runtime_content)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._UXuEeGCFJgBY8hxMA7ZDg9mqM2RDUp_label.sizePolicy().hasHeightForWidth())
        self._UXuEeGCFJgBY8hxMA7ZDg9mqM2RDUp_label.setSizePolicy(sizePolicy)
        self._UXuEeGCFJgBY8hxMA7ZDg9mqM2RDUp_label.setObjectName("categorization_runtime_label")
        self.gridLayout_2.addWidget(self._UXuEeGCFJgBY8hxMA7ZDg9mqM2RDUp_label, 0, 1, 1, 1)
        self._RqMthmX3AZ7Uto7cLSM4LGCgxJRAO9_label = QtWidgets.QLabel(self.runtime_content)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._RqMthmX3AZ7Uto7cLSM4LGCgxJRAO9_label.sizePolicy().hasHeightForWidth())
        self._RqMthmX3AZ7Uto7cLSM4LGCgxJRAO9_label.setSizePolicy(sizePolicy)
        self._RqMthmX3AZ7Uto7cLSM4LGCgxJRAO9_label.setObjectName("node_selection_runtime_label")
        self.gridLayout_2.addWidget(self._RqMthmX3AZ7Uto7cLSM4LGCgxJRAO9_label, 0, 2, 1, 1)
        self._RqMthmX3AZ7Uto7cLSM4LGCgxJRAO9 = QtWidgets.QLabel(self.runtime_content)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._RqMthmX3AZ7Uto7cLSM4LGCgxJRAO9.sizePolicy().hasHeightForWidth())
        self._RqMthmX3AZ7Uto7cLSM4LGCgxJRAO9.setSizePolicy(sizePolicy)
        self._RqMthmX3AZ7Uto7cLSM4LGCgxJRAO9.setStyleSheet("QLabel{\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #E0E0E0, stop: 1 #FFFFFF);\n"
"    border: 1px solid black;\n"
"}")
        self._RqMthmX3AZ7Uto7cLSM4LGCgxJRAO9.setText("")
        self._RqMthmX3AZ7Uto7cLSM4LGCgxJRAO9.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self._RqMthmX3AZ7Uto7cLSM4LGCgxJRAO9.setObjectName("node_selection_runtime")
        self.gridLayout_2.addWidget(self._RqMthmX3AZ7Uto7cLSM4LGCgxJRAO9, 1, 2, 1, 1)
        self.choosefile_widget_layout_2.addWidget(self.runtime_content, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.runtime_widget, 1, 0, 1, 2)
        self.choosefile_widget = QtWidgets.QWidget(categorization_widget)
        self.choosefile_widget.setMinimumSize(QtCore.QSize(0, 0))
        self.choosefile_widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
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
        self.gridLayout_3 = QtWidgets.QGridLayout(self.choosefile_content)
        self.gridLayout_3.setContentsMargins(20, 9, 20, 9)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self._wDiz2I79UfSU2EyoqyZ1k0yphMW4xf = QtWidgets.QPushButton(self.choosefile_content)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._wDiz2I79UfSU2EyoqyZ1k0yphMW4xf.sizePolicy().hasHeightForWidth())
        self._wDiz2I79UfSU2EyoqyZ1k0yphMW4xf.setSizePolicy(sizePolicy)
        self._wDiz2I79UfSU2EyoqyZ1k0yphMW4xf.setMinimumSize(QtCore.QSize(60, 0))
        self._wDiz2I79UfSU2EyoqyZ1k0yphMW4xf.setMaximumSize(QtCore.QSize(30, 16777215))
        self._wDiz2I79UfSU2EyoqyZ1k0yphMW4xf.setStyleSheet("")
        self._wDiz2I79UfSU2EyoqyZ1k0yphMW4xf.setObjectName("inputfile_explorerbutton")
        self.gridLayout_3.addWidget(self._wDiz2I79UfSU2EyoqyZ1k0yphMW4xf, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 5, 2, 1)
        self.input_file_label = QtWidgets.QLabel(self.choosefile_content)
        self.input_file_label.setObjectName("input_file_label")
        self.gridLayout_3.addWidget(self.input_file_label, 0, 0, 1, 1)
        self._7YjqUIzZuQRJN47RhRsY0jF2AXbI1p = QtWidgets.QPushButton(self.choosefile_content)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._7YjqUIzZuQRJN47RhRsY0jF2AXbI1p.sizePolicy().hasHeightForWidth())
        self._7YjqUIzZuQRJN47RhRsY0jF2AXbI1p.setSizePolicy(sizePolicy)
        self._7YjqUIzZuQRJN47RhRsY0jF2AXbI1p.setMinimumSize(QtCore.QSize(100, 0))
        self._7YjqUIzZuQRJN47RhRsY0jF2AXbI1p.setMaximumSize(QtCore.QSize(100, 16777215))
        self._7YjqUIzZuQRJN47RhRsY0jF2AXbI1p.setStyleSheet("")
        self._7YjqUIzZuQRJN47RhRsY0jF2AXbI1p.setObjectName("startbutton")
        self.gridLayout_3.addWidget(self._7YjqUIzZuQRJN47RhRsY0jF2AXbI1p, 0, 7, 1, 1)
        self._Jr6Qcp4H3XkYMJ6JLkrWAWauwuoiDU = QtWidgets.QLineEdit(self.choosefile_content)
        self._Jr6Qcp4H3XkYMJ6JLkrWAWauwuoiDU.setMinimumSize(QtCore.QSize(100, 0))
        self._Jr6Qcp4H3XkYMJ6JLkrWAWauwuoiDU.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self._Jr6Qcp4H3XkYMJ6JLkrWAWauwuoiDU.setStyleSheet("")
        self._Jr6Qcp4H3XkYMJ6JLkrWAWauwuoiDU.setObjectName("input_filepath_label")
        self.gridLayout_3.addWidget(self._Jr6Qcp4H3XkYMJ6JLkrWAWauwuoiDU, 0, 1, 1, 1)
        self.choosefile_widget_layout.addWidget(self.choosefile_content, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.choosefile_widget, 0, 0, 1, 2)
        self.categorized_strings_window = QtWidgets.QWidget(categorization_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.categorized_strings_window.sizePolicy().hasHeightForWidth())
        self.categorized_strings_window.setSizePolicy(sizePolicy)
        self.categorized_strings_window.setMinimumSize(QtCore.QSize(0, 0))
        self.categorized_strings_window.setStyleSheet("QWidget#categorized_strings_content{\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #606060, stop: 1 #B8B8B8);;\n"
"    border: 1px solid #484848;\n"
"    border-top: none;\n"
"}\n"
"")
        self.categorized_strings_window.setObjectName("categorized_strings_window")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.categorized_strings_window)
        self.gridLayout_12.setSpacing(0)
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.categorized_strings_title = QtWidgets.QLabel(self.categorized_strings_window)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.categorized_strings_title.setFont(font)
        self.categorized_strings_title.setStyleSheet("padding: 10px;\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #A8A8A8, stop: 1 #505050);\n"
"border: 1px solid #484848;")
        self.categorized_strings_title.setObjectName("categorized_strings_title")
        self.gridLayout_12.addWidget(self.categorized_strings_title, 1, 0, 1, 1)
        self.categorized_strings_content = QtWidgets.QWidget(self.categorized_strings_window)
        self.categorized_strings_content.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    padding: 5px;\n"
"}")
        self.categorized_strings_content.setObjectName("categorized_strings_content")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.categorized_strings_content)
        self.gridLayout_13.setSpacing(10)
        self.gridLayout_13.setContentsMargins(15, 15, 15, 15)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self._TyAtA8fKagkesFqN23znCX28kTkKzl = QtWidgets.QTableWidget(self.categorized_strings_content)
        self._TyAtA8fKagkesFqN23znCX28kTkKzl.setMinimumSize(QtCore.QSize(0, 0))
        self._TyAtA8fKagkesFqN23znCX28kTkKzl.setStyleSheet("background-color: #C0C0C0;")
        self._TyAtA8fKagkesFqN23znCX28kTkKzl.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self._TyAtA8fKagkesFqN23znCX28kTkKzl.setObjectName("categorized_strings_table")
        self._TyAtA8fKagkesFqN23znCX28kTkKzl.setColumnCount(3)
        self._TyAtA8fKagkesFqN23znCX28kTkKzl.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self._TyAtA8fKagkesFqN23znCX28kTkKzl.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self._TyAtA8fKagkesFqN23znCX28kTkKzl.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self._TyAtA8fKagkesFqN23znCX28kTkKzl.setHorizontalHeaderItem(2, item)
        self._TyAtA8fKagkesFqN23znCX28kTkKzl.horizontalHeader().setCascadingSectionResizes(True)
        self._TyAtA8fKagkesFqN23znCX28kTkKzl.horizontalHeader().setDefaultSectionSize(150)
        self._TyAtA8fKagkesFqN23znCX28kTkKzl.horizontalHeader().setHighlightSections(True)
        self._TyAtA8fKagkesFqN23znCX28kTkKzl.horizontalHeader().setMinimumSectionSize(50)
        self._TyAtA8fKagkesFqN23znCX28kTkKzl.horizontalHeader().setSortIndicatorShown(True)
        self._TyAtA8fKagkesFqN23znCX28kTkKzl.horizontalHeader().setStretchLastSection(True)
        self._TyAtA8fKagkesFqN23znCX28kTkKzl.verticalHeader().setVisible(False)
        self.gridLayout_13.addWidget(self._TyAtA8fKagkesFqN23znCX28kTkKzl, 2, 1, 1, 2)
        self.gridLayout_12.addWidget(self.categorized_strings_content, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.categorized_strings_window, 2, 0, 1, 1)

        self.retranslateUi(categorization_widget)
        QtCore.QMetaObject.connectSlotsByName(categorization_widget)

    def retranslateUi(self, categorization_widget):
        _translate = QtCore.QCoreApplication.translate
        categorization_widget.setWindowTitle(_translate("categorization_widget", "Form"))
        self.artifical_nodes_title.setText(_translate("categorization_widget", "<html><head/><body><p><span style=\" font-weight:600;\">Artificial Nodes</span></p></body></html>"))
        item = self._9sFzevNYeAJq045IX3LNXSxE2Tok0r.horizontalHeaderItem(0)
        item.setText(_translate("categorization_widget", "Regex"))
        self.runtime_title_label.setText(_translate("categorization_widget", "<html><head/><body><p><span style=\" font-weight:600;\">Run Time</span></p></body></html>"))
        self._UXuEeGCFJgBY8hxMA7ZDg9mqM2RDUp_label.setText(_translate("categorization_widget", "Categorization"))
        self._RqMthmX3AZ7Uto7cLSM4LGCgxJRAO9_label.setText(_translate("categorization_widget", "Selecting Minimal Sub Hierarchy"))
        self.choosefile_titlelabel.setText(_translate("categorization_widget", "<html><head/><body><p><span style=\" font-weight:600;\">Choose File</span></p></body></html>"))
        self._wDiz2I79UfSU2EyoqyZ1k0yphMW4xf.setText(_translate("categorization_widget", "Browse"))
        self.input_file_label.setText(_translate("categorization_widget", "Input File"))
        self._7YjqUIzZuQRJN47RhRsY0jF2AXbI1p.setText(_translate("categorization_widget", "Start"))
        self.categorized_strings_title.setText(_translate("categorization_widget", "<html><head/><body><p><span style=\" font-weight:600;\">Categorized Strings</span></p></body></html>"))
        item = self._TyAtA8fKagkesFqN23znCX28kTkKzl.horizontalHeaderItem(0)
        item.setText(_translate("categorization_widget", "String"))
        item = self._TyAtA8fKagkesFqN23znCX28kTkKzl.horizontalHeaderItem(1)
        item.setText(_translate("categorization_widget", "Regex"))
        item = self._TyAtA8fKagkesFqN23znCX28kTkKzl.horizontalHeaderItem(2)
        item.setText(_translate("categorization_widget", "Distance"))


from PyQt5 import *

class xNgJJbSWGEwAUkGPbKotLWcOrKOTPeh(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)     
        self.setWindowTitle('Fitness of Statistical Tests')
    def setupUi(self, fitness_of_statistical_tests_widget):
        fitness_of_statistical_tests_widget.setObjectName("fitness_of_statistical_tests_widget")
        fitness_of_statistical_tests_widget.resize(1343, 802)
        fitness_of_statistical_tests_widget.setMinimumSize(QtCore.QSize(0, 0))
        fitness_of_statistical_tests_widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        fitness_of_statistical_tests_widget.setStyleSheet("")
        self.gridLayout = QtWidgets.QGridLayout(fitness_of_statistical_tests_widget)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setContentsMargins(9, 9, 9, 9)
        self.gridLayout.setObjectName("gridLayout")
        self.resultslisting_widget_R = QtWidgets.QWidget(fitness_of_statistical_tests_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resultslisting_widget_R.sizePolicy().hasHeightForWidth())
        self.resultslisting_widget_R.setSizePolicy(sizePolicy)
        self.resultslisting_widget_R.setMinimumSize(QtCore.QSize(100, 0))
        self.resultslisting_widget_R.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.resultslisting_widget_R.setStyleSheet("QWidget#resultslisting_content_2{\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #606060, stop: 1 #B8B8B8);;\n"
"    border: 1px solid #484848;\n"
"    border-top: none;\n"
"}\n"
"")
        self.resultslisting_widget_R.setObjectName("resultslisting_widget_R")
        self.resultslisting_widget_R_layout = QtWidgets.QGridLayout(self.resultslisting_widget_R)
        self.resultslisting_widget_R_layout.setSpacing(0)
        self.resultslisting_widget_R_layout.setContentsMargins(0, 0, 0, 0)
        self.resultslisting_widget_R_layout.setObjectName("resultslisting_widget_R_layout")
        self.resultslisting_titlelabel_R = QtWidgets.QLabel(self.resultslisting_widget_R)
        self.resultslisting_titlelabel_R.setMinimumSize(QtCore.QSize(0, 40))
        self.resultslisting_titlelabel_R.setMaximumSize(QtCore.QSize(16777215, 40))
        self.resultslisting_titlelabel_R.setStyleSheet("padding: 10px;\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #A8A8A8, stop: 1 #505050);\n"
"border: 1px solid #484848;")
        self.resultslisting_titlelabel_R.setTextFormat(QtCore.Qt.RichText)
        self.resultslisting_titlelabel_R.setObjectName("resultslisting_titlelabel_R")
        self.resultslisting_widget_R_layout.addWidget(self.resultslisting_titlelabel_R, 0, 0, 1, 1)
        self.resultslisting_content_R = QtWidgets.QWidget(self.resultslisting_widget_R)
        self.resultslisting_content_R.setMinimumSize(QtCore.QSize(0, 0))
        self.resultslisting_content_R.setStyleSheet("QWidget#resultslisting_content_R{\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #606060, stop: 1 #B8B8B8);;\n"
"    border: 1px solid #484848;\n"
"    border-top: none;\n"
"}\n"
"")
        self.resultslisting_content_R.setObjectName("resultslisting_content_R")
        self.resultslisting_content_R_layout = QtWidgets.QGridLayout(self.resultslisting_content_R)
        self.resultslisting_content_R_layout.setSpacing(0)
        self.resultslisting_content_R_layout.setContentsMargins(0, 0, 0, 0)
        self.resultslisting_content_R_layout.setObjectName("resultslisting_content_R_layout")
        self._C0xbVaTqnfwVR0xv0QIssY0cByBe1L = QtWidgets.QListWidget(self.resultslisting_content_R)
        self._C0xbVaTqnfwVR0xv0QIssY0cByBe1L.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self._C0xbVaTqnfwVR0xv0QIssY0cByBe1L.setStyleSheet("border: 1px solid #606060;\n"
"margin: 9px;")
        self._C0xbVaTqnfwVR0xv0QIssY0cByBe1L.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self._C0xbVaTqnfwVR0xv0QIssY0cByBe1L.setUniformItemSizes(False)
        self._C0xbVaTqnfwVR0xv0QIssY0cByBe1L.setSelectionRectVisible(False)
        self._C0xbVaTqnfwVR0xv0QIssY0cByBe1L.setObjectName("regularexpressions_list_R")
        self.resultslisting_content_R_layout.addWidget(self._C0xbVaTqnfwVR0xv0QIssY0cByBe1L, 0, 0, 1, 1)
        self.resultslisting_widget_R_layout.addWidget(self.resultslisting_content_R, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.resultslisting_widget_R, 1, 2, 1, 1)
        self.resultslisting_widget_L = QtWidgets.QWidget(fitness_of_statistical_tests_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resultslisting_widget_L.sizePolicy().hasHeightForWidth())
        self.resultslisting_widget_L.setSizePolicy(sizePolicy)
        self.resultslisting_widget_L.setMinimumSize(QtCore.QSize(100, 0))
        self.resultslisting_widget_L.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.resultslisting_widget_L.setStyleSheet("QWidget#resultslisting_content{\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #606060, stop: 1 #B8B8B8);;\n"
"    border: 1px solid #484848;\n"
"    border-top: none;\n"
"}\n"
"")
        self.resultslisting_widget_L.setObjectName("resultslisting_widget_L")
        self.resultslisting_widget_L_layout = QtWidgets.QGridLayout(self.resultslisting_widget_L)
        self.resultslisting_widget_L_layout.setSpacing(0)
        self.resultslisting_widget_L_layout.setContentsMargins(0, 0, 0, 0)
        self.resultslisting_widget_L_layout.setObjectName("resultslisting_widget_L_layout")
        self.resultslisting_titlelabel_L = QtWidgets.QLabel(self.resultslisting_widget_L)
        self.resultslisting_titlelabel_L.setMinimumSize(QtCore.QSize(0, 40))
        self.resultslisting_titlelabel_L.setMaximumSize(QtCore.QSize(16777215, 40))
        self.resultslisting_titlelabel_L.setStyleSheet("padding: 10px;\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #A8A8A8, stop: 1 #505050);\n"
"border: 1px solid #484848;")
        self.resultslisting_titlelabel_L.setTextFormat(QtCore.Qt.RichText)
        self.resultslisting_titlelabel_L.setObjectName("resultslisting_titlelabel_L")
        self.resultslisting_widget_L_layout.addWidget(self.resultslisting_titlelabel_L, 0, 0, 1, 1)
        self.resultslisting_content_L = QtWidgets.QWidget(self.resultslisting_widget_L)
        self.resultslisting_content_L.setStyleSheet("QWidget#resultslisting_content_L{\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #606060, stop: 1 #B8B8B8);;\n"
"    border: 1px solid #484848;\n"
"    border-top: none;\n"
"}\n"
"")
        self.resultslisting_content_L.setObjectName("resultslisting_content_L")
        self.resultslisting_content_L_layout = QtWidgets.QGridLayout(self.resultslisting_content_L)
        self.resultslisting_content_L_layout.setSpacing(0)
        self.resultslisting_content_L_layout.setContentsMargins(0, 0, 0, 0)
        self.resultslisting_content_L_layout.setObjectName("resultslisting_content_L_layout")
        self._nkLW5QJXDX0FklzGW2FuIkM4UCbtYl = QtWidgets.QListWidget(self.resultslisting_content_L)
        self._nkLW5QJXDX0FklzGW2FuIkM4UCbtYl.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self._nkLW5QJXDX0FklzGW2FuIkM4UCbtYl.setStyleSheet("border: 1px solid #606060;\n"
"margin: 9px;")
        self._nkLW5QJXDX0FklzGW2FuIkM4UCbtYl.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self._nkLW5QJXDX0FklzGW2FuIkM4UCbtYl.setUniformItemSizes(False)
        self._nkLW5QJXDX0FklzGW2FuIkM4UCbtYl.setSelectionRectVisible(False)
        self._nkLW5QJXDX0FklzGW2FuIkM4UCbtYl.setObjectName("regularexpressions_list_L")
        self.resultslisting_content_L_layout.addWidget(self._nkLW5QJXDX0FklzGW2FuIkM4UCbtYl, 0, 0, 1, 1)
        self.resultslisting_widget_L_layout.addWidget(self.resultslisting_content_L, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.resultslisting_widget_L, 1, 0, 1, 1)
        self.statistical_area = QtWidgets.QWidget(fitness_of_statistical_tests_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statistical_area.sizePolicy().hasHeightForWidth())
        self.statistical_area.setSizePolicy(sizePolicy)
        self.statistical_area.setMinimumSize(QtCore.QSize(0, 0))
        self.statistical_area.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.statistical_area.setStyleSheet("")
        self.statistical_area.setObjectName("statistical_area")
        self.plotting_area_layout = QtWidgets.QGridLayout(self.statistical_area)
        self.plotting_area_layout.setSpacing(0)
        self.plotting_area_layout.setContentsMargins(0, 0, 0, 0)
        self.plotting_area_layout.setObjectName("plotting_area_layout")
        self._W5Ao0lqLYsswwargntPEK3NUIszIKp = QtWidgets.QStackedWidget(self.statistical_area)
        self._W5Ao0lqLYsswwargntPEK3NUIszIKp.setObjectName("statistical_stackedwidget")
        self.plotcontent_page = QtWidgets.QWidget()
        self.plotcontent_page.setObjectName("plotcontent_page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.plotcontent_page)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.plotcontent = QtWidgets.QWidget(self.plotcontent_page)
        self.plotcontent.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.plotcontent.setStyleSheet("QWidget#plotcontent{\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #606060, stop: 1 #B8B8B8);;\n"
"    border: 1px solid #484848;\n"
"    border-top: none;\n"
"}\n"
"\n"
"QLabel {\n"
"    background: transparent;\n"
"    border: 1px solid #606060;\n"
"}\n"
"\n"
"QSpinBox {\n"
"    border: 1px solid #606060;\n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"    margin-left: 5px;\n"
"    background-color: #E0E0E0;\n"
"    padding: 5px 9px;\n"
"}\n"
"")
        self.plotcontent.setObjectName("plotcontent")
        self.plotcontent_layout = QtWidgets.QGridLayout(self.plotcontent)
        self.plotcontent_layout.setSpacing(0)
        self.plotcontent_layout.setContentsMargins(0, 0, 0, 0)
        self.plotcontent_layout.setObjectName("plotcontent_layout")
        self._nrqL1pAu3gWRNx404rIfPJHaBx9BXm = QtWidgets.QWidget(self.plotcontent)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._nrqL1pAu3gWRNx404rIfPJHaBx9BXm.sizePolicy().hasHeightForWidth())
        self._nrqL1pAu3gWRNx404rIfPJHaBx9BXm.setSizePolicy(sizePolicy)
        self._nrqL1pAu3gWRNx404rIfPJHaBx9BXm.setMinimumSize(QtCore.QSize(0, 0))
        self._nrqL1pAu3gWRNx404rIfPJHaBx9BXm.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self._nrqL1pAu3gWRNx404rIfPJHaBx9BXm.setStyleSheet("background-color: white;\n"
"border: 1px solid #606060;\n"
"margin-top: 9px;\n"
"margin-left: 9px;\n"
"margin-right: 9px;\n"
"margin-bottom: 5px;")
        self._nrqL1pAu3gWRNx404rIfPJHaBx9BXm.setObjectName("plotwidget")
        self._nrqL1pAu3gWRNx404rIfPJHaBx9BXm_layout = QtWidgets.QGridLayout(self._nrqL1pAu3gWRNx404rIfPJHaBx9BXm)
        self._nrqL1pAu3gWRNx404rIfPJHaBx9BXm_layout.setSpacing(0)
        self._nrqL1pAu3gWRNx404rIfPJHaBx9BXm_layout.setContentsMargins(0, 0, 0, 0)
        self._nrqL1pAu3gWRNx404rIfPJHaBx9BXm_layout.setObjectName("plotwidget_layout")
        self.plotcontent_layout.addWidget(self._nrqL1pAu3gWRNx404rIfPJHaBx9BXm, 0, 0, 1, 5)
        self.runtime = QtWidgets.QLabel(self.plotcontent)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.runtime.sizePolicy().hasHeightForWidth())
        self.runtime.setSizePolicy(sizePolicy)
        self.runtime.setMinimumSize(QtCore.QSize(130, 0))
        self.runtime.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.runtime.setStyleSheet("padding: 5px;\n"
"margin-right: 9px;\n"
"border-radius: 0px;\n"
"border-left: none;\n"
"border-right: none;\n"
"border-top: none;")
        self.runtime.setText("")
        self.runtime.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.runtime.setObjectName("runtime")
        self.plotcontent_layout.addWidget(self.runtime, 2, 4, 1, 1)
        self.pvalue_label = QtWidgets.QLabel(self.plotcontent)
        self.pvalue_label.setMinimumSize(QtCore.QSize(70, 0))
        self.pvalue_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pvalue_label.setStyleSheet("padding-left: 5px;\n"
"margin-bottom: 9px;\n"
"margin-left: 9px;\n"
"border-radius: 0px;\n"
"border-bottom: none;\n"
"border-left: none;\n"
"border-top: none;")
        self.pvalue_label.setObjectName("pvalue_label")
        self.plotcontent_layout.addWidget(self.pvalue_label, 4, 0, 1, 1)
        self.runtime_label = QtWidgets.QLabel(self.plotcontent)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.runtime_label.sizePolicy().hasHeightForWidth())
        self.runtime_label.setSizePolicy(sizePolicy)
        self.runtime_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.runtime_label.setStyleSheet("padding: 5px;\n"
"border-radius: 0px;\n"
"border-left: none;\n"
"border-top: none;")
        self.runtime_label.setObjectName("runtime_label")
        self.plotcontent_layout.addWidget(self.runtime_label, 2, 3, 1, 1)
        self.ksstat_label_double = QtWidgets.QLabel(self.plotcontent)
        self.ksstat_label_double.setMinimumSize(QtCore.QSize(189, 0))
        self.ksstat_label_double.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.ksstat_label_double.setStyleSheet("padding: 5px;\n"
"margin-left: 9px;\n"
"border-radius: 0px;\n"
"border-top: none;\n"
"border-left: none;\n"
"")
        self.ksstat_label_double.setObjectName("ksstat_label_double")
        self.plotcontent_layout.addWidget(self.ksstat_label_double, 3, 0, 1, 1)
        self._6ttKm8xZyn5IVs2E3UYEK8ZhK7mF99 = QtWidgets.QLabel(self.plotcontent)
        self._6ttKm8xZyn5IVs2E3UYEK8ZhK7mF99.setMinimumSize(QtCore.QSize(130, 0))
        self._6ttKm8xZyn5IVs2E3UYEK8ZhK7mF99.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self._6ttKm8xZyn5IVs2E3UYEK8ZhK7mF99.setStyleSheet("padding: 5px;\n"
"border-radius: 0px;\n"
"border-left: none;\n"
"border-top: none;\n"
"")
        self._6ttKm8xZyn5IVs2E3UYEK8ZhK7mF99.setObjectName("ksstat_double")
        self.plotcontent_layout.addWidget(self._6ttKm8xZyn5IVs2E3UYEK8ZhK7mF99, 3, 1, 1, 2)
        self.bins_label = QtWidgets.QLabel(self.plotcontent)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bins_label.sizePolicy().hasHeightForWidth())
        self.bins_label.setSizePolicy(sizePolicy)
        self.bins_label.setStyleSheet("border: 0px;\n"
"margin-left: 5px;")
        self.bins_label.setObjectName("bins_label")
        self.plotcontent_layout.addWidget(self.bins_label, 3, 3, 1, 1)
        self.bins = QtWidgets.QSpinBox(self.plotcontent)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bins.sizePolicy().hasHeightForWidth())
        self.bins.setSizePolicy(sizePolicy)
        self.bins.setStyleSheet("margin-top: 2px;\n"
"margin-bottom: 2px;\n"
"margin-right: 9px;\n"
"margin-left: 2px;")
        self.bins.setAlignment(QtCore.Qt.AlignCenter)
        self.bins.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.bins.setMinimum(1)
        self.bins.setMaximum(999999999)
        self.bins.setProperty("value", 50)
        self.bins.setObjectName("bins")
        self.plotcontent_layout.addWidget(self.bins, 3, 4, 1, 1)
        self.twosidedresults_label = QtWidgets.QLabel(self.plotcontent)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.twosidedresults_label.sizePolicy().hasHeightForWidth())
        self.twosidedresults_label.setSizePolicy(sizePolicy)
        self.twosidedresults_label.setMinimumSize(QtCore.QSize(135, 0))
        self.twosidedresults_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.twosidedresults_label.setStyleSheet("padding: 5px;\n"
"margin-left: 9px;\n"
"border-radius: 0px;\n"
"border-left: none;\n"
"border-top: none;")
        self.twosidedresults_label.setObjectName("twosidedresults_label")
        self.plotcontent_layout.addWidget(self.twosidedresults_label, 2, 0, 1, 3)
        self._aEmZNzEK4eVKWLWzEXYey2zEnKabvx = QtWidgets.QLabel(self.plotcontent)
        self._aEmZNzEK4eVKWLWzEXYey2zEnKabvx.setMinimumSize(QtCore.QSize(130, 0))
        self._aEmZNzEK4eVKWLWzEXYey2zEnKabvx.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self._aEmZNzEK4eVKWLWzEXYey2zEnKabvx.setStyleSheet("padding: 5px;\n"
"margin-bottom: 9px;\n"
"border-radius: 0px;\n"
"border-left: none;\n"
"border-bottom: none;\n"
"border-top: none;")
        self._aEmZNzEK4eVKWLWzEXYey2zEnKabvx.setObjectName("pvalue_double")
        self.plotcontent_layout.addWidget(self._aEmZNzEK4eVKWLWzEXYey2zEnKabvx, 4, 1, 1, 2)
        self._JJDsOStF6pGh9hsjtpj5tmSKwNuxPJ = QtWidgets.QPushButton(self.plotcontent)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._JJDsOStF6pGh9hsjtpj5tmSKwNuxPJ.sizePolicy().hasHeightForWidth())
        self._JJDsOStF6pGh9hsjtpj5tmSKwNuxPJ.setSizePolicy(sizePolicy)
        self._JJDsOStF6pGh9hsjtpj5tmSKwNuxPJ.setStyleSheet("margin-right: 9px;\n"
"margin-bottom: 9px;")
        self._JJDsOStF6pGh9hsjtpj5tmSKwNuxPJ.setObjectName("updateplot_button")
        self.plotcontent_layout.addWidget(self._JJDsOStF6pGh9hsjtpj5tmSKwNuxPJ, 4, 3, 1, 2)
        self._EPPIJvylTr1KH2YZ870CJ85n1rQTA6 = QtWidgets.QPushButton(self.plotcontent)
        self._EPPIJvylTr1KH2YZ870CJ85n1rQTA6.setStyleSheet("margin: 5px;\n"
"margin-top:0px")
        self._EPPIJvylTr1KH2YZ870CJ85n1rQTA6.setObjectName("scottknott_button")
        self.plotcontent_layout.addWidget(self._EPPIJvylTr1KH2YZ870CJ85n1rQTA6, 5, 0, 1, 5)
        self.gridLayout_2.addWidget(self.plotcontent, 0, 0, 1, 1)
        self._W5Ao0lqLYsswwargntPEK3NUIszIKp.addWidget(self.plotcontent_page)
        self.scottknott_page = QtWidgets.QWidget()
        self.scottknott_page.setStyleSheet("QWidget#scottknott_page{\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #606060, stop: 1 #B8B8B8);;\n"
"    border: 1px solid #484848;\n"
"    border-top: none;\n"
"}\n"
"\n"
"QLabel {\n"
"    background: transparent;\n"
"    border: 1px solid #606060;\n"
"}\n"
"\n"
"QSpinBox {\n"
"    border: 1px solid #606060;\n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"    margin-left: 5px;\n"
"    background-color: #E0E0E0;\n"
"    padding: 5px 9px;\n"
"}\n"
"")
        self.scottknott_page.setObjectName("scottknott_page")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scottknott_page)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.scottknott_table = QtWidgets.QTableWidget(self.scottknott_page)
        self.scottknott_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.scottknott_table.setCornerButtonEnabled(False)
        self.scottknott_table.setObjectName("scottknott_table")
        self.scottknott_table.setColumnCount(3)
        self.scottknott_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.scottknott_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.scottknott_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.scottknott_table.setHorizontalHeaderItem(2, item)
        self.scottknott_table.horizontalHeader().setVisible(True)
        self.scottknott_table.horizontalHeader().setCascadingSectionResizes(False)
        self.scottknott_table.horizontalHeader().setSortIndicatorShown(False)
        self.scottknott_table.horizontalHeader().setStretchLastSection(True)
        self.scottknott_table.verticalHeader().setVisible(False)
        self.gridLayout_3.addWidget(self.scottknott_table, 0, 0, 1, 1)
        self._Y9rHCErysNrS9gho4uwKEBLey6qhh3 = QtWidgets.QPushButton(self.scottknott_page)
        self._Y9rHCErysNrS9gho4uwKEBLey6qhh3.setObjectName("distributions_button")
        self.gridLayout_3.addWidget(self._Y9rHCErysNrS9gho4uwKEBLey6qhh3, 1, 0, 1, 1)
        self._W5Ao0lqLYsswwargntPEK3NUIszIKp.addWidget(self.scottknott_page)
        self.plotting_area_layout.addWidget(self._W5Ao0lqLYsswwargntPEK3NUIszIKp, 2, 0, 1, 1)
        self.statistical_area_titlelabel = QtWidgets.QLabel(self.statistical_area)
        self.statistical_area_titlelabel.setMinimumSize(QtCore.QSize(0, 40))
        self.statistical_area_titlelabel.setMaximumSize(QtCore.QSize(16777215, 40))
        self.statistical_area_titlelabel.setStyleSheet("padding: 10px;\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #A8A8A8, stop: 1 #505050);\n"
"border: 1px solid #484848;")
        self.statistical_area_titlelabel.setTextFormat(QtCore.Qt.RichText)
        self.statistical_area_titlelabel.setObjectName("statistical_area_titlelabel")
        self.plotting_area_layout.addWidget(self.statistical_area_titlelabel, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.statistical_area, 1, 1, 2, 1)
        self.choosefile_widget = QtWidgets.QWidget(fitness_of_statistical_tests_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.choosefile_widget.sizePolicy().hasHeightForWidth())
        self.choosefile_widget.setSizePolicy(sizePolicy)
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
        self.chosefile_content_layout.setContentsMargins(9, -1, 9, 9)
        self.chosefile_content_layout.setObjectName("chosefile_content_layout")
        self._YxKtsZbMTmG34Ny3YANp0byCrksUmV = QtWidgets.QLineEdit(self.choosefile_content)
        self._YxKtsZbMTmG34Ny3YANp0byCrksUmV.setMinimumSize(QtCore.QSize(300, 20))
        self._YxKtsZbMTmG34Ny3YANp0byCrksUmV.setMaximumSize(QtCore.QSize(16777215, 20))
        self._YxKtsZbMTmG34Ny3YANp0byCrksUmV.setStyleSheet("")
        self._YxKtsZbMTmG34Ny3YANp0byCrksUmV.setObjectName("filepath_label")
        self.chosefile_content_layout.addWidget(self._YxKtsZbMTmG34Ny3YANp0byCrksUmV)
        self._mxFUsVLlnbD2x25IEu0Haab4IZTnMR = QtWidgets.QPushButton(self.choosefile_content)
        self._mxFUsVLlnbD2x25IEu0Haab4IZTnMR.setMinimumSize(QtCore.QSize(60, 25))
        self._mxFUsVLlnbD2x25IEu0Haab4IZTnMR.setMaximumSize(QtCore.QSize(60, 25))
        self._mxFUsVLlnbD2x25IEu0Haab4IZTnMR.setStyleSheet("")
        self._mxFUsVLlnbD2x25IEu0Haab4IZTnMR.setObjectName("file_explorerbutton")
        self.chosefile_content_layout.addWidget(self._mxFUsVLlnbD2x25IEu0Haab4IZTnMR)
        spacerItem = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.chosefile_content_layout.addItem(spacerItem)
        self._UcCIvMaCNIWoW398NrW4cf7nVIIZ7W = QtWidgets.QPushButton(self.choosefile_content)
        self._UcCIvMaCNIWoW398NrW4cf7nVIIZ7W.setMinimumSize(QtCore.QSize(100, 25))
        self._UcCIvMaCNIWoW398NrW4cf7nVIIZ7W.setMaximumSize(QtCore.QSize(100, 25))
        self._UcCIvMaCNIWoW398NrW4cf7nVIIZ7W.setStyleSheet("")
        self._UcCIvMaCNIWoW398NrW4cf7nVIIZ7W.setObjectName("startbutton")
        self.chosefile_content_layout.addWidget(self._UcCIvMaCNIWoW398NrW4cf7nVIIZ7W)
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
        self.gridLayout.addWidget(self.choosefile_widget, 0, 0, 1, 3)
        self.regexproperties_widget_L = QtWidgets.QWidget(fitness_of_statistical_tests_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.regexproperties_widget_L.sizePolicy().hasHeightForWidth())
        self.regexproperties_widget_L.setSizePolicy(sizePolicy)
        self.regexproperties_widget_L.setMinimumSize(QtCore.QSize(0, 0))
        self.regexproperties_widget_L.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.regexproperties_widget_L.setStyleSheet("")
        self.regexproperties_widget_L.setObjectName("regexproperties_widget_L")
        self.regexproperties_widget_L_layout = QtWidgets.QGridLayout(self.regexproperties_widget_L)
        self.regexproperties_widget_L_layout.setSpacing(0)
        self.regexproperties_widget_L_layout.setContentsMargins(0, 0, 0, 0)
        self.regexproperties_widget_L_layout.setObjectName("regexproperties_widget_L_layout")
        self.regexproperties_content_L = QtWidgets.QWidget(self.regexproperties_widget_L)
        self.regexproperties_content_L.setStyleSheet("QWidget#regexproperties_content_L{\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #606060, stop: 1 #B8B8B8);;\n"
"    border: 1px solid #484848;\n"
"    border-top: none;\n"
"}\n"
"\n"
"QLabel {\n"
"    background: transparent;\n"
"    border: 1px solid #606060;\n"
"}")
        self.regexproperties_content_L.setObjectName("regexproperties_content_L")
        self.regexproperties_content_L_layout = QtWidgets.QGridLayout(self.regexproperties_content_L)
        self.regexproperties_content_L_layout.setSpacing(0)
        self.regexproperties_content_L_layout.setContentsMargins(9, 9, 9, 9)
        self.regexproperties_content_L_layout.setObjectName("regexproperties_content_L_layout")
        self.bestdistribution_label_L = QtWidgets.QLabel(self.regexproperties_content_L)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bestdistribution_label_L.sizePolicy().hasHeightForWidth())
        self.bestdistribution_label_L.setSizePolicy(sizePolicy)
        self.bestdistribution_label_L.setMinimumSize(QtCore.QSize(106, 25))
        self.bestdistribution_label_L.setMaximumSize(QtCore.QSize(106, 16777215))
        self.bestdistribution_label_L.setStyleSheet("padding: 5px;\n"
"border-radius: 0px;\n"
"border-bottom: none;\n"
"border-left: none;")
        self.bestdistribution_label_L.setObjectName("bestdistribution_label_L")
        self.regexproperties_content_L_layout.addWidget(self.bestdistribution_label_L, 2, 0, 1, 1)
        self._uQTQphyn6n5DwvQpu9Y7ShIvIH0TY3 = QtWidgets.QLabel(self.regexproperties_content_L)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._uQTQphyn6n5DwvQpu9Y7ShIvIH0TY3.sizePolicy().hasHeightForWidth())
        self._uQTQphyn6n5DwvQpu9Y7ShIvIH0TY3.setSizePolicy(sizePolicy)
        self._uQTQphyn6n5DwvQpu9Y7ShIvIH0TY3.setMinimumSize(QtCore.QSize(0, 25))
        self._uQTQphyn6n5DwvQpu9Y7ShIvIH0TY3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self._uQTQphyn6n5DwvQpu9Y7ShIvIH0TY3.setStyleSheet("padding: 5px;\n"
"border-radius: 0px;\n"
"border-left: none;\n"
"border-right: none;\n"
"border-bottom: none;\n"
"")
        self._uQTQphyn6n5DwvQpu9Y7ShIvIH0TY3.setObjectName("totalitems_L")
        self.regexproperties_content_L_layout.addWidget(self._uQTQphyn6n5DwvQpu9Y7ShIvIH0TY3, 3, 1, 1, 1)
        self._3z91Lbqj3g133OE4g7Zp0osEK0o7qy = QtWidgets.QLabel(self.regexproperties_content_L)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._3z91Lbqj3g133OE4g7Zp0osEK0o7qy.sizePolicy().hasHeightForWidth())
        self._3z91Lbqj3g133OE4g7Zp0osEK0o7qy.setSizePolicy(sizePolicy)
        self._3z91Lbqj3g133OE4g7Zp0osEK0o7qy.setMinimumSize(QtCore.QSize(130, 25))
        self._3z91Lbqj3g133OE4g7Zp0osEK0o7qy.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self._3z91Lbqj3g133OE4g7Zp0osEK0o7qy.setStyleSheet("padding: 5px;\n"
"border-radius: 0px;\n"
"border-left: none;\n"
"border-bottom: none;\n"
"border-top: none;\n"
"border-right: none;")
        self._3z91Lbqj3g133OE4g7Zp0osEK0o7qy.setObjectName("ksstat_L")
        self.regexproperties_content_L_layout.addWidget(self._3z91Lbqj3g133OE4g7Zp0osEK0o7qy, 0, 1, 1, 1)
        self._zr18H0ijUB3ieyuwMp8TRNrAOYAY4L = QtWidgets.QLabel(self.regexproperties_content_L)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._zr18H0ijUB3ieyuwMp8TRNrAOYAY4L.sizePolicy().hasHeightForWidth())
        self._zr18H0ijUB3ieyuwMp8TRNrAOYAY4L.setSizePolicy(sizePolicy)
        self._zr18H0ijUB3ieyuwMp8TRNrAOYAY4L.setMinimumSize(QtCore.QSize(130, 25))
        self._zr18H0ijUB3ieyuwMp8TRNrAOYAY4L.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self._zr18H0ijUB3ieyuwMp8TRNrAOYAY4L.setStyleSheet("padding: 5px;\n"
"border-radius: 0px;\n"
"border-left: none;\n"
"border-bottom: none;\n"
"border-right: none;\n"
"")
        self._zr18H0ijUB3ieyuwMp8TRNrAOYAY4L.setObjectName("pvalue_L")
        self.regexproperties_content_L_layout.addWidget(self._zr18H0ijUB3ieyuwMp8TRNrAOYAY4L, 1, 1, 1, 1)
        self.pvalue_label_L = QtWidgets.QLabel(self.regexproperties_content_L)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pvalue_label_L.sizePolicy().hasHeightForWidth())
        self.pvalue_label_L.setSizePolicy(sizePolicy)
        self.pvalue_label_L.setMinimumSize(QtCore.QSize(106, 25))
        self.pvalue_label_L.setMaximumSize(QtCore.QSize(106, 16777215))
        self.pvalue_label_L.setStyleSheet("padding: 5px;\n"
"border-radius: 0px;\n"
"border-bottom: none;\n"
"border-left: none;")
        self.pvalue_label_L.setObjectName("pvalue_label_L")
        self.regexproperties_content_L_layout.addWidget(self.pvalue_label_L, 1, 0, 1, 1)
        self.ksstat_label_L = QtWidgets.QLabel(self.regexproperties_content_L)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ksstat_label_L.sizePolicy().hasHeightForWidth())
        self.ksstat_label_L.setSizePolicy(sizePolicy)
        self.ksstat_label_L.setMinimumSize(QtCore.QSize(106, 25))
        self.ksstat_label_L.setMaximumSize(QtCore.QSize(106, 16777215))
        self.ksstat_label_L.setStyleSheet("padding: 5px;\n"
"border-radius: 0px;\n"
"border-top: none;\n"
"border-left: none;\n"
"border-bottom: none;")
        self.ksstat_label_L.setObjectName("ksstat_label_L")
        self.regexproperties_content_L_layout.addWidget(self.ksstat_label_L, 0, 0, 1, 1)
        self.totalitems_label_L = QtWidgets.QLabel(self.regexproperties_content_L)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.totalitems_label_L.sizePolicy().hasHeightForWidth())
        self.totalitems_label_L.setSizePolicy(sizePolicy)
        self.totalitems_label_L.setMinimumSize(QtCore.QSize(106, 25))
        self.totalitems_label_L.setMaximumSize(QtCore.QSize(16777215, 25))
        self.totalitems_label_L.setStyleSheet("padding: 5px;\n"
"border-radius: 0px;\n"
"border-left: none;\n"
"border-bottom: none;\n"
"")
        self.totalitems_label_L.setObjectName("totalitems_label_L")
        self.regexproperties_content_L_layout.addWidget(self.totalitems_label_L, 3, 0, 1, 1)
        self._zPLeIKaBBj9E1oruGXC2zW1sBYbZNV = QtWidgets.QLabel(self.regexproperties_content_L)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._zPLeIKaBBj9E1oruGXC2zW1sBYbZNV.sizePolicy().hasHeightForWidth())
        self._zPLeIKaBBj9E1oruGXC2zW1sBYbZNV.setSizePolicy(sizePolicy)
        self._zPLeIKaBBj9E1oruGXC2zW1sBYbZNV.setMinimumSize(QtCore.QSize(130, 25))
        self._zPLeIKaBBj9E1oruGXC2zW1sBYbZNV.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self._zPLeIKaBBj9E1oruGXC2zW1sBYbZNV.setStyleSheet("padding: 5px;\n"
"border-radius: 0px;\n"
"border-left: none;\n"
"border-bottom: none;\n"
"border-right: none;\n"
"")
        self._zPLeIKaBBj9E1oruGXC2zW1sBYbZNV.setObjectName("bestdistribution_L")
        self.regexproperties_content_L_layout.addWidget(self._zPLeIKaBBj9E1oruGXC2zW1sBYbZNV, 2, 1, 1, 1)
        self.bestdistribution_label_L.raise_()
        self._3z91Lbqj3g133OE4g7Zp0osEK0o7qy.raise_()
        self._zr18H0ijUB3ieyuwMp8TRNrAOYAY4L.raise_()
        self.pvalue_label_L.raise_()
        self.ksstat_label_L.raise_()
        self.totalitems_label_L.raise_()
        self._zPLeIKaBBj9E1oruGXC2zW1sBYbZNV.raise_()
        self._uQTQphyn6n5DwvQpu9Y7ShIvIH0TY3.raise_()
        self.regexproperties_widget_L_layout.addWidget(self.regexproperties_content_L, 1, 0, 1, 2)
        self.regexproperties_titlelabel_L = QtWidgets.QLabel(self.regexproperties_widget_L)
        self.regexproperties_titlelabel_L.setMinimumSize(QtCore.QSize(0, 40))
        self.regexproperties_titlelabel_L.setMaximumSize(QtCore.QSize(16777215, 40))
        self.regexproperties_titlelabel_L.setStyleSheet("padding: 10px;\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #A8A8A8, stop: 1 #505050);\n"
"border: 1px solid #484848;")
        self.regexproperties_titlelabel_L.setTextFormat(QtCore.Qt.RichText)
        self.regexproperties_titlelabel_L.setObjectName("regexproperties_titlelabel_L")
        self.regexproperties_widget_L_layout.addWidget(self.regexproperties_titlelabel_L, 0, 0, 1, 2)
        self.gridLayout.addWidget(self.regexproperties_widget_L, 2, 0, 1, 1)
        self.regexproperties_widget_R = QtWidgets.QWidget(fitness_of_statistical_tests_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.regexproperties_widget_R.sizePolicy().hasHeightForWidth())
        self.regexproperties_widget_R.setSizePolicy(sizePolicy)
        self.regexproperties_widget_R.setMinimumSize(QtCore.QSize(0, 0))
        self.regexproperties_widget_R.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.regexproperties_widget_R.setStyleSheet("")
        self.regexproperties_widget_R.setObjectName("regexproperties_widget_R")
        self.regexproperties_widget_R_layout = QtWidgets.QGridLayout(self.regexproperties_widget_R)
        self.regexproperties_widget_R_layout.setSpacing(0)
        self.regexproperties_widget_R_layout.setContentsMargins(0, 0, 0, 0)
        self.regexproperties_widget_R_layout.setObjectName("regexproperties_widget_R_layout")
        self.regexproperties_titlelabel_R = QtWidgets.QLabel(self.regexproperties_widget_R)
        self.regexproperties_titlelabel_R.setMinimumSize(QtCore.QSize(0, 40))
        self.regexproperties_titlelabel_R.setMaximumSize(QtCore.QSize(16777215, 40))
        self.regexproperties_titlelabel_R.setStyleSheet("padding: 10px;\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #A8A8A8, stop: 1 #505050);\n"
"border: 1px solid #484848;")
        self.regexproperties_titlelabel_R.setTextFormat(QtCore.Qt.RichText)
        self.regexproperties_titlelabel_R.setObjectName("regexproperties_titlelabel_R")
        self.regexproperties_widget_R_layout.addWidget(self.regexproperties_titlelabel_R, 0, 0, 1, 2)
        self.regexproperties_content_R = QtWidgets.QWidget(self.regexproperties_widget_R)
        self.regexproperties_content_R.setStyleSheet("QWidget#regexproperties_content_R{\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #606060, stop: 1 #B8B8B8);;\n"
"    border: 1px solid #484848;\n"
"    border-top: none;\n"
"}\n"
"\n"
"QLabel {\n"
"    background: transparent;\n"
"    border: 1px solid #606060;\n"
"}")
        self.regexproperties_content_R.setObjectName("regexproperties_content_R")
        self.regexproperties_content_R_layout = QtWidgets.QGridLayout(self.regexproperties_content_R)
        self.regexproperties_content_R_layout.setSpacing(0)
        self.regexproperties_content_R_layout.setContentsMargins(9, 9, 9, 9)
        self.regexproperties_content_R_layout.setObjectName("regexproperties_content_R_layout")
        self.pvalue_label_R = QtWidgets.QLabel(self.regexproperties_content_R)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pvalue_label_R.sizePolicy().hasHeightForWidth())
        self.pvalue_label_R.setSizePolicy(sizePolicy)
        self.pvalue_label_R.setMinimumSize(QtCore.QSize(106, 25))
        self.pvalue_label_R.setMaximumSize(QtCore.QSize(16777215, 25))
        self.pvalue_label_R.setStyleSheet("padding: 5px;\n"
"border-radius: 0px;\n"
"border-bottom: none;\n"
"border-left: none;")
        self.pvalue_label_R.setObjectName("pvalue_label_R")
        self.regexproperties_content_R_layout.addWidget(self.pvalue_label_R, 2, 0, 1, 1)
        self._RfCmozGiipoJvcsqsfRaW2iexSYNJ5 = QtWidgets.QLabel(self.regexproperties_content_R)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._RfCmozGiipoJvcsqsfRaW2iexSYNJ5.sizePolicy().hasHeightForWidth())
        self._RfCmozGiipoJvcsqsfRaW2iexSYNJ5.setSizePolicy(sizePolicy)
        self._RfCmozGiipoJvcsqsfRaW2iexSYNJ5.setMinimumSize(QtCore.QSize(130, 25))
        self._RfCmozGiipoJvcsqsfRaW2iexSYNJ5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self._RfCmozGiipoJvcsqsfRaW2iexSYNJ5.setStyleSheet("padding: 5px;\n"
"border-radius: 0px;\n"
"border-left: none;\n"
"border-bottom: none;\n"
"border-right: none;\n"
"")
        self._RfCmozGiipoJvcsqsfRaW2iexSYNJ5.setObjectName("bestdistribution_R")
        self.regexproperties_content_R_layout.addWidget(self._RfCmozGiipoJvcsqsfRaW2iexSYNJ5, 3, 1, 1, 1)
        self.ksstat_label_R = QtWidgets.QLabel(self.regexproperties_content_R)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ksstat_label_R.sizePolicy().hasHeightForWidth())
        self.ksstat_label_R.setSizePolicy(sizePolicy)
        self.ksstat_label_R.setMinimumSize(QtCore.QSize(106, 25))
        self.ksstat_label_R.setMaximumSize(QtCore.QSize(16777215, 25))
        self.ksstat_label_R.setStyleSheet("padding: 5px;\n"
"border-radius: 0px;\n"
"border-top: none;\n"
"border-left: none;\n"
"border-bottom: none;")
        self.ksstat_label_R.setObjectName("ksstat_label_R")
        self.regexproperties_content_R_layout.addWidget(self.ksstat_label_R, 0, 0, 1, 1)
        self.bestdistribution_label_R = QtWidgets.QLabel(self.regexproperties_content_R)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bestdistribution_label_R.sizePolicy().hasHeightForWidth())
        self.bestdistribution_label_R.setSizePolicy(sizePolicy)
        self.bestdistribution_label_R.setMinimumSize(QtCore.QSize(106, 25))
        self.bestdistribution_label_R.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bestdistribution_label_R.setStyleSheet("padding: 5px;\n"
"border-radius: 0px;\n"
"border-bottom: none;\n"
"border-left: none;")
        self.bestdistribution_label_R.setObjectName("bestdistribution_label_R")
        self.regexproperties_content_R_layout.addWidget(self.bestdistribution_label_R, 3, 0, 1, 1)
        self._lIpvKybBa8gWPAuTgmQnMgosnnhq5N = QtWidgets.QLabel(self.regexproperties_content_R)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._lIpvKybBa8gWPAuTgmQnMgosnnhq5N.sizePolicy().hasHeightForWidth())
        self._lIpvKybBa8gWPAuTgmQnMgosnnhq5N.setSizePolicy(sizePolicy)
        self._lIpvKybBa8gWPAuTgmQnMgosnnhq5N.setMinimumSize(QtCore.QSize(130, 25))
        self._lIpvKybBa8gWPAuTgmQnMgosnnhq5N.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self._lIpvKybBa8gWPAuTgmQnMgosnnhq5N.setStyleSheet("padding: 5px;\n"
"border-radius: 0px;\n"
"border-left: none;\n"
"border-bottom: none;\n"
"border-right: none;\n"
"")
        self._lIpvKybBa8gWPAuTgmQnMgosnnhq5N.setObjectName("pvalue_R")
        self.regexproperties_content_R_layout.addWidget(self._lIpvKybBa8gWPAuTgmQnMgosnnhq5N, 2, 1, 1, 1)
        self._ewVBxbWP7GZ9FVyrV2IPFLw1f5cfzD = QtWidgets.QLabel(self.regexproperties_content_R)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._ewVBxbWP7GZ9FVyrV2IPFLw1f5cfzD.sizePolicy().hasHeightForWidth())
        self._ewVBxbWP7GZ9FVyrV2IPFLw1f5cfzD.setSizePolicy(sizePolicy)
        self._ewVBxbWP7GZ9FVyrV2IPFLw1f5cfzD.setMinimumSize(QtCore.QSize(130, 25))
        self._ewVBxbWP7GZ9FVyrV2IPFLw1f5cfzD.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self._ewVBxbWP7GZ9FVyrV2IPFLw1f5cfzD.setStyleSheet("padding: 5px;\n"
"border-radius: 0px;\n"
"border-left: none;\n"
"border-right: none;\n"
"border-bottom: none;\n"
"")
        self._ewVBxbWP7GZ9FVyrV2IPFLw1f5cfzD.setObjectName("totalitems_R")
        self.regexproperties_content_R_layout.addWidget(self._ewVBxbWP7GZ9FVyrV2IPFLw1f5cfzD, 4, 1, 1, 1)
        self.totalitems_label_R = QtWidgets.QLabel(self.regexproperties_content_R)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.totalitems_label_R.sizePolicy().hasHeightForWidth())
        self.totalitems_label_R.setSizePolicy(sizePolicy)
        self.totalitems_label_R.setMinimumSize(QtCore.QSize(106, 25))
        self.totalitems_label_R.setMaximumSize(QtCore.QSize(16777215, 25))
        self.totalitems_label_R.setStyleSheet("padding: 5px;\n"
"border-radius: 0px;\n"
"border-left: none;\n"
"border-bottom: none;\n"
"")
        self.totalitems_label_R.setObjectName("totalitems_label_R")
        self.regexproperties_content_R_layout.addWidget(self.totalitems_label_R, 4, 0, 1, 1)
        self._HVsftfRMgBaF4sSvwYahurWCWsAGTZ = QtWidgets.QLabel(self.regexproperties_content_R)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._HVsftfRMgBaF4sSvwYahurWCWsAGTZ.sizePolicy().hasHeightForWidth())
        self._HVsftfRMgBaF4sSvwYahurWCWsAGTZ.setSizePolicy(sizePolicy)
        self._HVsftfRMgBaF4sSvwYahurWCWsAGTZ.setMinimumSize(QtCore.QSize(130, 25))
        self._HVsftfRMgBaF4sSvwYahurWCWsAGTZ.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self._HVsftfRMgBaF4sSvwYahurWCWsAGTZ.setStyleSheet("padding: 5px;\n"
"border-radius: 0px;\n"
"border-left: none;\n"
"border-bottom: none;\n"
"border-top: none;\n"
"border-right: none;")
        self._HVsftfRMgBaF4sSvwYahurWCWsAGTZ.setObjectName("ksstat_R")
        self.regexproperties_content_R_layout.addWidget(self._HVsftfRMgBaF4sSvwYahurWCWsAGTZ, 0, 1, 1, 1)
        self.regexproperties_widget_R_layout.addWidget(self.regexproperties_content_R, 1, 0, 1, 2)
        self.gridLayout.addWidget(self.regexproperties_widget_R, 2, 2, 1, 1)

        self.retranslateUi(fitness_of_statistical_tests_widget)
        self._W5Ao0lqLYsswwargntPEK3NUIszIKp.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(fitness_of_statistical_tests_widget)

    def retranslateUi(self, fitness_of_statistical_tests_widget):
        _translate = QtCore.QCoreApplication.translate
        fitness_of_statistical_tests_widget.setWindowTitle(_translate("fitness_of_statistical_tests_widget", "Form"))
        self.resultslisting_titlelabel_R.setText(_translate("fitness_of_statistical_tests_widget", "<html><head/><body><p><span style=\" font-weight:600;\">Regular Expressions</span></p></body></html>"))
        self._C0xbVaTqnfwVR0xv0QIssY0cByBe1L.setSortingEnabled(True)
        self.resultslisting_titlelabel_L.setText(_translate("fitness_of_statistical_tests_widget", "<html><head/><body><p><span style=\" font-weight:600;\">Regular Expressions</span></p></body></html>"))
        self._nkLW5QJXDX0FklzGW2FuIkM4UCbtYl.setSortingEnabled(True)
        self.pvalue_label.setText(_translate("fitness_of_statistical_tests_widget", "P-Value"))
        self.runtime_label.setText(_translate("fitness_of_statistical_tests_widget", "Run Time"))
        self.ksstat_label_double.setText(_translate("fitness_of_statistical_tests_widget", "Kolmogorov-Smirnov Test Statistic"))
        self._6ttKm8xZyn5IVs2E3UYEK8ZhK7mF99.setText(_translate("fitness_of_statistical_tests_widget", "0"))
        self.bins_label.setText(_translate("fitness_of_statistical_tests_widget", "Bins"))
        self.twosidedresults_label.setText(_translate("fitness_of_statistical_tests_widget", "Two Sided Test Results"))
        self._aEmZNzEK4eVKWLWzEXYey2zEnKabvx.setText(_translate("fitness_of_statistical_tests_widget", "0"))
        self._JJDsOStF6pGh9hsjtpj5tmSKwNuxPJ.setText(_translate("fitness_of_statistical_tests_widget", "Update"))
        self._EPPIJvylTr1KH2YZ870CJ85n1rQTA6.setText(_translate("fitness_of_statistical_tests_widget", "Scott Knott Results"))
        item = self.scottknott_table.horizontalHeaderItem(0)
        item.setText(_translate("fitness_of_statistical_tests_widget", "Regex"))
        item = self.scottknott_table.horizontalHeaderItem(1)
        item.setText(_translate("fitness_of_statistical_tests_widget", "Mean"))
        item = self.scottknott_table.horizontalHeaderItem(2)
        item.setText(_translate("fitness_of_statistical_tests_widget", "Rank"))
        self._Y9rHCErysNrS9gho4uwKEBLey6qhh3.setText(_translate("fitness_of_statistical_tests_widget", "Distributions"))
        self.statistical_area_titlelabel.setText(_translate("fitness_of_statistical_tests_widget", "<html><head/><body><p><span style=\" font-weight:600;\">Statistical Tests</span></p></body></html>"))
        self._mxFUsVLlnbD2x25IEu0Haab4IZTnMR.setText(_translate("fitness_of_statistical_tests_widget", "Browse"))
        self._UcCIvMaCNIWoW398NrW4cf7nVIIZ7W.setText(_translate("fitness_of_statistical_tests_widget", "Start"))
        self.choosefile_titlelabel.setText(_translate("fitness_of_statistical_tests_widget", "<html><head/><body><p><span style=\" font-weight:600;\">Choose File</span></p></body></html>"))
        self.bestdistribution_label_L.setText(_translate("fitness_of_statistical_tests_widget", "Best Distribution"))
        self._uQTQphyn6n5DwvQpu9Y7ShIvIH0TY3.setText(_translate("fitness_of_statistical_tests_widget", "0"))
        self._3z91Lbqj3g133OE4g7Zp0osEK0o7qy.setText(_translate("fitness_of_statistical_tests_widget", "0"))
        self._zr18H0ijUB3ieyuwMp8TRNrAOYAY4L.setText(_translate("fitness_of_statistical_tests_widget", "0"))
        self.pvalue_label_L.setText(_translate("fitness_of_statistical_tests_widget", "P-Value"))
        self.ksstat_label_L.setText(_translate("fitness_of_statistical_tests_widget", "<html><head/><body><p>KS Test Statistic</p></body></html>"))
        self.totalitems_label_L.setText(_translate("fitness_of_statistical_tests_widget", "Total Items"))
        self._zPLeIKaBBj9E1oruGXC2zW1sBYbZNV.setText(_translate("fitness_of_statistical_tests_widget", "n/a"))
        self.regexproperties_titlelabel_L.setText(_translate("fitness_of_statistical_tests_widget", "<html><head/><body><p><span style=\" font-weight:600;\">Regular Expression Properties</span></p></body></html>"))
        self.regexproperties_titlelabel_R.setText(_translate("fitness_of_statistical_tests_widget", "<html><head/><body><p><span style=\" font-weight:600;\">Regular Expression Properties</span></p></body></html>"))
        self.pvalue_label_R.setText(_translate("fitness_of_statistical_tests_widget", "P-Value"))
        self._RfCmozGiipoJvcsqsfRaW2iexSYNJ5.setText(_translate("fitness_of_statistical_tests_widget", "n/a"))
        self.ksstat_label_R.setText(_translate("fitness_of_statistical_tests_widget", "KS Test Statistic"))
        self.bestdistribution_label_R.setText(_translate("fitness_of_statistical_tests_widget", "Best Distribution"))
        self._lIpvKybBa8gWPAuTgmQnMgosnnhq5N.setText(_translate("fitness_of_statistical_tests_widget", "0"))
        self._ewVBxbWP7GZ9FVyrV2IPFLw1f5cfzD.setText(_translate("fitness_of_statistical_tests_widget", "0"))
        self.totalitems_label_R.setText(_translate("fitness_of_statistical_tests_widget", "Total Items"))
        self._HVsftfRMgBaF4sSvwYahurWCWsAGTZ.setText(_translate("fitness_of_statistical_tests_widget", "0"))


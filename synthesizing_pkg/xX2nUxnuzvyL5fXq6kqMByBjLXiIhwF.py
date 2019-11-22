from PyQt5 import *

class Aym5ooT2hOIU6tN88bRqWOcbJ9f2o7(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self) 
        self.setWindowTitle('Synthesizing Help')
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 540)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri Light,sans-serif\'; font-size:9pt; font-weight:600; color:#000000;\">Input File</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri Light,sans-serif\'; font-size:9pt; color:#000000;\">Input should be in the format of a regular expression, followed by the a series of numbers, all of which are space seperated.  </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri Light,sans-serif\'; font-size:9pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri Light,sans-serif\'; font-size:9pt; color:#000000;\">Example:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri Light,sans-serif\'; font-size:9pt; font-style:italic; color:#000000;\">A*B* 9 32 2 2.2 91 2</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri Light,sans-serif\'; font-size:9pt; font-style:italic; color:#000000;\">BABA 9 1 2 2 2 3.3 5</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri Light,sans-serif\'; font-size:9pt;\"> </span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri Light,sans-serif\'; font-size:9pt; font-weight:600;\">Final Results Table</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri Light,sans-serif\'; font-size:9pt; color:#000000;\">The result of the merging process is given in the final results window. Each row is a separate entry consisting of a pattern, the total items grouped into that pattern, and the mean of all the items grouped into that pattern.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri Light,sans-serif\'; font-size:9pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri Light,sans-serif\'; font-size:9pt; font-weight:600;\">Box Plot</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri Light,sans-serif\'; font-size:9pt; color:#000000;\">This window is a box plot representation of the table in the final results window, by showing it in a box plot, we can also see the range of the items in each pattern. There are options to set the upper and lower limits of the y-axis. There are also linear, logarithmic, and symmetrical logarithmic scaling options, linear is the default scale. Symmetrical logarithmic can be treated as logarithmic but with negative values included. Once the desired settings are selected, click the update button to update the box plot.  </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri Light,sans-serif\'; font-size:9pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri Light,sans-serif\'; font-size:9pt; font-weight:600;\">Output Files</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri Light,sans-serif\'; font-size:9pt; color:#000000;\">There are two output files created as well as another file which is updated for every successful run of the merging process.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri Light,sans-serif\'; font-size:9pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri Light,sans-serif\'; font-size:9pt; color:#000000;\">The updated file logs the runtimes and can be found at &quot;gandhiwashingtonmethod/synthesizing_pkg/synthesizing_runtimes.csv&quot;. Each successful run is logged on a different line, and is in the format:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri Light,sans-serif\'; font-size:9pt; font-style:italic; color:#000000;\">date time, input_file_path, runtime</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri Light,sans-serif\'; font-size:9pt; font-style:italic; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri Light,sans-serif\'; font-size:9pt; color:#000000;\">One of the files created logs what patterns have been merged together as well as their p-value  as a result of the Mann-Whitney test at the time of merging. The format of the file name is, &quot;</span><span style=\" font-family:\'Calibri Light,sans-serif\'; font-size:9pt; font-style:italic; color:#000000;\">date time input_file </span><span style=\" font-family:\'Calibri Light,sans-serif\'; font-size:9pt; color:#000000;\">output_log</span><span style=\" font-family:\'Calibri Light,sans-serif\'; font-size:9pt; font-style:italic; color:#000000;\">&quot; </span><span style=\" font-family:\'Calibri Light,sans-serif\'; font-size:9pt; color:#000000;\">and can be found at &quot;gandhiwashingtonmethod/synthesizing_pkg/logs&quot;. Each new line is a different merge, the format is in csv format, first the child node, then the parent node, then the p-value.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri Light,sans-serif\'; font-size:9pt; color:#000000;\">Example:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri Light,sans-serif\'; font-size:9pt; font-style:italic; color:#000000;\">A*B, A*B*, 0.98</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri Light,sans-serif\'; font-size:9pt; font-style:italic; color:#000000;\">CB, (C*B*)*, 0.10</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri Light,sans-serif\'; font-size:9pt; font-style:italic; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri Light,sans-serif\'; font-size:9pt; color:#000000;\">The final file created logs the results of the merging process. The format of the file name is, &quot;</span><span style=\" font-family:\'Calibri Light,sans-serif\'; font-size:9pt; font-style:italic; color:#000000;\">date time input_file </span><span style=\" font-family:\'Calibri Light,sans-serif\'; font-size:9pt; color:#000000;\">final_output_log</span><span style=\" font-family:\'Calibri Light,sans-serif\'; font-size:9pt; font-style:italic; color:#000000;\">&quot; </span><span style=\" font-family:\'Calibri Light,sans-serif\'; font-size:9pt; color:#000000;\">and can be found at &quot;gandhiwashingtonmethod/synthesizing_pkg/logs&quot;.  Each line is a pattern, followed by the final number of items in that pattern.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri Light,sans-serif\'; font-size:9pt; font-style:italic; color:#000000;\"><br /></p></body></html>"))


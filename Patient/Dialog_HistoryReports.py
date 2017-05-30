
from PySide.QtGui import *
import Setting as s

from Patient import Widget_HistoryReport


class HistoryReportDialog(QDialog):
    def __init__(self, AN, history_report):
        QDialog.__init__(self, None)
        posX, posY, sizeW, sizeH = s.GEOMETRY_DIALOG_HISTORY_REPORT
        self.setGeometry(posX, posY, sizeW, sizeH)
        self.history_report = history_report
        self.initUI()
        self.initLayout()
        self.AN = AN

    def initUI(self):
        prepre = self.history_report.part_prepre
        pre = self.history_report.part_pre
        intra = self.history_report.part_intra
        post = self.history_report.part_post
        self.widget = Widget_HistoryReport.WidgetHistoryReport(prepre, pre, intra, post)
        self.b_close = self.widget.b_cancel
        self.b_close.clicked.connect(self.closePressed)

    def initLayout(self):
        layout = QGridLayout()
        layout.addWidget(self.widget)
        self.setLayout(layout)

    def closePressed(self):
        self.close()

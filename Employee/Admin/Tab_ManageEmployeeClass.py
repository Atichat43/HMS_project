from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *

from Base.Widget_ComboBox import comboBoxClass


class TabManagePerson(QWidget):
    def __init__(self, Person):
        QWidget.__init__(self)
        self.Person = Person
        self.filterColumnComboBox = comboBoxClass.ComboBoxWithTypingSearch()
        self.filterPatternLineEdit = QLineEdit()
        self.setUI()
        self.setConnect()


    def setUI(self):
        loader = QUiLoader()
        form = loader.load('Employee/Admin/View/Tab_ManagePerson.ui', self)
        self.proxyView = form.findChild(QTreeView, 'treeView')
        self.layoutSearch = form.findChild(QHBoxLayout, 'layout_search')
        self.b_edit = form.findChild(QPushButton, 'b_edit')
        self.b_newPerson = QPushButton("new " + self.Person)
        self.layoutSearch.addWidget(self.filterColumnComboBox)
        self.layoutSearch.addWidget(self.filterPatternLineEdit)
        self.layoutSearch.addWidget(self.b_newPerson)
        self.setProxyView()

    def setComboBox(self, lstHead):
        model = QStandardItemModel()
        for i, word in enumerate(lstHead):
            item = QStandardItem(word)
            model.setItem(i, 0, item)
        self.filterColumnComboBox.setModel(model)
        self.filterColumnComboBox.setModelColumn(0)

    def setConnect(self):
        self.filterPatternLineEdit.textChanged.connect(self.filterRegExpChanged)
        self.filterColumnComboBox.currentIndexChanged.connect(self.filterColumnChanged)
        self.b_edit.clicked.connect(self.editPerson)
        self.b_newPerson.clicked.connect(self.newPerson)

    # def editPerson(self):
    #     dialog = Dialog_editOrNewEmployeeClass.EditOrNewDoctorDialog("Edit")
    #     ans = dialog.exec_()
    #     print(ans)
    #
    # def newPerson(self):
    #     dialog = Dialog_editOrNewEmployeeClass.EditOrNewDoctorDialog("New")
    #     ans = dialog.exec_()
    #     print(ans)

    def setProxyView(self):
        self.proxyView.setRootIsDecorated(False)
        self.proxyView.setAlternatingRowColors(True)
        self.proxyView.setSortingEnabled(True)
        self.setProxyModel()

    def setProxyModel(self):
        self.proxyModel = QSortFilterProxyModel()
        self.proxyModel.setDynamicSortFilter(True)
        self.proxyView.setModel(self.proxyModel)

    def setSourceModel(self, lstHead, Allrow):
        self.sizeOFHead = len(lstHead)
        self.setComboBox(lstHead)
        self.createBarSort(lstHead)
        self.addAllRow(Allrow)
        self.proxyModel.setSourceModel(self.model)

    def filterRegExpChanged(self):
        regExp = QRegExp(self.filterPatternLineEdit.text())
        self.proxyModel.setFilterRegExp(regExp)

    def filterColumnChanged(self):
        self.proxyModel.setFilterKeyColumn(self.filterColumnComboBox.currentIndex())

    def createBarSort(self, lstHead):
        self.model = QStandardItemModel(0, len(lstHead), self)
        for i in range(self.sizeOFHead):
            self.model.setHeaderData(i, Qt.Horizontal, lstHead[i])

    def addAllRow(self, allRow):
        count = 0
        for row in allRow:
            self.model.insertRow(count)
            for i in range(self.sizeOFHead):
                self.model.setData(self.model.index(count, i), row[i])
            count += 1


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    tab1_widget = TabManagePerson("Doctor")
    lstHead = ["NAME","ID", "Position", "Phone"]
    allRow = [("Atichat","001", "Brain", "0971249197"), ("Tiger","002","Chest", "0971249194")]
    tab1_widget.setSourceModel(lstHead, allRow)
    tab1_widget.show()
    sys.exit(app.exec_())


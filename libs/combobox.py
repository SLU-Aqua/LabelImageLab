import sys

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QComboBox


class ComboBox(QWidget):
    # def __init__(self, parent=None, items=[]):
    #    super(ComboBox, self).__init__(parent)
    def __init__(self, items=[]):
        super(ComboBox, self).__init__()

        layout = QHBoxLayout()
        self.cb = QComboBox()
        self.items = items
        self.cb.addItems(self.items)

        # self.cb.currentIndexChanged.connect(parent.combo_selection_changed)

        layout.addWidget(self.cb)
        self.setLayout(layout)

    def update_items(self, items: list):
        self.items = items
        # print(len(items), type(items[0]))
        # for it in items:
        #     print(it)

        self.cb.clear()
        self.cb.addItems(self.items)

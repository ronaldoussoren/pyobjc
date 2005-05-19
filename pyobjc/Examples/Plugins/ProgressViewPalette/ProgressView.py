from AppKit import *
from ProgressCell import ProgressCell

class ProgressView (NSControl):
    """
    A simple progress view
    """

    def percentageIncrement(self):
        return self.cell().percentageIncrement()

    def setPercentageIncrement_(self, value):
        self.cell().setPercentageIncrement_(value)

    def percentage(self):
        return self.cell().percentage()

    def setPercentage_(self, value):
        self.cell().setPercentage_(value)

    def increment_(self, sender):
        self.cell().increment_(sender)

    def color(self):
        return self.cell().color()

    def setColor_(self, value):
        self.cell().setColor_(value)


ProgressView.setCellClass_(ProgressCell)

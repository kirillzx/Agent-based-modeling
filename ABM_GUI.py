from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5.QtGui import QIcon
import random

plt.style.use('ggplot')

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 380, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 310, 191, 16))
        self.label.setObjectName("label")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(310, 340, 160, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 340, 191, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(310, 310, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.startf)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        m = PlotCanvas(self)
        m.move(0,0)


    def startf(self):
        print('the model was start')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Start"))
        self.label.setText(_translate("MainWindow", "Enter the number of the agents"))
        self.label_2.setText(_translate("MainWindow", "Choose the proportion of agents"))


status = ['a', 'p']
types = ['R', 'AA', 'BA', 'P']
agents_num = 20
size = 50

class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=15, height=14, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        #self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot()


    def plot(self):
        data = [random.random() for i in range(25)]
        ax = self.figure.add_subplot(111)
        ax.plot(data, 'r-')
        ax.set_title('PyQt Matplotlib Example')
        self.draw()


class Agent:
    def __init__(self, agents_num):
        self.id = np.array(range(agents_num))
        self.x = np.random.randint(0, size, agents_num)
        self.y = np.random.randint(0, size, agents_num)
        self.age = np.random.randint(50, 100, agents_num)
        self.aw_vector = np.random.randint(0, 2, agents_num)

    def make_agent(self, status, types, age, inf, idf):
        return [status, types, age, inf, idf]

    def make_population(self, status, types, agents_num):

        population = []

        for i in range(agents_num):

            agent = self.make_agent(np.random.choice(status), np.random.choice(types), self.age[i], self.aw_vector[i], self.id[i])
            population.append(agent)
        return population

    def count(self, population):
        t = 0.
        for agent in population:
            if agent[0] == 'a':
                t += 1
        return t / len(population)

    def choose_pair(self, population):
        i = np.random.randint(0, len(population) - 1)
        j = np.random.randint(0, len(population) - 1)

        while i == j:
            j = np.random.randint(0, len(population) - 1)

        return [population[i], population[j]]

    def interact(self, listener, producer):
        #if (listener[1] == 'R' or listener[1] == 'AA') and (producer[1] == 'R' or producer[1] == 'AA'):

        if listener[0] == 'a' and producer[0] != 'a' and listener[3] == 1 :
            producer[0] = 'a'
            return producer
        elif listener[0] == 'a' and producer == 'a':
            return producer
        elif listener[0] != 'a' and producer[0] == 'a' and producer[3] == 1 :
            listener[0] = 'a'
            return listener
        else:
            listener[0] = np.random.choice(['a', 'p'])
            return listener
    def move(self, population):
        for i in self.id:
            self.age[i] -= 1
            if self.age[i] <= 0:
                self.id = self.id[self.id != i]
        for i in population:
            i[2] -= 1
            if i[2] <= 0:
                population.remove(i)
agents = Agent(agents_num)
population = agents.make_population(status, types, agents_num)
#print(agents.id)
#print(agents.x)
#print(agents.y)
#print(agents.count(population))
pair = agents.choose_pair(population)
#print(pair)
#print(agents.interact(pair[0], pair[1]))


def simulate(agents_num, k):
    population = agents.make_population(status, types, agents_num)

    proportion = []

    for i in range(k):
            agents.move(population)
            pair = agents.choose_pair(population)
            agents.interact(pair[0], pair[1])
            proportion.append(agents.count(population))
            agents.choose_pair(population)[0][0] = 'p'
    return population, proportion

new_pop, proportion = simulate(agents_num, 70)
print(new_pop)

plt.plot(proportion)
plt.title('Changes in the proportion of active users over time')
plt.xlabel('Time')
plt.ylabel('Proportion of active users')
#plt.show()
#plt.savefig('graphic.jpg')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

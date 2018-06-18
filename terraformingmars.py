# Terraforming Mars playerboard app
# Written by Daniel Larssoon
# Licensed under GPLV2
# This is released as it is not warranty
import PyQt5.QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import time

resources = {   'currentCurrency':0,
                'steelResource':0,
                'titaniumResource':0,
                'plantResource':0,
                'energyResource':0,
                'heatResource':0,
                'currentTR':20,
                'choice':False,
                'incomeCurrency':0,
                'incomeSteel':0,
                'incomeTitanium':0,
                'incomePlant':0,
                'incomeEnergy':0,
                'incomeHeat':0,
                'helion':False,
                'phob':False,}

def currency(c,tr,e):
    summa = c + tr
    summa = summa + e
    return summa

def resource(x,y):
    summa = x + y
    return summa


class Terraforming(QWidget):
    def __init__(self):
        def setLayout(self):
            self.layout = QGridLayout(self)
            self.setLayout(self.layout)
            self.setWindowTitle('Terraforming Mars')

        def setLabels(self):
            # Currency
            labeltext = "Currency" # Change varible in future
            label = QLabel(labeltext)
            label.setFixedHeight(20)
            label.setFixedWidth(120)
            self.layout.addWidget(label, 1, 0)

            # Steel
            labeltext = "Steel" # Change varible in future
            label = QLabel(labeltext)
            label.setFixedHeight(20)
            label.setFixedWidth(120)
            self.layout.addWidget(label, 1, 1)

            # Titanium
            labeltext = "Titanium" # Change varible in future
            label = QLabel(labeltext)
            label.setFixedHeight(20)
            label.setFixedWidth(120)
            self.layout.addWidget(label, 1, 2)

            # Plant
            labeltext = "Plant" # Change varible in future
            label = QLabel(labeltext)
            label.setFixedHeight(20)
            label.setFixedWidth(120)
            self.layout.addWidget(label, 5, 0)

            # Energy
            labeltext = "Energy" # Change varible in future
            label = QLabel(labeltext)
            label.setFixedHeight(20)
            label.setFixedWidth(120)
            self.layout.addWidget(label, 5, 1)

            # Heat
            labeltext = "Heat" # Change varible in future
            label = QLabel(labeltext)
            label.setFixedHeight(20)
            label.setFixedWidth(120)
            self.layout.addWidget(label, 5, 2)

        def displayCurrency(self):
            self.current_currency = QLCDNumber(self)
            self.current_currency.setFixedHeight(200)
            self.current_currency.setFixedWidth(200)
            self.current_currency.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
            self.layout.addWidget(self.current_currency,2, 0)
            self.current_currency.display(resources['currentCurrency'])

        def newTurn():
            
            def newCurrency():
                self.current_currency.display(currency(resources['currentTR'], resources['currentCurrency'], resources['incomeCurrency']))
                x = self.current_currency.value()
                resources.update({'currentCurrency': int(x)})

            def newSteel():
                self.current_steel.display(resource(resources['steelResource'], resources['incomeSteel']))
                x = self.current_steel.value()
                resources.update({'steelResource': int(x)})

            def newTitanium():
                self.current_titanium.display(resource(resources['titaniumResource'], resources['incomeTitanium']))
                x = self.current_titanium.value()
                resources.update({'titaniumResource': int(x)})

            def newPlant():
                self.current_plant.display(resource(resources['plantResource'], resources['incomePlant']))
                x = self.current_plant.value()
                resources.update({'plantResource': int(x)})

            def newEnergy():
                if self.current_energy.value() >= 0:
                    def updateHeat():
                        __newValue = resources['energyResource'] + resources['heatResource']
                        resources.update({'heatResource': __newValue})
                    
                    def updateEnergy():
                        self.current_energy.display(resources['incomeEnergy'])
                        x = self.current_energy.value()
                        resources.update({'energyResource': int(x)})
                    updateHeat()
                    updateEnergy()

                else:
                    self.current_energy.display(resources['incomeEnergy'])
                    x = self.current_energy.value()
                    resources.update({'energyResource': int(x)})

            def newHeat():
                self.current_heat.display(resource(resources['heatResource'], resources['incomeHeat']))
                x = self.current_heat.value()
                resources.update({'heatResource': int(x)})

            newCurrency()
            newSteel()
            newTitanium()
            newPlant()
            newEnergy()
            newHeat()

        def setResources(self):
            #Steel
            self.current_steel = QLCDNumber(self)
            self.current_steel.setFixedHeight(200)
            self.current_steel.setFixedWidth(200)
            self.layout.addWidget(self.current_steel,2, 1)
            self.current_steel.display(resources['steelResource'])

            # Titanium
            self.current_titanium = QLCDNumber(self)
            self.current_titanium.setFixedHeight(200)
            self.current_titanium.setFixedWidth(200)
            self.layout.addWidget(self.current_titanium,2, 2)
            self.current_titanium.display(resources['titaniumResource'])

            # Plant
            self.current_plant = QLCDNumber(self)
            self.current_plant.setFixedHeight(200)
            self.current_plant.setFixedWidth(200)
            self.layout.addWidget(self.current_plant,6, 0)
            self.current_plant.display(resources['plantResource'])

            # Energy
            self.current_energy = QLCDNumber(self)
            self.layout.addWidget(self.current_energy,6, 1)
            self.current_energy.display(resources['energyResource'])


            # Heat
            self.current_heat = QLCDNumber(self)
            self.layout.addWidget(self.current_heat,6, 2)
            self.current_heat.display(resources['heatResource'])

        def advanceAlloy(self):
                self.cardAdvanceAlloy = QRadioButton("Advanced Alloy Card",self)
                self.layout.addWidget(self.cardAdvanceAlloy, 2, 3)
                self.cardAdvanceAlloy.setChecked(False)

        def buttonCall(self):
            self.name = QLineEdit(self)
            self.name.setMaxLength(10)
            self.name.setFixedWidth(80)
            self.name.setPlaceholderText("Your name")
            self.layout.addWidget(self.name, 0, 0)
            self.yourName = self.name.text()
            #self.name.setDisabled(True)

        def callQuit(self):
            self.turnPass = QPushButton('Pass',self)
            self.layout.addWidget(self.turnPass,7, 6)
            self.turnPass.clicked.connect(newTurn)# insert function here

        def buyIncreaseOxygen():
            oxygen = QPushButton('Modify Plant',self)
            self.layout.addWidget(oxygen,8, 0)
            oxygen.setFixedWidth(150)
            oxygen.clicked.connect(popUpPlant)

        def buyIncreaseTemperature():
            temperature = QPushButton('Modify Heat',self)
            self.layout.addWidget(temperature,8, 2)
            temperature.clicked.connect(popUpHeat)

        def buyCard():
            buyCard = QPushButton('Buy a Card',self)
            self.layout.addWidget(buyCard,2, 6)
            buyCard.clicked.connect(popUpBuyCard)

        def buyWithSteel():
            steel = QPushButton('Modify Steel',self)
            self.layout.addWidget(steel,4,1)
            steel.setFixedWidth(150)
            steel.clicked.connect(popUpSteel)

        def buyWithTitanium():
            titanium = QPushButton('Modify Titanium',self)
            self.layout.addWidget(titanium,4,2)
            titanium.setFixedWidth(150)
            titanium.clicked.connect(popUpTitanium)

        def buyWithCurrency():
            __currency = QPushButton('Modify Currency',self)
            self.layout.addWidget(__currency,4,0)
            __currency.setFixedWidth(150)
            __currency.clicked.connect(popUpCurrency)

        def buyWithEnergy():
            __energy = QPushButton('Modify Energy',self)
            self.layout.addWidget(__energy,8,1)
            __energy.setFixedWidth(150)
            __energy.clicked.connect(popUpEnergy)

        def popUpBuyCard():
            d = QDialog()

            def calcBuyCardHelion():
                cost = int(cc.text())
                heatUse = heatSpin.value()
                steelUse = steelSpin.value() * 2
                titaniumUse = titaniumSpin.value() * 3
                resourcesUsed = (titaniumUse + steelUse) + heatUse
                summa = cost - resourcesUsed
                remainder.setText(str(summa))

            def calcBuyCard():
                if cc.isModified() == True:
                    if self.cardAdvanceAlloy.isChecked() == True:
                        cost = int(cc.text())
                        steelUse = steelSpin.value() * 3
                        titaniumUse = titaniumSpin.value() * 4
                        sum = (cost - steelUse) - titaniumUse
                        remainder.setText(str(sum))

                    elif self.cardAdvanceAlloy.isChecked() == True and resources['phob'] == True:
                        cost = int(cc.text())
                        steelUse = steelSpin.value() * 3
                        titaniumUse = titaniumSpin.value() * 5
                        sum = (cost - steelUse) - titaniumUse
                        remainder.setText(str(sum))

                    elif resources['phob'] == True:
                        cost = int(cc.text())
                        steelUse = steelSpin.value() * 2
                        titaniumUse = titaniumSpin.value() * 4
                        sum = (cost - steelUse) - titaniumUse
                        remainder.setText(str(sum))

                    else:
                        cost = int(cc.text())
                        steelUse = steelSpin.value() * 2
                        titaniumUse = titaniumSpin.value() * 3
                        sum = (cost - steelUse) - titaniumUse
                        remainder.setText(str(sum))
                else:
                    print("Please enter a Value")

            def helio():
                    x = int(remainder.text())
                    y = resources['currentCurrency']
                    steelUse = steelSpin.value()
                    titaniumUse = titaniumSpin.value()
                    heatUse = heatSpin.value()
                    if x > y:
                        print('Not enough Money')
                        if x >= 0:
                            if resources['steelResource'] >= steelUse and resources['titaniumResource'] >= titaniumUse and resources['heatResource'] >= heatUse:
                                __newValue1 = resources['steelResource'] - steelUse
                                __newValue2 = resources['titaniumResource'] - titaniumUse
                                __newValue3 = resources['heatResource'] - heatUse
                                resources.update({'steelResource':__newValue1})
                                resources.update({'titaniumResource':__newValue2})
                                resources.update({'heatResource':__newValue3})
                                self.current_titanium.display(resources['titaniumResource'])
                                self.current_steel.display(resources['steelResource'])
                                self.current_heat.display(resources['heatResource'])
                            else:
                                print("Not enough Resources")
                            if x < y:
                                self.current_currency.display(y - x)
                                resources['currentCurrency'] = y - x
                        else:
                            if resources['steelResource'] >= steelUse and resources['titaniumResource'] >= titaniumUse and resources['heatResource'] >= heatUse:
                                __newValue1 = resources['steelResource'] - steelUse
                                __newValue2 = resources['titaniumResource'] - titaniumUse
                                __newValue3 = resources['heatResource'] - heatUse
                                resources.update({'steelResource':__newValue1})
                                resources.update({'titaniumResource':__newValue2})
                                resources.update({'heatResource':__newValue3})
                                self.current_titanium.display(resources['titaniumResource'])
                                self.current_steel.display(resources['steelResource'])
                                self.current_heat.display(resources['heatResource'])
                            else:
                                print("Not enough Resources")

            def normal():
                x = int(remainder.text())
                y = resources['currentCurrency']
                steelUse = steelSpin.value()
                titaniumUse = titaniumSpin.value()
                if x > y:
                    print('Not enough Money!')
                else:
                    if x >= 0:
                        if resources['steelResource'] >= steelUse and resources['titaniumResource'] >= titaniumUse:
                            __newValue1 = resources['steelResource'] - steelUse
                            __newValue2 = resources['titaniumResource'] - titaniumUse
                            resources.update({'steelResource':__newValue1})
                            resources.update({'titaniumResource':__newValue2})
                            self.current_titanium.display(resources['titaniumResource'])
                            self.current_steel.display(resources['steelResource'])
                        else:
                            print("Not enough Resources")
                        if x < y:
                            self.current_currency.display(y - x)
                            resources['currentCurrency'] = y - x
                    else:
                        if resources['steelResource'] >= steelUse and resources['titaniumResource'] >= titaniumUse:
                            __newValue1 = resources['steelResource'] - steelUse
                            __newValue2 = resources['titaniumResource'] - titaniumUse
                            resources.update({'steelResource':__newValue1})
                            resources.update({'titaniumResource':__newValue2})
                            self.current_titanium.display(resources['titaniumResource'])
                            self.current_steel.display(resources['steelResource'])
                        else:
                            print("Not enough Resources")
                

            def buyIt():
                if resources['helion'] == True:
                    helio()
                
                else:
                    normal()
                d.close()

            d.setWindowTitle("Buy a Card")
            """Button"""
            b1 = QPushButton('Ok',d)
            b1.move(120,200)
            b1.clicked.connect(buyIt)
            """Button"""
            b2 = QPushButton("Cancel", d)
            b2.move(40,200)
            b2.clicked.connect(d.close)

            b3 = QPushButton("Calculate", d)
            b3.move(75,170)
            if resources['helion'] == True:
                b3.clicked.connect(calcBuyCardHelion)
            else:
                b3.clicked.connect(calcBuyCard)
            """Card Cost"""
            cc = QLineEdit(d)
            cc.setMaxLength(10)
            cc.setFixedWidth(80)
            cc.move(75,0)
            cc.setPlaceholderText("Card Cost")
            cc.setText("0")

            if resources['helion'] == True:
                labeltext = "Heat" # Change varible in future
                heatLabel = QLabel(labeltext,d)
                heatLabel.setFixedHeight(20)
                heatLabel.setFixedWidth(120)
                heatLabel.move(50,100)
                heatSpin = QSpinBox(d)
                heatSpin.setFixedHeight(20)
                heatSpin.setFixedWidth(100)
                heatSpin.move(75,100)
            else:
                pass

            """Steel QSpinBox"""
            labeltext = 'Steel'
            steelLabel = QLabel(labeltext,d)
            steelLabel.setFixedHeight(20)
            steelLabel.setFixedWidth(120)
            steelLabel.move(50,40)
            steelSpin = QSpinBox(d)
            steelSpin.setFixedHeight(20)
            steelSpin.setFixedWidth(100)
            steelSpin.move(75,40)
            """Titanium QSpinBox"""
            labeltext = 'Titanium'
            titaniumLabel = QLabel(labeltext,d)
            titaniumLabel.setFixedHeight(20)
            titaniumLabel.setFixedWidth(120)
            titaniumLabel.move(30,70)
            titaniumSpin = QSpinBox(d)
            titaniumSpin.setFixedHeight(20)
            titaniumSpin.setFixedWidth(100)
            titaniumSpin.move(75,70)
            """left to pay"""
            remainder = QLineEdit(d)
            remainder.setMaxLength(10)
            remainder.setFixedWidth(80)
            remainder.move(75,140)
            remainder.setPlaceholderText("30")
            remainder.setText("0")
            remainder.setReadOnly(True)

            d.exec_()

        def popUpCurrency():
            d = QDialog()

            def changeCurrencyIncome():
                __newValue = currencyIncomeSpin.value()
                resources.update({'incomeCurrency': __newValue})
                d.close()

            def changeCurrencyPop():
                __newValue = currencySpin.value()
                resources.update({'currentCurrency': __newValue})
                self.current_currency.display(resources['currentCurrency'])
                d.close()

            labeltext = "Currency" # Change varible in future
            label = QLabel(labeltext,d)
            label.move(10,0)
            label.setFixedHeight(20)
            label.setFixedWidth(120)

            labeltext = "Income" # Change varible in future
            label = QLabel(labeltext,d)
            label.move(10,50)
            label.setFixedHeight(20)
            label.setFixedWidth(120)

            currencySpin = QSpinBox(d)
            currencySpin.setFixedHeight(20)
            currencySpin.setFixedWidth(100)
            currencySpin.move(10,25)
            currencySpin.setValue(resources['currentCurrency'])

            currencyIncomeSpin = QSpinBox(d)
            currencyIncomeSpin.setValue(resources['incomeCurrency'])
            currencyIncomeSpin.setFixedHeight(20)
            currencyIncomeSpin.setFixedWidth(100)
            currencyIncomeSpin.setRange(-5,30)
            currencyIncomeSpin.move(10,75)

            b1 = QPushButton("Ok", d)
            b1.move(150,25)
            b1.clicked.connect(changeCurrencyPop)

            b2 = QPushButton("Ok", d)
            b2.move(150,75)
            b2.clicked.connect(changeCurrencyIncome)

            d.setWindowTitle("Currency")
            d.exec_()

        def popUpSteel():
            d = QDialog()

            def changeSteelIncome():
                __newValue = steelIncomeSpin.value()
                resources.update({'incomeSteel': __newValue})
                d.close()

            def changeSteelPop():
                __newValue = steelSpin.value()
                resources.update({'steelResource': __newValue})
                self.current_steel.display(resources['steelResource'])
                d.close()

            labeltext = "Current" # Change varible in future
            label = QLabel(labeltext,d)
            label.move(10,0)
            label.setFixedHeight(20)
            label.setFixedWidth(120)

            labeltext = "Income" # Change varible in future
            label = QLabel(labeltext,d)
            label.move(10,50)
            label.setFixedHeight(20)
            label.setFixedWidth(120)

            steelSpin = QSpinBox(d)
            steelSpin.setFixedHeight(20)
            steelSpin.setFixedWidth(100)
            steelSpin.move(10,25)
            steelSpin.setValue(resources['steelResource'])

            steelIncomeSpin = QSpinBox(d)
            steelIncomeSpin.setValue(resources['incomeSteel'])
            steelIncomeSpin.setFixedHeight(20)
            steelIncomeSpin.setFixedWidth(100)
            steelIncomeSpin.move(10,75)

            b1 = QPushButton("Done", d)
            b1.move(150,25)
            b1.clicked.connect(changeSteelPop)

            b2 = QPushButton("Done", d)
            b2.move(150,75)
            b2.clicked.connect(changeSteelIncome)

            d.setWindowTitle("Steel")
            d.exec_()

        def popUpTitanium():
            d = QDialog()

            def changeTitaniumIncome():
                __newValue = titaniumIncomeSpin.value()
                resources.update({'incomeTitanium': __newValue})
                d.close()

            def changeTitaniumPop():
                __newValue = titaniumSpin.value()
                resources.update({'titaniumResource': __newValue})
                self.current_titanium.display(resources['titaniumResource'])
                d.close()

            labeltext = "Current" # Change varible in future
            label = QLabel(labeltext,d)
            label.move(10,0)
            label.setFixedHeight(20)
            label.setFixedWidth(120)

            labeltext = "Income" # Change varible in future
            label = QLabel(labeltext,d)
            label.move(10,50)
            label.setFixedHeight(20)
            label.setFixedWidth(120)

            titaniumSpin = QSpinBox(d)
            titaniumSpin.setFixedHeight(20)
            titaniumSpin.setFixedWidth(100)
            titaniumSpin.move(10,25)
            titaniumSpin.setValue(resources['titaniumResource'])

            titaniumIncomeSpin = QSpinBox(d)
            titaniumIncomeSpin.setFixedHeight(20)
            titaniumIncomeSpin.setFixedWidth(100)
            titaniumIncomeSpin.move(10,75)
            titaniumIncomeSpin.setValue(resources['incomeTitanium'])

            b1 = QPushButton("Ok", d)
            b1.move(150,25)
            b1.clicked.connect(changeTitaniumPop)

            b2 = QPushButton("Ok", d)
            b2.move(150,75)
            b2.clicked.connect(changeTitaniumIncome)

            d.setWindowTitle("Titanium")
            d.exec_()

        def popUpPlant():
            d = QDialog()

            def IncreaseOxygen():
                if resources['choice'] == True:
                    if resources['plantResource'] >= 7:
                        __newValue = resources['plantResource']
                        __newValue = __newValue - 7
                        resources.update({'plantResource': __newValue})
                        self.current_plant.display(resources['plantResource'])
                        plantSpin.setValue(resources['plantResource'])
                        __newTR = resources['currentTR']
                        __newTR = __newTR + 1
                        resources.update({'currentTR': __newTR})
                        d.close()
                    else:
                        print('Not enough plant resources')
                        d.close()
                else:
                    if resources['plantResource'] >= 8:
                        __newValue = resources['plantResource']
                        __newValue = __newValue - 8
                        resources.update({'plantResource': __newValue})
                        self.current_plant.display(resources['plantResource'])
                        plantSpin.setValue(resources['plantResource'])
                        __newTR = resources['currentTR']
                        __newTR = __newTR + 1
                        resources.update({'currentTR': __newTR})
                        d.close()
                    else:
                        print('Not enough plant resources')
                        d.close()

            def changePlantPop():
                __newValue = plantSpin.value()
                resources.update({'plantResource': __newValue})
                self.current_plant.display(resources['plantResource'])
                d.close()

            def changePlantIncome():
                __newValue = plantIncomeSpin.value()
                resources.update({'incomePlant': __newValue})
                d.close()

            labeltext = "Current" # Change varible in future
            label = QLabel(labeltext,d)
            label.move(10,0)
            label.setFixedHeight(20)
            label.setFixedWidth(120)

            labeltext = "income" # Change varible in future
            label = QLabel(labeltext,d)
            label.move(10,50)
            label.setFixedHeight(20)
            label.setFixedWidth(120)

            plantSpin = QSpinBox(d)
            plantSpin.setFixedHeight(20)
            plantSpin.setFixedWidth(100)
            plantSpin.setValue(resources['plantResource'])
            plantSpin.move(10,25)

            plantIncomeSpin = QSpinBox(d)
            plantIncomeSpin.setValue(resources['incomePlant'])
            plantIncomeSpin.setFixedHeight(20)
            plantIncomeSpin.setFixedWidth(100)
            plantIncomeSpin.move(10,75)

            b1 = QPushButton("Ok", d)
            b1.move(150,25)
            b1.clicked.connect(changePlantPop)

            b2 = QPushButton("Ok", d)
            b2.move(150,75)
            b2.clicked.connect(changePlantIncome)

            oxygen = QPushButton('Buy Oxygen increase',d)
            oxygen.setFixedWidth(150)
            oxygen.move(10,150)
            oxygen.clicked.connect(IncreaseOxygen)

            d.setWindowTitle("Plant")
            d.exec_()

        def popUpEnergy():
            d = QDialog()

            def changeEnergyPop():
                __newValue = energySpin.value()
                resources.update({'energyResource': __newValue})
                self.current_energy.display(resources['energyResource'])
                d.close()

            def changeEnergyIncome():
                __newValue = energyIncomeSpin.value()
                resources.update({'incomeEnergy': __newValue})
                d.close()

            labeltext = "Current" # Change varible in future
            label = QLabel(labeltext,d)
            label.move(10,0)
            label.setFixedHeight(20)
            label.setFixedWidth(120)

            labeltext = "Income" # Change varible in future
            label = QLabel(labeltext,d)
            label.move(10,50)
            label.setFixedHeight(20)
            label.setFixedWidth(120)

            energySpin = QSpinBox(d)
            energySpin.setFixedHeight(20)
            energySpin.setFixedWidth(100)
            energySpin.setValue(resources['energyResource'])
            energySpin.move(10,25)

            energyIncomeSpin = QSpinBox(d)
            energyIncomeSpin.setFixedHeight(20)
            energyIncomeSpin.setFixedWidth(100)
            energyIncomeSpin.setValue(resources['incomeEnergy'])
            energyIncomeSpin.move(10,75)

            b1 = QPushButton("Ok", d)
            b1.move(150,25)
            b1.clicked.connect(changeEnergyPop)

            b2 = QPushButton("Ok", d)
            b2.move(150,75)
            b2.clicked.connect(changeEnergyIncome)

            d.setWindowTitle("Energy")
            d.exec_()

        def popUpHeat():
            d = QDialog()

            def IncreaseTemperature():
                if resources['choice'] == True:
                    if resources['heatResource'] >= 7:
                        __newValue = resources['heatResource']
                        __newValue = __newValue - 7
                        resources.update({'heatResource': __newValue})
                        self.current_heat.display(resources['heatResource'])
                        __newTR = resources['currentTR']
                        __newTR = __newTR + 1
                        resources.update({'currentTR': __newTR})
                        d.close()
                    else:
                        print('Not enough heat resources')
                        d.close()
                else:
                    if resources['heatResource'] >= 8:
                        __newValue = resources['heatResource']
                        __newValue = __newValue - 8
                        resources.update({'heatResource': __newValue})
                        self.current_heat.display(resources['heatResource'])
                        __newTR = resources['currentTR']
                        __newTR = __newTR + 1
                        resources.update({'currentTR': __newTR})
                        d.close()
                    else:
                        print('Not enough heat resources')
                        d.close()

            def changeHeatPop():
                __newValue = heatSpin.value()
                resources.update({'heatResource': __newValue})
                self.current_heat.display(resources['heatResource'])
                d.close()

            def changeHeatIncome():
                __newValue = heatIncomeSpin.value()
                resources.update({'incomeHeat': __newValue})
                d.close()

            labeltext = "Current" # Change varible in future
            label = QLabel(labeltext,d)
            label.move(10,0)
            label.setFixedHeight(20)
            label.setFixedWidth(120)

            labeltext = "Income" # Change varible in future
            label = QLabel(labeltext,d)
            label.move(10,50)
            label.setFixedHeight(20)
            label.setFixedWidth(120)

            temperature = QPushButton('Buy Temperature increase',d)
            temperature.setFixedWidth(200)
            temperature.move(10,150)
            temperature.clicked.connect(IncreaseTemperature)

            heatSpin = QSpinBox(d)
            heatSpin.setFixedHeight(20)
            heatSpin.setFixedWidth(100)
            heatSpin.setValue(resources['heatResource'])
            heatSpin.move(10,25)

            heatIncomeSpin = QSpinBox(d)
            heatIncomeSpin.setFixedHeight(20)
            heatIncomeSpin.setFixedWidth(100)
            heatIncomeSpin.setValue(resources['incomeHeat'])
            heatIncomeSpin.move(10,75)

            b1 = QPushButton("Ok", d)
            b1.move(150,25)
            b1.clicked.connect(changeHeatPop)

            b2 = QPushButton("Ok", d)
            b2.move(150,75)
            b2.clicked.connect(changeHeatIncome)

            d.setWindowTitle("Heat")
            d.exec_()

        def corpChoice(self):

            def choicePicked():
                def killWidget(argv):
                    self.choice.setDisabled(True)
                    self.name.setDisabled(True)
                    x = 'Terraforming Mars                  Corperation: ' + argv
                    self.setWindowTitle(x)

                if str(self.choice.currentIndex()) == '0':
                    resources.update({'currentCurrency': 42})
                    self.current_currency.display(resources['currentCurrency'])
                    #self.current_currency.display(resources['currentCurrency']) FIXA!!!
                    killWidget('Beginner Corperation')

                elif str(self.choice.currentIndex()) == '1':
                    resources.update({'currentCurrency': 57})
                    self.current_currency.display(resources['currentCurrency'])
                    killWidget('Credicor')

                elif str(self.choice.currentIndex()) == '2':
                    resources.update({'currentCurrency': 36})
                    resources.update({'plantResource': 3})
                    resources.update({'incomePlant': 2})
                    resources.update({'choice': True})
                    self.current_currency.display(resources['currentCurrency'])
                    self.current_plant.display(resources['plantResource'])
                    #self.current_currency.display(resources['currentCurrency']) FIXA!!!
                    killWidget('Ecoline')

                elif str(self.choice.currentIndex()) == '3':
                    resources.update({'currentCurrency': 42})
                    resources.update({'incomeHeat': 3})
                    resources.update({'helion': True})
                    self.current_currency.display(resources['currentCurrency'])
                    #self.current_currency.display(resources['currentCurrency']) FIXA!!!
                    killWidget('Helion')

                elif str(self.choice.currentIndex()) == '4':
                    resources.update({'currentCurrency': 30})
                    resources.update({'steelResource': 20})
                    self.current_currency.display(resources['currentCurrency'])
                    self.current_steel.display(resources['steelResource'])
                    #self.current_currency.display(resources['currentCurrency']) FIXA!!!
                    killWidget('Interplanetary Cinematics')

                elif str(self.choice.currentIndex()) == '5':
                    resources.update({'currentCurrency': 45})
                    self.current_currency.display(resources['currentCurrency'])
                    #self.current_currency.display(resources['currentCurrency']) FIXA!!!
                    killWidget('Inventrix')

                elif str(self.choice.currentIndex()) == '6':
                    resources.update({'currentCurrency': 30})
                    resources.update({'steelResource': 5})
                    resources.update({'incomeSteel': 1})
                    self.current_currency.display(resources['currentCurrency'])
                    self.current_steel.display(resources['steelResource'])
                    #self.current_currency.display(resources['currentCurrency']) FIXA!!!
                    killWidget('Mining Guild')

                elif str(self.choice.currentIndex()) == '7':
                    resources.update({'currentCurrency': 23})
                    resources.update({'titaniumResource': 10})
                    resources.update({'phob': True}) #Titanium is worth 1 more currency Need to implement function for this
                    self.current_currency.display(resources['currentCurrency'])
                    self.current_steel.display(resources['steelResource'])
                    #self.current_currency.display(resources['currentCurrency']) FIXA!!!
                    killWidget('Mining Guild')

                elif str(self.choice.currentIndex()) == '8':
                    resources.update({'currentCurrency': 40})
                    self.current_currency.display(resources['currentCurrency'])
                    killWidget('Republic Tharis')

                elif str(self.choice.currentIndex()) == '9':
                    resources.update({'currentCurrency': 42})
                    resources.update({'incomeTitanium': 1})
                    self.current_currency.display(resources['currentCurrency'])
                    #self.current_currency.display(resources['currentCurrency']) FIXA!!!
                    killWidget('Saturn Systems')

                elif str(self.choice.currentIndex()) == '10':
                    resources.update({'currentCurrency': 60})
                    self.current_currency.display(resources['currentCurrency'])
                    killWidget('Teractor')

                elif str(self.choice.currentIndex()) == '11':
                    resources.update({'currentCurrency': 48})
                    resources.update({'incomeEnergy': 1})
                    self.current_currency.display(resources['currentCurrency'])
                    #self.current_currency.display(resources['currentCurrency']) FIXA!!!
                    killWidget('Thorgate')

                elif str(self.choice.currentIndex()) == '12':
                    resources.update({'currentCurrency': 40})
                    self.current_currency.display(resources['currentCurrency'])
                    killWidget('United Nations Mars Initiative')

                elif str(self.choice.currentIndex()) == '13':
                    resources.update({'currentCurrency': 40})
                    resources.update({'steelResource': 10})
                    self.current_currency.display(resources['currentCurrency'])
                    self.current_steel.display(resources['steelResource'])
                    killWidget('Arcadian Communities')

                elif str(self.choice.currentIndex()) == '14':
                    resources.update({'currentCurrency': 44})
                    self.current_currency.display(resources['currentCurrency'])
                    killWidget('Splice')

                elif str(self.choice.currentIndex()) == '15':
                    resources.update({'currentCurrency': 38})
                    resources.update({'incomeSteel': 1})
                    self.current_currency.display(resources['currentCurrency'])
                    #self.current_currency.display(resources['currentCurrency']) FIXA!!!
                    killWidget('Recyclon')

                else:
                    print('Add function')

            self.choice = QComboBox(self)
            self.choice.addItem('Beginner Corperation')
            self.choice.addItem('Credicor')
            self.choice.addItem('Ecoline')
            self.choice.addItem('Helion')
            self.choice.addItem('Interplanetary Cinematics')
            self.choice.addItem('Inventrix')
            self.choice.addItem('Mining Guild')
            self.choice.addItem('Phob Log')
            self.choice.addItem('Republic Tharis')
            self.choice.addItem('Saturn Systems')
            self.choice.addItem('Teractor')
            self.choice.addItem('Thorgate')
            self.choice.addItem('United Nations Mars Initiative')
            self.choice.addItem('Arcadian Communities')
            self.choice.addItem('Splice')
            self.choice.addItem('Recyclon')
            self.layout.addWidget(self.choice,0,4)
            self.choice.setMaxVisibleItems(20)

            self.choose = QPushButton('Done',self)
            self.layout.addWidget(self.choose,0, 5)
            self.choose.clicked.connect(choicePicked)

        QWidget.__init__(self)
        setLayout(self)
        setLabels(self)
        displayCurrency(self)
        setResources(self)
        advanceAlloy(self)
        buttonCall(self)
        buyIncreaseOxygen()
        buyIncreaseTemperature()
        buyCard()
        buyWithTitanium()
        buyWithSteel()
        buyWithCurrency()
        buyWithEnergy()
        callQuit(self)
        corpChoice(self)


def main():
    app = QApplication(sys.argv)
    dialog = Terraforming()
    dialog.resize(1024,480)
    dialog.show()
    app.exec_()

if __name__ == '__main__':
    main()

import sys				
from RegresionLineal import * 
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
import matplotlib.pyplot as plt

class Ecuacion(QtWidgets.QMainWindow): 
	def __init__(self):						
		super().__init__()					
		self.ui = Ui_Dialog()			
		self.ui.setupUi(self)

		#validar todos los lineEdits para que reciban únicamente números
		self.ui.txtn.setValidator(QIntValidator())
		self.ui.txtxi1.setValidator(QDoubleValidator())
		self.ui.txtxi2.setValidator(QDoubleValidator())
		self.ui.txtxi3.setValidator(QDoubleValidator())
		self.ui.txtxi4.setValidator(QDoubleValidator())
		self.ui.txtxi5.setValidator(QDoubleValidator())
		self.ui.txtxi6.setValidator(QDoubleValidator())
		self.ui.txtxi7.setValidator(QDoubleValidator())
		self.ui.txtxi8.setValidator(QDoubleValidator())
		self.ui.txtxi9.setValidator(QDoubleValidator())
		self.ui.txtxi10.setValidator(QDoubleValidator())
		self.ui.txtyi1.setValidator(QDoubleValidator())
		self.ui.txtyi2.setValidator(QDoubleValidator())
		self.ui.txtyi3.setValidator(QDoubleValidator())
		self.ui.txtyi4.setValidator(QDoubleValidator())
		self.ui.txtyi5.setValidator(QDoubleValidator())
		self.ui.txtyi6.setValidator(QDoubleValidator())
		self.ui.txtyi7.setValidator(QDoubleValidator())
		self.ui.txtyi8.setValidator(QDoubleValidator())
		self.ui.txtyi9.setValidator(QDoubleValidator())
		self.ui.txtyi10.setValidator(QDoubleValidator())
		#botones y sus acciones
		self.ui.btnEcuacion.clicked.connect(self.evaluar)
		self.ui.btnGrafica.clicked.connect(self.grafica)
		self.ui.btnDefinirN.clicked.connect(self.definirN)
		self.ui.btnBorrar.clicked.connect(self.borrartodo)

	def definirN(self):
		n=self.ui.txtn.text()
		mensaje=QMessageBox()
		mensaje.setWindowTitle("Información")
		if len(n):
			try:
				n=int(n)
			except:
				mensaje.setIcon(QMessageBox.Warning)
				mensaje.setText("El valor de n debe ser numérico")
				mensaje.exec_()
			if n==5:
				self.ui.txtxi1.setEnabled(True)
				self.ui.txtxi2.setEnabled(True)
				self.ui.txtxi3.setEnabled(True)
				self.ui.txtxi4.setEnabled(True)
				self.ui.txtxi5.setEnabled(True)
				self.ui.txtyi1.setEnabled(True)
				self.ui.txtyi2.setEnabled(True)
				self.ui.txtyi3.setEnabled(True)
				self.ui.txtyi4.setEnabled(True)
				self.ui.txtyi5.setEnabled(True)
				self.ui.btnEcuacion.setEnabled(True)
				self.ui.txtn.setEnabled(False)
				self.ui.btnDefinirN.setEnabled(False)
				self.ui.lblxi.setText("Ingrese los "+str(n)+" \nde xi:")
				self.ui.lblyi.setText("Ingrese los "+str(n)+" \nde yi:")
			elif n==6:
				self.ui.txtxi1.setEnabled(True)
				self.ui.txtxi2.setEnabled(True)
				self.ui.txtxi3.setEnabled(True)
				self.ui.txtxi4.setEnabled(True)
				self.ui.txtxi5.setEnabled(True)
				self.ui.txtxi6.setEnabled(True)
				self.ui.txtyi1.setEnabled(True)
				self.ui.txtyi2.setEnabled(True)
				self.ui.txtyi3.setEnabled(True)
				self.ui.txtyi4.setEnabled(True)
				self.ui.txtyi5.setEnabled(True)
				self.ui.txtyi6.setEnabled(True)
				self.ui.btnEcuacion.setEnabled(True)
				self.ui.txtn.setEnabled(False)
				self.ui.btnDefinirN.setEnabled(False)
				self.ui.lblxi.setText("Ingrese los "+str(n)+" \nde xi:")
				self.ui.lblyi.setText("Ingrese los "+str(n)+" \nde yi:")
			elif n==7:
				self.ui.txtxi1.setEnabled(True)
				self.ui.txtxi2.setEnabled(True)
				self.ui.txtxi3.setEnabled(True)
				self.ui.txtxi4.setEnabled(True)
				self.ui.txtxi5.setEnabled(True)
				self.ui.txtxi6.setEnabled(True)
				self.ui.txtxi7.setEnabled(True)
				self.ui.txtyi1.setEnabled(True)
				self.ui.txtyi2.setEnabled(True)
				self.ui.txtyi3.setEnabled(True)
				self.ui.txtyi4.setEnabled(True)
				self.ui.txtyi5.setEnabled(True)
				self.ui.txtyi6.setEnabled(True)
				self.ui.txtyi7.setEnabled(True)
				self.ui.btnEcuacion.setEnabled(True)
				self.ui.txtn.setEnabled(False)
				self.ui.btnDefinirN.setEnabled(False)
				self.ui.lblxi.setText("Ingrese los "+str(n)+" \nde xi:")
				self.ui.lblyi.setText("Ingrese los "+str(n)+" \nde yi:")
			elif n==8:
				self.ui.txtxi1.setEnabled(True)
				self.ui.txtxi2.setEnabled(True)
				self.ui.txtxi3.setEnabled(True)
				self.ui.txtxi4.setEnabled(True)
				self.ui.txtxi5.setEnabled(True)
				self.ui.txtxi6.setEnabled(True)
				self.ui.txtxi7.setEnabled(True)
				self.ui.txtxi8.setEnabled(True)
				self.ui.txtyi1.setEnabled(True)
				self.ui.txtyi2.setEnabled(True)
				self.ui.txtyi3.setEnabled(True)
				self.ui.txtyi4.setEnabled(True)
				self.ui.txtyi5.setEnabled(True)
				self.ui.txtyi6.setEnabled(True)
				self.ui.txtyi7.setEnabled(True)
				self.ui.txtyi8.setEnabled(True)
				self.ui.btnEcuacion.setEnabled(True)
				self.ui.txtn.setEnabled(False)
				self.ui.btnDefinirN.setEnabled(False)
				self.ui.lblxi.setText("Ingrese los "+str(n)+" \nde xi:")
				self.ui.lblyi.setText("Ingrese los "+str(n)+" \nde yi:")
			elif n==9:
				self.ui.txtxi1.setEnabled(True)
				self.ui.txtxi2.setEnabled(True)
				self.ui.txtxi3.setEnabled(True)
				self.ui.txtxi4.setEnabled(True)
				self.ui.txtxi5.setEnabled(True)
				self.ui.txtxi6.setEnabled(True)
				self.ui.txtxi7.setEnabled(True)
				self.ui.txtxi8.setEnabled(True)
				self.ui.txtxi9.setEnabled(True)
				self.ui.txtyi1.setEnabled(True)
				self.ui.txtyi2.setEnabled(True)
				self.ui.txtyi3.setEnabled(True)
				self.ui.txtyi4.setEnabled(True)
				self.ui.txtyi5.setEnabled(True)
				self.ui.txtyi6.setEnabled(True)
				self.ui.txtyi7.setEnabled(True)
				self.ui.txtyi8.setEnabled(True)
				self.ui.txtyi9.setEnabled(True)
				self.ui.btnEcuacion.setEnabled(True)
				self.ui.txtn.setEnabled(False)
				self.ui.btnDefinirN.setEnabled(False)
				self.ui.lblxi.setText("Ingrese los "+str(n)+" \nde xi:")
				self.ui.lblyi.setText("Ingrese los "+str(n)+" \nde yi:")
			elif n==10:
				self.ui.txtxi1.setEnabled(True)
				self.ui.txtxi2.setEnabled(True)
				self.ui.txtxi3.setEnabled(True)
				self.ui.txtxi4.setEnabled(True)
				self.ui.txtxi5.setEnabled(True)
				self.ui.txtxi6.setEnabled(True)
				self.ui.txtxi7.setEnabled(True)
				self.ui.txtxi8.setEnabled(True)
				self.ui.txtxi9.setEnabled(True)
				self.ui.txtxi10.setEnabled(True)
				self.ui.txtyi1.setEnabled(True)
				self.ui.txtyi2.setEnabled(True)
				self.ui.txtyi3.setEnabled(True)
				self.ui.txtyi4.setEnabled(True)
				self.ui.txtyi5.setEnabled(True)
				self.ui.txtyi6.setEnabled(True)
				self.ui.txtyi7.setEnabled(True)
				self.ui.txtyi8.setEnabled(True)
				self.ui.txtyi9.setEnabled(True)
				self.ui.txtyi10.setEnabled(True)
				self.ui.btnEcuacion.setEnabled(True)
				self.ui.txtn.setEnabled(False)
				self.ui.btnDefinirN.setEnabled(False)
				self.ui.lblxi.setText("Ingrese los "+str(n)+" \nde xi:")
				self.ui.lblyi.setText("Ingrese los "+str(n)+" \nde yi:")
			else:
				mensaje.setIcon(QMessageBox.Warning)
				mensaje.setText("Ingrese un número entre 5 y 10")
				mensaje.exec_()
		else:
			mensaje.setIcon(QMessageBox.Warning)
			mensaje.setText("n no puede quedar vacio")
			mensaje.exec_()

	def evaluar(self):
		n=int(self.ui.txtn.text())
		mensaje=QMessageBox()
		mensaje.setWindowTitle("Información")
		if n==5:
			xi1=self.ui.txtxi1.text()
			xi2=self.ui.txtxi2.text()
			xi3=self.ui.txtxi3.text()
			xi4=self.ui.txtxi4.text()
			xi5=self.ui.txtxi5.text()
			yi1=self.ui.txtyi1.text()
			yi2=self.ui.txtyi2.text()
			yi3=self.ui.txtyi3.text()
			yi4=self.ui.txtyi4.text()
			yi5=self.ui.txtyi5.text()
			#Creación de arreglos
			xin=[xi1,xi2,xi3,xi4,xi5]
			yin=[yi1,yi2,yi3,yi4,yi5]
				#Arreglos vacíos para llenar más adelante
			xiyi=[0,0,0,0,0]
			xicuadrado=[0,0,0,0,0]
			if len(xi1) and len(xi2)and len(xi3)and len(xi4)and len(xi5):
				if len(yi1) and len(yi2)and len(yi3)and len(yi4)and len(yi5):
					try:
						xi1=float(xi1)
						xi2=float(xi2)
						xi3=float(xi3)
						xi4=float(xi4)
						xi5=float(xi5)
						xin=[xi1,xi2,xi3,xi4,xi5]
					except:
						mensaje.setIcon(QMessageBox.Warning)
						mensaje.setText("Los valores de xi deben ser numéricos")
						mensaje.exec_()
					try:
						yi1=float(yi1)
						yi2=float(yi2)
						yi3=float(yi3)
						yi4=float(yi4)
						yi5=float(yi5)
						yin=[yi1,yi2,yi3,yi4,yi5]
					except:
						mensaje.setIcon(QMessageBox.Warning)
						mensaje.setText("Los valores de yi deben ser numéricos")
						mensaje.exec_()

					sumaXi=0
					for i in range(len(xin)):
						sumaXi+=xin[i]
					self.ui.txtSumxi.setText(str(sumaXi))

					sumaYi=0
					for i in range(len(yin)):
						sumaYi+=yin[i]
					self.ui.txtSumyi.setText(str(sumaYi))

					for i in range(len(xin)):
						xiyi[i]=(xin[i])*(yin[i])
					self.ui.txtxiyi1.setText(str(xiyi[0]))
					self.ui.txtxiyi2.setText(str(xiyi[1]))
					self.ui.txtxiyi3.setText(str(xiyi[2]))
					self.ui.txtxiyi4.setText(str(xiyi[3]))
					self.ui.txtxiyi5.setText(str(xiyi[4]))

					sumaXiYi=0
					for i in range(len(xiyi)):
						sumaXiYi+=xiyi[i]
					self.ui.txtSumxiyi.setText(str(sumaXiYi))


					for i in range(len(xin)):
						xicuadrado[i]=(xin[i]**2)
					self.ui.txtxi12.setText(str(xicuadrado[0]))
					self.ui.txtxi22.setText(str(xicuadrado[1]))
					self.ui.txtxi32.setText(str(xicuadrado[2]))
					self.ui.txtxi42.setText(str(xicuadrado[3]))
					self.ui.txtxi52.setText(str(xicuadrado[4]))
					sumaXiCuadrado=0
					for i in range(len(xicuadrado)):
						sumaXiCuadrado+=xicuadrado[i]
					self.ui.txtSumxi2.setText(str(sumaXiCuadrado))

					xiSumaCuadrado=sumaXi**2
					self.ui.txtxiSum22.setText(str(sumaXi))

					a1=round(((n*sumaXiYi)-(sumaXi*sumaYi))/((n*sumaXiCuadrado)-(xiSumaCuadrado)),4)
					self.ui.txta1.setText(str(a1))

					mediaX=round((sumaXi/n),4)
					self.ui.txtxiM.setText(str(mediaX))

					mediaY=round((sumaYi/n),4)
					self.ui.txtyiM.setText(str(mediaY))

					a0=round((mediaY-(a1*mediaX)),4)
					self.ui.txta0.setText(str(a0))

					self.ui.lblRespuesta.setText("La función es:")
					resultado= str(a0) +"+"+ str(a1)+"x"
					self.ui.txtEcuacion.setText(resultado)

					self.ui.btnGrafica.setEnabled(True)
					self.ui.txtxi1.setEnabled(False)
					self.ui.txtxi2.setEnabled(False)
					self.ui.txtxi3.setEnabled(False)
					self.ui.txtxi4.setEnabled(False)
					self.ui.txtxi5.setEnabled(False)
					self.ui.txtyi1.setEnabled(False)
					self.ui.txtyi2.setEnabled(False)
					self.ui.txtyi3.setEnabled(False)
					self.ui.txtyi4.setEnabled(False)
					self.ui.txtyi5.setEnabled(False)
				else:
					mensaje.setIcon(QMessageBox.Warning)
					mensaje.setText("No pueden quedar campos vacíos en yi")
					mensaje.exec_()
			else:
				mensaje.setIcon(QMessageBox.Warning)
				mensaje.setText("No pueden quedar campos vacíos en xi")
				mensaje.exec_()

		elif n==6:
			xi1=self.ui.txtxi1.text()
			xi2=self.ui.txtxi2.text()
			xi3=self.ui.txtxi3.text()
			xi4=self.ui.txtxi4.text()
			xi5=self.ui.txtxi5.text()
			xi6=self.ui.txtxi6.text()
			xi7=self.ui.txtxi7.text()
			yi1=self.ui.txtyi1.text()
			yi2=self.ui.txtyi2.text()
			yi3=self.ui.txtyi3.text()
			yi4=self.ui.txtyi4.text()
			yi5=self.ui.txtyi5.text()
			yi6=self.ui.txtyi6.text()
			#Creación de arreglos
			xin=[xi1,xi2,xi3,xi4,xi5,xi6]
			yin=[yi1,yi2,yi3,yi4,yi5,yi6]
			#Arreglos vacíos para llenar más adelante
			xiyi=[0,0,0,0,0,0,]
			xicuadrado=[0,0,0,0,0,0,]
			if len(xi1) and len(xi2)and len(xi3)and len(xi4)and len(xi5)and len(xi6):
				if len(yi1) and len(yi2)and len(yi3)and len(yi4)and len(yi5)and len(yi6):
					try:
						xi1=float(xi1)
						xi2=float(xi2)
						xi3=float(xi3)
						xi4=float(xi4)
						xi5=float(xi5)
						xi6=float(xi6)
						xin=[xi1,xi2,xi3,xi4,xi5,xi6]
					except:
						mensaje.setIcon(QMessageBox.Warning)
						mensaje.setText("Los valores de xi deben ser numéricos")
						mensaje.exec_()
					try:
						yi1=float(yi1)
						yi2=float(yi2)
						yi3=float(yi3)
						yi4=float(yi4)
						yi5=float(yi5)
						yi6=float(yi6)
						yin=[yi1,yi2,yi3,yi4,yi5,yi6]
					except:
						mensaje.setIcon(QMessageBox.Warning)
						mensaje.setText("Los valores de yi deben ser numéricos")
						mensaje.exec_()

					sumaXi=0
					for i in range(len(xin)):
						sumaXi+=xin[i]
					self.ui.txtSumxi.setText(str(sumaXi))

					sumaYi=0
					for i in range(len(yin)):
						sumaYi+=yin[i]
					self.ui.txtSumyi.setText(str(sumaYi))

					for i in range(len(xin)):
						xiyi[i]=(xin[i])*(yin[i])
					self.ui.txtxiyi1.setText(str(xiyi[0]))
					self.ui.txtxiyi2.setText(str(xiyi[1]))
					self.ui.txtxiyi3.setText(str(xiyi[2]))
					self.ui.txtxiyi4.setText(str(xiyi[3]))
					self.ui.txtxiyi5.setText(str(xiyi[4]))
					self.ui.txtxiyi6.setText(str(xiyi[5]))

					sumaXiYi=0
					for i in range(len(xiyi)):
						sumaXiYi+=xiyi[i]
					self.ui.txtSumxiyi.setText(str(sumaXiYi))


					for i in range(len(xin)):
						xicuadrado[i]=(xin[i]**2)
					self.ui.txtxi12.setText(str(xicuadrado[0]))
					self.ui.txtxi22.setText(str(xicuadrado[1]))
					self.ui.txtxi32.setText(str(xicuadrado[2]))
					self.ui.txtxi42.setText(str(xicuadrado[3]))
					self.ui.txtxi52.setText(str(xicuadrado[4]))
					self.ui.txtxi62.setText(str(xicuadrado[5]))
					sumaXiCuadrado=0
					for i in range(len(xicuadrado)):
						sumaXiCuadrado+=xicuadrado[i]
					self.ui.txtSumxi2.setText(str(sumaXiCuadrado))

					xiSumaCuadrado=sumaXi**2
					self.ui.txtxiSum22.setText(str(sumaXi))

					a1=round(((n*sumaXiYi)-(sumaXi*sumaYi))/((n*sumaXiCuadrado)-(xiSumaCuadrado)),4)
					self.ui.txta1.setText(str(a1))

					mediaX=round((sumaXi/n),4)
					self.ui.txtxiM.setText(str(mediaX))

					mediaY=round((sumaYi/n),4)
					self.ui.txtyiM.setText(str(mediaY))

					a0=round((mediaY-(a1*mediaX)),4)
					self.ui.txta0.setText(str(a0))

					self.ui.lblRespuesta.setText("La función es:")
					resultado= str(a0) +"+"+ str(a1)+"x"
					self.ui.txtEcuacion.setText(resultado)

					self.ui.btnGrafica.setEnabled(True)
					self.ui.txtxi1.setEnabled(False)
					self.ui.txtxi2.setEnabled(False)
					self.ui.txtxi3.setEnabled(False)
					self.ui.txtxi4.setEnabled(False)
					self.ui.txtxi5.setEnabled(False)
					self.ui.txtxi6.setEnabled(False)
					self.ui.txtyi1.setEnabled(False)
					self.ui.txtyi2.setEnabled(False)
					self.ui.txtyi3.setEnabled(False)
					self.ui.txtyi4.setEnabled(False)
					self.ui.txtyi5.setEnabled(False)
					self.ui.txtyi6.setEnabled(False)
				else:
					mensaje.setIcon(QMessageBox.Warning)
					mensaje.setText("No pueden quedar campos vacíos en yi")
					mensaje.exec_()
			else:
				mensaje.setIcon(QMessageBox.Warning)
				mensaje.setText("No pueden quedar campos vacíos en xi")
				mensaje.exec_()
		elif n==7:
			#Recolección de valores
			xi1=self.ui.txtxi1.text()
			xi2=self.ui.txtxi2.text()
			xi3=self.ui.txtxi3.text()
			xi4=self.ui.txtxi4.text()
			xi5=self.ui.txtxi5.text()
			xi6=self.ui.txtxi6.text()
			xi7=self.ui.txtxi7.text()
			yi1=self.ui.txtyi1.text()
			yi2=self.ui.txtyi2.text()
			yi3=self.ui.txtyi3.text()
			yi4=self.ui.txtyi4.text()
			yi5=self.ui.txtyi5.text()
			yi6=self.ui.txtyi6.text()
			yi7=self.ui.txtyi7.text()

			#Creación de arreglos
			xin=[xi1,xi2,xi3,xi4,xi5,xi6,xi7]
			yin=[yi1,yi2,yi3,yi4,yi5,yi6,yi7]
			#Arreglos vacíos para llenar más adelante
			xiyi=[0,0,0,0,0,0,0]
			xicuadrado=[0,0,0,0,0,0,0]
			mensaje=QMessageBox()
			mensaje.setWindowTitle("Información")
			if len(xi1) and len(xi2)and len(xi3)and len(xi4)and len(xi5)and len(xi6)and len(xi7):
				if len(yi1) and len(yi2)and len(yi3)and len(yi4)and len(yi5)and len(yi6)and len(yi7):
					try:
						xi1=float(xi1)
						xi2=float(xi2)
						xi3=float(xi3)
						xi4=float(xi4)
						xi5=float(xi5)
						xi6=float(xi6)
						xi7=float(xi7)
						xin=[xi1,xi2,xi3,xi4,xi5,xi6,xi7]
					except:
						mensaje.setIcon(QMessageBox.Warning)
						mensaje.setText("Los valores de xi deben ser numéricos")
						mensaje.exec_()
					try:
						yi1=float(yi1)
						yi2=float(yi2)
						yi3=float(yi3)
						yi4=float(yi4)
						yi5=float(yi5)
						yi6=float(yi6)
						yi7=float(yi7)
						yin=[yi1,yi2,yi3,yi4,yi5,yi6,yi7]
					except:
						mensaje.setIcon(QMessageBox.Warning)
						mensaje.setText("Los valores de yi deben ser numéricos")
						mensaje.exec_()

					sumaXi=0
					for i in range(len(xin)):
						sumaXi+=xin[i]
					self.ui.txtSumxi.setText(str(sumaXi))

					sumaYi=0
					for i in range(len(yin)):
						sumaYi+=yin[i]
					self.ui.txtSumyi.setText(str(sumaYi))

					for i in range(len(xin)):
						xiyi[i]=(xin[i])*(yin[i])
					self.ui.txtxiyi1.setText(str(xiyi[0]))
					self.ui.txtxiyi2.setText(str(xiyi[1]))
					self.ui.txtxiyi3.setText(str(xiyi[2]))
					self.ui.txtxiyi4.setText(str(xiyi[3]))
					self.ui.txtxiyi5.setText(str(xiyi[4]))
					self.ui.txtxiyi6.setText(str(xiyi[5]))
					self.ui.txtxiyi7.setText(str(xiyi[6]))

					sumaXiYi=0
					for i in range(len(xiyi)):
						sumaXiYi+=xiyi[i]
					self.ui.txtSumxiyi.setText(str(sumaXiYi))


					for i in range(len(xin)):
						xicuadrado[i]=(xin[i]**2)
					self.ui.txtxi12.setText(str(xicuadrado[0]))
					self.ui.txtxi22.setText(str(xicuadrado[1]))
					self.ui.txtxi32.setText(str(xicuadrado[2]))
					self.ui.txtxi42.setText(str(xicuadrado[3]))
					self.ui.txtxi52.setText(str(xicuadrado[4]))
					self.ui.txtxi62.setText(str(xicuadrado[5]))
					self.ui.txtxi72.setText(str(xicuadrado[6]))

					sumaXiCuadrado=0
					for i in range(len(xicuadrado)):
						sumaXiCuadrado+=xicuadrado[i]
					self.ui.txtSumxi2.setText(str(sumaXiCuadrado))

					xiSumaCuadrado=sumaXi**2
					self.ui.txtxiSum22.setText(str(sumaXi))

					a1=round(((n*sumaXiYi)-(sumaXi*sumaYi))/((n*sumaXiCuadrado)-(xiSumaCuadrado)),4)
					self.ui.txta1.setText(str(a1))

					mediaX=round((sumaXi/n),4)
					self.ui.txtxiM.setText(str(mediaX))

					mediaY=round((sumaYi/n),4)
					self.ui.txtyiM.setText(str(mediaY))

					a0=round((mediaY-(a1*mediaX)),4)
					self.ui.txta0.setText(str(a0))

					self.ui.lblRespuesta.setText("La función es:")
					resultado= str(a0) +"+"+ str(a1)+"x"
					self.ui.txtEcuacion.setText(resultado)

					self.ui.btnGrafica.setEnabled(True)
					self.ui.txtxi1.setEnabled(False)
					self.ui.txtxi2.setEnabled(False)
					self.ui.txtxi3.setEnabled(False)
					self.ui.txtxi4.setEnabled(False)
					self.ui.txtxi5.setEnabled(False)
					self.ui.txtxi6.setEnabled(False)
					self.ui.txtxi7.setEnabled(False)
					self.ui.txtyi1.setEnabled(False)
					self.ui.txtyi2.setEnabled(False)
					self.ui.txtyi3.setEnabled(False)
					self.ui.txtyi4.setEnabled(False)
					self.ui.txtyi5.setEnabled(False)
					self.ui.txtyi6.setEnabled(False)
					self.ui.txtyi7.setEnabled(False)
				else:
					mensaje.setIcon(QMessageBox.Warning)
					mensaje.setText("No pueden quedar campos vacíos en yi")
					mensaje.exec_()
			else:	
				mensaje.setIcon(QMessageBox.Warning)
				mensaje.setText("No pueden quedar campos vacíos en xi")
				mensaje.exec_()
		elif n==8:
			#Recolección de valores
			xi1=self.ui.txtxi1.text()
			xi2=self.ui.txtxi2.text()
			xi3=self.ui.txtxi3.text()
			xi4=self.ui.txtxi4.text()
			xi5=self.ui.txtxi5.text()
			xi6=self.ui.txtxi6.text()
			xi7=self.ui.txtxi7.text()
			xi8=self.ui.txtxi8.text()
			yi1=self.ui.txtyi1.text()
			yi2=self.ui.txtyi2.text()
			yi3=self.ui.txtyi3.text()
			yi4=self.ui.txtyi4.text()
			yi5=self.ui.txtyi5.text()
			yi6=self.ui.txtyi6.text()
			yi7=self.ui.txtyi7.text()
			yi8=self.ui.txtyi8.text()

			#Creación de arreglos
			xin=[xi1,xi2,xi3,xi4,xi5,xi6,xi7,xi8]
			yin=[yi1,yi2,yi3,yi4,yi5,yi6,yi7,yi8]
			#Arreglos vacíos para llenar más adelante
			xiyi=[0,0,0,0,0,0,0,0]
			xicuadrado=[0,0,0,0,0,0,0,0]
			mensaje=QMessageBox()
			mensaje.setWindowTitle("Información")
			if len(xi1) and len(xi2)and len(xi3)and len(xi4)and len(xi5)and len(xi6)and len(xi7) and len(xi8):
				if len(yi1) and len(yi2)and len(yi3)and len(yi4)and len(yi5)and len(yi6)and len(yi7) and len(yi8):
					try:
						xi1=float(xi1)
						xi2=float(xi2)
						xi3=float(xi3)
						xi4=float(xi4)
						xi5=float(xi5)
						xi6=float(xi6)
						xi7=float(xi7)
						xi8=float(xi8)
						xin=[xi1,xi2,xi3,xi4,xi5,xi6,xi7,xi8]
					except:
						mensaje.setIcon(QMessageBox.Warning)
						mensaje.setText("Los valores de xi deben ser numéricos")
						mensaje.exec_()
					try:
						yi1=float(yi1)
						yi2=float(yi2)
						yi3=float(yi3)
						yi4=float(yi4)
						yi5=float(yi5)
						yi6=float(yi6)
						yi7=float(yi7)
						yi8=float(yi8)
						yin=[yi1,yi2,yi3,yi4,yi5,yi6,yi7,yi8]
					except:
						mensaje.setIcon(QMessageBox.Warning)
						mensaje.setText("Los valores de yi deben ser numéricos")
						mensaje.exec_()

					sumaXi=0
					for i in range(len(xin)):
						sumaXi+=xin[i]
					self.ui.txtSumxi.setText(str(sumaXi))

					sumaYi=0
					for i in range(len(yin)):
						sumaYi+=yin[i]
					self.ui.txtSumyi.setText(str(sumaYi))

					for i in range(len(xin)):
						xiyi[i]=(xin[i])*(yin[i])
					self.ui.txtxiyi1.setText(str(xiyi[0]))
					self.ui.txtxiyi2.setText(str(xiyi[1]))
					self.ui.txtxiyi3.setText(str(xiyi[2]))
					self.ui.txtxiyi4.setText(str(xiyi[3]))
					self.ui.txtxiyi5.setText(str(xiyi[4]))
					self.ui.txtxiyi6.setText(str(xiyi[5]))
					self.ui.txtxiyi7.setText(str(xiyi[6]))
					self.ui.txtxiyi8.setText(str(xiyi[7]))

					sumaXiYi=0
					for i in range(len(xiyi)):
						sumaXiYi+=xiyi[i]
					self.ui.txtSumxiyi.setText(str(sumaXiYi))

					for i in range(len(xin)):
						xicuadrado[i]=(xin[i]**2)
					self.ui.txtxi12.setText(str(xicuadrado[0]))
					self.ui.txtxi22.setText(str(xicuadrado[1]))
					self.ui.txtxi32.setText(str(xicuadrado[2]))
					self.ui.txtxi42.setText(str(xicuadrado[3]))
					self.ui.txtxi52.setText(str(xicuadrado[4]))
					self.ui.txtxi62.setText(str(xicuadrado[5]))
					self.ui.txtxi72.setText(str(xicuadrado[6]))
					self.ui.txtxi82.setText(str(xicuadrado[7]))

					sumaXiCuadrado=0
					for i in range(len(xicuadrado)):
						sumaXiCuadrado+=xicuadrado[i]
					self.ui.txtSumxi2.setText(str(sumaXiCuadrado))

					xiSumaCuadrado=sumaXi**2
					self.ui.txtxiSum22.setText(str(sumaXi))

					a1=round(((n*sumaXiYi)-(sumaXi*sumaYi))/((n*sumaXiCuadrado)-(xiSumaCuadrado)),4)
					self.ui.txta1.setText(str(a1))

					mediaX=round((sumaXi/n),4)
					self.ui.txtxiM.setText(str(mediaX))

					mediaY=round((sumaYi/n),4)
					self.ui.txtyiM.setText(str(mediaY))

					a0=round((mediaY-(a1*mediaX)),4)
					self.ui.txta0.setText(str(a0))

					self.ui.lblRespuesta.setText("La función es:")
					resultado= str(a0) +"+"+ str(a1)+"x"
					self.ui.txtEcuacion.setText(resultado)

					self.ui.btnGrafica.setEnabled(True)
					self.ui.txtxi1.setEnabled(False)
					self.ui.txtxi2.setEnabled(False)
					self.ui.txtxi3.setEnabled(False)
					self.ui.txtxi4.setEnabled(False)
					self.ui.txtxi5.setEnabled(False)
					self.ui.txtxi6.setEnabled(False)
					self.ui.txtxi7.setEnabled(False)
					self.ui.txtxi8.setEnabled(False)
					self.ui.txtyi1.setEnabled(False)
					self.ui.txtyi2.setEnabled(False)
					self.ui.txtyi3.setEnabled(False)
					self.ui.txtyi4.setEnabled(False)
					self.ui.txtyi5.setEnabled(False)
					self.ui.txtyi6.setEnabled(False)
					self.ui.txtyi7.setEnabled(False)
					self.ui.txtyi8.setEnabled(False)
				else:
					mensaje.setIcon(QMessageBox.Warning)
					mensaje.setText("No pueden quedar campos vacíos en yi")
					mensaje.exec_()
			else:	
				mensaje.setIcon(QMessageBox.Warning)
				mensaje.setText("No pueden quedar campos vacíos en xi")
				mensaje.exec_()
		elif n==9:
			#Recolección de valores
			xi1=self.ui.txtxi1.text()
			xi2=self.ui.txtxi2.text()
			xi3=self.ui.txtxi3.text()
			xi4=self.ui.txtxi4.text()
			xi5=self.ui.txtxi5.text()
			xi6=self.ui.txtxi6.text()
			xi7=self.ui.txtxi7.text()
			xi8=self.ui.txtxi8.text()
			xi9=self.ui.txtxi9.text()
			yi1=self.ui.txtyi1.text()
			yi2=self.ui.txtyi2.text()
			yi3=self.ui.txtyi3.text()
			yi4=self.ui.txtyi4.text()
			yi5=self.ui.txtyi5.text()
			yi6=self.ui.txtyi6.text()
			yi7=self.ui.txtyi7.text()
			yi8=self.ui.txtyi8.text()
			yi9=self.ui.txtyi9.text()

			#Creación de arreglos
			xin=[xi1,xi2,xi3,xi4,xi5,xi6,xi7,xi8,xi9]
			yin=[yi1,yi2,yi3,yi4,yi5,yi6,yi7,yi8,yi9]
			#Arreglos vacíos para llenar más adelante
			xiyi=[0,0,0,0,0,0,0,0,0]
			xicuadrado=[0,0,0,0,0,0,0,0,0]
			mensaje=QMessageBox()
			mensaje.setWindowTitle("Información")
			if len(xi1) and len(xi2)and len(xi3)and len(xi4)and len(xi5)and len(xi6)and len(xi7) and len(xi8) and len(xi9):
				if len(yi1) and len(yi2)and len(yi3)and len(yi4)and len(yi5)and len(yi6)and len(yi7) and len(yi8) and len(yi9):
					try:
						xi1=float(xi1)
						xi2=float(xi2)
						xi3=float(xi3)
						xi4=float(xi4)
						xi5=float(xi5)
						xi6=float(xi6)
						xi7=float(xi7)
						xi8=float(xi8)
						xi9=float(xi9)
						xin=[xi1,xi2,xi3,xi4,xi5,xi6,xi7,xi8,xi9]
					except:
						mensaje.setIcon(QMessageBox.Warning)
						mensaje.setText("Los valores de xi deben ser numéricos")
						mensaje.exec_()
					try:
						yi1=float(yi1)
						yi2=float(yi2)
						yi3=float(yi3)
						yi4=float(yi4)
						yi5=float(yi5)
						yi6=float(yi6)
						yi7=float(yi7)
						yi8=float(yi8)
						yi9=float(yi9)
						yin=[yi1,yi2,yi3,yi4,yi5,yi6,yi7,yi8,yi9]
					except:
						mensaje.setIcon(QMessageBox.Warning)
						mensaje.setText("Los valores de yi deben ser numéricos")
						mensaje.exec_()

					sumaXi=0
					for i in range(len(xin)):
						sumaXi+=xin[i]
					self.ui.txtSumxi.setText(str(sumaXi))

					sumaYi=0
					for i in range(len(yin)):
						sumaYi+=yin[i]
					self.ui.txtSumyi.setText(str(sumaYi))

					for i in range(len(xin)):
						xiyi[i]=(xin[i])*(yin[i])
					self.ui.txtxiyi1.setText(str(xiyi[0]))
					self.ui.txtxiyi2.setText(str(xiyi[1]))
					self.ui.txtxiyi3.setText(str(xiyi[2]))
					self.ui.txtxiyi4.setText(str(xiyi[3]))
					self.ui.txtxiyi5.setText(str(xiyi[4]))
					self.ui.txtxiyi6.setText(str(xiyi[5]))
					self.ui.txtxiyi7.setText(str(xiyi[6]))
					self.ui.txtxiyi8.setText(str(xiyi[7]))
					self.ui.txtxiyi9.setText(str(xiyi[8]))

					sumaXiYi=0
					for i in range(len(xiyi)):
						sumaXiYi+=xiyi[i]
					self.ui.txtSumxiyi.setText(str(sumaXiYi))


					for i in range(len(xin)):
						xicuadrado[i]=(xin[i]**2)
					self.ui.txtxi12.setText(str(xicuadrado[0]))
					self.ui.txtxi22.setText(str(xicuadrado[1]))
					self.ui.txtxi32.setText(str(xicuadrado[2]))
					self.ui.txtxi42.setText(str(xicuadrado[3]))
					self.ui.txtxi52.setText(str(xicuadrado[4]))
					self.ui.txtxi62.setText(str(xicuadrado[5]))
					self.ui.txtxi72.setText(str(xicuadrado[6]))
					self.ui.txtxi82.setText(str(xicuadrado[7]))
					self.ui.txtxi92.setText(str(xicuadrado[8]))

					sumaXiCuadrado=0
					for i in range(len(xicuadrado)):
						sumaXiCuadrado+=xicuadrado[i]
					self.ui.txtSumxi2.setText(str(sumaXiCuadrado))

					xiSumaCuadrado=sumaXi**2
					self.ui.txtxiSum22.setText(str(sumaXi))

					a1=round(((n*sumaXiYi)-(sumaXi*sumaYi))/((n*sumaXiCuadrado)-(xiSumaCuadrado)),4)
					self.ui.txta1.setText(str(a1))

					mediaX=round((sumaXi/n),4)
					self.ui.txtxiM.setText(str(mediaX))

					mediaY=round((sumaYi/n),4)
					self.ui.txtyiM.setText(str(mediaY))

					a0=round((mediaY-(a1*mediaX)),4)
					self.ui.txta0.setText(str(a0))

					self.ui.lblRespuesta.setText("La función es:")
					resultado= str(a0) +"+"+ str(a1)+"x"
					self.ui.txtEcuacion.setText(resultado)

					self.ui.btnGrafica.setEnabled(True)
					self.ui.txtxi1.setEnabled(False)
					self.ui.txtxi2.setEnabled(False)
					self.ui.txtxi3.setEnabled(False)
					self.ui.txtxi4.setEnabled(False)
					self.ui.txtxi5.setEnabled(False)
					self.ui.txtxi6.setEnabled(False)
					self.ui.txtxi7.setEnabled(False)
					self.ui.txtxi8.setEnabled(False)
					self.ui.txtxi9.setEnabled(False)
					self.ui.txtyi1.setEnabled(False)
					self.ui.txtyi2.setEnabled(False)
					self.ui.txtyi3.setEnabled(False)
					self.ui.txtyi4.setEnabled(False)
					self.ui.txtyi5.setEnabled(False)
					self.ui.txtyi6.setEnabled(False)
					self.ui.txtyi7.setEnabled(False)
					self.ui.txtyi8.setEnabled(False)
					self.ui.txtyi9.setEnabled(False)
				else:
					mensaje.setIcon(QMessageBox.Warning)
					mensaje.setText("No pueden quedar campos vacíos en yi")
					mensaje.exec_()
			else:	
				mensaje.setIcon(QMessageBox.Warning)
				mensaje.setText("No pueden quedar campos vacíos en xi")
				mensaje.exec_()
		elif n==10:
			#Recolección de valores
			xi1=self.ui.txtxi1.text()
			xi2=self.ui.txtxi2.text()
			xi3=self.ui.txtxi3.text()
			xi4=self.ui.txtxi4.text()
			xi5=self.ui.txtxi5.text()
			xi6=self.ui.txtxi6.text()
			xi7=self.ui.txtxi7.text()
			xi8=self.ui.txtxi8.text()
			xi9=self.ui.txtxi9.text()
			xi10=self.ui.txtxi10.text()
			yi1=self.ui.txtyi1.text()
			yi2=self.ui.txtyi2.text()
			yi3=self.ui.txtyi3.text()
			yi4=self.ui.txtyi4.text()
			yi5=self.ui.txtyi5.text()
			yi6=self.ui.txtyi6.text()
			yi7=self.ui.txtyi7.text()
			yi8=self.ui.txtyi8.text()
			yi9=self.ui.txtyi9.text()
			yi10=self.ui.txtyi10.text()

			#Creación de arreglos
			xin=[xi1,xi2,xi3,xi4,xi5,xi6,xi7,xi8,xi9,xi10]
			yin=[yi1,yi2,yi3,yi4,yi5,yi6,yi7,yi8,yi9,yi10]
			#Arreglos vacíos para llenar más adelante
			xiyi=[0,0,0,0,0,0,0,0,0,0]
			xicuadrado=[0,0,0,0,0,0,0,0,0,0]
			mensaje=QMessageBox()
			mensaje.setWindowTitle("Información")
			if len(xi1) and len(xi2)and len(xi3)and len(xi4)and len(xi5)and len(xi6)and len(xi7) and len(xi8) and len(xi9)and len(xi10):
				if len(yi1) and len(yi2)and len(yi3)and len(yi4)and len(yi5)and len(yi6)and len(yi7) and len(yi8) and len(yi9)and len(xi10):
					try:
						xi1=float(xi1)
						xi2=float(xi2)
						xi3=float(xi3)
						xi4=float(xi4)
						xi5=float(xi5)
						xi6=float(xi6)
						xi7=float(xi7)
						xi8=float(xi8)
						xi9=float(xi9)
						xi10=float(xi10)
						xin=[xi1,xi2,xi3,xi4,xi5,xi6,xi7,xi8,xi9,xi10]
					except:
						mensaje.setIcon(QMessageBox.Warning)
						mensaje.setText("Los valores de xi deben ser numéricos")
						mensaje.exec_()
					try:
						yi1=float(yi1)
						yi2=float(yi2)
						yi3=float(yi3)
						yi4=float(yi4)
						yi5=float(yi5)
						yi6=float(yi6)
						yi7=float(yi7)
						yi8=float(yi8)
						yi9=float(yi9)
						yi10=float(yi10)
						yin=[yi1,yi2,yi3,yi4,yi5,yi6,yi7,yi8,yi9,yi10]
					except:
						mensaje.setIcon(QMessageBox.Warning)
						mensaje.setText("Los valores de yi deben ser numéricos")
						mensaje.exec_()

					sumaXi=0
					for i in range(len(xin)):
						sumaXi+=xin[i]
					self.ui.txtSumxi.setText(str(sumaXi))

					sumaYi=0
					for i in range(len(yin)):
						sumaYi+=yin[i]
					self.ui.txtSumyi.setText(str(sumaYi))

					for i in range(len(xin)):
						xiyi[i]=(xin[i])*(yin[i])
					self.ui.txtxiyi1.setText(str(xiyi[0]))
					self.ui.txtxiyi2.setText(str(xiyi[1]))
					self.ui.txtxiyi3.setText(str(xiyi[2]))
					self.ui.txtxiyi4.setText(str(xiyi[3]))
					self.ui.txtxiyi5.setText(str(xiyi[4]))
					self.ui.txtxiyi6.setText(str(xiyi[5]))
					self.ui.txtxiyi7.setText(str(xiyi[6]))
					self.ui.txtxiyi8.setText(str(xiyi[7]))
					self.ui.txtxiyi9.setText(str(xiyi[8]))
					self.ui.txtxiyi10.setText(str(xiyi[9]))

					sumaXiYi=0
					for i in range(len(xiyi)):
						sumaXiYi+=xiyi[i]
					self.ui.txtSumxiyi.setText(str(sumaXiYi))


					for i in range(len(xin)):
						xicuadrado[i]=(xin[i]**2)
					self.ui.txtxi12.setText(str(xicuadrado[0]))
					self.ui.txtxi22.setText(str(xicuadrado[1]))
					self.ui.txtxi32.setText(str(xicuadrado[2]))
					self.ui.txtxi42.setText(str(xicuadrado[3]))
					self.ui.txtxi52.setText(str(xicuadrado[4]))
					self.ui.txtxi62.setText(str(xicuadrado[5]))
					self.ui.txtxi72.setText(str(xicuadrado[6]))
					self.ui.txtxi82.setText(str(xicuadrado[7]))
					self.ui.txtxi92.setText(str(xicuadrado[8]))
					self.ui.txtxi102.setText(str(xicuadrado[9]))

					sumaXiCuadrado=0
					for i in range(len(xicuadrado)):
						sumaXiCuadrado+=xicuadrado[i]
					self.ui.txtSumxi2.setText(str(sumaXiCuadrado))

					xiSumaCuadrado=sumaXi**2
					self.ui.txtxiSum22.setText(str(sumaXi))

					a1=round(((n*sumaXiYi)-(sumaXi*sumaYi))/((n*sumaXiCuadrado)-(xiSumaCuadrado)),4)
					self.ui.txta1.setText(str(a1))

					mediaX=round((sumaXi/n),4)
					self.ui.txtxiM.setText(str(mediaX))

					mediaY=round((sumaYi/n),4)
					self.ui.txtyiM.setText(str(mediaY))

					a0=round((mediaY-(a1*mediaX)),4)
					self.ui.txta0.setText(str(a0))

					self.ui.lblRespuesta.setText("La función es:")
					resultado= str(a0) +"+"+ str(a1)+"x"
					self.ui.txtEcuacion.setText(resultado)

					self.ui.btnGrafica.setEnabled(True)
					self.ui.txtxi1.setEnabled(False)
					self.ui.txtxi2.setEnabled(False)
					self.ui.txtxi3.setEnabled(False)
					self.ui.txtxi4.setEnabled(False)
					self.ui.txtxi5.setEnabled(False)
					self.ui.txtxi6.setEnabled(False)
					self.ui.txtxi7.setEnabled(False)
					self.ui.txtxi8.setEnabled(False)
					self.ui.txtxi9.setEnabled(False)
					self.ui.txtxi10.setEnabled(False)
					self.ui.txtyi1.setEnabled(False)
					self.ui.txtyi2.setEnabled(False)
					self.ui.txtyi3.setEnabled(False)
					self.ui.txtyi4.setEnabled(False)
					self.ui.txtyi5.setEnabled(False)
					self.ui.txtyi6.setEnabled(False)
					self.ui.txtyi7.setEnabled(False)
					self.ui.txtyi8.setEnabled(False)
					self.ui.txtyi9.setEnabled(False)
					self.ui.txtyi10.setEnabled(False)
				else:
					mensaje.setIcon(QMessageBox.Warning)
					mensaje.setText("No pueden quedar campos vacíos en yi")
					mensaje.exec_()
			else:	
				mensaje.setIcon(QMessageBox.Warning)
				mensaje.setText("No pueden quedar campos vacíos en xi")
				mensaje.exec_()
		else:	
			mensaje.setIcon(QMessageBox.Warning)
			mensaje.setText("Error inesperado, fuera de rango")
			mensaje.exec_()

	def grafica(self):
		n=int(self.ui.txtn.text())
		mensaje=QMessageBox()
		mensaje.setWindowTitle("Información")
		if n==5:
			xi1=float(self.ui.txtxi1.text())
			xi2=float(self.ui.txtxi2.text())
			xi3=float(self.ui.txtxi3.text())
			xi4=float(self.ui.txtxi4.text())
			xi5=float(self.ui.txtxi5.text())
			yi1=float(self.ui.txtyi1.text())
			yi2=float(self.ui.txtyi2.text())
			yi3=float(self.ui.txtyi3.text())
			yi4=float(self.ui.txtyi4.text())
			yi5=float(self.ui.txtyi5.text())
			#Creación de arreglos
			xin=[xi1,xi2,xi3,xi4,xi5]
			yin=[yi1,yi2,yi3,yi4,yi5]
			a1=float(self.ui.txta1.text())
			a0=float(self.ui.txta0.text())
			def f(x):
				return a0 + a1*x
			Xmenor=int(min(xin))
			Xmayor=int(max(xin))
			x1=range(Xmenor,Xmayor+1)		
			fig, ax=plt.subplots()	
			ax.scatter(xin,yin)
			plt.plot(x1,[f(i) for i in x1])
			plt.axhline(0,color="black")
			plt.axvline(0,color="black")
			plt.savefig('Diagrama-disperción.png')
			plt.show()
		elif n==6:
			xi1=float(self.ui.txtxi1.text())
			xi2=float(self.ui.txtxi2.text())
			xi3=float(self.ui.txtxi3.text())
			xi4=float(self.ui.txtxi4.text())
			xi5=float(self.ui.txtxi5.text())
			xi6=float(self.ui.txtxi6.text())
			yi1=float(self.ui.txtyi1.text())
			yi2=float(self.ui.txtyi2.text())
			yi3=float(self.ui.txtyi3.text())
			yi4=float(self.ui.txtyi4.text())
			yi5=float(self.ui.txtyi5.text())
			yi6=float(self.ui.txtyi6.text())
			#Creación de arreglos
			xin=[xi1,xi2,xi3,xi4,xi5,xi6]
			yin=[yi1,yi2,yi3,yi4,yi5,yi6]
			a1=float(self.ui.txta1.text())
			a0=float(self.ui.txta0.text())
			def f(x):
				return a0 + a1*x
			Xmenor=int(min(xin))
			Xmayor=int(max(xin))
			x1=range(Xmenor,Xmayor+1)		
			fig, ax=plt.subplots()	
			ax.scatter(xin,yin)
			plt.plot(x1,[f(i) for i in x1])
			plt.axhline(0,color="black")
			plt.axvline(0,color="black")
			plt.savefig('Diagrama-disperción.png')
			plt.show()
		elif n==7:
			xi1=float(self.ui.txtxi1.text())
			xi2=float(self.ui.txtxi2.text())
			xi3=float(self.ui.txtxi3.text())
			xi4=float(self.ui.txtxi4.text())
			xi5=float(self.ui.txtxi5.text())
			xi6=float(self.ui.txtxi6.text())
			xi7=float(self.ui.txtxi7.text())
			yi1=float(self.ui.txtyi1.text())
			yi2=float(self.ui.txtyi2.text())
			yi3=float(self.ui.txtyi3.text())
			yi4=float(self.ui.txtyi4.text())
			yi5=float(self.ui.txtyi5.text())
			yi6=float(self.ui.txtyi6.text())
			yi7=float(self.ui.txtyi7.text())
			#Creación de arreglos
			xin=[xi1,xi2,xi3,xi4,xi5,xi6,xi7]
			yin=[yi1,yi2,yi3,yi4,yi5,yi6,yi7]
			a1=float(self.ui.txta1.text())
			a0=float(self.ui.txta0.text())
			def f(x):
				return a0 + a1*x
			Xmenor=int(min(xin))
			Xmayor=int(max(xin))
			x1=range(Xmenor,Xmayor+1)		
			fig, ax=plt.subplots()	
			ax.scatter(xin,yin)
			plt.plot(x1,[f(i) for i in x1])
			plt.axhline(0,color="black")
			plt.axvline(0,color="black")
			plt.savefig('Diagrama-disperción.png')
			plt.show()
		elif n==8:
			xi1=float(self.ui.txtxi1.text())
			xi2=float(self.ui.txtxi2.text())
			xi3=float(self.ui.txtxi3.text())
			xi4=float(self.ui.txtxi4.text())
			xi5=float(self.ui.txtxi5.text())
			xi6=float(self.ui.txtxi6.text())
			xi7=float(self.ui.txtxi7.text())
			xi8=float(self.ui.txtxi8.text())
			yi1=float(self.ui.txtyi1.text())
			yi2=float(self.ui.txtyi2.text())
			yi3=float(self.ui.txtyi3.text())
			yi4=float(self.ui.txtyi4.text())
			yi5=float(self.ui.txtyi5.text())
			yi6=float(self.ui.txtyi6.text())
			yi7=float(self.ui.txtyi7.text())
			yi8=float(self.ui.txtyi8.text())
			#Creación de arreglos
			xin=[xi1,xi2,xi3,xi4,xi5,xi6,xi7,xi8]
			yin=[yi1,yi2,yi3,yi4,yi5,yi6,yi7,yi8]
			a1=float(self.ui.txta1.text())
			a0=float(self.ui.txta0.text())
			def f(x):
				return a0 + a1*x
			Xmenor=int(min(xin))
			Xmayor=int(max(xin))
			x1=range(Xmenor,Xmayor+1)		
			fig, ax=plt.subplots()	
			ax.scatter(xin,yin)
			plt.plot(x1,[f(i) for i in x1])
			plt.axhline(0,color="black")
			plt.axvline(0,color="black")
			plt.savefig('Diagrama-disperción.png')
			plt.show()
		elif n==9:
			xi1=float(self.ui.txtxi1.text())
			xi2=float(self.ui.txtxi2.text())
			xi3=float(self.ui.txtxi3.text())
			xi4=float(self.ui.txtxi4.text())
			xi5=float(self.ui.txtxi5.text())
			xi6=float(self.ui.txtxi6.text())
			xi7=float(self.ui.txtxi7.text())
			xi8=float(self.ui.txtxi8.text())
			xi9=float(self.ui.txtxi9.text())
			yi1=float(self.ui.txtyi1.text())
			yi2=float(self.ui.txtyi2.text())
			yi3=float(self.ui.txtyi3.text())
			yi4=float(self.ui.txtyi4.text())
			yi5=float(self.ui.txtyi5.text())
			yi6=float(self.ui.txtyi6.text())
			yi7=float(self.ui.txtyi7.text())
			yi8=float(self.ui.txtyi8.text())
			yi9=float(self.ui.txtyi9.text())
			#Creación de arreglos
			xin=[xi1,xi2,xi3,xi4,xi5,xi6,xi7,xi8,xi9]
			yin=[yi1,yi2,yi3,yi4,yi5,yi6,yi7,yi8,yi9]
			a1=float(self.ui.txta1.text())
			a0=float(self.ui.txta0.text())
			def f(x):
				return a0 + a1*x
			Xmenor=int(min(xin))
			Xmayor=int(max(xin))
			x1=range(Xmenor,Xmayor+1)		
			fig, ax=plt.subplots()	
			ax.scatter(xin,yin)
			plt.plot(x1,[f(i) for i in x1])
			plt.axhline(0,color="black")
			plt.axvline(0,color="black")
			plt.savefig('Diagrama-disperción.png')
			plt.show()
		elif n==10:
			xi1=float(self.ui.txtxi1.text())
			xi2=float(self.ui.txtxi2.text())
			xi3=float(self.ui.txtxi3.text())
			xi4=float(self.ui.txtxi4.text())
			xi5=float(self.ui.txtxi5.text())
			xi6=float(self.ui.txtxi6.text())
			xi7=float(self.ui.txtxi7.text())
			xi8=float(self.ui.txtxi8.text())
			xi9=float(self.ui.txtxi9.text())
			xi10=float(self.ui.txtxi10.text())
			yi1=float(self.ui.txtyi1.text())
			yi2=float(self.ui.txtyi2.text())
			yi3=float(self.ui.txtyi3.text())
			yi4=float(self.ui.txtyi4.text())
			yi5=float(self.ui.txtyi5.text())
			yi6=float(self.ui.txtyi6.text())
			yi7=float(self.ui.txtyi7.text())
			yi8=float(self.ui.txtyi8.text())
			yi9=float(self.ui.txtyi9.text())
			yi10=float(self.ui.txtyi10.text())
			#Creación de arreglos
			xin=[xi1,xi2,xi3,xi4,xi5,xi6,xi7,xi8,xi9]
			yin=[yi1,yi2,yi3,yi4,yi5,yi6,yi7,yi8,yi9]
			a1=float(self.ui.txta1.text())
			a0=float(self.ui.txta0.text())
			def f(x):
				return a0 + a1*x
			Xmenor=int(min(xin))
			Xmayor=int(max(xin))
			x1=range(Xmenor,Xmayor+1)		
			fig, ax=plt.subplots()	
			ax.scatter(xin,yin)
			plt.plot(x1,[f(i) for i in x1])
			plt.axhline(0,color="black")
			plt.axvline(0,color="black")
			plt.savefig('Diagrama-disperción.png')
			plt.show()
		else:
			mensaje.setIcon(QMessageBox.Warning)
			mensaje.setText("Error inesperado, fuera de rango")
			mensaje.exec_()

	def borrartodo(self):
		self.ui.btnGrafica.setEnabled(False)
		self.ui.txtxi1.clear()
		self.ui.txtxi2.clear()
		self.ui.txtxi3.clear()
		self.ui.txtxi4.clear()
		self.ui.txtxi5.clear()
		self.ui.txtxi6.clear()
		self.ui.txtxi7.clear()
		self.ui.txtxi8.clear()
		self.ui.txtxi9.clear()
		self.ui.txtxi10.clear()
		self.ui.txtyi1.clear()
		self.ui.txtyi2.clear()
		self.ui.txtyi3.clear()
		self.ui.txtyi4.clear()
		self.ui.txtyi5.clear()
		self.ui.txtyi6.clear()
		self.ui.txtyi7.clear()
		self.ui.txtyi8.clear()
		self.ui.txtyi9.clear()
		self.ui.txtyi10.clear()
		#Limpiar sumas xi y yi
		self.ui.txtSumxi.clear()
		self.ui.txtSumyi.clear()
		#Limpiar xiyi
		self.ui.txtxiyi1.clear()
		self.ui.txtxiyi2.clear()
		self.ui.txtxiyi3.clear()
		self.ui.txtxiyi4.clear()
		self.ui.txtxiyi5.clear()
		self.ui.txtxiyi6.clear()
		self.ui.txtxiyi7.clear()
		self.ui.txtxiyi8.clear()
		self.ui.txtxiyi9.clear()
		self.ui.txtxiyi10.clear()
		#Limpiar suma xiyi
		self.ui.txtSumxiyi.clear()
		#Limpiar xi al cuadrado
		self.ui.txtxi12.clear()
		self.ui.txtxi22.clear()
		self.ui.txtxi32.clear()
		self.ui.txtxi42.clear()
		self.ui.txtxi52.clear()
		self.ui.txtxi62.clear()
		self.ui.txtxi72.clear()
		self.ui.txtxi82.clear()
		self.ui.txtxi92.clear()
		self.ui.txtxi102.clear()
		#limpiar suma xi al cuadrado
		self.ui.txtSumxi2.clear()
		#Limpiando otros datos complementarios de utilidad
		self.ui.txtxiSum22.clear()
		self.ui.txta1.clear()
		self.ui.txtxiM.clear()
		self.ui.txtyiM.clear()
		self.ui.txta0.clear()
		self.ui.lblRespuesta.setText("")
		self.ui.txtEcuacion.clear()
		self.ui.txtn.clear()
		self.ui.btnDefinirN.setEnabled(True)
		self.ui.txtn.setEnabled(True)
		self.ui.btnGrafica.setEnabled(False)
		self.ui.btnEcuacion.setEnabled(False)
		self.ui.txtxi1.setEnabled(False)
		self.ui.txtxi2.setEnabled(False)
		self.ui.txtxi3.setEnabled(False)
		self.ui.txtxi4.setEnabled(False)
		self.ui.txtxi5.setEnabled(False)
		self.ui.txtxi6.setEnabled(False)
		self.ui.txtxi7.setEnabled(False)
		self.ui.txtxi8.setEnabled(False)
		self.ui.txtxi9.setEnabled(False)
		self.ui.txtxi10.setEnabled(False)
		self.ui.txtyi1.setEnabled(False)
		self.ui.txtyi2.setEnabled(False)
		self.ui.txtyi3.setEnabled(False)
		self.ui.txtyi4.setEnabled(False)
		self.ui.txtyi5.setEnabled(False)
		self.ui.txtyi6.setEnabled(False)
		self.ui.txtyi7.setEnabled(False)
		self.ui.txtyi8.setEnabled(False)
		self.ui.txtyi9.setEnabled(False)
		self.ui.txtyi10.setEnabled(False)

if __name__=='__main__':					
	app=QtWidgets.QApplication(sys.argv)	
	myapp=Ecuacion()					
	myapp.show()							
	sys.exit(app.exec_())
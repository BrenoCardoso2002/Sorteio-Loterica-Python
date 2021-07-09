# importações
import os
import random
import sys
from PyQt5.QtGui import QPixmap, QIntValidator
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QWidget, QLabel, QGraphicsOpacityEffect, QLineEdit, QPushButton, QMessageBox
from PyQt5 import QtGui
from PyQt5.QtCore import Qt


# Função MsgBox de Erro de preenchimento:
def MsgBoxErroPreenchimento():
    box = QMessageBox()
    pixmap = QPixmap('logo.png').scaledToHeight(32, Qt.SmoothTransformation)
    box.setIconPixmap(pixmap)
    box.setWindowTitle('Erro!')
    box.setText('Há algum campo em branco!!!')
    box.exec_()


# Função MsgBox de Erro de Nome de arquivo:
def MsgBoxErroNomeArquivo():
    box = QMessageBox()
    pixmap = QPixmap('logo.png').scaledToHeight(32, Qt.SmoothTransformation)
    box.setIconPixmap(pixmap)
    box.setWindowTitle('Erro!')
    box.setText('Nome de arquivo inválido!!!')
    box.exec_()


# Função MsgBox de Erro nos números:
def MsgBoxErroNumeros():
    box = QMessageBox()
    pixmap = QPixmap('logo.png').scaledToHeight(32, Qt.SmoothTransformation)
    box.setIconPixmap(pixmap)
    box.setWindowTitle('Erro!')
    box.setText('Nenhum dos números pode ser zero!!!')
    box.exec_()


# Função MsgBox de Erro de Nome de arquivo:
def MsgBoxSucess():
    box = QMessageBox()
    pixmap = QPixmap('logo.png').scaledToHeight(32, Qt.SmoothTransformation)
    box.setIconPixmap(pixmap)
    box.setWindowTitle('Sucesso!')
    box.setText('Arquivo criado com sucesso!\nSe quiser fazer outro arquivo feche o programa e o abra novamente!')
    box.exec_()


# Função que valida o nome do arquivo
def ValidaNomeArquivo(Nome):
    File = '{}.csv'.format(Nome)
    Exist = os.path.isfile(File)  # True for Existe | False for Not Existe
    if Exist:
        return True
    else:
        return False


# Função que realiza os jogos:
def RealizaJogos(Jogos, Numeros, Arquivo):
    Lista = []
    while Jogos > 0:
        Jogos -= 1
        texto = ''
        Lista1 = []
        for n in range(Numeros):
            while True:
                sorteado = random.randint(1, 80)
                if sorteado not in Lista1:
                    break
            Lista1.append(sorteado)
            texto = texto + '{};'.format(sorteado)
        texto = texto[:-1]
        if texto in Lista:
            Jogos += 1
        else:
            Lista.append(texto)
    LancaExcel(Arquivo, Lista)


# Função que lança os dados no excel:
def LancaExcel(Arquivo, lista):
    f = open("{}.csv".format(Arquivo), "w")
    for n in range(len(lista)):
        f.writelines('{}\n'.format(lista[n]))
    f.close()


# classe da janela
class Janela(QWidget):
    def __init__(self):
        super().__init__()

        # dados da tela:
        self.topo = 0
        self.esquerda = 0
        self.largura = 380
        self.altura = 380
        self.titulo = 'Sorteio Loterica'
        self.setFixedSize(self.largura, self.altura)
        self.setWindowIcon(QtGui.QIcon('logo.png'))
        self.setStyleSheet('background-image: logo.png')
        # Variaveis:
        self.OnlyInt = QIntValidator()

        # Background Image:
        label1 = QLabel(self)
        pixmap = QPixmap('logo.png')
        label1.setPixmap(pixmap)
        label1.move(10, 10)
        label1.resize(370, 370)
        label1.setScaledContents(100)
        self.opacity_effect = QGraphicsOpacityEffect()
        self.opacity_effect.setOpacity(0.15)
        label1.setGraphicsEffect(self.opacity_effect)

        # label titulo:
        label2 = QLabel(self)
        label2.setText("{}:".format(self.titulo))
        label2.move(15, 15)
        label2.setStyleSheet('QLabel {font: bold; font-size: 26px; color: black}')

        # label número de jogos:
        label3 = QLabel(self)
        label3.setText('Quantidade de jogos:')
        label3.move(25, 50)
        label3.setStyleSheet('QLabel {font: bold; font-size: 22px; color: black}')

        # Caixa de textos numero de Jogos:
        self.NJogos = QLineEdit(self)
        self.NJogos.setPlaceholderText('Quantidade de jogos...')
        self.NJogos.move(40, 85)
        self.NJogos.setStyleSheet('QLineEdit {font: bold; font-size: 18px; color: black; padding: 2px}')
        self.NJogos.resize(220, 35)
        self.NJogos.setValidator(self.OnlyInt)
        self.NJogos.setMaxLength(3)

        # Label numero de numeros:
        label4 = QLabel(self)
        label4.setText('Quantidade de numeros:')
        label4.move(25, 125)
        label4.setStyleSheet('QLabel {font: bold; font-size: 22px; color: black}')

        # Caixa de textos numero de Numeros:
        self.NNumeros = QLineEdit(self)
        self.NNumeros.setPlaceholderText('Quantidade de numeros...')
        self.NNumeros.move(40, 160)
        self.NNumeros.setStyleSheet('QLineEdit {font: bold; font-size: 18px; color: black; padding: 2px}')
        self.NNumeros.resize(250, 35)
        self.NNumeros.setValidator(self.OnlyInt)
        self.NNumeros.setMaxLength(2)

        # Label nome do arquivo:
        label5 = QLabel(self)
        label5.setText('Nome do arquivo:')
        label5.move(25, 200)
        label5.setStyleSheet('QLabel {font: bold; font-size: 22px; color: black}')

        # Caixa de textos nome do arquivo:
        self.NomeArquivo = QLineEdit(self)
        self.NomeArquivo.setPlaceholderText('Nome do arquivo...')
        self.NomeArquivo.move(40, 235)
        self.NomeArquivo.setStyleSheet('QLineEdit {font: bold; font-size: 18px; color: black; padding: 2px}')
        self.NomeArquivo.resize(190, 35)
        self.NomeArquivo.textChanged.connect(self.NomeChanged)

        # Label nome ja usado:
        self.label6 = QLabel(self)
        self.label6.setText('Nome já usado!')
        self.label6.move(240, 245)
        self.label6.setStyleSheet('QLabel {font: bold; font-size: 16px; color: red}')
        self.label6.setVisible(False)

        # Botão de Criar arquivo CSV
        self.Botao = QPushButton(self)
        self.Botao.setText('Criar Arquivo')
        self.Botao.move(100, 280)
        self.Botao.setStyleSheet('QPushButton {font: bold; font-size: 20px; color: black; padding: 5px 15px 5px 15px}')
        self.Botao.clicked.connect(self.ClickedButton)

        # Abre a Janela
        self.CarregarJanela()

    # Função que Carrega a Janela
    def CarregarJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.center()
        self.show()

    # Centraliza na tela:
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # Função de mudança de valor no nome do arquivo:
    def NomeChanged(self):
        Nome = self.NomeArquivo.text()
        if Nome != '':
            if not Nome.replace(' ', '').isalnum() and Nome[len(Nome) - 1] != ' ':
                Nome = Nome[:-1]
            self.NomeArquivo.setText(Nome)
            self.label6.setVisible(False)
            if ValidaNomeArquivo(Nome):
                self.label6.setVisible(True)

    # Função de Clique de criar arquivo
    def ClickedButton(self):
        Nome = self.NomeArquivo.text()
        Numero = self.NNumeros.text()
        Jogos = self.NJogos.text()
        if Nome.replace(' ', '') == '' or Numero == '' or Jogos == '':
            MsgBoxErroPreenchimento()
        else:
            if ValidaNomeArquivo(Nome):
                MsgBoxErroNomeArquivo()
                self.NomeArquivo.setText('')
                self.NomeArquivo.setFocus()
            else:
                Numero = int(Numero)
                Jogos = int(Jogos)
                if Numero == 0 or Jogos == 0:
                    MsgBoxErroNumeros()
                    self.NNumeros.setText('')
                    self.NJogos.setText('')
                    self.NJogos.setFocus()
                else:
                    RealizaJogos(Jogos, Numero, Nome)
                    self.ArqCriado()

    # Função chamada depois de que o arquivo foi criado:
    def ArqCriado(self):
        self.NJogos.setEnabled(False)
        self.NomeArquivo.setEnabled(False)
        self.NNumeros.setEnabled(False)
        self.Botao.setEnabled(False)
        MsgBoxSucess()


# Inicializa Tela
aplicacao = QApplication(sys.argv)
Window = Janela()
sys.exit(aplicacao.exec_())

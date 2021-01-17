# Importando bibliotecas 
import pandas as pd
from PyQt5 import uic, QtWidgets

# Conectando a aplicação
app=QtWidgets.QApplication([])

def alterar():
    """
    Convertendo o arquivo XLSX para CSV com a biblioteca pandas.
    """
    try:
        read_file = pd.read_excel(str(primeira_tela.lineEdit.text()))
        read_file.to_csv(str(primeira_tela.lineEdit_2.text()), index = None, header=True)
        primeira_tela.close()
        segunda_tela.show()
    except:
        primeira_tela.close()
        terceira_tela.show()

# CARREGANDO OS ARQUIVOS
primeira_tela = uic.loadUi('primeira_tela.ui')
segunda_tela = uic.loadUi('segunda_tela.ui')
terceira_tela = uic.loadUi('terceira_tela.ui')
# MOSTRANDO A PRIMEIRA TELA
primeira_tela.show()
# BOTÕES
primeira_tela.pushButton.clicked.connect(alterar)
# EXECUTANDO A APLICAÇÃO
app.exec()


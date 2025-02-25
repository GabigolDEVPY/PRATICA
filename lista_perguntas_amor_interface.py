from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QRadioButton, QButtonGroup, QMessageBox
from PySide6.QtCore import Qt
import sys

class QuizWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.perguntas = [
            {
                'Pergunta': 'Qual a data de aniversário dela?',
                'Opções': ['11/05', '29/05', '30/05', '32/05'],
                'Resposta': '32/05',
            },
            {
                'Pergunta': 'Qual o chocolate preferido dela?',
                'Opções': ['Ao leite', 'Meio Amargo', 'Branco', '100% cacau'],
                'Resposta': 'Ao leite',
            },
            {
                'Pergunta': 'Qual treino favorito dela?',
                'Opções': ['Glúteos', 'Costas e bíceps', 'Ficar em casa dormindo', 'Peito e tríceps'],
                'Resposta': 'Ficar em casa dormindo',
            },
            {
                'Pergunta': 'Qual filme desses ela mais gosta?',
                'Opções': ['Alice no País das Maravilhas', 'Divertida Mente 2', 'Era do Gelo', 'Menino do Pijama Listrado'],
                'Resposta': 'Divertida Mente 2',
            },
            {
                'Pergunta': 'Qual desses apelidos ela odeia te chamar?',
                'Opções': ['Gatinho', 'Garoto', 'Meu bem', 'Princeso'],
                'Resposta': 'Garoto',
            },
        ]
        self.qtd_acertos = 0
        self.current_question = 0

        # Definindo a janela principal
        self.setWindowTitle("Quiz Sobre Sua GATINHA")
        self.setGeometry(200, 200, 600, 400)
        self.setStyleSheet("background-color: #000000;")

        # Layout principal
        self.layout = QVBoxLayout()

        # Pergunta
        self.label_pergunta = QLabel(self.perguntas[self.current_question]['Pergunta'])
        self.label_pergunta.setAlignment(Qt.AlignCenter)
        self.label_pergunta.setStyleSheet("font-size: 18px; font-weight: bold; margin-bottom: 20px;")
        self.layout.addWidget(self.label_pergunta)

        # Opções (Botões de Radio)
        self.button_group = QButtonGroup()
        self.opcoes = []
        for i, opcao in enumerate(self.perguntas[self.current_question]['Opções']):
            radio_button = QRadioButton(opcao)
            radio_button.setStyleSheet("font-size: 16px;")
            self.layout.addWidget(radio_button)
            self.opcoes.append(radio_button)
            self.button_group.addButton(radio_button, i)

        # Botão para confirmar
        self.btn_confirmar = QPushButton("Confirmar Resposta")
        self.btn_confirmar.setStyleSheet("""
            QPushButton {
                background-color: #007BFF;
                color: white;
                font-size: 16px;
                padding: 10px;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """)
        self.btn_confirmar.clicked.connect(self.verificar_resposta)
        self.layout.addWidget(self.btn_confirmar)

        # Widget e Layout
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def verificar_resposta(self):
        escolha_id = self.button_group.checkedId()
        if escolha_id == -1:
            return  # Nenhuma opção selecionada

        resposta_correta = self.perguntas[self.current_question]['Resposta']
        if self.perguntas[self.current_question]['Opções'][escolha_id] == resposta_correta:
            self.qtd_acertos += 1
            self.mostrar_mensagem("Parabéns!", "Você acertou a pergunta! 😉")
        else:
            self.mostrar_mensagem("Que pena!", "Você errou a pergunta! 😢")

        self.current_question += 1
        if self.current_question < len(self.perguntas):
            self.atualizar_pergunta()
        else:
            self.mostrar_resultado()

    def atualizar_pergunta(self):
        self.label_pergunta.setText(self.perguntas[self.current_question]['Pergunta'])
        for i, opcao in enumerate(self.perguntas[self.current_question]['Opções']):
            self.opcoes[i].setText(opcao)
            self.opcoes[i].setChecked(False)

    def mostrar_mensagem(self, titulo, mensagem):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(titulo)
        msg_box.setText(mensagem)
        msg_box.setStyleSheet("font-size: 14px;")
        msg_box.exec()

    def mostrar_resultado(self):
        if self.qtd_acertos == len(self.perguntas):
            self.mostrar_mensagem("Resultado", f"Você está completamente apaixonado por ela 😍😍😍\nVocê acertou {self.qtd_acertos} de {len(self.perguntas)} perguntas!")
        else:
            self.mostrar_mensagem("Resultado", f"Você errou algumas perguntas simples.\nVocê acertou {self.qtd_acertos} de {len(self.perguntas)} perguntas.")

        self.label_pergunta.setText(f"Você acertou {self.qtd_acertos} de {len(self.perguntas)} perguntas!")
        for opcao in self.opcoes:
            opcao.hide()
        self.btn_confirmar.hide()

# Aplicação principal
app = QApplication(sys.argv)

window = QuizWindow()
window.show()

sys.exit(app.exec())

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QHBoxLayout,QPushButton, QVBoxLayout,QRadioButton,QMessageBox
from random import randint

app = QApplication([])

main_win = QWidget()
main_win.setWindowTitle('BlaBlablu')
main_win.resize(500,500)
main_win.move(700,300)


text1 = QLabel('Добро пожаловать в програму по определению состояния здоровья!')
text = QLabel('Данное приложение позволит вам с помощью теста Руфье провести первичную диагностику вашего здоровья.\n'
                   'Проба Руфье представляет собой нагрузочный комплекс, предназначенный для оценки работоспособности сердца при физической нагрузке.\n'
                   'У испытуемого, находящегося в положении лежа на спине в течение 5 мин, определяют частоту пульса за 15 секунд;\n'
                   'затем в течение 45 секунд испытуемый выполняет 30 приседаний.\n'
                   'После окончания нагрузки испытуемый ложится, и у него вновь подсчитывается число пульсаций за первые 15 секунд,\n'
                   'а потом — за последние 15 секунд первой минуты периода восстановления.\n'
                   'Важно! Если в процессе проведения испытания вы почувствуете себя плохо (появится головокружение, шум в\n'
                   'ушах, сильная одышка и др.), то тест необходимо прервать и обратиться к врачу.')
button = QPushButton('Начать')         
button.setText('Начать')     
button.text()
v_line = QVBoxLayout()
v_line.addWidget(text1, alignment = Qt.AlignCenter)
v_line.addWidget(text, alignment = Qt.AlignCenter)
v_line.addWidget(button, alignment = Qt.AlignCenter)
main_win.setLayout(v_line)


main_win.show()

app.exec_()
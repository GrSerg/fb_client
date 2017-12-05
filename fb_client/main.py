#!/usr/bin/env python

# Клиент чата Finger balabolka

import sys
import socket

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QThread, pyqtSlot

from core.client import Client
from core.handlers import GuiReciever
from utils.utils import get_params
from ui.gui_class import UserGUI


userGUI = UserGUI(client)
window = userGUI.get_chat()


@pyqtSlot(str)
def update_chat(data):
    ''' Отображение сообщения в чате
    '''
    try:
        msg = data
        window.append(msg)
    except Exception as e:
        print(e)


def main(GUI):
    app = QtWidgets.QApplication(sys.argv)

    params = get_params()
    client = Client(**params)

    reciever = GuiReciever(client)
    reciever.gotData.connect(update_chat)
    th = QThread()
    reciever.moveToThread(th)
    th.started.connect(reciever.poll)
    th.start()

    GUI.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main(userGUI)
from server.instance import server

from controllers.pix import *
from controllers.token import *

server.run()


# SE DER ERRO VOCE VAI NO CAMINHO
# venv/lib/site-packages/flask_restplus/models.py
# apaga o MutableMapping que vem do collections e adiciona o codigo abaixo
"""
import sys
if sys.version_info[:2] >= (3, 8):
    from collections.abc import MutableMapping
else:
    from collections import MutableMapping
"""
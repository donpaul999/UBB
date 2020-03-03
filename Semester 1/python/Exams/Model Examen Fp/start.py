from ui import *
from Repo import *
from TextRepo import *
from controller import *

repo = TextRepository("reservations.txt")
service = Service(repo)
ui = UI(service)

ui.start()
# https://www.youtube.com/watch?v=WIqX3kDxDKE
class Accident(Exception):
    def __init__(self, msg):
        self.msg = msg
    def print_exception(self):
        print("User defined exception:", self.msg)

try:
    raise Accident('Crash between two cars')
except Accident as e:
    e.print_exception()


class Accident(Exception):
    def __init__(self, msg):
        self.msg = msg
    def handle(self):
        print("User defined exception:", self.msg)

try:
    raise Accident('Crash between two cars')
except Accident as e:
    e.handle()

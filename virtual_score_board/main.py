from twisted.internet import task
from twisted.internet import reactor
from virtual_score_board.models import Timer

timer = Timer()

def runEverySecond():
    print(int(timer.get_seconds()))

l = task.LoopingCall(runEverySecond)
timer.start()
l.start(1.0)

reactor.run()

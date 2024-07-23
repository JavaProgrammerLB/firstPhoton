from leptonai.photon import Photon

class Counter(Photon):
    # The init method implements any custom initialization logic we need.
    def init(self):
        self.counter = 0

    # When no name is specified, the handler name is the method name.
    @Photon.handler
    def add(self, x: int) -> int:
        self.counter += x
        return self.counter

    # Or, we can specify a name for the handler.
    @Photon.handler("billsub")
    def sub(self, x: int) -> int:
        return self.add(-x)
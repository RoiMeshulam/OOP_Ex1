class CallForElevator:
    def __init__(self,time,src,dest,status,allocatedTo):
        self._time = time
        self._src = src
        self._dest = dest
        self._status = status
        self._allocatedTo = allocatedTo

    def __str__(self):
        return f"Call was made at {self._time}, from {self._src} to {self._dest} and it was allocated to {self._allocatedTo}"

    def __repr__(self):
        return f"Call was made at {self._time}, from {self._src} to {self._dest} and it was allocated to {self._allocatedTo}"

if __name__== '__main__':
    c1 = CallForElevator(0,1,2,-1,-1)
    print(c1)
    c1.from_csv("Calls_a.csv")
    print(c1._allCalls)
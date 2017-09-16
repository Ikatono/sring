class sring:
    
    #don't mess with defaults when creating a new sring
    def __init__(self, dat, size=1, eprev=None, enext=None):
        self.dat = dat
        self.size = size
        if eprev is None:
            self.eprev = self
            self.enext = self
        else:
            self.eprev = eprev
            self.enext = enext
    
    def __getitem__(self, index):
        return self.rotate(index).dat
    
    def __delitem__(self, index):
        loc = self.rotate(index)
        loc.eprev.enext = loc.enext
        loc.enext.eprev = loc.eprev
        self.propsize(self.size-1)
    
    def __str__(self):
        return str(self.cut())
    
    def __len__(self):
        return self.size
    
    def rotate(self, index):
        if not isinstance(index, int):
            raise TypeError('index must be an integer')
        ind = ((index + self.size / 2) % self.size) - self.size / 2
        if ind == 0:
            return self
        elif ind < 0:
            loc = self
            while ind != 0:
                loc = loc.eprev
                ind += 1
            return loc
        elif index > 0:
            loc = self
            while ind != 0:
                loc = loc.enext
                ind -= 1
            return loc
    
    #inserts AFTER the given index
    def insert(self, dat, index=-1):
        target = self.rotate(index)
        tarnext = target.enext
        enew = sring(dat, eprev=target, enext = tarnext)
        target.enext = enew
        tarnext.eprev = enew
        self.propsize(self.size+1)
    
    def cut(self, index=0):
        loc = self.rotate(index)
        data = [loc.dat]
        nex = loc.enext
        while nex != loc:
            data += [nex.dat]
            nex = nex.enext
        return data

    def propsize(self, nsize):
        self.size = nsize
        loc = self.enext
        while loc != self:
            loc.size = nsize
            loc = loc.enext

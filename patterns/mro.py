class Adam: pass
class Eva: pass
class Raymod(Adam, Eva): pass
class Gayl(Adam, Eva): pass
class Raf(Raymod, Gayl): pass
class Polina(Adam, Eva): pass
class Vasya(Adam, Eva): pass
class PolinaVasya(Polina, Vasya):pass
class Mat(Raf, PolinaVasya):pass



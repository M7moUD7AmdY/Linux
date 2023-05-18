def set_bit(var, bitno):
    var |= (1 << bitno)
    return var

def clr_bit(var, bitno):
    var &= ~(1 << bitno)
    return var

def tog_bit(var, bitno):
    var ^= (1 << bitno)
    return var

def get_bit(var, bitno):
    return (var >> bitno) & 0x01
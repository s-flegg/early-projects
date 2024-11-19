scale = 0.1

def forwards(input):
    if input > 0:
        return input
    else:
        return input * scale

def derivative(input):
    if input < 0:
        return scale
    else:
        return 1
from example import algae, fractal_binary_tree, koch_snowflake

# Taken from https://en.wikipedia.org/wiki/L-system
def test_algae():
    system = algae()
    system.step(7)

    assert str(system).replace(" ", "") == "ABAABABAABAABABAABABAABAABABAABAAB"

def test_fractal_binary_tree():
    system = fractal_binary_tree()
    system.step(3)

    assert str(system).replace(" ", "") == "1111[11[1[0]0]1[0]0]11[1[0]0]1[0]0"

def test_koch_snowflake():
    system = koch_snowflake()
    system.step(3)

    assert str(system).replace(" ", "") == "F+F--F+F+F+F--F+F--F+F--F+F+F+F--F+F+F+F--F+F+F+F--F+F--F+F--F+F+F+F--F+F--F+F--F+F+F+F--F+F--F+F--F+F+F+F--F+F+F+F--F+F+F+F--F+F--F+F--F+F+F+F--F+F"

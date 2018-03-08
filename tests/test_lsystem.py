from lsystem import LSystem

def test_koch_snowflake():
    system = LSystem(
        axiom="F",
        rules={
            "F": "F+F--F+F"
        }
    )

    system.step(3)

    assert system.state == "F+F--F+F+F+F--F+F--F+F--F+F+F+F--F+F+F+F--F+F+F+F--F+F--F+F--F+F+F+F--F+F--F+F--F+F+F+F--F+F--F+F--F+F+F+F--F+F+F+F--F+F+F+F--F+F--F+F--F+F+F+F--F+F"

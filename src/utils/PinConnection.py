from enum import Enum


class PinConnection(Enum):
    """
    Enum class for the connection of the pins.
    F - Front
    R - Rear
    L - Left
    Ri - Right
    M - Motor
    S - Servo
    Se - Sensor
    """
    FLM = 1  # Front Left Motor
    FRiM = 2  # Front Right Motor
    RLM = 3  # Rear Left Motor
    RRM = 4  # Rear Right Motor


if __name__ == '__main__':
    print(PinConnection.RLM.value)

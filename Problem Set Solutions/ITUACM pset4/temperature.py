class Temperature:
    def __init__(self, celsius: float):
        """
        initializes the temperature instance with celsius as the base unit.
        """
        self._celsius = celsius

    @classmethod
    def from_celsius(cls, value: float):
        """
        creates an instance from a temperature in celsius.
        """
        return cls(value)

    @classmethod
    def from_fahrenheit(cls, value: float):
        """
        creates an instance from a temperature in fahrenheit.
        """
        celsius = (value - 32) * 5 / 9
        return cls(celsius)

    @classmethod
    def from_kelvin(cls, value: float):
        """
        creates an instance from a temperature in kelvin.
        """
        celsius = value - 273.15
        return cls(celsius)

    def to_celsius(self) -> float:
        """
        returns the temperature in celsius.
        """
        return self._celsius

    def to_fahrenheit(self) -> float:
        """
        converts and returns the temperature in fahrenheit.
        """
        return self._celsius * 9 / 5 + 32

    def to_kelvin(self) -> float:
        """
        converts and returns the temperature in kelvin.
        """
        return self._celsius + 273.15

# example usage
def main():
    # create an instance from celsius
    temp = Temperature.from_celsius(25)
    print(f"25°C to fahrenheit: {temp.to_fahrenheit()}°F")
    print(f"25°C to kelvin: {temp.to_kelvin()}K")

    # create an instance from fahrenheit
    temp = Temperature.from_fahrenheit(32)
    print(f"32°F to celsius: {temp.to_celsius()}°C")
    print(f"32°F to kelvin: {temp.to_kelvin()}K")

    # create an instance from kelvin
    temp = Temperature.from_kelvin(300)
    print(f"300K to celsius: {temp.to_celsius()}°C")
    print(f"300K to fahrenheit: {temp.to_fahrenheit()}°F")

if __name__ == "__main__":
    main()


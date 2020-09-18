class MyTemperature:
    
    def __init__(self, t):
        self.celsius = t

    @property    
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, new_value):
        self._celsius = new_value
        
    @property
    def fahrenheit(self):
        return (self._celsius * 1.8) + 32

    @fahrenheit.setter
    def fahrenheit(self, new_value):
        self._celsius = (new_value - 32)/1.8
        
        
t1 = MyTemperature(37)

print(t1.celsius)
print(t1.fahrenheit)


t1.celsius = 27
print(t1.celsius)
print(t1.fahrenheit)

t1.fahrenheit = 80.6
print(t1.celsius)
print(t1.fahrenheit)
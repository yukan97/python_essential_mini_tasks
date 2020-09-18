class YearNotInRange(Exception):
    
    def __init__(self, year):
        self.year = year
        self.message = "Year is not in range [2000, 2020]!"
        super().__init__(self.message)
        
def get_year():
    
    year = int(input("please, enter your year -> "))
    if not 2000 <= year <= 2020:
        raise YearNotInRange(year)
        
get_year()
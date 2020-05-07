class ChangeNumeralSistem:
    

    sis_numbers = []

    def __init__(self, number, base):
        self.base = base
        self.x = number
        self.first_number = number
    
    def __change(self):
        while self.x > 0:
            self.sis_numbers.append(self.x % self.base)
            self.x //= self.base
        if self.base > 10:
            alph_numbers = {10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f"}
            for n in range(len(self.sis_numbers)):
                if self.sis_numbers[n] in alph_numbers:
                    self.sis_numbers[n] = alph_numbers[self.sis_numbers[n]]
        self.sis_numbers.reverse()
        return self.sis_numbers
    
    def show_number(self):
        print(f'Число {self.first_number} в системе исчисления {self.base}', end=': ')
        for val in self.__change():
            print(val, end='')
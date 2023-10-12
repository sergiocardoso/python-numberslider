'''
Class Base from Number Slice
@author Sérgio Cardoso
Euristica Jogo 8Number
- 8 numeros
- 9 posições

 1 | 2 | 3
-----------
 4 | 5 | 6
-----------
 7 | 8 | X

TODO:
- metodo para sortear aleatoriamente os números em posícoes de 1 a 9
- metodo para criar o grid (design) com os respectivos números 
'''

import random

class MakeGrid:
    def __init__(self):
        self.numbers = random.sample(range(0,9),9)

    def show(self):
        print(" {pos1} | {pos2} | {pos3} ".format(pos1=self.numbers[0], pos2=self.numbers[1], pos3=self.numbers[2]))
        print(" {pos4} | {pos5} | {pos6} ".format(pos4=self.numbers[3], pos5=self.numbers[4], pos6=self.numbers[5]))
        print(" {pos7} | {pos8} | {pos9} ".format(pos7=self.numbers[6], pos8=self.numbers[7], pos9=self.numbers[8]))


if __name__ == "__main__":
    MakeGrid().show();

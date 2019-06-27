import os
os.system('pylint comparar.py')
var=os.system('radon cc comparar.py -a')
print('valor: ',var)

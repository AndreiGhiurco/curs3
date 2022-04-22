km =int(input('introdu km pe ora'))
print(km > 0)
if (km < 0):
    print('masina stationeaza')
elif (km <= 50):
    print('merge in localitate')
elif ( km <=90) :
    print('ruleaza pe DN')
elif (km <= 120):
      print('ruleaza pe A1')

else:
    print ('Adio viata')
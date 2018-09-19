import mymodule

#print(myfunction()) #error!
print(mymodule.myfunction())

from mymodule import myfunction

print(myfunction())

def main():
#-----------------------------------------------------
 def perfection(z):
    x = []
    for i in range(1, z):
     if z % i == 0:
      x.append(i)
     return x
#-----------------------------------------------------
 def summa(x, y):
    if y == sum(x):
        print("Число совершенное")
    else:
        print("Число несовершенное")
 y = int(input("Введите число: "))
 x = perfection(y)
 print(x)
 summa(x, y)
#-----------------------------------------------------
if __name__ == "__main__":       
    main() 




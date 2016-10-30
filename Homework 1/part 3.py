def main():
   #show 1-11, all the related odd number, and also the power of 2&3
   maxVal = 11
   for x in range(1, maxVal+1):       #include [1, 11), have 1, no 11
      if(x % 2 ==  1 ):
         print(repr(x).rjust(2), repr(x*x).rjust(3), repr(x*x*x).rjust(4))

main()   

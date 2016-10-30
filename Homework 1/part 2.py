def main():
    
   in1 = input("Enter the Hour: ")

   num = 0 + eval(in1)     # eval() convert the input string into a number
   if (num <= 0) or (num >= 25):
      print(in1,'is out of range')
      return 0   #if it is over 25, print and terminate
   else:
      num1 = num % 12  #2%12 =2;

   if(num == 24):
      f12 = "MIDNIGHT"
   elif(num < 10):
      f12 = "0"+str(num1)+" AM" # 1-9, convert 1 to 01 
   elif(num > 12):
      f12 =  str(num1)+" PM"  # >12, convert 13 to 1
      #f12 =  str(num-12)+" PM"  # >12, convert 13 to 1
   elif num == 12:
      f12 = "NOON"
   else:
      f12 = str(num1)+" AM" # 10,11, 12
   print("Time", in1,  "using 12-hour clock: ",f12)

   if(num == 24):
       f24 = "MIDNIGHT"
   elif(num == 12):
       f24 = "NOON"
   elif(num < 10):
       f24 = in1
   else:
       f24 = in1
   print("Time", in1,  "using 24-hour clock: ",f24)
main()

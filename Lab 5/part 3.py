def main():

    degreeC = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    degreeF = [0] * 21
    i = 0
    
    while i < 21:
    
        degreeF[i] = round((degreeC[i] * 1.8) + 32,2)
        i = i + 1

    print("------------------------------")
    print("Celcius", "          ", "Farenheight")
    print()
    for i in range (0,21,1):
        print(degreeC[i], "C", "                ", degreeF[i], "F")
        print("------------------------------")

    
main()

'''
------------------------------
Celcius            Farenheight

0 C                  32.0 F
------------------------------
1 C                  33.8 F
------------------------------
2 C                  35.6 F
------------------------------
3 C                  37.4 F
------------------------------
4 C                  39.2 F
------------------------------
5 C                  41.0 F
------------------------------
6 C                  42.8 F
------------------------------
7 C                  44.6 F
------------------------------
8 C                  46.4 F
------------------------------
9 C                  48.2 F
------------------------------
10 C                  50.0 F
------------------------------
11 C                  51.8 F
------------------------------
12 C                  53.6 F
------------------------------
13 C                  55.4 F
------------------------------
14 C                  57.2 F
------------------------------
15 C                  59.0 F
------------------------------
16 C                  60.8 F
------------------------------
17 C                  62.6 F
------------------------------
18 C                  64.4 F
------------------------------
19 C                  66.2 F
------------------------------
20 C                  68.0 F
------------------------------
'''

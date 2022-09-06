import math

#number of digits of precision
precision = int(1000000)

target = int(2 * 10 ** (2 * precision))

x = int(10 ** precision)

#In the babylonian method the number of correct digits doubles with each iteration.
#Therefore, since the first number is a 1(which is correct) the number of iterations required is the log base 2 of the precision
for i in range(math.ceil(math.log2(precision))):
    #Babylonian method of approximating square roots
    x = int((x + (target // x)) // 2)

file = open("out.txt", "w")

out = str(x)

file.write(out)

file.close()
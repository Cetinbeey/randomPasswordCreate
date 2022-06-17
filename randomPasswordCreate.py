import random

upperCase="ABCDEFGİJKLMNOPRSTUVYZ"
loverCase="abcdefghijklmnoprstvyz"
numbers="1234567890"
sepecialCar="!'^+%&/()=?_>#${[]}"

top=upperCase+loverCase+numbers+sepecialCar

password="".join(random.sample(top,20))
print("your password created is : "+password)
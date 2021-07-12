txt = "hello, i am pearl"

x = txt.capitalize()

print (x)


txt = "Hello, I am Pearl"

x = txt.casefold()

print(x)


txt = "banana"

x = txt.center(20)

print(x)


txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple")

print(x)


txt = "My name is Pearl"

x = txt.encode()

print(x)


txt = "Hello, I am Pearl."

x = txt.endswith(".")

print(x)


txt = "P\te\ta\tr\tl"

x =  txt.expandtabs(2)

print(x)


txt = "Hello, welcome to my world."

x = txt.find("welcome")

print(x)


txt = "For only {price:.2f} rupees!"
print(txt.format(price = 49))


txt = "Hello, welcome to my world."

x = txt.index("welcome")

print(x)


txt = "Company12"

x = txt.isalnum()

print(x)


txt = "CompanyX"

x = txt.isalpha()

print(x)


txt = "\u0033" #unicode for 3

x = txt.isdecimal()

print(x)


txt = "50800"

x = txt.isdigit()

print(x)


txt = "Demo"

x = txt.isidentifier()

print(x)


txt = "hello world!"

x = txt.islower()

print(x)


txt = "565543"

x = txt.isnumeric()

print(x)


txt = "Hello! Are you #1?"

x = txt.isprintable()

print(x)


txt = "   "

x = txt.isspace()

print(x)


txt = "Hello, And Welcome To My World!"

x = txt.istitle()

print(x)


txt = "I AM PEARL!"

x = txt.isupper()

print(x)


myTuple = ("Pearl", "Ruth", "Rebecca")

x = "#".join(myTuple)

print(x)



txt = "strawberries"

x = txt.ljust(20)

print(x, "are my favorite fruit.")


txt = "Hello I am Pearl"

x = txt.lower()

print(x)


txt = "     strawberries     "

x = txt.lstrip()

print("of all fruits", x, "is my favorite")


txt = "Hello Sam!"
mytable = txt.maketrans("S", "P")
print(txt.translate(mytable))


txt = "I could eat strawberries all day"

x = txt.partition("strawberries")

print(x)


txt = "I like bananas"

x = txt.replace("bananas", "strawberries")

print(x)


txt = "Mi casa, su casa."

x = txt.rfind("casa")

print(x)


txt = "Mi casa, su casa."

x = txt.rindex("casa")

print(x)


txt = "strawberries"

x = txt.rjust(20)

print(x, "is my favorite fruit.")



txt = "I could eat strawberries all day, strawberries are my favorite fruit"

x = txt.rpartition("strawberries")

print(x)


txt = "apple, banana, cherry"

x = txt.rsplit(", ")

print(x)


txt = "     strawberries     "

x = txt.rstrip()

print("of all fruits", x, "is my favorite")


txt = "welcome to the jungle"

x = txt.split()

print(x)


txt = "Thank you for the music\nWelcome to the jungle"

x = txt.splitlines()

print(x)


txt = "Hello, welcome to my world."

x = txt.startswith("Hello")

print(x)


txt = "     banana     "

x = txt.strip()

print("of all fruits", x, "is my favorite")


txt = "Hello My Name Is PEARL"

x = txt.swapcase()

print(x)


txt = "Welcome to my world"

x = txt.title()

print(x)


#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))



txt = "Hello I am Pearl"

x = txt.upper()

print(x)


txt = "50"

x = txt.zfill(10)

print(x)



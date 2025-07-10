y=10
print(y+"Dollars")
# This will raise a TypeError because you cannot concatenate a string and an integer directly.

y=10
print(str(y)+"Dollars") 
#10 Dollars
# This will work because we convert the integer to a string first.

"I'm fine" 
# This is a string literal, and it will be printed as is.
'I\'m fine'
# This is a string literal with an escaped single quote, which allows it to be included in the string.

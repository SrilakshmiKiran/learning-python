#question 4_ expressions
import hello


print(2+3)
print('hello' + 'world')
print(len('spam'))

spam=10
print(spam+ 5)

#expressions vs statements
#expression (has values)
print(2+3)
print(len('hello'))
#statement(do things)
spam=10
print(hello)
# QUESTION 6: BACON PROBLEM
bacon = 20
print(bacon + 1)    # This prints 21 but does NOT change bacon
print(bacon)        # Still 20

bacon = bacon + 1   # This CHANGES bacon
print(bacon)        # Now 21


# QUESTION 7B: STRING MULTIPLICATION
print('spam' * 3)
print(3 * 'spam')
print('A' * 10)


# QUESTION 8: VARIABLE NAMES
eggs = 10
_eggs = 20
# 100 = 30    # Uncomment this to see error

print(eggs)
print(_eggs)


# QUESTION 9: TYPE CONVERSION FUNCTIONS
print(int('42'))
print(int(3.9))
print(float('3.14'))
print(float(5))
print(str(99))
print(str(3.14))

# Q10 FIX
print('I eat ' + str(99) + ' burritos.')


# BONUS: BINARY
print(bin(5))
print(bin(13))
print(hex(255))
print(ord('A'))
print(bin(ord('A')))

s = set()
s.add(20)
s.add(20.0)
s.add("20")  # length of s after these operations?
print(len(s))
print(
    20 == 20.0
)  # If values are same then Python will return true but if one is the integer type and another is string type then Python returns false
# First type conversions will take place in this int type will be coerced or converted to float type
# Then comparison take place
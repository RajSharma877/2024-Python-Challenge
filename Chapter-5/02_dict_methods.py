marks = {"Raj": 85, "Ritiksha": 98, "Gaurav": 84, 0: "Raj"}

# print(marks.items())  # returns a dictionary like view that is list of key value pairs
# print(marks.keys())
# print(marks.values())
# marks.update({"Gaurav": 99, "Harsh": 100})
# print(marks)

print(marks.get("Ritiksha"))
print(
    marks["Ritiksha2"]
)  # There is a difference in direct accessing element in dictionary and get() method
# If the key is not present in dictionary then get() will return None but direct accessing can give KeyError.

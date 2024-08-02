letter = """
Dear <|Name|>,
You are selected!
<|Date|>
"""

print(
    letter.replace("<|Name|>", "Raj").replace("<|Date|>", "<|24th September, 2050|>")
)  # This is known as chaining in which we are checking whether another string is there to replace

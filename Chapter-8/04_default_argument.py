def goodDay(
    name, ending="Thank You"
):  # ending="Thank You" is a default parameter which is passed to the function. When no arguments are passed on runtime then default parameter is passed.
    print(f"Good morning!, {name}")
    print(ending)
    return "Hii"


goodDay("Raj")

# When we provide value then the new value will be returned as an argument passed to the function when the function is called

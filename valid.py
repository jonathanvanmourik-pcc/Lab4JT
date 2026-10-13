def get_integer(prompt):
    #gets_int
    val = 0
    while True:
        try:
            val = int(input(prompt))
            return val
        except:
            print("Invalid integer.")

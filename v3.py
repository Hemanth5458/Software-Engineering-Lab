with open("input_single.txt", "r") as file:
    data = file.readlines()
a = int(data[0].strip())
b = int(data[1].strip())
c = int(data[2].strip())
x = 1
y = a * (x**2) + b * x + c
if y:
    print(f"The model prediction: Probability of rain tomorrow is {y}%")
else:
    print("Some error has occurred, contact developer.")

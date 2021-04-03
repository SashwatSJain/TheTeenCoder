# 6
# mean calculator
# 3 April 2021

data = input(">>")
dataset = data.strip(" ")
dataset = dataset.split(",")

for i in range(0, len(dataset)):
    dataset[i] = int(dataset[i])

y = sum(dataset)
print(y/len(dataset))

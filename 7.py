# 7
# 4 April 2021
# percentage calculator for 5 subjects

s1 = int(input("marks in Subject1:-"))
s2 = int(input("marks in Subject2:-"))
s3 = int(input("marks in Subject3:-"))
s4 = int(input("marks in Subject4:-"))
s5 = int(input("marks in Subject5:-"))

out_of = int(input("maximum marks:"))

print(f"percentage in Subject1 = {s1*100/out_of}%")
print(f"percentage in Subject2 = {s2*100/out_of}%")
print(f"percentage in Subject3 = {s3*100/out_of}%")
print(f"percentage in Subject4 = {s4*100/out_of}%")
print(f"percentage in Subject5 = {s5*100/out_of}%")

overall_percentage = (s1+s2+s3+s4+s5)*(100)/(out_of*5)

print(f"overall percentage : {overall_percentage}%")

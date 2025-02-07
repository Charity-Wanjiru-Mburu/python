weight=int(input("Enter the mass in kg :"))
height=int(input("Enter the height in cm:"))
bmi=weight/(height*height)

if weight>=100:
    weight="overwieght"
elif weight>=75:
    weight="not bad"
elif weight>=50:
    weight="normal weight"
elif weight>=35:
    weight="not enough"
else:
    weight="under weight"
if bmi>=5:
    bmi="overbmi"
elif bmi>=3:
    weight="not bad bmi"
elif bmi>=1:
    bmi="normal bmi"
else:
    bmi="under bmi"
print(f"What is my {weight} and {bmi}")
    
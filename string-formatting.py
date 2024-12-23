#f-string
#inconvinience 
letter = "Hey my name is {0} and iam from {1}"
name = "Mahadev"
country = "India"

print(letter.format(name, country))

#f-string
print(f"Hey my name is {name} and iam from {country}")

#to display as it is:
print(f"Hey my name is {{name}} and iam from {{country}}")

#.2f
txt = "For only {price:.2f} dollars!"
print(txt)
print(txt.format(price = 49.09999))

#example
print(type(f"{2 * 30}"))
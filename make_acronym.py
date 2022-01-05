user_input = input("enter the full meaning of an organization or concept:\r\n").title()
acronym = ''
for i in user_input:
    if i.isupper():
        acronym += i

print(f"The acronym is {acronym}")

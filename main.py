import pandas

data = [
    ["zura", "begadze", 23],
    ["giorgi", "lomize", 24],
    ["ana", "kalabegashvili", 20],
]

df = pandas.DataFrame(data, columns=['name', 'lastname', 'age'], index = ["z", "g", "a"])
df.to_csv('persons.csv')

df.to_excel('persons.xlsx')

results_cvs = pandas.read_csv('persons.csv')
results_exel = pandas.read_excel('persons.xlsx')
# print(results_cvs)
# print(results_exel)

# print(results_exel["name"])
# ages = results_exel["age"]
# lst1 =[]
# for i in ages:
#     if i > 20:
#         lst1.append(i)
# print(lst1)
# დავალაგოთ სახელების სიგრძის მიხედვით
name = pandas.read_csv('persons.csv')['name']
print(name.values)

sort_name = sorted(name.values)
print(sort_name)


import csv

strs = [
    ["Top Gun", "RiskyBusiness", "Minority Report"],
    ["Titanic", "The Revenant", "Inception"],
    ["Training Day", "Man on Fire", "Flight"]
]

with open("3.csv", "w") as f:
    w = csv.writer(f, delimiter=",")
    for str in strs:
        w.writerow(str)
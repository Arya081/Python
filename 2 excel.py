import csv

data_dict = {}
with open("student.csv", mode="r") as stud:
    reader = csv.DictReader(stud)
    for r in reader:
        total = int(r["Sub1"]) + int(r["Sub2"]) + int(r["Sub3"])
        data_dict[r["Roll No"]] = {
            "name": r["Name"],
            "subjects": [int(row["Sub1"]), int(row["Sub2"]), int(row["Sub3"])],
            "total": total
        }

print(data_dict)

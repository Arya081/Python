import csv

with open("stud.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Roll No", "Name", "Sub1", "Sub2", "Sub3"])
    writer.writerow([1, "Arya", 90, 96, 87])
    writer.writerow([2, "alia", 50, 78, 80])

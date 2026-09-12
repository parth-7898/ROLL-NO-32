import csv

results = [['name', 'grade'],
           ['Amit', 'A'],
           ['Jeetom', 'A+'],]
    
with open('grades.csv', 'w',
          newline='') as f:
    writer = csv.writer(f)
    writer.writerows(results)
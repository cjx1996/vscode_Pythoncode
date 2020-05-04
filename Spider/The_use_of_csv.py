import csv

#test the use of csv
with open('E:/code/vscode_Pythoncode/spider/result.csv',encoding='utf-8')as f:
    reader=csv.DictReader(f)
    print(reader)
    for row in reader:
        print(row)
        username=row['name']
        grade=row['grade']
        age=row['age']
        gender=row['gender']
        print(username)
        print(age)
        print(grade)
        print(gender)


#test the write of csv
data=[{'name':'kingname','age':24,'salary':9999},
{'name':'meiji','age':20,'salary':100},
{'name':'小明','age':30,'salary':'N/A'},]
with open('new.csv','w',encoding='utf-8') as f:
    writer=csv.DictWriter(f,['name','age','salary'])
    writer.writeheader()
    writer.writerows(data)
    writer.writerow({'name':'超人','age':999,'salary':0})






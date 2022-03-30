import csv
from csv import reader, writer
from collections import Counter
from collections import defaultdict
import re

#
def generate_covid_result():
    with open('covidTrain.csv', 'r') as f1, open('covidResult.csv', 'w', newline='') as f2:
        next(f1)
        reader = csv.reader(f1)
        writer = csv.writer(f2)
        writer.writerow(['ID', 'age', 'sex', 'city', 'province', 'country', 'latitude', 'longitude', 'date_onset_symptoms', 'date_admission_hospital', 'date_confirmation', 'symptoms'])
        for row in reader:
            row[8] = row[8].replace(row[8], change_date_format(row[8]))
            row[9] = row[9].replace(row[9], change_date_format(row[9]))
            row[10] = row[10].replace(row[10], change_date_format(row[10]))

            if re.search('[-]', row[1]):
                row[1] = row[1].replace(row[1], find_avg_age(row[1]))
            if row[6]=='NaN':
                row[6] = row[6].replace(row[6], most_common_longlat(row[4], 0))
            if row[7]=='NaN':
                row[7] = row[7].replace(row[7], most_common_longlat(row[4], 1))
            if row[3]=='NaN':
                row[3] = row[3].replace(row[3], most_common_city(row[4]))
            if row[11]=='NaN':
                row[11] = row[11].replace(row[11], most_common_symptom(row[4]))
                writer.writerow(row)
            else:
                writer.writerow(row)
                
        writer.writerows(reader)
#everything below is a helper method 
def find_avg_age(string):
    res = re.findall('\d+', string)
    average = round((int(res[0])+int(res[1]))/2)

    return str(average)

#dd.mm.yyyy to mm.dd.yyyy
def change_date_format(string):
    return re.sub(r'(\d{1,2}).(\d{1,2}).(\d{4})', '\\2.\\1.\\3', string)

#used to find either avg lat OR long for a province
#str province #int option
def most_common_longlat(province, option):
     with open('covidTrain.csv', 'r') as f1:
        next(f1)
        reader = csv.reader(f1)
        tot = 0
        count = 0
    
        for row in reader:
            if row[4]==province and option==0 and row[6]!='NaN':
                tot+=(float((row[6])))
                count+= 1
            if row[4]==province and option==1 and row[7]!='NaN':
                tot+=(float((row[7])))
                count+= 1
        if(count == 0):
            return 0
        else: 
            avg = str(round(tot/count, 2))     
            return avg
#         
def most_common_city(province):
    with open('covidTrain.csv', 'r') as f1: 
        next(f1)
        reader = csv.reader(f1)
        cities_in_province = []
        for row in reader:
            if row[4]==province and row[3]!='NaN':
                cities_in_province.append(row[3])
        return most_common(cities_in_province)
#    
def most_common_symptom(province):
    with open('covidTrain.csv', 'r') as f1:
        next(f1)
        reader = csv.reader(f1)
        symptoms_in_province = []
        for row in reader:
            if row[4]==province and row[11]!='NaN':
                lst = re.split('; |, ', row[11])
                symptoms_in_province.extend(lst)
        return most_common(symptoms_in_province)
#
def most_common(lst):
    lst.sort()
    data = Counter(lst)
    return max(lst, key=data.get)


def main():
    generate_covid_result()
main()
    
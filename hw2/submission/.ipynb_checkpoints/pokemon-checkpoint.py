import csv
from csv import reader, writer
from collections import Counter
from collections import defaultdict



####helper functions 

# finds most common element in list 
def most_common(lst):
    lst.sort()
    data = Counter(lst)
    return max(lst, key=data.get)

def calculate_type(weakness):
    with open('pokemonTrain.csv', 'r') as file:
        next(file)
        reader = csv.reader(file)
        type_lst = []
        for row in reader: 
            if row[5]==weakness and row[4]!='NaN':
                type_lst.append(row[5])
        return most_common(type_lst)
    
def calculate_atk():
     with open('pokemonTrain.csv', 'r') as file:
        next(file)
        reader = csv.reader(file)
        tot_over_40 = 0
        count_over_40 = 0
        tot_leq_40 = 0
        count_leq_40 = 0
        for row in reader:
            if row[6] != 'NaN':
                if int((float(row[2]))) > 40:
                    tot_over_40 += int(float((row[6])))
                    count_over_40+=1
                if int((float(row[2]))) <= (40):
                    tot_leq_40 += int(float((row[6])))
                    count_leq_40+=1
        avg_over_40 = round((tot_over_40/count_over_40), 1)
        avg_leq_40 = round((tot_leq_40/count_leq_40), 1)
        return avg_over_40, avg_leq_40

    
def calculate_def():
     with open('pokemonTrain.csv', 'r') as file:
        next(file)
        reader = csv.reader(file)
        tot_over_40 = 0
        count_over_40 = 0
        tot_leq_40 = 0
        count_leq_40 = 0
        for row in reader:
            if row[7] != 'NaN':
                if int((float(row[2]))) > 40:
                    tot_over_40 += int(float((row[7])))
                    count_over_40+=1
                if int((float(row[2]))) <= (40):
                    tot_leq_40 += int(float((row[7])))
                    count_leq_40+=1
        avg_over_40 = round((tot_over_40/count_over_40), 1)
        avg_leq_40 = round((tot_leq_40/count_leq_40), 1)
        return avg_over_40, avg_leq_40
    
def calculate_hp():
     with open('pokemonTrain.csv', 'r') as file:
        next(file)
        reader = csv.reader(file)
        tot_over_40 = 0
        count_over_40 = 0
        tot_leq_40 = 0
        count_leq_40 = 0
        for row in reader:
            if row[8] != 'NaN':
                if int((float(row[2]))) > 40:
                    tot_over_40 += int(float((row[8])))
                    count_over_40+=1
                if int((float(row[2]))) <= (40):
                    tot_leq_40 += int(float((row[8])))
                    count_leq_40+=1
        avg_over_40 = round((tot_over_40/count_over_40), 1)
        avg_leq_40 = round((tot_leq_40/count_leq_40), 1)
        return avg_over_40, avg_leq_40
    
#1.1
def over40():
    with open('pokemonTrain.csv', 'r') as file:
        next(file)
        reader = csv.reader(file)
        firetot = 0
        over40fire = 0
        for row in reader:
            if float(row[2])>=40 and row[4]=='fire':
                over40fire+=1
                firetot+=1
            else:
                if row[4]=='fire':
                    firetot+=1
        percent = round(over40fire/firetot*100)
        print(f"Percentage of fire type Pokemons at or above level 40 = {percent}")
    with open('pokemon1.txt', 'w') as file:
        file.write(f"Percentage of fire type Pokemons at or above level 40 = {percent}")


#1.2 and 1.3

def generate_new_csv():
    atkover_40, atkleq_40 = calculate_atk()
    defover_40, defleq_40 = calculate_def()
    hpover_40, hpleq_40 = calculate_hp()
   
    with open('pokemonTrain.csv', 'r') as f1, open('pokemonResult.csv', 'w', newline='') as f2:
        #next(f1)
        reader = csv.reader(f1)
        writer = csv.writer(f2)


        for row in reader:

            if row[4]=='NaN':
                row[4] = row[4].replace('NaN', calculate_type(row[5]))
            #    
            if row[6]=='NaN' and int(float(row[2]))>40:
                row[6] = row[6].replace('NaN', str(atkover_40))
            if row[6]=='NaN' and int(float(row[2]))<=40:
                row[6] = row[6].replace('NaN', str(atkleq_40))
            #    
            if row[7]=='NaN' and int(float(row[2]))>40:
                row[7] = row[7].replace('NaN', str(defover_40))
            if row[7]=='NaN' and int(float(row[2]))<=40:
                row[7] = row[7].replace('NaN', str(defleq_40))                   
            if row[8]=='NaN' and int(float(row[2]))>40:
                row[8] = row[8].replace('NaN', str(hpover_40))
            if row[8]=='NaN' and int(float(row[2]))<=40:
                row[8] = row[8].replace('NaN', str(hpleq_40))                 
                writer.writerow(row)
            else:
                writer.writerow(row)
        writer.writerows(reader)
        
#1.4
def type_to_personality():
    with open('pokemonResult.csv', 'r') as f1:
        next(f1)
        reader = csv.reader(f1)
        
        d = {}
        
        for row in reader:
            pokemon_personality = row[3]
            pokemon_type = row[4]
            try:
                d[pokemon_type].append(pokemon_personality)
            except:
                d[pokemon_type]=[pokemon_personality]
        
        res = dict()
        for key in sorted(d):
            res[key] = sorted(d[key])
            
        res_keys = list(res.keys())
        res_values = list(res.values())

    with open('pokemon4.txt', 'w') as f2:
        print("Pokemon type to personality mapping: \n")
        f2.write("Pokemon type to personality mapping: \n")
        for ind in range(0, len(res_keys)):
            print("      " + res_keys[ind] + ": " + " ".join(res_values[ind]) + "\n")
            f2.write("      " + res_keys[ind] + ": " + " ".join(res_values[ind]) + "\n")


#1.5
def avg_hp_over3():
    with open('pokemonResult.csv', 'r') as f1:
        next(f1)
        reader = csv.reader(f1)
        totalHp = 0
        count = 0
        for row in reader:
            if int(float(row[9]))>=3:
                totalHp+=int(float(row[8]))
                count+=1
        avg = round(totalHp/count)
    with open('pokemon5.txt', 'w') as f2:
        print("Average hit point for Pokemons of stage 3.0 = " + str(avg))
        f2.write("Average hit point for Pokemons of stage 3.0 = ")
        f2.write(str(avg))


def main(): 
    # print('1')
    over40()
    # print('2')
    generate_new_csv()
    # print('3')
    type_to_personality()
    # print('4')
    avg_hp_over3()
    
    
main()
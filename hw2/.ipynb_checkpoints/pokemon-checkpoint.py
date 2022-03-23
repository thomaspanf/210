import csv
from csv import reader, writer
from collections import Counter



####helper functions 

# finds most common element in list 
def most_common(lst):
    lst.sort()
    data = Counter(lst)
    return max(lst, key=data.get)

# copies csv and writes to new csv file, removing whitespaces
def copy_csv(csv_string):
    with open(csv_string) as input, open('pokemonResult.csv', 'w') as output:
        non_blank = (line for line in input if line.strip())
        output.writelines(non_blank)

def calculate_weakness():
    with open('pokemonTrain.csv', 'r') as file:
        next(file)
        reader = csv.reader(file)
        
        #calculate weakness weighting
        waterweakness = []
        fightingweakness = []
        flyingweakness = []
        fireweakness = []
        poisonweakness = []
        groundweakness = []
        
        for row in reader:
            if row[5]=='water' and row[4]!='NaN':
                 waterweakness.append(row[4])  
            if row[5]=='fighting' and row[4]!='NaN':
                fightingweakness.append(row[4])
            if row[5]=='flying' and row[4]!='NaN':
                flyingweakness.append(row[4])
            if row[5]=='fire' and row[4]!='NaN':
                fireweakness.append(row[4])
            if row[5]=='poison' and row[4]!='NaN':
                poisonweakness.append(row[4])
            if row[5]=='ground' and row[4]!='NaN':
                groundweakness.append(row[4])
                
                
                
        water = most_common(waterweakness)
        fighting = most_common(fightingweakness)
        flying = most_common(flyingweakness)
        fire = most_common(fireweakness)
        poison = most_common(poisonweakness)
        ground = most_common(groundweakness)
        
    return water, fighting, flying, fire, poison, ground

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
        total = 0
        over40 = 0
        for row in reader:
            total+=1
            if float(row[2])>=40:
                over40+=1
        percent = round(over40/total*100)
        print(f"Percentage of fire type Pokemons at or above level 40 = {percent}")
    with open('pokemon1.txt', 'w') as file:
        file.write(f"Percentage of fire type Pokemons at or above level 40 = {percent}")

#1.1 and 1.2
def generate_new_csv():
    water, fighting, flying, fire, poison, ground = calculate_weakness()
    atkover_40, atkleq_40 = calculate_atk()
    defover_40, defleq_40 = calculate_def()
    hpover_40, hpleq_40 = calculate_hp()
    
    
    with open('pokemonTrain.csv', 'r') as f1, open('pokemonResult.csv', 'w') as f2:
        #next(f1)
        reader = csv.reader(f1)
        writer = csv.writer(f2)

        for row in reader:
            print(row)
            if row[4]=='NaN' and row[5]=='water':
                replaced = row[4].replace('NaN',water)  
                row[4] = replaced
            if row[4]=='NaN' and row[5]=='fighting':
                replaced = row[4].replace('NaN',fighting)  
                row[4] = replaced                 
            if row[4]=='NaN' and row[5]=='flying':
                replaced = row[4].replace('NaN',flying)  
                row[4] = replaced                 
            if row[4]=='NaN' and row[5]=='fire':
                replaced = row[4].replace('NaN',fire)  
                row[4] = replaced                 
            if row[4]=='NaN' and row[5]=='poison':
                replaced = row[4].replace('NaN',poison)  
                row[4] = replaced                 
                writer.writerow(row)
            if row[4]=='NaN' and row[5]=='ground':
                replaced = row[4].replace('NaN',ground)  
                row[4] = replaced 
            #
            if row[6]=='NaN' and int(float(row[2]))>40:
                replaced = row[6].replace('NaN', str(atkover_40))
                row[6] = replaced
            if row[6]=='NaN' and int(float(row[2]))<=40:
                replaced = row[6].replace('NaN', str(atkleq_40))
                row[6] = replaced

            #    
            if row[7]=='NaN' and int(float(row[2]))>40:
                replaced = row[7].replace('NaN', str(defover_40))
                row[7] = replaced
            if row[7]=='NaN' and int(float(row[2]))<=40:
                replaced = row[7].replace('NaN', str(defleq_40))       
                row[7] = replaced            
            if row[8]=='NaN' and int(float(row[2]))>40:
                replaced = row[8].replace('NaN', str(hpover_40))
                row[8] = replaced
            if row[8]=='NaN' and int(float(row[2]))<=40:
                replaced = row[8].replace('NaN', str(hpleq_40))                 
                row[8] = replaced
                writer.writerow(row)
            else:
                writer.writerow(row)
        writer.writerows(reader)
        non_blank = (line for line in input if line.strip())
        f2.writelines(non_blank)


def main(): 
    
    print("testtt")
    over40()
    generate_new_csv()
    
    
main()
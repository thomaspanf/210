import csv



####helper functions 

# finds most common element in list 
def most_common(lst):
    return max(set(lst), key=lst.count)

# copies csv and writes to new csv file
def copy_csv(csv_string):
    with open('pokemonTrain.csv') as input, open('pokemonResult.csv', 'w') as output:
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
        for row in reader:
            if row[5]=='water' and row[4]!='NaN':
                 waterweakness.append(row[4])  
            if row[5]=='fighting' and row[4]!='NaN':
                fightingweakness.append(row[4])
            if row[5]=='flying' and row[4]!='NaN':
                flyingweakness.append(row[4])
            if row[5]=='fire' and row[4]!='NaN':
                fireweakness.append(row[4])
                
        water = most_common(waterweakness)
        fighting = most_common(fightingweakness)
        flying = most_common(flyingweakness)
        fire = most_common(fireweakness)
        
    return water, fighting, flying, fire

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




def main(): 
    
    print("testtt")
    over40()
    
main()
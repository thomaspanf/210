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
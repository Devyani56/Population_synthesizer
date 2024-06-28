#This program synthesizes data for 50000 individuals based on the representative sample
#Author: Devyani Remulkar
import csv
import random
# Define the file path
file_path = 'Data.csv'

# Open the CSV file
with open(file_path, 'r') as csv_file:
    # Create a CSV reader object
    csv_reader = csv.reader(csv_file)
    #initialise frequencies to 0
    male =0
    female=0
    below_twenty_two=0
    bet_twenty_two_sixty=0
    above_sixty =0
    no_formal_edu=0
    primary_edu =0
    sec_edu=0
    grad_and_abv=0
    # Skip the header row
    next(csv_reader)
    #Count frequencies in the given data
    for row in csv_reader:
        Sex=int(row[0])
        Age_group=int(row[1])
        Highest_education_level=int(row[2])
        if(Sex==1):
            male+=1
        else:
            female+=1
        
        if(Age_group==1):
            below_twenty_two+=1
        elif(Age_group==2):
            bet_twenty_two_sixty +=1
        else:
            above_sixty+=1

        if(Highest_education_level==0):
            no_formal_edu+=1
        elif(Highest_education_level==1):
            primary_edu+=1
        elif(Highest_education_level==2):
            sec_edu+=1
        else:
            grad_and_abv +=1

#Calculating percentages from the given data
male_pc = male/200
female_pc=female/200
below_twenty_two_pc=below_twenty_two/200
bet_twenty_two_sixty_pc=bet_twenty_two_sixty/200
above_sixty_pc=above_sixty/200
no_formal_edu_pc=no_formal_edu/200
primary_edu_pc=primary_edu/200
sec_edu_pc=sec_edu/200
grad_and_abv_pc=grad_and_abv/200

# Synthesize population with 50000 individuals based on representative sample
Male =0
Female=0
Below_twenty_two=0
Bet_twenty_two_sixty=0
Above_sixty =0
No_formal_edu=0
Primary_edu =0
Sec_edu=0
Grad_and_abv=0
for i in range(0,50000):
    sex = random.random()
    if(sex<=male_pc):
        Male+=1
    else:
        Female+=1
    
    age_group = random.random()
    if(age_group<=below_twenty_two_pc):
        Below_twenty_two+=1
    elif(age_group<=(1-above_sixty_pc)):
        Bet_twenty_two_sixty+=1
    else:
        Above_sixty+=1

    edu_level = random.random()
    if(edu_level<no_formal_edu_pc):
        No_formal_edu+=1
    elif(edu_level<= (no_formal_edu_pc+primary_edu_pc)):
        Primary_edu+=1
    elif(edu_level<=(1-grad_and_abv_pc)):
        Sec_edu+=1
    else:
        Grad_and_abv+=1

# Variables for which frequencies need to be computed
variables_of_interest = ["Sex","Age_group","Highest_education_level"]

frequencies = {}
frequencies["Sex"]={"Male":Male,"Female":Female}
frequencies["Age_group"]={"Below 22 years":Below_twenty_two,"22-60 years":Bet_twenty_two_sixty,"Above 60 years":Above_sixty}
frequencies["Highest_education_level"]={"No formal education":No_formal_edu,"Primary education":Primary_edu,"Secondary education":Sec_edu,"Graduation and above":Grad_and_abv}
# Save frequencies to a .txt file
output_file = "population_frequencies.txt"
with open(output_file, "w") as f:
    for var in variables_of_interest:
        f.write(f"Variable: {var}\n")
        for value, frequency in frequencies[var].items():
            f.write(f"{value}: {frequency}\n")
        f.write("\n")

print("Frequencies saved to", output_file)



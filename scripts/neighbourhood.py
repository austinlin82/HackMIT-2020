import pandas as pd
import os

set_abs_path = os.path.abspath("datasets/Toronto_Neighbourhood.csv")
danger_write = os.path.abspath("scripts/neighbourhood_names/danger.txt")
safety_write = os.path.abspath("scripts/neighbourhood_names/safety.txt")

#due to VSCode pylint limitations, must use absolute path, change in release or when using locally
set_abs_path = set_abs_path.replace('\\', '/')
neighbourhoods = pd.read_csv(set_abs_path)
#C:/Users/lavao/Documents/GitHub/HackMIT-2020/datasets/Toronto_Neighbourhood.csv

neighbourhoods.drop(["Neighbourhood ID"], axis = 1, inplace = True)
#neighbourhoods.drop(["Missing Address/Postal Code"], axis = 0, inplace = True)

#higher count neighbourhood, sorted by descending
higher_count = neighbourhoods.sort_values(by=['Case Count'], ascending=False)
danger_zone = higher_count['Neighbourhood Name'].head(n=6).tolist()

#list comprehension, using lists in place of df
danger_zone[:] = [x for x in danger_zone if "Missing Address/Postal Code" not in x]

#slimming
while (len(danger_zone) > 5):
    del (danger_zone[-1])

#opens absolute path danger.txt in write mode and prints each item of list
with open(danger_write, "w") as output_file:
   for item in danger_zone:
       output_file.write(str(item + '\n'))

#lower count neighbourhood, sorted by ascending
lower_count = neighbourhoods.sort_values(by=['Case Count'], ascending=True)
safety_zone = lower_count['Neighbourhood Name'].head(n=6).tolist()
safety_zone[:] = [x for x in safety_zone if "Missing Address/Postal Code" not in x]

while (len(safety_zone) > 5):
    del (safety_zone[-1])

with open(safety_write, "w") as output_file:
   for item in safety_zone:
       output_file.write(str(item + '\n'))

if __name__ == '__main__':
    print(danger_zone)
    print(safety_zone)
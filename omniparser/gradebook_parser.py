import pandas
import os
 

#def calculate_average_grade_from_csv(my_csv_filepath):
df = pandas.read_csv('/Users/richiebubbs/Downloads/GitHub/omniparser-starter-py/data/gradebook_2019.csv')
rows = df.to_dict()

grades = [r["final_grade"] for r in rows]
avg_grades = sum(grades)/len(grades)
print(avg_grades)


#calculate_average_grade_from_csv(my_csv_filepath)




if __name__ == "__main__":

    print("PARSING SOME EXAMPLE GRADEBOOK FILES HERE...")

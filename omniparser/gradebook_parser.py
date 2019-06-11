import pandas
import os
import statistics
 

def calculate_average_grade_from_csv(my_csv_filepath):
    df = pandas.read_csv(my_csv_filepath)
    rows = df.to_dict("records")

    grades = [r["final_grade"] for r in rows]
    avg_grade = statistics.mean(grades)

    print(avg_grade)

df =pandas.read_csv("/Users/richiebubbs/Downloads/GitHub/omniparser-starter-py/data/gradebook_2018.csv")

calculate_average_grade_from_csv("/Users/richiebubbs/Downloads/GitHub/omniparser-starter-py/data/gradebook_2018.csv")

breakpoint()

#calculate_average_grade_from_csv(my_csv_filepath)




if __name__ == "__main__":

    print("PARSING SOME EXAMPLE GRADEBOOK FILES HERE...")

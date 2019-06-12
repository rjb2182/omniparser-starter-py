import pandas
import os
import statistics
 

#def calculate_average_grade_from_csv(my_csv_filepath):
#    df = pandas.read_csv(my_csv_filepath)
#    rows = df.to_dict("records")
#
#    grades = [r["final_grade"] for r in rows]
#    avg_grade = statistics.mean(grades)
#
#    print(avg_grade)

#df =pandas.read_csv("/Users/richiebubbs/Downloads/GitHub/omniparser-starter-py/data/gradebook_2018.csv")

#calculate_average_grade_from_csv("/Users/richiebubbs/Downloads/GitHub/omniparser-starter-py/data/gradebook_2018.csv")

#breakpoint()

#calculate_average_grade_from_csv(my_csv_filepath)

## JSON VERSION
##
#
def calculate_average_grade_from_json(gradebook_filepath):
    gradebook_filepath = os.path.join(os.path.dirname(__file__), "Downloads", "GitHub", "data", "gradebook_2019.json")
    grades = [r["final_grade"] for r in rows]
    avg_grade = statistics.mean(grades)
    print(avg_grade)
    
breakpoint()

#def test_calculate_average_grade_from_json():
#    gradebook_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "gradebook_2019.json")
#    assert calculate_average_grade_from_json(gradebook_filepath) == 90.64
#
#    prev_gradebook_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "gradebook_2018.json")
#    assert calculate_average_grade_from_json(prev_gradebook_filepath) == 83.64
#```


if __name__ == "__main__":

    print("PARSING SOME EXAMPLE GRADEBOOK FILES HERE...")

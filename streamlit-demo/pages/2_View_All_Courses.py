import streamlit as st
import pandas as pd
import json
import os

# Get absolute path to the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Go up to the parent folder and then into /data
data_path = os.path.join(script_dir, '..', 'data', 'courses-full.json')

# Normalize the path (helps avoid issues on Windows/macOS/Linux)
filepath = os.path.abspath(data_path)

# Load the JSON file
with open(filepath, 'r') as file:
    json_string = file.read()
    dict_of_courses = json.loads(json_string)
    print(dict_of_courses)

# Extract the value of the `dict_of_courses` dictionary
# If you are not sure what the dictionary looks like, you can print it out
list_of_dict = []
for course_name, details_dict in dict_of_courses.items():
    list_of_dict.append(details_dict)

# display the `dict_of_course` as a Pandas DataFrame
df = pd.DataFrame(list_of_dict)
df
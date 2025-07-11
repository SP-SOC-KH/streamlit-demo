import json

filepath = '../data/courses-full.json'
# filepath = 'courses-full.json'

# dict_of_courses = {}

with open(filepath, 'r') as file:
    json_string = file.read()
    dict_of_courses = json.loads(json_string)


def get_course_details(list_of_category_n_course: list[dict]):
    course_names_list = []
    for x in list_of_category_n_course:
        course_names_list.append(x.get('course_name')) # x["course_name"]
    print(course_names_list)
    list_of_course_details = []
    for course_name in course_names_list:
        list_of_course_details.append(dict_of_courses.get(course_name))
    return list_of_course_details

# This is a sample input to test the function
sample_input = [{'category': 'Programming and Development','course_name': 'Web Development Bootcamp'},
                {'category': 'Data Science & AI', 'course_name': 'Data Science with Python'},
                {'category': 'Data Science & AI', 'course_name': 'AI and Machine Learning for Beginners'}]


product_details = get_course_details(sample_input)
print(product_details)
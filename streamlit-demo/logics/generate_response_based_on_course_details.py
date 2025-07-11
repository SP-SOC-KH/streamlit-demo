import sys, os, json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from helper_functions import llm # <--- This is the helper function that we have created 



def generate_response_based_on_course_details(user_message, product_details):
    delimiter = "####"

    system_message = f"""
    Follow these steps to answer the customer queries.
    The customer query will be delimited with a pair {delimiter}.

    Step 1:{delimiter} If the user is asking about course, \
    understand the relevant course(s) from the following list.
    All available courses shown in the json data below:
    {product_details}

    Step 2:{delimiter} Use the information about the course to \
    generate the answer for the customer's query.
    You must only rely on the facts or information in the course information.
    Your response should be as detail as possible and \
    include information that is useful for customer to better understand the course.

    Step 3:{delimiter}: Answer the customer in a friendly tone.
    Make sure the statements are factually accurate.
    Your response should be comprehensive and informative to help the \
    the customers to make their decision.
    Complete with details such rating, pricing, and skills to be learnt.
    Use Neural Linguistic Programming to construct your response.

    Use the following format:
    Step 1:{delimiter} <step 1 reasoning>
    Step 2:{delimiter} <step 2 reasoning>
    Step 3:{delimiter} <step 3 response to customer>

    Make sure to include {delimiter} to separate every step.
    """

    messages =  [
        {'role':'system',
         'content': system_message},
        {'role':'user',
         'content': f"{delimiter}{user_message}{delimiter}"},
    ]

    response_to_customer = llm.get_completion_by_messages(messages)
    response_to_customer = response_to_customer.split(delimiter)[-1]
    return response_to_customer

# Testing the function to make sure it works
# This part should not be included as part of the Python script.

user_query = f"""Do you have any coding or data related courses that are under $1000 """

response = generate_response_based_on_course_details(user_query, product_details)
print(response)
import streamlit as st
from bs4 import BeautifulSoup
import requests
import google.generativeai as genai

# Define a function that takes a URL as input and returns some output
def process_url(url):
    response = requests.get(url)


    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Initialize an empty dictionary to store the extracted text
        extracted_text = {
            'h1': [],
            'h2': [],
            'p': [],
            'li': []
        }
        
        # Find all <h1> tags and store their text in the dictionary
        h1_tags = soup.find_all('h1')
        for h1_tag in h1_tags:
            extracted_text['h1'].append(h1_tag.text.strip())
        
        # Find all <h2> tags and store their text in the dictionary
        h2_tags = soup.find_all('h2')
        for h2_tag in h2_tags:
            extracted_text['h2'].append(h2_tag.text.strip())
        
        # Find all <p> tags and store their text in the dictionary
        p_tags = soup.find_all('p')
        for p_tag in p_tags:
            extracted_text['p'].append(p_tag.text.strip())
        
        # Find all <ul> and <ol> tags
        list_tags = soup.find_all(['ul', 'ol'])
        for list_tag in list_tags:
            # Find all <li> tags within the list and store their text in the dictionary
            list_items = list_tag.find_all('li')
            for list_item in list_items:
                extracted_text['li'].append(list_item.text.strip())
        
        # Print the extracted text stored in the dictionary
       
    else:
       
        print("Failed to retrieve the webpage")
    genai.configure(api_key='AIzaSyB6GypDXF3xZFQrbgx9G3uKRSIR0EAmj_8')

# Initialize the Generative Model
    model = genai.GenerativeModel('gemini-pro')
    prompt="""I am giving you the data scrapped from a website that describes it's services ,the data is structured in the following way ({h1:" " ,h2:" ",p:" " ,li:" "}) i want you to go through it can understand what exactly the product does and give a short description for that i can use for ecommerce website,the output format should be "Product Name:\nProduct Description"keep product name and description in seperate paras.Talk more about the usefulness of the product. Keep it 150 words at max.The data is as follows ","""  # replace {text} with the text you want to translate
 

    request=prompt+str(extracted_text)
    # Generate content
    response = model.generate_content(request)

    # Print the generated content
    
        
    return response.text

def main():
    
    st.title("Generate Product Description")
    
    # Text Input for URL
    url_input = st.text_input('Enter a URL', '')
    
    # Button to trigger processing
    if st.button('Process URL'):
        # Call the process_url function with the input URL
        output = process_url(url_input)
        # Display the output
        st.write(output)

if __name__ == '__main__':
    main()
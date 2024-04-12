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
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    genai.configure(api_key=GOOGLE_API_KEY)
   

# Initialize the Generative Model
    model = genai.GenerativeModel('gemini-pro')
    prompt="""Given the structured data containing descriptions of services from a website ({h1:" " ,h2:" ",p:" " ,li:" "}), generate short descriptions for each product that can be used for an ecommerce website. Some example outputs are given below:
        Product Description:ChatRecruit™ is the leading post-application chat management platform that empowers recruiting and hiring teams to streamline communication and enhance the candidate experience. With its intuitive interface and secure platform, it enables recruiters to seamlessly bridge the communication gap from the initial application stage to onboarding. ChatRecruit™ seamlessly integrates with leading ATS, CRM, and VMS systems, eliminating siloed systems and streamlining communication flows. By providing tailored communication solutions for complex brands, it helps organizations reduce the risk of losing top talent and improve recruitment velocity.
       
        Product Description:Litzia Managed IT Services offers a comprehensive suite of solutions to help businesses navigate the complexities of modern technology. With a dedicated tech support staff available Monday through Friday, businesses can access expert guidance and support whenever they need it. Litzia's proactive monitoring tools provide network protection, uptime, and critical maintenance, ensuring minimal downtime and maximum productivity. Whether it's network implementation and maintenance, vendor management, or Virtual Chief Information Officer (VCIO) services, Litzia tailors its offerings to meet the unique needs of each business. By partnering with Litzia, businesses can leverage technology to increase efficiency, optimize operations, and achieve their strategic goals.
       
        Product Description:
Aim Agency, a renowned London-based PR agency, offers bespoke PR solutions tailored to elevate the profiles, refine the messaging, and expand the reach of its clientele. With a strategic approach to each brief, Aim Agency meticulously determines the most potent communication channels and PR messages to effectively engage target audiences. The agency's expertise spans a wide range of industries, catering to CEOs, senior executives, founders, entrepreneurs, and high-net-worth individuals, ensuring the tailored delivery of impactful PR campaigns. By leveraging Aim Agency's services, clients gain access to a team of experienced professionals dedicated to enhancing their visibility, establishing a strong brand identity, and driving meaningful connections with their target audiences.
        give each product description, highlighting its key features and benefits in approximately 150 words.the input is as follows: """  # replace {text} with the text you want to translate
 
    print(extracted_text)
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

#
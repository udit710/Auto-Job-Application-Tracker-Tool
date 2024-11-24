import os
import config
import google.generativeai as genai

def summarize_description(description):
    
    # get the instructions to pass to the model
    instructions = os.getenv("INSTRUCTIONS")
    
    # Initialize the model
    genai.configure(api_key=os.getenv("GEN_API_KEY"))
    model = genai.GenerativeModel("gemini-1.5-flash")
    
    # Use the model to get essential information from the job description
    response = model.generate_content(instructions+description)
    
    # with open("job_description.txt", "w") as file:
    #     file.write(response.candidates[0].content.parts[0].text)
    
    # print(response.candidates[0].content.parts[0].text)
        
    # file.close()
    
    return response.candidates[0].content.parts[0].text

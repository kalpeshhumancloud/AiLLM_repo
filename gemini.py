import os
import google.generativeai as genai
google_api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=google_api_key)

model = genai.GenerativeModel('gemini-2.0-flash')

# Prompt
prompt = "give an interview quetions for java 4 years of experience candidate " \
"give me just 5 interview quetions in JSON format"

# Get response

response = model.generate_content(prompt)

# Print response
print("######################### Response Recived #################################")
print(response.text)

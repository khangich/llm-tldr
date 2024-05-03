import json
import openai
from openai import OpenAI
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.getenv("OPENAI_API_KEY"),
)

#chain of thought example
def find_lcm(numbers):
    prompt = f"Explain the steps to find the least common multiple (LCM) of these numbers: {numbers} and provide the answer in JSON format with your thoughts and the final answer.\n\n"
    prompt += "Step 1: Identify the greatest number among the given numbers.\n"
    prompt += "Step 2: Start with the greatest number as a potential LCM.\n"
    prompt += "Step 3: Check if this potential LCM is divisible by all the other numbers.\n"
    prompt += "Step 4: If it is divisible by all, that's the LCM. If not, increase the potential LCM by the greatest number and repeat step 3.\n"
    prompt += "Step 5: Continue this process until the LCM is found.\n\n"
    prompt += "Using this method, calculate the LCM and format your response as a JSON object with keys 'thoughts' and 'answer'."

    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=250,
        temperature=0.3,
        n=1,
        stop=None
    )
    response = chat_completion.choices[0].message  # Corrected line
    response_json = json.loads(response.content)
    print(response_json)

    return response_json['answer']

# Example use
numbers = [12, 15, 18]
lcm_result = find_lcm(numbers)
print("Calculated LCM:", lcm_result)

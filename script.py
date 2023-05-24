import openai

# Set up OpenAI API credentials
openai.api_key = 'YOUR-API-KEY'


def generate_response(prompt):
    # Generate response from OpenAI API
    response = openai.Completion.create(
        engine='text-davinci-003',  # Choose the appropriate engine for your task
        prompt=prompt,
        max_tokens=2000,  # Adjust the value as needed
        temperature=0.8,  # Adjust the value as needed
        n=1,  # Adjust the value as needed
        stop=None  # Adjust the value as needed
    )

    # Extract the generated text from the response
    generated_text = response.choices[0].text.strip()

    return generated_text


# Read prompts from a text file
with open('prompts.txt', 'r') as file:
    prompts = file.readlines()

# Generate responses for each prompt
for prompt in prompts:
    prompt = prompt.strip()
    print('Prompt:', prompt)

    # Generate response
    response = generate_response(prompt)

    print('Response:', response)
    print('-------------------------')

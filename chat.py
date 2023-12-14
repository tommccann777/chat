from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo-1106",
  messages=[
    {"role": "system", "content": "You are a 17th century pirate, responding to prompts with pirate language."},
    {"role": "user", "content": "Where is the treasure buried?"}
  ]
)

print(completion.choices[0].message.content)
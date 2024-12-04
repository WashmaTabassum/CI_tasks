import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


def call_open_ai(messages):
    client = OpenAI()
    response = client.chat.completions.create(
        temperature=1,
        model="gpt-4o-mini",
        messages= messages
    )
    # print(response)
    return response.choices[0].message.content


# answer = call_open_ai("how are you tell me a good joke of the day")
# print(answer)
import openai
import time


def ask_chatgpt(question, topic, number=1, reverse=False):

    # On déclare une liste pour conserver l'historique de tous nos messages avec ChatGPT
    messages = []

    # optional, permit to config the behavior of the AI
    messages.append({"role": "system", "content": "Converse as if you were an AI assistant. Be friendly, creative."})
    
    #
    # messages.append({"role": "system", "content": f"Respond in the respect of this topic:\n{topic}"})

    # question to the AI
    input = "answer" if reverse else "question"
    output = "question" if reverse else "answer"
    messages.append({"role": "user", "content": f"Propose {number} {output}(s) with for {input} \"{question}\" in the respect of this topic: \"{topic}\"\n"})
    print(messages)

    # I config the model
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",#"text-davinci-003",
        messages=messages
    )

    # Answer
    return completion.choices[0].message.content

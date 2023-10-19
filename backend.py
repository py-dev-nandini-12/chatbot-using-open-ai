import openai

class Chatbot():
    def __init__(self):
        openai.api_key = "your api key"
    
    def get_response(self,user_input):
        response = openai.Completion.create(
            engine = "text-davinci-003",
            prompt = user_input,
            max_tokens =1024,
            temperature = 0.5
        )
        message = response.choices[0].text
        return message
    
if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("write a joke about birds")
    print(response)


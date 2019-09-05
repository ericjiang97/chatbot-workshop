import dialogflow_v2 as dialogflow
import os


def chatbot_with_dialogflow():
    running = True
    while running:
        text = str(input('Me: '))
        if(text == 'bye'):
            running = False
        else:
            nlp_response, nlp_intent = detect_intent_texts(
                "deep-dfcuda", "123", [text], "en-US")
            try:
                print(f"Chatbot: {nlp_response}")
            except:
                print("idk")


def detect_intent_texts(project_id, session_id, texts, language_code):
    os.environment['GOOGLE_APPLICATION_CREDENTIALS'] = './keyfiles/deep-dfcuda-5f57ef20d57c.json'

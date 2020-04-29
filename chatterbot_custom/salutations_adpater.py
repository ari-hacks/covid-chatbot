from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement
import logging
import random

logging.basicConfig(level=logging.INFO)

class SalutationsAdapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
     super().__init__(chatbot, **kwargs)

    def can_process(self,statement):
        words = ['Hi', 'Howdy', 'Hello','until next time', 'bye','ciao', 'adios','its been real']
        if any(x.lower() for x in words):
           return True
        else:
           return False

    def process(self, input_statement, additional_response_selection_parameters):

        user_input = input_statement.text.lower()
        if 'hi' or 'howdy' or 'hello' in user_input:
             #add help response
            responses = ["""Hello \U0001F31F""", "Hi there!", "How are you","Hi, My name is Rona"]
            response_statement = Statement(random.choice(responses))
            response_statement.confidence = .85
            logging.info(response_statement)
            return response_statement
   
        elif 'bye' or 'ciao' or 'adios' or 'its been real' in user_input:
             #add help response
            responses = ["""Bye \U0001F31F""", "Chat later!", "Have a good one"]
            response_statement = Statement(random.choice(responses))
            response_statement.confidence = .95
            logging.info(response_statement)
            return response_statement
        else: 
            response_statement.confidence = 0
        return response_statement
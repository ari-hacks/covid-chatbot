from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement
import logging
from app.services.stats_service import getUsStats, getUkStats
from app.services.news_service import getNews
import random

logging.basicConfig(level=logging.INFO)


class MyLogicAdapter(LogicAdapter):


    def can_process(self, statement):

        input_words = ['uk', 'us', 'covid','stats','uk confirmed','uk deaths','uk recovered','uk critical',
                'us confirmed','us deaths','us recovered','us critical','all','good news', 'good covid news',
                'tell me someting good','coronavirus positive news','covid positive news',
                'Hi', 'Howdy', 'Hello','until next time', 'bye','ciao', 'adios','its been real'
                ]
        if any(x.lower() for x in input_words):
            return True
        else:
            return False


    def process(self, input_statement, additional_response_selection_parameters):

        user_input = input_statement.text.lower()
        uk_response = getUkStats()
        us_response = getUsStats()
        news_response = getNews()
        
        if 'uk confirmed' in user_input:
            confirmed = uk_response[0].get("confirmed", "")
            response_statement = Statement(text='Confirmed Uk Cases {}'.format(confirmed))
            response_statement.confidence = 1
            logging.info(response_statement)     
            return response_statement

        elif  'uk deaths' in user_input:
            deaths = uk_response[0].get("deaths", "")
            response_statement = Statement(text='Confirmed Uk Deaths {}'.format(deaths))
            response_statement.confidence = 1
            logging.info(response_statement)     
            return response_statement

        elif 'uk recovered' in user_input:
            recovered = uk_response[0].get("recovered", "")
            response_statement = Statement(text='Recovered Uk Cases {}'.format(recovered))
            response_statement.confidence = 1
            logging.info(response_statement)     
            return response_statement
    
        elif  'uk critical' in user_input:
            critical = uk_response[0].get("critical", "")
            response_statement = Statement(text='Critical Uk Cases {}'.format(critical))
            response_statement.confidence = 1
            logging.info(response_statement)     
            return response_statement
    
        elif  'us confirmed' in user_input:
            confirmed = us_response[0].get("confirmed", "")
            response_statement = Statement(text='Confirmed Us Cases {}'.format(confirmed))
            response_statement.confidence = 1
            logging.info(response_statement)     
            return response_statement

  
        elif  'us deaths' in user_input:
            deaths = us_response[0].get("deaths", "")
            response_statement = Statement(text='Confirmed Us Deaths {}'.format(deaths))
            response_statement.confidence = 1
            logging.info(response_statement)     
            return response_statement

        elif  'us recovered' in user_input:
            recovered = us_response[0].get("recovered", "")
            response_statement = Statement(text='Recovered Us Cases {}'.format(recovered))
            response_statement.confidence = 1
            logging.info(response_statement)     
            return response_statement
    
        elif  'us critical' in user_input:
            critical = us_response[0].get("critical", "")
            response_statement = Statement(text='Critical Us Cases {}'.format(critical))
            response_statement.confidence = 1
            logging.info(response_statement)     
            return response_statement
        
        elif 'all' and 'us' in user_input:
            response_statement = Statement(text='United States Stats: {}'.format(
                '\nconfirmed: ' + str(us_response[0].get("confirmed", "")) +
                '\nrecovered: ' + str(us_response[0].get("recovered", "")) +
                '\ncritical: '+ str(us_response[0].get("critical", "")) +
                '\ndeaths: '+  str(us_response[0].get("deaths", "")) 
            ))
            response_statement.confidence = 1
            logging.info(response_statement)     
            return response_statement
        
        elif 'all' and 'uk' in user_input:
            response_statement = Statement(text='United Kingdom Stats: {}'.format(
                '\nconfirmed: ' + str(uk_response[0].get("confirmed", "")) +
                '\nrecovered: ' + str(uk_response[0].get("recovered", "")) +
                '\ncritical: '+ str(uk_response[0].get("critical", "")) +
                '\ndeaths: '+  str(uk_response[0].get("deaths", "")) 
            ))
            response_statement.confidence = 1
            logging.info(response_statement)     
            return response_statement
        
        elif 'news' or 'positive' or 'happy' or 'good' in user_input:
            response_statement = Statement(news_response)
            response_statement.confidence = .8
            logging.info(response_statement)     
            return response_statement
        
        elif 'hi' or 'howdy' or 'hello' in user_input:
             #add help response
            responses = ["""Hello \U0001F31F""", "Hi there!", "How are you","Hi, My name is Rona"]
            response_statement = Statement(random.choice(responses))
            response_statement.confidence = 1
            logging.info(response_statement)
            return response_statement
   
        elif 'bye' or 'ciao' or 'adios' or 'its been real' in user_input:
             #add help response
            responses = ["""Bye \U0001F31F""", "Chat later!", "Have a good one"]
            response_statement = Statement(random.choice(responses))
            response_statement.confidence = 1
            logging.info(response_statement)
            return response_statement
  
        else:
            response_statement =  Statement(text="I'm sorry I could not understand")
            response_statement.confidence = 0
            return response_statement
        
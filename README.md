# Covid-19 ChatBot

![MIT license](https://img.shields.io/badge/License-MIT-blue.svg) [![Build Status](https://travis-ci.com/ari-hacks/covid-chatbot.svg?branch=master)](https://travis-ci.com/ari-hacks/covid-chatbot)


## About

This is a simple api that gives stats on Covid-19 in the US & UK. The api also provides some good news in light of recent times all transmitted via WhatsApp.

### How it works

Users interact with WhatsApp to communicate with the ChatBot. 
The Bot replies to greetings along with different variations of the following questions.

### Sample Questions:

Input | Output| 
---------|----------|
Greeting!| Hi | 
Hi, How is it going? | Good | 
uk confirmed cases? | Confirmed Uk Cases 165221 | 
How many uk confirmed cases? | Confirmed Uk Cases 165221 
What are the us covid stats? | United States Stats: confirmed: 1055303 recovered: 144423 critical: 18665 deaths: 61112
uk stats |United Kingdom Stats: confirmed: 165221 recovered: 1918 critical: 1559 deaths: 26097
what are the uk covid stats? | United Kingdom Stats: confirmed: 165221 recovered: 1918 critical: 1559 deaths: 26097
how many have us recovered cases? | Recovered Us Cases 147411
tell me some positive news, please? | https://www.theguardian.com/news/2020/apr/13/coronavirus-looking-for-good-news-run-for-heroes-and-an-opera-singing-doctor



## Features

- Python web framework using [FastApi](https://fastapi.tiangolo.com/)
- [Twilio](https://www.twilio.com/whatsapp) API for WhatsApp 
- Automated responses and bot training with [Chatterbot](https://chatterbot.readthedocs.io/en/stable/)
- Testing with [`pytest`](https://docs.pytest.org/en/latest/)
- Automated CI testing using [Travis CI](https://travis-ci.com/github/ari-hacks/covid-chatbot)
- Project specific environment variables using `.env` 
- Built-in API documentation with Open API [docs](https://covid-chatterbot.herokuapp.com/docs)
- One click deploy buttons for Heroku


## Set up

### Requirements

- [Python](https://www.python.org/) 3.8.1
- A Twilio account - [sign up](https://www.twilio.com/whatsapp)
- [WhatsApp](https://www.whatsapp.com/)
- [ngrok](https://ngrok.com/)


### Local development

After the above requirements have been met:

1. Clone this repository and `cd` into it

```bash
git clone https://github.com/ari-hacks/covid-chatbot.git
cd covid-chatbot
```

2. Install dependencies

```bash
pip3 install chatterbot==1.0.4
pip3 install twilio 
pip3 install pytest 
pip3 install uvicorn    
pip3 install fastapi  
pip3 install nltk   
pip3 install httpx         
```

4. Run the application

```bash
uvicorn app.main:app --reload 

#uvicorn runs on http://127.0.0.1:8000    
```

5. Next we need to unzip the ngork [download](https://ngrok.com/download). Ngork creates a secure public tunnel for us to use when communicating with WhatsApp via the twilio API. From your terminal run the following command: 

```bash
./ngrok http 8000

#this port must match the app port
```
6. After you have created your [twilio account](https://www.twilio.com/whatsapp) navigate to the [dashboard's sandbox](https://www.twilio.com/console/sms/whatsapp/sandbox) in the field titled ` when a message comes in ` enter the generated forwarding address from your terminal and save. The forwarding url will look like this: 

![Alt text](/ngork_ex.png?raw=true "Demo")



### Tests

You can run the tests locally by typing:

```bash
pytest
```
### Troubleshooting
If you run into issues with nltk 

```bash
#error in terminal related to ssl verification
#solution - in the terminal run the following commands, make sure you change the version of python accordingly 
>>/Applications/Python 3.8/Install Certificates.command

>>Python3

>>Import nltk

>>nltk.download() 
```

### Cloud deployment

To try this application locally, you can deploy it to Heroku

Please [Sign up](https://www.heroku.com/)  before Deploying. 

 [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)                                               



## Contributing

This template is open source and welcomes contributions. All contributions are subject to our [Code of Conduct](https://github.com/twilio-labs/.github/blob/master/CODE_OF_CONDUCT.md).


## License

[MIT](http://www.opensource.org/licenses/mit-license.html)

## Disclaimer

No warranty expressed or implied. Software is as is.
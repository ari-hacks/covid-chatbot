# Covid-19 ChatBot

![MIT license](https://img.shields.io/badge/License-MIT-blue.svg) [![Build Status](https://travis-ci.com/ari-hacks/covid-chatbot.svg?branch=master)](https://travis-ci.com/ari-hacks/covid-chatbot)


## Table of Contents
## [About](#About)
## [Features](#Features)
## [How to Use it](#how-to-use-it)


## About

This is a Chatbot that sends and receives messages over WhatsApp via the Twilio api to provide Covid-19 stats from the US and the UK. The bot also provides positive news articles to read during these tough times. 

### How it works

Users interact with the WhatsApp App to communicate with the chatbot. 

The Chatbot replies to greetings along with different variations of the following questions.

Sample Questions:




## Features

- Node.js web server using [Express.js](https://npm.im/express)
- Basic web user interface using [Handlebars](https://npm.im/express-handlebars) for templating and Bootstrap for UI
- User interface to create reminders.
- Unit tests using [`mocha`](https://npm.im/mocha) and [`chai`](https://npm.im/chai)
- End to End UI testing using [Cypress](https://www.cypress.io/)
- [Automated CI testing using GitHub Actions](/.github/workflows/nodejs.yml)
- Linting and formatting using [ESLint](https://npm.im/eslint) and [Prettier](https://npm.im/prettier)
- Interactive configuration of environment variables upon running `npm run setup` using [`configure-env`](https://npm.im/configure-env)
- Project specific environment variables using `.env` files and [`dotenv-safe`](https://npm.im/dotenv-safe) by comparing `.env.example` and `.env`.
- One click deploy buttons for Heroku, Glitch and now.sh

## How to use it

1. Create a copy using [GitHub's repository template](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-from-a-template) functionality
2. Update the [`README.md`](README.md), [`package.json`](package.json) and [`app.json`](app.json) with the respective values.
3. Build your app as necessary while making sure the tests pass.
4. Publish your app to GitHub

## Set up

### Requirements

- [Node.js](https://nodejs.org/)
- A Twilio account - [sign up](https://www.twilio.com/try-twilio)

### Twilio Account Settings

This application should give you a ready-made starting point for writing your
own appointment reminder application. Before we begin, we need to collect
all the config values we need to run the application:

| Config&nbsp;Value | Description                                                                                                                                                  |
| :---------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Account&nbsp;Sid  | Your primary Twilio account identifier - find this [in the Console](https://www.twilio.com/console).                                                         |
| Auth&nbsp;Token   | Used to authenticate - [just like the above, you'll find this here](https://www.twilio.com/console).                                                         |
| Phone&nbsp;number | A Twilio phone number in [E.164 format](https://en.wikipedia.org/wiki/E.164) - you can [get one here](https://www.twilio.com/console/phone-numbers/incoming) |

### Local development

After the above requirements have been met:

1. Clone this repository and `cd` into it

```bash
git clone git@github.com:twilio-labs/sample-template-nodejs.git
cd sample-template-nodejs
```

2. Install dependencies

```bash
npm install
```

3. Set your environment variables

```bash
npm run setup
```

See [Twilio Account Settings](#twilio-account-settings) to locate the necessary environment variables.

4. Run the application

```bash
npm start
```

Alternatively, you can use this command to start the server in development mode. It will reload whenever you change any files.

```bash
npm run dev
```

5. Navigate to [http://localhost:3000](http://localhost:3000)

That's it!

### Tests

You can run the tests locally by typing:

```bash
npm test
```

### Cloud deployment

Additionally to trying out this application locally, you can deploy it to Heroku

Please Sign up on [Heroku.com](https://www.heroku.com/)  before Deploying. 

 [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)                                               

## Resources

- [GitHub's repository template](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-from-a-template) functionality

## Contributing

This template is open source and welcomes contributions. All contributions are subject to our [Code of Conduct](https://github.com/twilio-labs/.github/blob/master/CODE_OF_CONDUCT.md).

[Visit the project on GitHub](https://github.com/twilio-labs/sample-template-nodejs)

## License

[MIT](http://www.opensource.org/licenses/mit-license.html)

## Disclaimer

No warranty expressed or implied. Software is as is.

[twilio]: https://www.twilio.com
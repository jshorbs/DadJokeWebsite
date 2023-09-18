Code repo for the website This Dad Joke Does Not Exist (thisdadjokedoesnotexist.com)


The web site generates a dad joke at every refresh. Why? The main goal is for the author to explore the OpenAI's ChatGPT API.

It consists of a single page frontend (currently hosted on GCS) with Javascript that runs a Flask backend (currently hosted on Cloud Run). The backend generates a random word and calls the ChatGPT API with a prompt for a dad joke relevant to that random word. 

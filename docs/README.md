Gets a random word from word list (backend/words.txt) and prompts ChatGPT API for a dad joke based on that word
  
- backend/app.py contains a Flask/Python API app in (app.py)
- backed/Dockerfile + backend/requirements.txt + backend/tasks.py package the API into a container for Google Cloud Run
- index.html is single page with Javascript that calls the API
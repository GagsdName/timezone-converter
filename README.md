# Timezone Converter
Shows local time at selected timezone. 

## Server
To fire-up the server after cloning the repo -

* Make sure you have the right path for your python installation in server/env/pyvenv.cfg file. 
* Run `python -m venv --upgrade ENV_DIR` in the server folder, where ENV_DIR is your absolute path to the server/env directory in this repo or alternatively update `VIRTUAL_ENV` variable in server/env/Scripts/activate.bat file.
* Run server/env/Scripts/activate. This will activate a virtual environment.
* Run `pip install -r requirements.txt` in the server directory. This will install server dependencies.
* Run `python app.py` to start the server.
* Make sure the server launches on localhost:5000 as client expects server to launch on port 5000. (This behavior can be updated or tied to some production domain)


## Client
To fire-up the client after cloning the repo - 

* Navigate to the client directory and run `npm install`.
* If it throws line-ending or any other linting issues, run `npm run lint --fix`.
* Run `npm serve`. 
* Navigate to localhost:8080 in your browser to use the app.

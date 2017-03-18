from flask import Flask
from github import Github
import yaml
import json
import sys
cmd=str(sys.argv[1])
app = Flask(__name__)
g = Github("praneethadevireddy1595@gmail.com","*******")
cmd=cmd.split("/")
value=cmd[len(cmd)-1]
user = g.get_user()
repo = user.get_repo(value)
@app.route("/")
def hello():
    return "Hello from Dockerized Flask App!!"
@app.route("/v1/<filename>")
def read(filename):
        filename=filename.split(".")
        extension=filename[1]
        filename=filename[0]
        if extension == "json":
                files= repo.get_file_contents(filename+".yml")
                data=str(files.decoded_content)
                files=json.dumps(yaml.load(data))
                return files
        elif extension == "yml":
                files= repo.get_file_contents(filename+"."+extension)
                return yaml.dump(yaml.load(files.decoded_content))
        else:
                return " Please provide yml or json extension"
        
if __name__ == "__main__":
            app.run(debug=True,host='0.0.0.0')

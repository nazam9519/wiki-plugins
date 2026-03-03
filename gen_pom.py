#!/Users/nabila/maven-xwiki/plugins-git/xwiki-plugins/.venv/bin/python
import os
from jinja2 import Environment,FileSystemLoader
from pathlib import Path

def get_template_env(template_path:str) -> Environment:
    return Environment(loader=FileSystemLoader(template_path))

def main():
    outfile = "pom.xml"
    cwd = Path.cwd()
    for dir in os.listdir(cwd):
        path = os.path.join(cwd,dir)
        if(os.path.isdir(path) and os.path.exists(f"{path}/gen_pom.xml")):
            print(f"ok path:{path}/gen_pom.xml")
            outfile_path = f"{path}/{outfile}"
            template = get_template_env(path).get_template("gen_pom.xml")
            output = template.render(
                drawio_version = DRAWIO_VERSION,
                xwiki_version = XWIKI_VERSION,
                jira_version = JIRA_VERSION,
                confluence_version = CONF_VERSION
            )
            with open(outfile_path,"w") as pomfile:
                pomfile.write(output)

if __name__ == "__main__":
    XWIKI_VERSION = os.environ.get("XWIKI_VERSION")
    CONF_VERSION = os.environ.get("CONF_VERSION")
    JIRA_VERSION = os.environ.get("JIRA_VERSION")
    DRAWIO_VERSION = os.environ.get("DRAWIO_VERSION")
    print(f"VERSIONS:\nXWIKI: {XWIKI_VERSION}\nCONFLUENCE: {CONF_VERSION}\nJIRA: {JIRA_VERSION}\nDRAW:{DRAWIO_VERSION}")
    main()
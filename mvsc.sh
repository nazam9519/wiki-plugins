#!/opt/homebrew/bin/bash

export MAVEN_OPTS="--add-opens=java.base/java.net=ALL-UNNAMED --add-opens=java.base/java.lang=ALL-UNNAMED --add-opens=java.base/java.util=ALL-UNNAMED"
export XWIKI_VERSION=17.10.3
export JIRA_VERSION=11.1.2
export CONF_VERSION=1.0.38
export XWIKI_PRO_VERSION=13.13.4
export DRAWIO_VERSION=1.22.11

./gen_pom.py
mvn clean install -U
#mvn clean package -U && mvn install -U
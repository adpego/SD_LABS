# Pràctica 2 - Big Data challenge

1. ### Idea

2. ### Plataforma
S'ha utilitzat [IBM Cloud](https://www.ibm.com/cloud) per emmagatzermar dades i executar funcions i el framework [Lithops](https://github.com/lithops-cloud/lithops) per a facilitar l'ús d'utlitats del cloud.

3. ### Obtenció de dades
- [Twitter API](https://developer.twitter.com/en/docs/twitter-api) → Hastag: [\#Bitcoin](https://twitter.com/search?q=%23Bitcoin)
- [Reddit](https://reddit.com) → Comunitat: [Bitcoin](https://www.reddit.com/r/Bitcoin/) → JSON: https://www.reddit.com/r/Bitcoin/.json
- [Bitcoin API](https://api.coindesk.com/v1/bpi/currentprice.json)

4. ### Crawler scheduler

| **Min** | **Hour** | **Day** | **Month** | **Week** | **Function** |
|:-:|:-:|:-:|:-:|:-:|---|
|50|*/2|*|*|*| Twitter Crawler
|0|*|*|*|*| Reddit Crawler
|45|23|*|*|*| Reddit Comments Crawler
|*/15|*|*|*|*| Bitcoin Crawler 

5. ### Docker
S'ha pujat el contenedor a [Docker Hub](https://hub.docker.com/) per a poderlo utilitzar a les functions de IBM Cloud seguint la seva documentació: https://cloud.ibm.com/docs/openwhisk?topic=openwhisk-prep

**Contenidor docker:** adpego/bigdatachallenge:latest

**Imatge utilitzada:** ibmfunctions/action-python-v3.7

**Llibreries instalades al docker:**
- urllib3==1.24.2
- setuptools
- lithops
- tweepy
- vaderSentiment
- requests




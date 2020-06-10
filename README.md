# nshm-srm-paleo

The aim of the project is to explore the application of Spark and GeoMesa  and to contrast this 
wiht GeoPandas and pure python alternatives.

## 1) Geo-spatial joins

Performing geo joins of datasets from different projects

 - Paleo slip rate data in XLXS format
 - Site data in ESRFI shapefile format
 - NZ Active Fault Databse in ESRI Shapefile
 - t-surface data created with MOVE in GOCAD t-surf format

# Getting started

### Pre-requisites:

 - You must have a working docker installation
 - clone this repo
 
### Startup
 - Open a terminal and cd into the ```docker``` folder
 - run ```docker-compose up -d``` from the docker folder
 - run ```docker-compose logs notebook``` and cut-n-paste the URL 
   e.g. http://127.0.0.1:8888/?token=**********
 - opem the URL in your brower and open the DEMO folder.

You're in, try out the notebooks yourself.

### Usage

 - Notice that docker-compose is running 4 containers. To shutdown all together, just run ```docker-compose down```
 - Any changes or new notebooks will be saved to the host filesystem in docker/fs/home/jovyan. You may check this in to the git repo is you want to share them.






# DAMS Repository
This repository contains the Personal Health Train Metadata schema, as described in DAMS: A Distributed Analytics Metadata Schema (Link tba). This schema aims at making our work openly accessible and to promote discussion and feedback for it. Note that the metadata schema is still under developement and can therefore change.
## Content
### schema.ttl
This file contains the general RDFS definitions of the Schema in Turtle serialization. This includes a definition of the hierachy of the different classes.
### Train
This folder contains the shacl definitions for the train part of the metadata.
### Station 
This folder contains the shacl definitions for the station part of the metadata.
### DevelopementArtifacts
This folder contains the different documents we created during the developement process of the schema. These are the list of the user stories (userstories.pdf) we collected through the interviews and the tables mapping the user stories onto attributes (tables.pdf).
### Thesis
This folder contains the original thesis through which the metadata schema was developed. It describes the metadata schema and the developement process of it in more detail.
### converter.py
This python script creates rdfs definitions out of given shacl definitions. With this it is ensured that the rdfs definitions always comply with the shacl documents and it reduces the effort of creating the rdfs document.
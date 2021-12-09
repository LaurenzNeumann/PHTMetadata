# DAMS Repository
This repository contains the Personal Health Train Metadata schema, as described in DAMS: A Distributed Analytics Metadata Schema (Link tba). This schema aims at making our work openly accessible and to promote discussion and feedback for it. Note that the metadata schema is still under developement and can therefore change.
## Content
This branch contains the version 2.
Due to limitations in rdfs/shacl itself and also in the tools, the new version is created in OWL.
The goal of this new version is to solve problems which we encountered with of the old schema. 
For this, new concepts are introduced for more abstraction. This should allow a better description, especially for the sake of interoperability.

## Discussion
- Do we need to adapt the "wagons inside the train" paradigm?
- How do we model the transformation of one format into one another?
- How do we model if the execution has no user given order?
### DRF Architecture

* Single app project because of migration foreign key problems when large project

* Use django view classes, but if you have business logic then divide views on 
Presentation and Use Case layers. 

* Use only coupled settings in config for django features, if you have 
independent infrastructure module like Redis Recommendation System then 
use local config



### DRF Architecture

* Single app project because of migration foreign key problems when large project.

* Use django view classes, but if you have business logic then divide views on 
Presentation and Use Case layers. 

* Use only coupled settings in config for django features, if you have 
independent infrastructure module like Redis Recommendation System then 
use local config.

### Spaces

* Relationships:
    - OneToOne - select
    - OneToMany - prefetch
    - ManyToOne - select
    - ManyToMany - prefetch

* Validation:
    - Django - form.is_valid() or model.full_clean()
    - DRF - serializer.is_valid() or model.full_clean()
    - FastAPI - Pydantic auto validation, session.add(item) - auto validation

* Examples  ###################

### Domain Entities with Django

........

### Endpoints DRF and FastAPI way where:

* fastapi way is custom logic

* DRF is just django views

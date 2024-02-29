from pydantic import ConfigDict, BaseModel


class Model(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    def as_dict(self) -> dict:
        return self.model_dump()

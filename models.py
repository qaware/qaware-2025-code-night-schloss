from pydantic import BaseModel
from pydantic.class_validators import Optional


class Autoteilbeschreibung(BaseModel):
    # TODO: Füge relevante Daten hinzu
    seriennummer: int
    zeitstempel: Optional[str]

    def to_dict(self):
        return {
            # TODO: Füge relevante Daten hinzu
            "seriennummer": self.seriennummer,
            "zeitstempel": self.zeitstempel
        }

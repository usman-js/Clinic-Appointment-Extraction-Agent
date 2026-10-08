from typing import Literal

from pydantic import BaseModel, Field


class Appointment(BaseModel):
    # TODO: add all 7 boxes from the table in the assignment.
    # Here is the first one, to show you the pattern:
    Name: str | None = Field(description="Name of the person writing the message, otherwise null")
    Phone: str | None = Field(description="Phone number of the person writing the message, otherwise null")
    Doctor: Literal["general", "skin", "eye", "dentist"] | None = Field(description="Which doctor they need, otherwise null")
    Day: str | None = Field(description="Which day they need, otherwise null")
    Time_of_day: str | None = Field(description="Which time of day they need, otherwise null")
    Reason: str | None = Field(description="Reason they need a doctor, otherwise null")
    urgent: bool | None = Field(description="Whether they need a doctor urgently, otherwise null")


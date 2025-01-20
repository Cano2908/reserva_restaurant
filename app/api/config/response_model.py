from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field

class ResponseModel[_DT](BaseModel):
    """
    Represents a response object with status, date, detail, and data.

    Attributes:
        status (bool): The status of the response.
        date (datetime): The date and time when the response was created.
        data (T): The data associated with the response.
        detail (str): A detailed description or additional information about the response.
        metadata (M): Additional information or metadata about the response.
    """

    date: Annotated[
        datetime,
        Field(
            default_factory=datetime.now,
            examples=[str(datetime.now())],
        ),
    ] = datetime.now()
    status: bool
    detail: str
    data: _DT = None

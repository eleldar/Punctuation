#!/bin/bash
import os
from typing import List, Union

from fastapi import FastAPI
from pydantic import BaseModel

from src.neuro_comma.cache import ModelCache

app = FastAPI()


class Data(BaseModel):
    data: Union[str, List[str]]


class InputData(Data):
    class Config:
        schema_extra = {
            "example": {
                "data": ("Заполнить знаками препинания "
                         "текст на русском языке который получен "
                         "из спонтанной речи")
            }
        }


class OutputData(Data):
    class Config:
        schema_extra = {
            "example": {
                "data": ("Заполнить знаками препинания "
                         "текст на русском языке, который получен "
                         "из спонтанной речи.")
            }
        }


@app.post("/", response_model=OutputData)
async def punctuation_restoration(input: InputData):
    model = ModelCache().model
    data = input.data
    if isinstance(data, str):
        output_data = model(data)
    else:
        output_data = [model(text) for text in data]  # type: ignore
    return {"data": output_data}



if __name__ == "__main__":
    import uvicorn
    os.environ["TRANSFORMERS_OFFLINE"] = "1"
    uvicorn.run(app, host="127.0.0.1", port=8000)

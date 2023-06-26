from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel
import nltk

nltk.download("stopwords")
from nltk.corpus import stopwords

stop_words = stopwords.words("english")

# Create a new FastAPI app instance
app = FastAPI()


class Text(BaseModel):
    text: str


# Initialize the text generation pipeline
# This function will be able to generate text
# given an input.
pipe = pipeline(
    "sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment-latest"
)


@app.get("/sentiment")
async def sentiment(text):
    _text = " ".join([x for x in text.split() if x not in stop_words])
    # Use the pipeline to process text from the given input text

    while _text:
        try:
            output = pipe(_text)
            break
        except Exception as exp:
            len_text = len(_text)
            if len_text - 1 == 0:
                raise Exception("Could not process text")
            _text = " ".join(_text.split()[0 : len_text - 1])

    # Return the generated text in a JSON response
    # return {"output": output[0]["generated_text"]}
    return {"output": output}

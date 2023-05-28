from pydantic import BaseModel
import json
import openai


openai.api_key = "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"

PROMPT_PARSE = """
This is a conversation between “farmer” and “Lithos”. Your job is to extract information from the transcript to record pertinent information in a structured format.

__A__: Extract the information in the following format:
{
  'fields': []{
  'name': `type: str, description: name of field` ,
  'ph_level': `type: float, description: average ph level, pick exactly one number.`,
  'crop': `type: str, description: crop planted on field`,
  'limed': `type: bool, description: has field been limed`,
  'fertilizer': `type: str, description: fertilizer used on field`,
  'tilling': `type: str, description: field tilling technique`,
  'spreader': `type: bool, description: does farmer have a spreader`,
  'spreader_tons': `type: str, description: capacity of spreader`
  },
'timeline': int,
'follow_up': str
}

Note: fill up timeline in number of days and follow-up is a choice between mobile and email.
For any information not present in transcript, return N.A

Transcript:
"""


# class FieldData(BaseModel):
#     from typing import Optional

#     name: Optional[str]
#     ph_level: Optional[float]
#     crop: Optional[str]
#     limed: Optional[bool]
#     fertilizer: Optional[str]
#     tilling: Optional[str]
#     spreader: Optional[bool]
#     spreader_tons: Optional[str]


def clean_json_str(raw_str):
    # Clean string and parse as json
    temp = raw_str.replace("\n", "")
    temp = temp.replace("'", '"')
    temp = temp.replace("True", "true")
    temp = temp.replace("False", "false")

    # return dict(FieldData(**(json.loads(temp))))
    return json.loads(temp)


def parse_transcript(transcript):
    message = PROMPT_PARSE + transcript
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            # {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message},
            # {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
            # {"role": "user", "content": "Where was it played?"},
        ],
    )

    # Clean and convert to json
    return clean_json_str(response["choices"][0]["message"]["content"])

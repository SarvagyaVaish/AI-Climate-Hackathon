from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import time
import json


app = FastAPI()

# https://fastapi.tiangolo.com/tutorial/cors/
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

# This is a cache of conversations to avoid reprocessing
CONVERSATIONS = {
    "conv1": {
        "name": "May 27th  ·  Morning Dew",
        "audio": "data/conversation1.m4a",
        "transcript": "number of fields that need a ton or half a ton, right? Yes. One question I had for you is what is your pH target? Where do you want your pHs to be? We're doing potatoes, so we want to be 6.2, 6.3, anywhere from 6 to 6.5 is our target. Okay, got it. And are you worried about going higher at all or is that... Well, it is not so much. You know, we don't want to be, you know, 7 runs up a red flag. Okay. You don't want to be at 7 is what you're saying? No, we don't want to be 7 or above. Not to say that we don't have some spots that are, but... And why is that? Are you worried about manganese or like what's the... Why are you worried about going to 7? That is on tobacco, you know, that is always been, you know, you get a better... It takes up the... When you get to that point, it seems like you lose part of your fertilization program. Yep, yep. But you still have tobacco fields or...? Yeah, we still got some, but you know, most of those have been, you know, put lime on them already. Okay, got it, got it. The fields that... And I don't know if you noticed off the top of your head, but the fields that Mary had shared with me are the Green Pond CMC, Green Pond Loop and Bailey HQ. You know what's going on these fields this year? Yeah, sweet potatoes. On all of them? On the ones you just called over, the Bailey headquarters and... Green Pond Loop and Green Pond CMC? Yes, yes. Okay. Well, no, the Green Pond, the big field at Green Pond has had lime on it for... Because it's going to put tobacco in it. Because it's done last week. Oh, so you already put lime on those? Oh, yes, on that one field there. Okay, got it. On the bigger one? Yes, yes, sir. Okay, got it. That's like the 55, 60 acres, that field? That's correct, yes. Right, okay, got it. So let me write that down. So Green Pond CMC has already put lime. Okay, got it. For the Bailey field, let me... Are you good with email communication? Is that good if I send you something over email and what our recommendations for those fields would be? Yes, that's fine. Okay, okay, excellent. So yeah, let me send that over to you for the Bailey field and then for the smaller Green Pond field as well. Okay. What's going on to the smaller Green Pond field? They're basically putting the taro on. Okay, got it, got it. And so are you tilling those fields at all? Yes, we will be. Yep, yep, okay, perfect. And then when is your ideal timing? Like when do you want to put the... When would you like? Yeah, I would like to go on and get it on now. Okay. Let it be working, let it be breaking down. Yep, yep. So as soon as possible. When are you planting the sweet potatoes? The sweet potatoes are going to go on there in late April. And then we got to gas the land, so we got to be three weeks, two to, let's say two weeks ahead of the end of the plant. Okay, got it. That's the reason we went on with this tobacco because, on the line, because we don't have that window to wait to the day that we're ready to plant. Yep, yep. Okay.",
        "chat_completion": "{\n  'fields': [\n  {\n    'name': 'Green Pond CMC',\n    'ph_level': 6.3,\n    'crop': 'tobacco',\n    'limed': True,\n    'fertilizer': 'N.A',\n    'tilling': 'N.A',\n    'spreader': 'N.A',\n    'spreader_tons': 'N.A'\n  },\n  {\n    'name': 'Green Pond Loop',\n    'ph_level': 6.3,\n    'crop': 'sweet potatoes',\n    'limed': 'N.A',\n    'fertilizer': 'N.A',\n    'tilling': True,\n    'spreader': 'N.A',\n    'spreader_tons': 'N.A'\n  },\n  {\n    'name': 'Bailey HQ',\n    'ph_level': 6.3,\n    'crop': 'sweet potatoes',\n    'limed': 'N.A',\n    'fertilizer': 'N.A',\n    'tilling': 'N.A',\n    'spreader': 'N.A',\n    'spreader_tons': 'N.A'\n  }\n  ],\n  'timeline': 0,\n  'follow_up': 'email'\n}",
        "questions": [
            "Is the Green Pond Loop field limed?",
            "What is the tilling status of Bailey HQ field?",
            "Is the Bailey HQ field limed?",
        ],
    },
    "conv2": {
        "name": "May 25th  ·  Harvest Hill",
        "audio": "data/conversation2.m4a",
        "transcript": "Can you tell me a bit more about your farm? How many acres do you guys farm? It ain't quite 500. About 500? Yeah. Got it, and what crops do you grow? Soybeans, corn, produce, strawberries, we do sweet corn, pumpkins. Okay. Little tobacco, nothing but. Got it, got it. And then do you have any acres where you still need lime for the spring? Yes, sir. How many acres is that? It's probably around 50. About 50? Yeah. Okay, and how much lime would you apply on those fields if you had it? Probably a ton. About a ton? I did a soil sample last year, it came off a half a ton, so I didn't put any last year, so it probably needs a ton each year, I would think. Okay, yeah, that makes sense. And what pH do you usually try to get your soils to? I think on the vine, it's around six, so that's what we try to do every time. Got it, I see. Would you be open to going a little bit higher on these 50 acres, just to try it out? Yes, sir. Okay. Okay. So, yeah, one thing to know is that, so the application rates for this material, the material is called basalt. It's a volcanic rock, it's the most common volcanic rock in the world. And so the inherent liming ability of the material is a little bit lower, because it actually has a lot of silicon. So I don't know if you guys have ever participated in one of these pumpkin competitions, where you try to get the largest pumpkin or something. Like a lot of folks put silicon into their soils for that. So it should also help with growth usually, and yield increases here and there. I'm not promising that, but the data has been pretty good on that, but no promises made on that. But yeah, so the application rate is gonna be a little bit higher than normally, but if you'd be open to going up to a little bit higher pH, we like to put out a little bit more material, because that's better from a carbon perspective. But obviously we don't wanna do anything that's bad for your soils. But in our trials with the University of Illinois, we've run eight year trials now. Every year we put out 20 tons to the ABA, or so just to see what happens if you put like a crazy amount out. And we've never seen any yield decreases, no heavy metal buildup or anything like that. So it's really safe material. Okay. Yeah. Would you guys be able to send me those soil test results that you pulled last year, or the most recent results that you have for this farm through email, is that possible? Yeah, okay. Okay. I'll text you my email address. And then the other question I have is, do you have maps for your farm as well? Oh, I've got some here for the site now. Yeah, do you have those digitally, or do you have those printed out? I got them printed out. Got it. Would you be able, so sometimes what folks, because I kind of need the maps to be able to know exactly where the fields are and things like that. If you can call the FSA representative, they can just email them to me directly. They've been doing this a lot for me. So if you give them a call and you tell them my email address, then they can send those to me directly. Okay. Yeah. And then when are you guys planting on this field? Like how quickly do we need to get your material? Probably in the next probably three weeks or so. Okay. Okay, we should be able to do that. Yeah. You guys, who does the spreading for you usually? Well, we have a spreader truck. Okay. What kind of spreader is it? It's a new little, it's an international truck with a new little bed. Okay. And is it, does it have a chain or a belt or something at the bottom? It has a chain. Or something at the bottom? It has a belt. A belt. Okay, perfect. Yeah, that's great. And you know how the width of it is an inch? Yeah. Okay, got it. Got it. Yeah, that should work. Would you be open to spreading the material yourself? Do you have time for that? Otherwise we can help you find a spreader. I guess we would be open to it. Yeah, we could do it. You could do it? You think so? Yes, sir. Okay. Do you know how, like how many tons does the spreader hold usually? Oh, well, I've got probably about four or five tons of the land. Okay. Okay, yeah, I got it. Yeah, the density of the material is very similar to lime. So it'll be holding about four or five tons as well. And I would guess, you know, if you, if you haven't limed that land and you'd be open to going up a little bit, you'd probably, we'd probably want to apply sort of six or seven tons to the acre, I think. So, you know, you probably, you probably want to do sort of one or two passes on each acre. Would that be, would that work for you guys? Yeah. Yeah? Okay, excellent. Any other questions that I can answer? No, I don't think so. Okay. I don't have. Okay, so what I'll do is Charles, sorry, Jack, I'll send you my, I'll send you my email address through text and then if you can send me your soil sample results and then if you can call the FSA to send me those maps, then we'll take it from there. Okay. Yeah. Yep, sounds good. Great, and then maybe you can, when you send me the maps or when the FSA sends me the maps, can you just let me know what the name of the field is or the like tract ID and the farm ID of those fields that you, that still need the lime? Okay. Yeah? Yeah, sure. Maybe once I have those, I'll just give you another call and we can talk it through. Okay. Okay. Excellent. All right, see ya.",
        "chat_completion": "{\n  'fields': [{\n  'name': 'N.A',\n  'ph_level': 6.0,\n  'crop': 'Soybeans, corn, produce, strawberries, sweet corn, pumpkins, tobacco',\n  'limed': False,\n  'fertilizer': 'basalt',\n  'tilling': 'N.A',\n  'spreader': True,\n  'spreader_tons': '4 or 5'\n  }],\n'timeline': 21,\n'follow_up': 'email'\n}",
        "questions": [
            "What is the recommended pH level for optimal crop growth?",
            "Do you use any specific type of basalt fertilizer?",
            "What is the ideal timeline for spreading the basalt fertilizer?",
            "Are there any additional nutrients or materials added to the soil along with the basalt?",
        ],
    },
}


class Conversation(BaseModel):
    convId: str


class Forecast(BaseModel):
    days: int


@app.get("/")
async def main():
    return {"message": "Hello World"}


@app.post("/reset_airtable")
async def reset_airtable():
    from airtable import clear_table

    clear_table()


@app.post("/weather")
async def reset_airtable(forecast: Forecast):
    from weather import geocode_location, get_temperature_forecast

    latitude, longitude = geocode_location()
    temperature, precipitation = get_temperature_forecast(
        forecast.days, latitude, longitude
    )

    return {
        "temperature": temperature,
        "precipitation": precipitation,
    }


@app.post("/parse")
async def parse(conv: Conversation):
    from openai_wrapper import parse_transcript, clean_json_str, generate_questions
    from airtable import insert_row, clear_table, print_table

    conv_id = conv.convId
    conv_data = CONVERSATIONS[conv_id]

    # Step 1: Transcribe
    print("Getting transcript")
    # TODO: Implement whisper call. Something like...
    # transcript = transcribe_audio(conv_data["audio"])
    transcript = conv_data["transcript"]

    # Step 2: Parse
    print("Parsing transcript")
    # parsed_json = parse_transcript(transcript)
    parsed_json = clean_json_str(conv_data["chat_completion"])

    # Step 3: Send to airtable
    print("Populating airtable")
    clear_table()
    for row in parsed_json["fields"]:
        insert_row(row)

    # Step 4: Generate questions
    print("Generating questions")
    # questions = generate_questions(transcript, parsed_json)["questions"]
    questions = conv_data["questions"]

    return {
        "transcript": transcript,
        "parsed_json": parsed_json,
        "questions": questions,
    }

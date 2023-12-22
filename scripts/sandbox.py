import os

from dotenv import load_dotenv
import openai

# Load env vars
load_dotenv("../backend/.env")

# Set up OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")

print(os.getenv("OPENAI_API_KEY"))

# Variables to control the script
CONVERSATION_FILE = "data/conversation1.m4a"
TRANSCRIBE = False

#
# 1. Transcribe
#
# - play with "prompt" field to guide transcription
#   https://platform.openai.com/docs/api-reference/audio/create#audio/create-prompt
#   https://platform.openai.com/docs/guides/speech-to-text/prompting
# - play with "temperature" field to guide transcription: https://platform.openai.com/docs/api-reference/audio/create#audio/create-prompt
transcript = None

if TRANSCRIBE:
    print("Transcribing audio ...")
    audio_file = open(CONVERSATION_FILE, "rb")
    transcribe_response = openai.Audio.transcribe("whisper-1", audio_file)
    transcript = transcribe_response["text"]
    # Cache it
    with open(CONVERSATION_FILE + ".transcript", "w") as f:
        f.write(transcript)
else:
    print("Loading transcript from cache ...")
    # Load from cache
    with open(CONVERSATION_FILE + ".transcript", "r") as f:
        transcript = f.read()

print("-- TRANSCRIPT --")
print(transcript)

#
# 2. GPT completion
#

# # Load prompt from file and append the transcript to it
# with open("prompt2.txt", "r") as f:
#     prompt_text = f.read()
# prompt_text += transcript["text"]

# # Call GPT
# response = openai.ChatCompletion.create(
#     model="gpt-4",
#     messages=[
#         # {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": prompt_text},
#         # {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
#         # {"role": "user", "content": "Where was it played?"},
#     ],
# )
# print(response)



# # Step 1: Transcribe
# # transcript = transcribe_audio(conv_data["audio_filename"]) # TODO: Implement whisper call
# print("Getting transcript")
# transcript = conv_data["transcript"]

# # Step 2: Parse
# print("Parsing transcript")
# # time.sleep(3)
# # parsed_json = parse_transcript(transcript)
# parsed_json = clean_json_str(conv_data["chat_completion"])

# # Step 3: Send to airtable
# print("Populating airtable")
# clear_table()
# for row in parsed_json["fields"]:
#     insert_row(row)

# # Step 4: Generate questions
# print("Generating questions")
# # time.sleep(3)
# # questions = generate_questions(transcript, parsed_json)
# # print(questions)
# # questions = questions["questions"]
# questions = conv_data["questions"]

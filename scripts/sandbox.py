import os
import openai

openai.api_key = "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"

#
# 1. Transcribe
#
# - play with "prompt" field to guide transcription
#   https://platform.openai.com/docs/api-reference/audio/create#audio/create-prompt
#   https://platform.openai.com/docs/guides/speech-to-text/prompting
# - play with "temperature" field to guide transcription: https://platform.openai.com/docs/api-reference/audio/create#audio/create-prompt
conv_filename = "data/conversation1.m4a"
conv_transcript = None

if not conv_transcript:
    audio_file = open(conv_filename, "rb")
    conv_transcript = openai.Audio.transcribe("whisper-1", audio_file)
print(conv_transcript)

#
# 2. GPT completion
#

# Load prompt from file and append the transcript to it
with open("prompt2.txt", "r") as f:
    prompt_text = f.read()
prompt_text += conv_transcript["text"]

# Call GPT
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        # {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt_text},
        # {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        # {"role": "user", "content": "Where was it played?"},
    ],
)
print(response)

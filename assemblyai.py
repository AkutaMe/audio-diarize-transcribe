
import assemblyai as aai


aai.settings.api_key = "4fe5130c7f394eeca5397a02680bcd0c"

transcriber = aai.Transcriber()
#upload ur local file
transcript = transcriber.transcribe("./my-local-audio-file.wav")

print(transcript.text)
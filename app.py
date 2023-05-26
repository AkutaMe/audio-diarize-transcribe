from flask import Flask, render_template, request, jsonify
import assemblyai as aai

app = Flask(__name__)
app.config["SECRET_KEY"] = "your-secret-key"

# Configure AssemblyAI
aai.settings.api_key = "your-assemblyai-api-key"

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Check if the post request has the file part
        if "audio_file" not in request.files:
            return jsonify({"error": "No file part in the request"})

        audio = request.files["audio_file"]

        # Check if the user selected a file
        if audio.filename == "":
            return jsonify({"error": "No file selected"})

        # Save the uploaded audio file to a local path
        audio_path = "./uploads/" + audio.filename
        audio.save(audio_path)

        # Transcribe the audio using AssemblyAI
        transcriber = aai.Transcriber()
        transcript = transcriber.transcribe(audio_path, diarization=True)

        # Render the template with the transcript
        return render_template("index.html", transcript=transcript.text)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

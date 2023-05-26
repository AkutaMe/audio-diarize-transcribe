First, I began researching Whisper, WhisperX, and everything related to audio transcription and diarization.  

I was able to install Whisper and use it in my code, but WhisperX was giving me some problems!  So, I started researching different ways to approach this problem. I found PyDub, pyAudioAnalysis, and similar libraries, which didn't really work for me. 

Then, I returned to WhisperX. I wanted it to work, but I don't know why, it had some errors while I was installing it on my PC. 
 
After dealing with those issues, I looked into some APIs like Google Cloud Text-to-Speech AI, which transcribes audio files. However, that also didn't work well for me. 
 
After that, I began researching AIs that specialize in this type of work and discovered OpenVino libraries and Assembly AI. In the end, I chose Assembly AI because it seemed really easy to use. You just need to get the API key, make a function and run the code. 

This felt like a cheat code to me, so I thought about taking it a step further and implementing it with Flask to create a website. 

I successfully completed the web design part as I intended, but I still encountered some errors while attempting to transcribe the audio files. 

I was getting this error:  POST http://127.0.0.1:5500/ 405 (Method Not Allowed). 

Tried to debug it in any way possible, but I couldn’t find a way to fix it. 

I am still pretty sure I am using correct functionality in my python code of GET, POST. 

I believe my problem lies in how I am running the Python Flask server. I am almost certain that I am executing all the necessary steps correctly, but the outcomes indicate otherwise. 

I will provide both the Python code that utilizes AssemblyAI(assemblyai.py) and my attempt to transform it into a functional website. 

I would greatly appreciate it if I could receive feedback on my errors!  

P.S. Please do not assume that my message indicates that I have given up on the task. On the contrary, I am genuinely intrigued by this topic, and I am reaching out for feedback to enhance my results. As we both acknowledge, I am new to this field, so receiving feedback is the most valuable input I can receive at this point. 

I added comments in every field that executes something for better understanding. 

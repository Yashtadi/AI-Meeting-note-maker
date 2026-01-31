# Why I built this
  Meetings are ubiquitous but inefficient: long recordings, poor notes, missed action items. I wanted a tool that:
    -Respects privacy (local LLM inference) while keeping Seech to Text accuracy (using AssemblyAI).
    -Is practical for real users — simple, fast, and produces immediate, usable meeting notes.
    -Demonstrates full-stack thinking: signal processing, API integration, LLM prompting, UX & deployment tradeoffs.

# Status
  I have just started this project and divided into three phases among which first phase is completed as of now and i am working on the second phase
  
# What it does today(Phase 1)
  -Accepts an audio file (or recorded audio) as input.
  -Uploads audio to AssemblyAI and obtains a diarized, punctuated transcript.
  -Sends cleaned transcript to a locally running LLM (via Ollama) for summarization and structured note generation.
  -Produces output files:
    -notes.md: human-readable meeting summary (agenda, decisions, action items, participants, short highlights).

# Phase 2: UI development
  GUI: Desktop app or Python GUI (PyQt) with:
    1. Record/Upload buttons
    2. Progress indicator (uploading → transcribing → summarizing)
    3. Visual summaries, copy/export buttons (PDF/Markdown/JSON)
    4. Settings: summary length, format choices, API key input
    5. Local/Remote LLM selection toggle (run local Ollama or call hosted inference)
    6. Lightweight installer / single-click .exe for Windows

# Phase 3: Deployment
  Deployment options:
  1. Cloud VM (DigitalOcean / GCP / AWS): host Ollama + model for central inference; app becomes thin client.
  2. Raspberry Pi (edge deployment): run lightweight model on-device for offline users (if model fits).

  Optimizing the application and improving performance , which involves trying to integrate better LLM models , provide features like special prompting to users, etc

# How to run Phase 1:
  1) Prepare .env file
     <img width="588" height="41" alt="image" src="https://github.com/user-attachments/assets/a7a271e6-241b-4d14-97a9-db97425efe41" />
  2) Install dependancies
     <img width="1006" height="122" alt="image" src="https://github.com/user-attachments/assets/15661dea-e763-4851-937f-f7bbb632a186" />
  3) Run Ollama locally on your laptop
     Install Ollama and the LLaMA 3.2 model locally
  4) Now run the main.py file and press enter to start recording and cntrl + c to stop recording once you are done
  5) Wait till it generates notes.md



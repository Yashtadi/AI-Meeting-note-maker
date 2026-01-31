import os  
import assemblyai as aai
import ollama  
from dotenv import load_dotenv

load_dotenv()

class MeetingProcessor:

    def __init__(self):
        aai.settings.api_key = os.getenv("ASSEMBLYAI_API_KEY")      

    def transcribe_and_diarize(self, audio_filepath):
        
        print("Uploading and Transcribing...")
        transcriber = aai.Transcriber()
        config = aai.TranscriptionConfig(speaker_labels=True)
        transcript = transcriber.transcribe(audio_filepath, config)
        
        if transcript.status == aai.TranscriptStatus.error:
            raise Exception(f"Transcription failed: {transcript.error}")

        full_text = ""
        for utterance in transcript.utterances:
            full_text += f"Speaker {utterance.speaker}: {utterance.text}\n"
            
        return full_text

    def generate_minutes(self, raw_transcript):
        print("Generating detailed notes with Local LLM (Ollama)...")
        
        system_prompt = """
        You are an elite executive assistant. 
        Analyze the provided meeting transcript and output a structured summary.
        
        Format:
        ## Executive Summary
        (2-3 sentences)
        
        ## Key Discussion Points
        - (Bullet points)
        
        ## Action Items
        - [ ] Who: Task
        """

        response = ollama.chat(model='llama3.2', messages=[
            {
                'role': 'system',
                'content': system_prompt,
            },
            {
                'role': 'user',
                'content': f"Here is the transcript:\n\n{raw_transcript}",
            },
        ])

        return response['message']['content']

if __name__ == "__main__":
    proc = MeetingProcessor()
    
    fake_transcript = """
    Speaker A: I think we should switch to Python for the backend.
    Speaker B: I agree, but we need to check if the team knows it.
    Speaker A: Good point. John, can you survey the team by Friday?
    Speaker B: Sure, I will do that.
    """
    
    print("--- Testing Local LLM ---")
    notes = proc.generate_minutes(fake_transcript)
    print(notes)
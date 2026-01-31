import time
import os
from recorder import AudioRecorder 
from processor import MeetingProcessor

def main():
    audio_filename = "meeting_recording.wav" 
    
    recorder = AudioRecorder(filename=audio_filename)
    processor = MeetingProcessor()

    print("\nMEETING COMPANION")
    print("---------------------------------------------")

    input("Press Enter to START recording...")

    recorder.start()
    
    try:
        while recorder.recording:
            time.sleep(0.1) 

    except KeyboardInterrupt:
        print("\n\nStopping recording...")
        recorder.stop()

    print("---------------------------------------------")
    print("Please wait. Transcribing audio to text...")
    
    try:
        raw_transcript = processor.transcribe_and_diarize(audio_filename)
        
        print("\n--- Raw Transcript ---")
        print(raw_transcript[:200] + "...") 

        print("\n--- Generating Notes ---")
        summary = processor.generate_minutes(raw_transcript)

        print("\nMEETING NOTES:")
        print(summary)
        
        with open("notes.md", "w") as f:
            f.write(summary)
            
    except Exception as e:
        print(f" Error: {e}")

if __name__ == "__main__":
    main()
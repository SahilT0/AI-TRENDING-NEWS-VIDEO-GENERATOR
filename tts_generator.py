import pyttsx3

def text_to_audio(script, output_file="output.mp3"):
    engine = pyttsx3.init()
    engine.save_to_file(script, output_file)
    engine.runAndWait()
    print(f"Audio saved as {output_file}")

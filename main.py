import os
import time

from news_scraper import get_title_and_content_from_same_article
from script_generator import generate_script_with_openrouter
from tts_generator import text_to_audio
from video_creator import create_video_with_headline_and_audio

os.environ["IMAGEMAGICK_BINARY"] = r"C:\Program Files\ImageMagick-7.1.2-Q16-HDRI\magick.exe"

def main():
    print("Starting Pipeline\n")
    start_time = time.time()

    print("Step 1: Fetching trending news")
    title, content = get_title_and_content_from_same_article()
    if not title or not content:
        print("❌ No news data found.")
        return

    print(f"Title: {title}")
    print(f"Content: {content[:150]}...\n")

    print("Step 2: Generating script")
    t2 = time.time()
    script = generate_script_with_openrouter(title, content)
    if not script:
        print("Script generation failed. Exiting...")
        return
    print(f"Script Generated in {time.time() - t2:.2f} seconds\n")
    print(script)

    print("🎤 Step 3: Converting to audio...")
    audio_file = "output.mp3"
    text_to_audio(script, audio_file)

    print("Step 4: Creating video...")
    create_video_with_headline_and_audio(
        heading=title,
        image_path="background.jpg",
        audio_path=audio_file,
        output_path="final_video.mp4",
        duration=40
    )

    print(f"Pipeline completed in {time.time() - start_time:.2f} seconds.")

if __name__ == "__main__":
    main()


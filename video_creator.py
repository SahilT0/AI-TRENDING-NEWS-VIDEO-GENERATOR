from moviepy.editor import *
import moviepy.config as mpyconf
from image_generator import generate_image_from_prompt

IMAGEMAGICK_PATH = r"C:\Program Files\ImageMagick-7.1.2-Q16-HDRI\magick.exe"
os.environ["IMAGEMAGICK_BINARY"] = IMAGEMAGICK_PATH
mpyconf.IMAGEMAGICK_BINARY = IMAGEMAGICK_PATH

def create_video_with_headline_and_audio(heading,image_path, audio_path, output_path="final_video.mp4", duration=45):
    if not os.path.exists(audio_path):
        raise ValueError("Audio file not found.")

    headline_text = heading
    if not headline_text:
        raise ValueError("Headline not found.")

    # Get the audio and limit its length to 'duration'
    audio_clip = AudioFileClip(audio_path).subclip(0, duration)
    actual_duration = audio_clip.duration

    background = ImageClip(image_path).set_duration(actual_duration)
    video_width, video_height = background.size
    ticker_height = 80
    ticker_y = video_height - ticker_height

    # Generate AI image
    ai_image_path = "ai_image.jpg"
    generate_image_from_prompt(headline_text, output_path=ai_image_path)
    ai_image = ImageClip(ai_image_path).set_duration(actual_duration).resize(width=500).set_position(("center", "center"))

    # Scrolling headline text
    text_clip = TextClip(
        txt=headline_text,
        fontsize=40,
        font='Arial-Bold',
        color='white',
        method='caption',
        size=(video_width * 3, ticker_height)
    ).set_duration(actual_duration)
    scrolling_text = text_clip.set_position(lambda t: (video_width - t * 150, ticker_y))

    # Combine all clips
    final_video = CompositeVideoClip([background, ai_image, scrolling_text])
    final_video = final_video.set_audio(audio_clip)

    # Export video
    final_video.write_videofile(output_path, fps=24, codec='libx264')
    print(f"✅ Video saved as {output_path}")


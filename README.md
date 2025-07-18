
https://github.com/user-attachments/assets/24c00500-10a5-4a3f-904b-58fdf0432c17
# 🧠 AI News Video Generator 🎬

This is a Python-based AI-powered tool that generates short, engaging news videos from trending headlines. It uses live news content, converts it into a script with AI, generates voiceover and images, and compiles everything into a short video.

---

## 📌 Features

- 📡 Fetches trending news headlines and summaries
- ✍️ Generates a 40–60 second YouTube-style script using OpenRouter (LLM API)
- 🎤 Converts script to audio using TTS
- 🖼️ Creates an AI-generated image based on the news using ClipDrop API
- 🎞️ Combines everything into a professional-looking video using MoviePy and ImageMagick

---

## 📂 Project Structure

```
Ai_video_generator/
│
├── main.py                    # Orchestrates the entire pipeline
├── news_scraper.py           # Fetches trending news (title + content)
├── script_generator.py       # Generates a script from the news
├── tts_generator.py          # Converts script to audio
├── video_creator.py          # Builds the video with scrolling headline and image
├── image_generator.py        # Generates an image using ClipDrop API
│
├── outputs/
│   ├── output.mp3            # Generated voiceover
│   ├── ai_image.jpg          # Generated image
│   └── final_video.mp4       # Final combined video
│
├── requirements.txt
└── README.md
```

---

## 🛠️ Technologies Used

| Feature                  | Tool/API Used                            |
|-------------------------|-------------------------------------------|
| News Fetching           | NewsAPI / scraping methods                |
| Script Generation       | OpenRouter API with `deepseek-r1` model  |
| Text-to-Speech          | TTS (custom)                              |
| Image Generation        | ClipDrop API                              |
| Video Editing           | MoviePy + ImageMagick                     |

---

## 🧪 Sample Output

### 📺 Final Generated Video

https://github.com/yourusername/ai-video-generator/assets/sample_video.mp4  
*Duration: 40–50 seconds*

### 🖼️ AI Generated Image

![AI Generated Image](outputs/ai_image.jpg)

---

## 📋 Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/ai-video-generator
cd ai-video-generator
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add API Keys
Create a `.env` or add to `script_generator.py` and `image_generator.py`:
```bash
OPENROUTER_API_KEY=your_key_here
CLIPDROP_API_KEY=your_key_here
```

### 4. Run the Project
```bash
python main.py
```

---

## 📑 Output Files

- `output.mp3` – TTS audio file
- `ai_image.jpg` – AI-generated news-relevant image<img width="1024" height="1024" alt="ai_image" src="https://github.com/user-attachments/assets/80c015fa-55a0-45da-ab80-3cdd12988c84" />

- `final_video.mp4` – Combined news video with audio, image, and title

https://github.com/user-attachments/assets/51868b73-0b18-4d21-9e53-4f0fdcf75e72



---

## 📘 Report Included

See attached **AI_Video_Generator_Report.docx** for step-by-step explanation.

---

## 🙌 Acknowledgements

- [OpenRouter](https://openrouter.ai/)
- [ClipDrop](https://clipdrop.co/)
- [MoviePy](https://zulko.github.io/moviepy/)
- [ImageMagick](https://imagemagick.org/)

---

## 🔒 Note

Please do not share API keys publicly. Use environment variables or `.env` files to keep them secure.

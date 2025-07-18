from openai import OpenAI

API_KEY = "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"

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=API_KEY,
)

def generate_script_with_openrouter(title, content):
    try:
        prompt = (
            "You are a professional script writer. "
            "Generate a 40-second YouTube video script based on this news article.\n\n"
            f"Title: {title}\n\nContent: {content}"
        )

        completion = client.chat.completions.create(
            model="deepseek/deepseek-r1-0528-qwen3-8b:free",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
        )

        return completion.choices[0].message.content

    except Exception as e:
        print("Error generating script:", e)
        return None


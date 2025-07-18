import requests

CLIPDROP_API_KEY = "16d5d057418e048ea5f9272167b86e69531d5df13cf2719e139e191dd57be76cf1bb179967ca4ccb908d6e7ab074dd30"  # 🔁 UPDATE THIS

def generate_image_from_prompt(prompt: str, output_path: str = "ai_image.jpg"):
    url = "https://clipdrop-api.co/text-to-image/v1"

    headers = {
        "x-api-key": CLIPDROP_API_KEY
    }

    files = {
        "prompt": (None, prompt, "text/plain")
    }

    print(f"Generating image for prompt: {prompt}")

    try:
        response = requests.post(url, files=files, headers=headers)

        if response.ok:
            with open(output_path, "wb") as f:
                f.write(response.content)
            print(f"Image saved to {output_path}")
        else:
            print("ClipDrop API request failed:", response.status_code)
            print(response.text)

    except Exception as e:
        print(" Exception during image generation:", e)


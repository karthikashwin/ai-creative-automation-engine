from logger import log_generation
import os
import requests
from datetime import datetime
from dotenv import load_dotenv
from prompt_engine import generate_prompt

load_dotenv()

API_TOKEN = os.getenv("HF_API_TOKEN")

if not API_TOKEN:
    raise ValueError("HF_API_TOKEN not found in .env file")

headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

API_URL = "https://router.huggingface.co/hf-inference/models/stabilityai/stable-diffusion-xl-base-1.0"


def run_campaign(campaign_name, base_theme, num_images=5):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    campaign_folder = f"campaigns/{campaign_name}_{timestamp}"
    os.makedirs(campaign_folder, exist_ok=True)

    print(f"Starting campaign: {campaign_name}")
    print(f"Generating {num_images} images...\n")

    for i in range(num_images):
        prompt = generate_prompt(base_theme)

        payload = {
            "inputs": prompt
        }

        response = requests.post(API_URL, headers=headers, json=payload)

        if response.status_code == 200:
            image_path = os.path.join(campaign_folder, f"image_{i+1}.png")

            with open(image_path, "wb") as f:
                f.write(response.content)

            print(f"Saved: {image_path}")
            log_generation(campaign_name, prompt, image_path)
        else:
            print(f"Error {response.status_code}: {response.text}")

    print("\nCampaign complete!")
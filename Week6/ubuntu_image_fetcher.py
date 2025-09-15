#imports
import requests
import os
from urllib.parse import urlparse
from hashlib import md5

def fetch_image(url):
    """Fetch and save a single image from a URL safely."""
    try:
        # Create directory if it doesn't exist
        os.makedirs("Fetched_Images", exist_ok=True)

        # Add headers to mimic a browser (some servers block scripts)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }

        # Fetch the image
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise exception for HTTP errors

        # Check Content-Type to ensure it's an image
        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            print(f"✗ Skipped URL (not an image): {url}")
            return

        # Optional: Check Content-Length to avoid huge files (e.g., >10MB)
        content_length = response.headers.get("Content-Length")
        if content_length and int(content_length) > 10_000_000:
            print(f"⚠ Skipped large image (>10MB): {url}")
            return

        # Extract filename from URL or generate one using hash
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        if not filename:
            filename = f"image_{md5(url.encode()).hexdigest()}.jpg"

        # Prevent duplicate downloads
        filepath = os.path.join("Fetched_Images", filename)
        if os.path.exists(filepath):
            print(f"⚠ Image already exists: {filename}")
            return

        # Save image in binary mode
        with open(filepath, 'wb') as f:
            f.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
    except Exception as e:
        print(f"✗ An unexpected error occurred: {e}")

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Prompt for multiple URLs separated by commas
    urls = input("Enter image URL(s), separated by commas: ").split(',')

    for url in urls:
        url = url.strip()  # Remove leading/trailing whitespace
        if url:
            fetch_image(url)

    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()

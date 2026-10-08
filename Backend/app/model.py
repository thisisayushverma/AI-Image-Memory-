from ollama import chat

image_path = r"C:\Users\devil\OneDrive\Pictures\Travel\rajghat\IMG-20241102-WA0025.jpg"

response = chat(
    model="qwen3-vl:2b-instruct",
    messages=[
        {
            "role": "user",
            "content": """
                Analyze this image and provide a detailed description in English.

                Include:
                1. Scene description
                2. Important objects
                3. Environment
                4. Lighting and time of day
                5. Activities or events
                6. Visible text
                7. Overall context
                8. Useful search keywords
                """,
            "images": [image_path],
        }
    ],
    options={
        "num_ctx": 8192,
        "temperature": 0.2,
        "num_predict": 500,
    },

)


print(response)
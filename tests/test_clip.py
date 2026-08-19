from pathlib import Path

import torch
import open_clip
from PIL import Image


def main():

    print("=" * 60)
    print("Loading OpenCLIP...")
    print("=" * 60)

    device = "cuda" if torch.cuda.is_available() else "cpu"

    model, _, preprocess = open_clip.create_model_and_transforms(
        model_name="ViT-B-32",
        pretrained="openai",
        device=device,
    )

    tokenizer = open_clip.get_tokenizer("ViT-B-32")

    image_path = Path("test_images/chair.jpg")

    image = preprocess(
        Image.open(image_path)
    ).unsqueeze(0).to(device)

    labels = [
        "chair",
        "table",
        "laptop",
        "car",
        "bicycle",
        "sofa",
        "television",
        "bed",
    ]

    text = tokenizer(
        [f"a photo of a {label}" for label in labels]
    ).to(device)

    with torch.no_grad():

        image_features = model.encode_image(image)
        text_features = model.encode_text(text)

        image_features /= image_features.norm(dim=-1, keepdim=True)
        text_features /= text_features.norm(dim=-1, keepdim=True)

        similarity = (100.0 * image_features @ text_features.T)

        probabilities = similarity.softmax(dim=-1)

    best = probabilities.argmax().item()

    print()
    print("=" * 60)
    print("Prediction")
    print("=" * 60)

    print(f"Label      : {labels[best]}")
    print(f"Confidence : {probabilities[0][best].item():.4f}")

    print("=" * 60)


if __name__ == "__main__":
    main()
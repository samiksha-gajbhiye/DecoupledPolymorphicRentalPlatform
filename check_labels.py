from transformers import AutoModelForImageClassification
model = AutoModelForImageClassification.from_pretrained(
    "Smogy/SMOGY-Ai-images-detector",
    cache_dir="models/authenticity",
)
print(model.config.id2label)
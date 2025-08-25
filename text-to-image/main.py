from diffusers import StableDiffusionPipeline
import torch

def generate_image(prompt):
    model_id = "runwayml/stable-diffusion-v1-5"
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float32)
    pipe = pipe.to("cpu")

    image = pipe(prompt,
                num_inference_steps=20,  
                guidance_scale=7.5,      
                width=512,
                height=512).images[0]
    image.save("generated.png")
    print("Image saved as generated.png")

generate_image("A car is flying and fish is dancing")
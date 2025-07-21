import torch
import gradio as gr
from diffusers import AnimateDiffPipeline, MotionAdapter, EulerDiscreteScheduler
from diffusers.utils import export_to_gif
from huggingface_hub import hf_hub_download
from safetensors.torch import load_file

device = "cuda"
dtype = torch.float16
step = 4  # Options: [1,2,4,8]
repo = "ByteDance/AnimateDiff-Lightning"
ckpt = f"animatediff_lightning_{step}step_diffusers.safetensors"
base = "emilianJR/epiCRealism"

adapter = MotionAdapter().to(device, dtype)
adapter.load_state_dict(load_file(hf_hub_download(repo, ckpt), device=device))

# Load AnimateDiff pipeline
pipe = AnimateDiffPipeline.from_pretrained(base, motion_adapter=adapter, torch_dtype=dtype).to(device)
pipe.scheduler = EulerDiscreteScheduler.from_config(pipe.scheduler.config, timestep_spacing="trailing", beta_schedule="linear")

def generate_animation(prompt):
    output = pipe(prompt=prompt, guidance_scale=1.0, num_inference_steps=step)
    gif_path = "animation.gif"
    export_to_gif(output.frames[0], gif_path)
    return gif_path

interface = gr.Interface(
    fn=generate_animation,
    inputs=gr.Textbox(label="Prompt", placeholder="e.g. A girl smiling"),
    outputs=gr.Image(type="filepath", label="Generated Animation (GIF)"),
    title="AniFusion",
    description="Generate motion-animated GIFs from prompts using AniFusion"
)
interface.launch(debug=True, share=True)

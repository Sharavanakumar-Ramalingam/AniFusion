# 🎞️ AniFusion – Prompt-to-Animation Generator

AniFusion is an AI-based application that generates motion-animated GIFs from simple natural language prompts. It leverages the AnimateDiff Lightning model pipeline and diffusion-based video generation to bring your ideas to life with motion. The app is built using PyTorch, Hugging Face diffusers, and Gradio for an interactive interface.

---

## 📁 Project Structure

anifusion/  
├── main.py                  # Core Python script with AnimateDiff pipeline  
├── requirements.txt         # Python dependencies  

---

## 🚀 Features

🎨 Turn text prompts into animated GIFs  
💡 Powered by AnimateDiff Lightning  
⚡ Fast generation using GPU and 4-step diffusion  
🎛️ Clean and responsive Gradio interface  
📁 Saves output as downloadable .gif file  

---

## ⚙️ Technologies Used

- Python 3.10+  
- PyTorch  
- diffusers (Hugging Face)  
- safetensors  
- huggingface_hub  
- Gradio  

---

## 🧪 Installation & Running Locally

1. Clone the repository  
git clone https://github.com/Sharavanakumar-Ramalingam/AniFusion.git  
cd anifusion  

2. Create and activate virtual environment (optional)  
python -m venv venv  
source venv/bin/activate (Linux/macOS) or venv\Scripts\activate (Windows)  

3. Install dependencies  
pip install -r requirements.txt  

4. Run the app  
python main.py  

Gradio will launch the interface at  
http://127.0.0.1:7860 or provide a public `gradio.live` link  

---

## 🧠 How It Works

The app uses AnimateDiff Lightning from the ByteDance repository and loads motion weights from Hugging Face using safetensors.  
The user enters a prompt, which is processed by the AnimateDiffPipeline with a 4-step inference scheduler.  
The output frames are exported as an animated `.gif` using the export_to_gif utility and displayed to the user.  

MotionAdapter enables the model to create dynamic temporal changes in the image frames to produce realistic animation results.  

---

## 📜 requirements.txt

torch  
gradio  
diffusers  
transformers  
accelerate  
huggingface_hub  
safetensors  

These can be copied into a requirements.txt file and installed with pip.  

---

## 🙏 Acknowledgements

- ByteDance for AnimateDiff Lightning  
- Hugging Face diffusers team  
- safetensors for fast checkpoint loading  
- Gradio for easy web UI  

---

## 👨‍💻 Author

Sharavanakumar Ramalingam  
> Built as a generative animation experiment using the latest open models  

---

## 🌟 Support

If you found this project helpful, consider starring it on GitHub:  
https://github.com/your-username/anifusion

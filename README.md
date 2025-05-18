# **Miku Voice Assistant** 🎤✨  
*A cute anime-style virtual assistant for Raspberry Pi*  

![Miku Assistant Demo](demo.gif) *(Example: Replace with actual demo image)*  

---

## **Features** 🌟  
- 🎙️ **Voice-controlled** (Wake word: "Miku")  
- 🤖 **AI-powered responses** (OpenAI GPT-3.5)  
- 🎵 **Anime-style voice & personality**  
- 🖥️ **Optimized for Raspberry Pi**  

---

## **Installation Guide** ⚙️  

### **1. Prerequisites**  
- **Raspberry Pi 3/4/5** (Recommended: **RPi 4+** for best performance)  
- **Microphone** (USB recommended for better clarity)  
- **Speaker** (3.5mm or HDMI audio)  
- **OpenAI API Key** ([Get one here](https://platform.openai.com/api-keys))  

---

### **2. Setup Raspberry Pi**  
#### **Update System**  
```bash
sudo apt update && sudo apt upgrade -y
```

#### **Install Dependencies**  
```bash
sudo apt install python3 python3-pip portaudio19-dev libasound2-dev espeak -y
```

---

### **3. Clone & Configure the Project**  
```bash
git clone https://github.com/yourusername/miku-voice-assistant.git
cd miku-voice-assistant
```

#### **Set Up Environment Variables**  
1. Create a `.env` file:  
   ```bash
   nano .env
   ```
2. Add your OpenAI API key:  
   ```plaintext
   OPENAI_API_KEY=your_api_key_here
   ```
3. Save (`Ctrl+X` → `Y` → `Enter`).  

---

### **4. Install Python Libraries**  
```bash
pip3 install -r requirements.txt
```
*(If `requirements.txt` doesn't exist, install manually:)*  
```bash
pip3 install speechrecognition pyttsx3 openai python-dotenv gtts playsound
```

---

### **5. Run Miku Assistant**  
```bash
python3 miku_assistant.py
```
- **Say "Miku"** to activate! 🎤  
- Ask your question after the beep.  

---

## **Troubleshooting** 🔧  

| Issue | Solution |
|-------|----------|
| **Microphone not detected** | Run `alsamixer` and unmute mic |
| **Slow responses** | Use `gpt-3.5-turbo-instruct` in code |
| **PyAudio errors** | Install manually: `pip3 install pyaudio --no-cache-dir` |
| **Voice too robotic** | Try `gTTS` (Google TTS) instead of `pyttsx3` |

---

## **Auto-Start on Boot (Optional)**  
To launch Miku automatically:  
1. Edit `rc.local`:  
   ```bash
   sudo nano /etc/rc.local
   ```
2. Add before `exit 0`:  
   ```bash
   su - pi -c "python3 /home/pi/miku-voice-assistant/miku_assistant.py &"
   ```
3. Reboot:  
   ```bash
   sudo reboot
   ```

## **License** 📜  
MIT License - Free for personal & commercial use.  

**Made with ❤️ by [HARSHIL GAUTAM]**  



Would you like me to add a **FAQ section** or **more customization tips**? 😊

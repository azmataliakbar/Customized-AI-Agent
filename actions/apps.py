# actions/apps.py
import subprocess
import os

def open_application(command: str):
    command = command.lower()

    if "word" in command:
        subprocess.Popen(["start", "winword"], shell=True)
        return "AI Agent, Opening Microsoft Word..."

    elif "excel" in command:
        subprocess.Popen(["start", "excel"], shell=True)
        return "AI Agent, Opening Microsoft Excel..."

    elif "outlook" in command:
        subprocess.Popen(["start", "outlook"], shell=True)
        return "AI Agent, Opening Microsoft Outlook..."

    elif "notepad" in command:
        subprocess.Popen(["notepad"])
        return "AI Agent, Opening Notepad..."

    elif "calculator" in command or "calc" in command:
        subprocess.Popen(["calc"])
        return "AI Agent, Opening Calculator..."

    elif "whatsapp" in command:
        try:
            # Try launching WhatsApp using the App URI (Microsoft Store app)
            subprocess.run([
                "powershell", "-Command",
                "Start-Process 'shell:AppsFolder\\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App'"
            ], check=True)
            return "AI Agent, Opening WhatsApp ..."
        except subprocess.CalledProcessError:
            # Fallback: Try opening WhatsApp using direct path (if installed manually)
            fallback_path = r"C:\Users\WWW.SZLAIWIIT.COM\AppData\Local\Packages\5319275A.WhatsAppDesktop_cv1g1gvanyjgm\WhatsApp\WhatsApp.exe"
            if os.path.exists(fallback_path):
                subprocess.Popen([fallback_path])
                return "Opening WhatsApp via fallback path..."
            else:
                return "WhatsApp is not installed at the default location."

    else:
        return "Application not recognized."


import chainlit as cl
import re
import os
import shutil
from actions.apps import open_application
from actions.webs import open_website
from actions.files import (create_folder, delete_folder, delete_folder_recursive, move_folder, list_folder_contents, folder_exists,rename_folder)

from actions.translate import translate_text
from actions.weather import get_weather

@cl.on_chat_start
async def start():
    # Main Headings
    await cl.Message(
        content=(
            "✨🌟 ***Welcome from Azmat Ali*** 🌟✨\n"
            "🤖 **AI Agent with Customized Services.** 🤖\n\n"
            "---\n"
            "📁 **1. Folder & File Operations** 📁\n"
            "`create folder`, `rename folder`, `move folder`, `list folder contents`, `folder exists`, `delete folder`, `create file note1.txt`, `create file report1.docx`\n\n"
            "💻 **2. Apps** 💻\n"
            "`word`, `excel`, `outlook`, `notepad`, `calculator`, `WhatsApp`\n\n"
            "🌐 **3. Webs** 🌐\n"
            "`youtube`, `facebook`, `googlemap`, `google`, `linkedin`, `chatgpt`, `gemini`, `deepseek`, `yahoo`, `hotmail`, `gmail`, `twitter`, `giais`, `draz`\n\n"
            "☁️ **4. Weather** ☁️\n"
            "`weather London`, `weather Berlin`, `weather Kualalumpur`, etc.\n\n"
            "🌍 **5. Translate** 🌍\n"
            "`translate welcome to Karachi to Arabic`, `... to Japanese`, `... to Russian`, `... to Korean`\n"
            "\n\n\n✍️🖋️ ***Please type the text in input area*** 🖋️✍️"

        )
    ).send()

FOLDER_NAME = "New Folder"
RENAMED_FOLDER_NAME = "Renamed Folder"
BACKUP_LOCATION = "C:\\Backup"

def create_file(folder_name, file_name):
    try:
        folder_path = os.path.join(os.path.expanduser("~"), "Desktop", folder_name)
        file_path = os.path.join(folder_path, file_name)

        if not os.path.exists(folder_path):
            return f"AI Agent, Folder '{folder_name}' does not exist."

        open(file_path, "w").close()  # This creates an empty file
        return f"AI Agent, File '{file_name}' created in folder '{folder_name}'."
    except Exception as e:
        return f"AI Agent, Error: {str(e)}"

SUPPORTED_WEBSITES = ["youtube", "facebook", "daraz", "yahoo", "hotmail", "gmail", "twitter", "google", "googletranslate", "googlemap", "linkedin", "chatgpt", "gemini", "deepseek", "giaic"]

SUPPORTED_APPS = ["word", "excel", "outlook", "notepad", "calculator", "whatsapp"]

LANG_MAP = {
    "afrikaans": ("af", "Afrikaans"),
    "albanian": ("sq", "Albanian"),
    "amharic": ("am", "Amharic"),
    "arabic": ("ar", "Arabic"),
    "armenian": ("hy", "Armenian"),
    "assamese": ("as", "Assamese"),
    "aymara": ("ay", "Aymara"),
    "azerbaijani": ("az", "Azerbaijani"),
    "bambara": ("bm", "Bambara"),
    "basque": ("eu", "Basque"),
    "belarusian": ("be", "Belarusian"),
    "bengali": ("bn", "Bengali"),
    "bhojpuri": ("bho", "Bhojpuri"),
    "bosnian": ("bs", "Bosnian"),
    "bulgarian": ("bg", "Bulgarian"),
    "catalan": ("ca", "Catalan"),
    "cebuano": ("ceb", "Cebuano"),
    "chichewa": ("ny", "Chichewa"),
    "chinese (simplified)": ("zh-CN", "Chinese (Simplified)"),
    "chinese (traditional)": ("zh-TW", "Chinese (Traditional)"),
    "corsican": ("co", "Corsican"),
    "croatian": ("hr", "Croatian"),
    "czech": ("cs", "Czech"),
    "danish": ("da", "Danish"),
    "dhivehi": ("dv", "Dhivehi"),
    "dogri": ("doi", "Dogri"),
    "dutch": ("nl", "Dutch"),
    "english": ("en", "English"),
    "esperanto": ("eo", "Esperanto"),
    "estonian": ("et", "Estonian"),
    "ewe": ("ee", "Ewe"),
    "filipino": ("tl", "Filipino"),
    "finnish": ("fi", "Finnish"),
    "french": ("fr", "French"),
    "frisian": ("fy", "Frisian"),
    "galician": ("gl", "Galician"),
    "georgian": ("ka", "Georgian"),
    "german": ("de", "German"),
    "greek": ("el", "Greek"),
    "guarani": ("gn", "Guarani"),
    "gujarati": ("gu", "Gujarati"),
    "haitian creole": ("ht", "Haitian Creole"),
    "hausa": ("ha", "Hausa"),
    "hawaiian": ("haw", "Hawaiian"),
    "hebrew": ("iw", "Hebrew"),
    "hindi": ("hi", "Hindi"),
    "hmong": ("hmn", "Hmong"),
    "hungarian": ("hu", "Hungarian"),
    "icelandic": ("is", "Icelandic"),
    "igbo": ("ig", "Igbo"),
    "ilocano": ("ilo", "Ilocano"),
    "indonesian": ("id", "Indonesian"),
    "irish": ("ga", "Irish"),
    "italian": ("it", "Italian"),
    "japanese": ("ja", "Japanese"),
    "javanese": ("jw", "Javanese"),
    "kannada": ("kn", "Kannada"),
    "kazakh": ("kk", "Kazakh"),
    "khmer": ("km", "Khmer"),
    "kinyarwanda": ("rw", "Kinyarwanda"),
    "konkani": ("gom", "Konkani"),
    "korean": ("ko", "Korean"),
    "krio": ("kri", "Krio"),
    "kurdish (kurmanji)": ("ku", "Kurdish (Kurmanji)"),
    "kurdish (sorani)": ("ckb", "Kurdish (Sorani)"),
    "kyrgyz": ("ky", "Kyrgyz"),
    "lao": ("lo", "Lao"),
    "latin": ("la", "Latin"),
    "latvian": ("lv", "Latvian"),
    "lingala": ("ln", "Lingala"),
    "lithuanian": ("lt", "Lithuanian"),
    "luganda": ("lg", "Luganda"),
    "luxembourgish": ("lb", "Luxembourgish"),
    "macedonian": ("mk", "Macedonian"),
    "maithili": ("mai", "Maithili"),
    "malagasy": ("mg", "Malagasy"),
    "malay": ("ms", "Malay"),
    "malayalam": ("ml", "Malayalam"),
    "maltese": ("mt", "Maltese"),
    "maori": ("mi", "Maori"),
    "marathi": ("mr", "Marathi"),
    "meiteilon (manipuri)": ("mni-Mtei", "Meiteilon (Manipuri)"),
    "mizo": ("lus", "Mizo"),
    "mongolian": ("mn", "Mongolian"),
    "myanmar": ("my", "Myanmar"),
    "nepali": ("ne", "Nepali"),
    "norwegian": ("no", "Norwegian"),
    "odia (oriya)": ("or", "Odia (Oriya)"),
    "oromo": ("om", "Oromo"),
    "pashto": ("ps", "Pashto"),
    "persian": ("fa", "Persian"),
    "polish": ("pl", "Polish"),
    "portuguese": ("pt", "Portuguese"),
    "punjabi": ("pa", "Punjabi"),
    "quechua": ("qu", "Quechua"),
    "romanian": ("ro", "Romanian"),
    "russian": ("ru", "Russian"),
    "samoan": ("sm", "Samoan"),
    "sanskrit": ("sa", "Sanskrit"),
    "scots gaelic": ("gd", "Scots Gaelic"),
    "sepedi": ("nso", "Sepedi"),
    "serbian": ("sr", "Serbian"),
    "sesotho": ("st", "Sesotho"),
    "shona": ("sn", "Shona"),
    "sindhi": ("sd", "Sindhi"),
    "sinhala": ("si", "Sinhala"),
    "slovak": ("sk", "Slovak"),
    "slovenian": ("sl", "Slovenian"),
    "somali": ("so", "Somali"),
    "spanish": ("es", "Spanish"),
    "sundanese": ("su", "Sundanese"),
    "swahili": ("sw", "Swahili"),
    "swedish": ("sv", "Swedish"),
    "tajik": ("tg", "Tajik"),
    "tamil": ("ta", "Tamil"),
    "tatar": ("tt", "Tatar"),
    "telugu": ("te", "Telugu"),
    "thai": ("th", "Thai"),
    "tigrinya": ("ti", "Tigrinya"),
    "tsonga": ("ts", "Tsonga"),
    "turkish": ("tr", "Turkish"),
    "turkmen": ("tk", "Turkmen"),
    "twi": ("ak", "Twi"),
    "ukrainian": ("uk", "Ukrainian"),
    "urdu": ("ur", "Urdu"),
    "uyghur": ("ug", "Uyghur"),
    "uzbek": ("uz", "Uzbek"),
    "vietnamese": ("vi", "Vietnamese"),
    "welsh": ("cy", "Welsh"),
    "xhosa": ("xh", "Xhosa"),
    "yiddish": ("yi", "Yiddish"),
    "yoruba": ("yo", "Yoruba"),
    "zulu": ("zu", "Zulu")
}




def is_website_command(content: str) -> bool:
    return any(site in content for site in SUPPORTED_WEBSITES)


def is_application_command(content: str) -> bool:
    return any(app in content for app in SUPPORTED_APPS)


def is_translate_command(content: str) -> bool:
    return "translate" in content


def is_weather_command(content: str) -> bool:
    return "weather" in content


async def handle_translate_command(content: str) -> str:
    try:
        parts = content.split("translate", 1)[1].strip()
        if "to" not in parts:
            return "❗ Please use the format: `translate <text> to <language>`"

        text, lang = parts.rsplit("to", 1)
        lang = lang.strip().lower()

        # Get language code and display name
        lang_code, lang_display = LANG_MAP.get(lang, ("en", "English"))

        return await translate_text(text.strip(), lang_code, lang_display)

    except Exception as e:
        return f"⚠️ Translation error: {e}"



def handle_weather_command(content: str) -> str:
    match = re.search(r'weather(?:.*in)?\s+([a-zA-Z\s]+)', content)
    city = match.group(1).strip() if match else "Lahore"
    return get_weather(city)


@cl.on_message
async def handle_message(message: cl.Message):
    content = message.content.lower()

    try:
        if is_website_command(content):
            response = open_website(content)

        elif is_application_command(content):
            response = open_application(content)

        elif "create folder" in content:
            response = create_folder(FOLDER_NAME)


        elif "create file" in content:
            # Example user input: create file report.docx OR create file notes.txt
            parts = content.split("create file", 1)
            file_name = parts[1].strip() if len(parts) > 1 and parts[1].strip() else "newfile.txt"
            response = create_file(FOLDER_NAME, file_name)


        elif "delete folder" in content:
            if folder_exists(RENAMED_FOLDER_NAME):
                response = delete_folder(RENAMED_FOLDER_NAME)
            elif folder_exists(FOLDER_NAME):
                response = delete_folder(FOLDER_NAME)
            else:
                response = r"AI Agent, Folder not found to delete / Check folder in C:\Backup."

        elif "delete folder recursive" in content or "delete folder with contents" in content:
            response = delete_folder_recursive(RENAMED_FOLDER_NAME)

        elif "move folder" in content:
            target_folders = ["Renamed Folder", "New Folder"]
            for folder_name in target_folders:
                if folder_exists(folder_name):
                    response = move_folder(folder_name, "C:\\Backup")
                    break
            else:
                response = r"AI Agent, Folder not found to move / Check folder on Desktop."

        elif "list folder contents" in content:
            if folder_exists(RENAMED_FOLDER_NAME):
                response = list_folder_contents(RENAMED_FOLDER_NAME)
            elif folder_exists(FOLDER_NAME):
                response = list_folder_contents(FOLDER_NAME)
            else:
                response = r"AI Agent, Folder not found to list / Check folder in C:\Backup."

        elif "folder exists" in content:
            folders_found = []

            if folder_exists(RENAMED_FOLDER_NAME):
                folders_found.append(RENAMED_FOLDER_NAME)
        
            if folder_exists(FOLDER_NAME):
                folders_found.append(FOLDER_NAME)
        
            if folders_found:
                folder_list = ", ".join(folders_found)
                response = f"AI Agent, The following folder(s) exist on Desktop: {folder_list}"
            else:
                response = "AI Agent, No folder found on Desktop."

        elif "rename folder" in content:
            response = rename_folder(FOLDER_NAME, RENAMED_FOLDER_NAME)

        elif is_translate_command(content):
            response = await handle_translate_command(content)

        elif is_weather_command(content):
            response = handle_weather_command(content)

        else:
            response = "❌ Sorry, I don't understand the command."

    except Exception as e:
        response = f"⚠️ An unexpected error occurred: {e}"

    await cl.Message(content=response).send()

# uv run chainlit run main.py -w
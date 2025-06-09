import os
import shutil
from docx import Document

# =============================
# Create folder on Desktop
# =============================
def create_folder(name):
    try:
        path = os.path.join(os.path.expanduser("~"), "Desktop", name)
        os.makedirs(path, exist_ok=True)
        return f"AI Agent, Folder '{name}' created on Desktop."
    except Exception as e:
        return f"AI Agent, Error: {str(e)}"
    
# ==================================
# Create file in folder on Desktop
# ==================================
def create_file(folder_name, file_name):
    try:
        folder_path = os.path.join(os.path.expanduser("~"), "Desktop", folder_name)
        file_path = os.path.join(folder_path, file_name)

        if not os.path.exists(folder_path):
            return f"AI Agent, Folder '{folder_name}' does not exist."

        # Create .txt file
        if file_name.endswith(".txt"):
            with open(file_path, "w") as f:
                f.write("This is a new text file created by AI Agent.")
            return f"AI Agent, Text file '{file_name}' created in folder '{folder_name}'."

        # Create .docx file
        elif file_name.endswith(".docx"):
            doc = Document()
            doc.add_paragraph("This is a new Word document created by AI Agent.")
            doc.save(file_path)
            return f"AI Agent, Word file '{file_name}' created in folder '{folder_name}'."

        else:
            return "AI Agent, Please use either a '.txt' or '.docx' file extension."
        
    except Exception as e:
        return f"AI Agent, Error: {str(e)}"



# =============================
# Delete empty folder on Desktop
# =============================
def delete_folder(name):
    try:
        path = os.path.join(os.path.expanduser("~"), "Desktop", name)
        os.rmdir(path)
        return f"AI Agent, Folder '{name}' deleted from Desktop."
    except Exception as e:
        return f"AI Agent, Error: {str(e)}"

# =============================
# Delete folder with contents
# =============================
def delete_folder_recursive(name):
    try:
        path = os.path.join(os.path.expanduser("~"), "Desktop", name)
        shutil.rmtree(path)
        return f"AI Agent, Folder '{name}' and its contents deleted."
    except Exception as e:
        return f"AI Agent, Error: {str(e)}"

# =============================
# Rename a folder on Desktop
# =============================
def rename_folder(old_name, new_name):
    try:
        desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        old_path = os.path.join(desktop, old_name)
        new_path = os.path.join(desktop, new_name)
        os.rename(old_path, new_path)
        return f"AI Agent, Folder renamed from '{old_name}' to '{new_name}'."
    except Exception as e:
        return f"Error: {str(e)}"

# =============================
# Move folder to another location
# =============================
def move_folder(name, new_location):
    try:
        old_path = os.path.join(os.path.expanduser("~"), "Desktop", name)
        new_path = os.path.join(new_location, name)
        shutil.move(old_path, new_path)
        return f"AI Agent,  Folder '{name}' moved to {new_location}."
    except Exception as e:
        return f"Error: {str(e)}"

# =============================
# List contents of a folder
# =============================
def list_folder_contents(name):
    try:
        path = os.path.join(os.path.expanduser("~"), "Desktop", name)
        items = os.listdir(path)
        return f"AI Agent,  Contents of '{name}': {items}"
    except Exception as e:
        return f"Error: {str(e)}"

# =============================
# Check if a folder exists
# =============================
def folder_exists(name):
    path = os.path.join(os.path.expanduser("~"), "Desktop", name)
    return os.path.isdir(path)



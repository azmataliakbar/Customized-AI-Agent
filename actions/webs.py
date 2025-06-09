import webbrowser

def open_website(command: str):
    if "youtube" in command:
        webbrowser.open("https://www.youtube.com")
        return "AI Agent, Opening YouTube..."
    
    elif "facebook" in command:
        webbrowser.open("https://www.facebook.com")
        return "AI Agent, Opening Facebook..."
    
    elif "googlemap" in command:
        webbrowser.open("https://www.google.com/maps/@24.8642822,67.0501542,469m/data=!3m1!1e3?entry=ttu&g_ep=EgoyMDI1MDYwNC4wIKXMDSoASAFQAw%3D%3D")
        return "AI Agent, Opening Google Map..."
    
    elif "google" in command:
        webbrowser.open("https://www.google.com/")
        return "AI Agent, Opening Google..."
    
    
    elif "linkedin" in command:
        webbrowser.open("https://www.linkedin.com/feed/?legoTrackingToken=c34ZpnFFkTBxr71PqmgCc2UMfmlOrSdjtOoZsC5gr6litOoZp6Zdr6litOoVejAVejRApnhPpnlNpl9JtmUCjAZ9l4BjjR0Zuk9OpmhOjThBpShFtOpHsCZTnSZQnSVBs6ZvcDpAon1EoSVRomMZp4BQpmtAqnsCcjRKrSBQqndLk7hBpShFtOoMbz0Zpn9LoRdOpOoZsC5gr6lisCsCfmhLjmNBkD9D9z0ZrCZFt6BPrR1MtmZOpOoVejAVejRApnhPpnlNpl9JtkVMtmZOpOpPrCZFt6dxfmh9s7lLsCsCjAZ9l4BjjR0Zuk9OpmhOrOpQr7lxpClAfmh9t6VBrmtBsOpPoCZGfmh9t6ZIsOpQr7lxpClAfmh9t7lLum5I9z9Sp65Mq6dKtm5IfmlJokVBpS5M9CxQtSZOpPRAin1MoioUdj0PejRAimVLqndOpnoCcjsUdj4Sd3wNfmh9tioVejxxcm8PdChCcz0Jpz4Se2QUejwQbjwUdCkJpC4Pp3cNd3wZp4BQu6lQrCZz&trk=opento_lp")
        return "AI Agent, Opening Linkedin..."
    
    elif "chatgpt" in command:
        webbrowser.open("https://chatgpt.com/")
        return "AI Agent, Opening ChatGpt..."
    
    elif "gemini" in command:
        webbrowser.open("https://gemini.google.com/app")
        return "AI Agent, Opening Gemini..."
    
    elif "deepseek" in command:
        webbrowser.open("https://chat.deepseek.com/")
        return "AI Agent, Opening DeepSeek..."
    
    elif "yahoo" in command:
        webbrowser.open("https://mail.yahoo.com/n/inbox/priority?.src=ym&reason=myc")
        return "AI Agent, Opening Yahoo..."
    
    elif "hotmail" in command:
        webbrowser.open("https://mail.yahoo.com/n/inbox/priority?.src=ym&reason=myc&listFilter=PRIORITY&accountIds=1")
        return "AI Agent, Opening Hotmail..."
    
    elif "gmail" in command:
        webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
        return "AI Agent, Opening Gmail..."
    
    elif "twitter" in command:
        webbrowser.open("https://x.com/home")
        return "AI Agent, Opening Twitter..."
    
    elif "giaic" in command:
        webbrowser.open("https://portal.governorsindh.com/home")
        return "AI Agent, Opening GIAIS Portal..."
    
    elif "daraz" in command:
        webbrowser.open("https://www.daraz.pk/#?")
        return "AI Agent, Opening Daraz..."
    
    else:
        return "Website not recognized."


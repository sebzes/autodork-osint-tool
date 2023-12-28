import os
import webbrowser
import unicodedata
import time
import keyboard

choicesYes = ["yes", "y"]
choicesNo = ["no", "n"]

def osint(keyword):
    defaultIGramNames = []
    fileTypeSearch = f'https://www.google.com/search?q="{keyword}"+filetype:xlsx+OR+filetype:docx+OR+filetype:pdf'
    inTextSearch = f'https://www.google.com/search?q=intext:"{keyword}"'
    facebookSearch = f'https://www.google.com/search?q=site:facebook.com+intext:"{keyword}"'
    facebookProfileSearch = f'https://www.facebook.com/search/top/?q={keyword}'
    oldKeyword = str(keyword)
    oldKeyword = oldKeyword.lower()
    
    # Tisztítás az ékezetek és írásjelek eltávolításával > basic username-ekhez
    oldKeyword = ''.join(c for c in unicodedata.normalize('NFD', oldKeyword) if unicodedata.category(c) != 'Mn')
    oldKeyword = ''.join(e for e in oldKeyword if e.isalnum() or e.isspace())
    
    if " " in oldKeyword: # basic instagram username-ek generálása
        oldKeyword = oldKeyword.replace(" ", ".") # space > .
        defaultIGramNames.append(oldKeyword)
        oldKeyword = oldKeyword.replace(".", "_") # . > _
        defaultIGramNames.append(oldKeyword)
        oldKeyword = oldKeyword.replace("_", "__") # _ > __
        defaultIGramNames.append(oldKeyword)

    instagramProfileSearch = f'https://www.google.com/search?q=site:instagram.com+intext:{oldKeyword}'
    webbrowser.open(fileTypeSearch)
    webbrowser.open(inTextSearch)
    webbrowser.open(facebookSearch)
    webbrowser.open(facebookProfileSearch)
    print(f"Default instagram names:",*defaultIGramNames,''.join(", "))
    print(f"URL's searched:\n{fileTypeSearch}\n{inTextSearch}\n{facebookSearch}\n{facebookProfileSearch}")
    print(f"\nOSINT to {keyword} is done!")

def advancedResearchEngine(keyword):
    chatGPTurl = "https://chat.openai.com"
    print("\nWould you like to search for Excel (.xlsx), Word (.docx) or Portable Document Format (.pdf) documents?")
    documentsChoice = str(input("Choice > "))
    documentsChoice = documentsChoice.lower()
    while documentsChoice not in choicesYes and documentsChoice not in choicesNo:
        print("[!] Bad input, try again.")
        documentsChoice = str(input("Choice > "))
    if documentsChoice in choicesYes:
        print("Yes")
    if documentsChoice in choicesNo:
        print("No")

    print("\nAre you logged in to your OpenAI account and has your password been saved?")
    chatGPTdata = str(input("Choice > ")) # Ha igen, akkor chatGPT-t is használ
    chatGPTdata = chatGPTdata.lower()
    while chatGPTdata not in choicesYes and chatGPTdata not in choicesNo:
        print("[!] Bad input, try again.")
        chatGPTdata = str(input("Choice > "))
    
    # URL-ek amikre rá fog, vagy lehetséges, hogy rá fog keresni
    fileTypeSearch = f'https://www.google.com/search?q="{keyword}"+filetype:xlsx+OR+filetype:docx+OR+filetype:pdf'
    inTextSearch = f'https://www.google.com/search?q=intext:"{keyword}"'
        
    urlsSeachedMessage = f"\nURL's searched:\n{fileTypeSearch}\n{inTextSearch}\n{chatGPTurl}"
    if chatGPTdata in choicesYes:
        chatGPTdata = True
    if chatGPTdata in choicesNo:
        chatGPTdata = False
        urlsSeachedMessage = urlsSeachedMessage.replace(f"\n{chatGPTurl}", "")
    if documentsChoice in choicesYes:
        webbrowser.open(fileTypeSearch)
    if documentsChoice in choicesNo:
        urlsSeachedMessage = urlsSeachedMessage.replace(f"{fileTypeSearch}\n", "")

    # Opening browser tabs
    webbrowser.open(inTextSearch)
    if chatGPTdata == True:
        webbrowser.open(chatGPTurl)
        time.sleep(5)
        keyboard.write(f"Give me informations about {keyword}")
        keyboard.press_and_release("enter")
    print(urlsSeachedMessage) # URL's cached
    print(f"\nAdvanced Researching to {keyword} is done!")

os.system('cls')

print('''
                        ╭──────────────────────────────────╮
                        │     [1] OSINT                    │
                        │     [2] Advanced Research Engine │
                        │                                  │
                        │       author's discord:          │
                        │         zalan_l_rizz             │
                        ╰──────────────────────────────────╯
''')

choice = int(input("Choice > "))

while choice < 1 or choice > 2:
    print("[!] Bad input, try again.")
    choice = int(input("Choice > "))

if choice == 1:
    print('''
        -----------------------------------------------------------
    
                                    OSINT
    
        -----------------------------------------------------------
        ''')
    osint(input("\nSearch > ")) # OSINT Search

else:
    print('''
        -----------------------------------------------------------
    
                         Advanced Research Engine
    
        -----------------------------------------------------------
        ''')
    advancedResearchEngine(input("\nSearch > "))

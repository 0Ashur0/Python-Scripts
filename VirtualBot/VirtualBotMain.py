import Assistant


#Intialisation
keyboard =  Assistant.Controller()
engine = Assistant.pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

if __name__ == "__main__":
    Assistant.wishMe()
    while True:

        text = Assistant.takeCommand().lower()
        if 'ashbot' in text:
            text = text.replace("ashbot" , "")
            joke = Assistant.pyjokes.get_joke()
            if 'search on wikipedia' in text:
                Assistant.speak('Searching Wikipedia...')
                text = text.replace("search on wikipedia", "")
                results = Assistant.wikipedia(text)
                Assistant.speak("According to Wikipedia")
                print(results)
                Assistant.speak(results)

            elif 'open youtube' in text:
                Assistant.openLink("www.youtube.com")

            elif 'open google' in text:
                Assistant.openLink("https://google.com")

            elif 'search on google' in text:
                Assistant.speak('what do you want to serch')
                content = Assistant.takeCommand()
                Assistant.search(content)

            elif 'open facebook' in text:
                Assistant.openLink("https://facebook.com")

            elif 'play dad favourite song' in text or "play dad's favourite song" in text:
                Assistant.openLink("https://www.youtube.com/watch?v=lLh424CadXc")


            elif 'play a song' in text:
                song = Assistant.takeCommand()
                Assistant.speak('playing ' + song)
                Assistant.playonyt(song)

            elif 'play on youtube' in text:
                Assistant.speak('what do you want me to play')
                video = Assistant.takeCommand()
                Assistant.speak('playing ' + video)
                Assistant.playonyt(video)

            elif 'time' in text:
                Assistant.speak(f"Sir, the time is {Assistant.time()}")

            elif 'open brave' in text:
                Assistant.openApp('brave.exe')

            elif 'close brave' in text:
                Assistant.cmdCommand("TASKKILL /F /IM brave.exe /T")

            elif 'covid cases' in text:
                Assistant.search('covid cases')

            elif 'abc news' in text:
                Assistant.openLink('https://abcnews.go.com')

            elif 'type' in text:
                Assistant.speak('what do you want me to type')
                message = Assistant.takeCommand()
                Assistant.type(message)

            # elif 'text selector' in text:
            #     speak('how much words to select')
            #     NUM = takeCommand()
            #     NUM = int(NUM)
            #     Nothing = 0
            #     while Nothing < NUM:
            #         keyboard.press(Key.ctrl)
            #         keyboard.press(Key.shift)
            #         keyboard.press(Key.left)
            #         Nothing = Nothing + 1

            elif 'press enter' in text:
                Assistant.press(Assistant.Key.enter)

            elif 'screenshot' in text:
                myScreenshot = Assistant.pyautogui.screenshot()
                myScreenshot.save(r'C:\Users\dawoo\Pictures\Screenshots\screenshot.png')

            elif 'screen select'in text:
                Assistant.snipingTool()

            elif 'desktop' in text:
                Assistant.desktop()

            elif 'delete all' in text:
                Assistant.deleteAll()

            elif 'select all' in text:
                Assistant.selectAll()

            elif 'delete' in text:
                Assistant.delete()

            elif 'copy text' in text:
                Assistant.copyText()

            elif 'paste text' in text:
                Assistant.pasteText()

            elif 'close tab' in text:
                Assistant.closeTab()

            elif 'open opera' in text:
                Assistant.openApp('opera.exe')

            elif 'close opera' in text:
                Assistant.cmdCommand("TASKKILL /F /IM opera.exe /T")

            elif 'open word' in text:
                Assistant.openApp('winword.exe')

            elif 'close word' in text:
                Assistant.cmdCommand("TASKKILL /F /IM winword.exe /T")

            elif 'shut down' in text:
                Assistant.cmdCommand(["shutdown /s"])
                Assistant.press(Assistant.Key.enter)

            elif 'joke' in text:
                print(joke)
                Assistant.speak(joke)

            elif 'see you later' in text or 'goodbye' in text or 'goodnight' in text:
                Assistant.speak('byeee')
                exit()
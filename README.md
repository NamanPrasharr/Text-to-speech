# Text-to-Speech Program

## Overview
This is a simple Python program that converts text input into speech using the `pyttsx3` library. The program runs in a loop, allowing users to enter text, which is then spoken aloud. Users can exit the program by entering 'q'.

## Features
- Converts user input text into speech
- Uses `pyttsx3`, which works offline
- Continuous input loop for multiple speech outputs
- Exit the program by entering 'q'

## Prerequisites
Ensure you have Python installed on your system. You also need to install `pyttsx3`:
```sh
pip install pyttsx3
```

## Installation & Usage
1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/text-to-speech.git
   cd text-to-speech
   ```
2. Run the script:
   ```sh
   python text_to_speech.py
   ```
3. Enter the text you want the program to speak. To exit, type `q`.

## Code Explanation
```python
import pyttsx3  

engine = pyttsx3.init()  

if __name__ == '__main__':
    while True:
        print("Welcome to text-to-speech program by Naman")
        x = input("Enter what you want me to speak: ")
        if x == "q":
            engine.say("Bye bye friend")
            engine.runAndWait()
            break
        engine.say(x)
        engine.runAndWait()
```
### How It Works
- Initializes the `pyttsx3` engine.
- Runs an infinite loop, prompting the user for input.
- Converts the input text into speech.
- If the user enters 'q', the program says "Bye bye friend" and exits.

## Contributions
Feel free to contribute by creating issues or submitting pull requests.

## License
This project is licensed under the MIT License.

---
Let me know if you want any modifications! 🚀

# Text-to-speech

# Chat Bot

Uses OpenAI GPT2 with a language model head provided by hugging face transformers to 
predict human-like response given a human speech input. Initial speech to text uses Google's
Speech Recognition API while the text to speech conversion makes use of Google's Text To Speech API.


## 1. Python packages
<p>python == v3.9</p>
To install packages, git clone the repo. Open command prompt and navigate to the root dir of 
where the repo is stored. In the command prompt type:
<code>pip install -r requirements.txt</code>
<br>

## 2. Running the Bot
Open command prompt and navigate to where the repo is stored and type:<code>python main.py</code>

There are options to select different model sizes<br>
small: <code>python main.py --s small</code><br>
medium: <code>python main.py --s medium</code><br>
large: <code>python main.py --s large</code><br>

Greet Bot by saying:  *'Hey Kai'*

To exit loop press 'esc' key, else it will leave the loop after 10 input-response loops

## 3. Optimal conditions
Best used in places with lower background noise

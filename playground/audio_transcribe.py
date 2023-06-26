import whisper
import traceback
try:
    model = whisper.load_model('base')
    result = model.transcribe(
        './_output/mp3/myaudio.mp3', fp16=False)

    with open('./_output/mp3/myaudio.txt', 'w') as f:
        text = result['text']
        f.write(text)

except FileNotFoundError as e:
    print("File not found error:", e)
    traceback.print_exc()

except Exception as e:
    print("An error occurred:", e)

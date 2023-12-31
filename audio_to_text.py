import io

import librosa
import numpy as np
import soundfile
import torch
import wavfile
from IPython.display import Audio
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor, Wav2Vec2Tokenizer


def audio_to_text(audio_data, tokenizer, model):
    """
    Transcribes an audio file into text using the Wav2Vec2 model.

    Args:
        None

    Returns:
        str: The transcribed text from the audio file.

    """

    # Read the audio file "audio.wav"
    # audio_path = "audio.wav"
    # audio_data, sample_rate = librosa.core.load(io.BytesIO(audio_recording), sr=16000) #soundfile.read(audio_path)

    # Resample audio file 
    # target_sample_rate = 16000
    # audio_data_resampled = librosa.resample(y=audio_data, orig_sr=sample_rate, target_sr=target_sample_rate)

    # Tokenize input audio, return tensors
    input_values = tokenizer(audio_data, return_tensors="pt").input_values
    logits = model(input_values).logits

    predicted_ids = torch.argmax(logits, dim=-1)
    text = tokenizer.batch_decode(predicted_ids)[0]
    text = text.lower()

    return text


def audio_to_text_our_model(audio_data, tokenizer, model):
    """
    Transcribes an audio file into text using our finetuned Wav2Vec2 model.

    Returns:
    str: The transcribed text from the audio file.
    """
    # Read the audio file "audio.wav"
    # audio_path = "audio.wav"
    # waveform, sample_rate = librosa.core.load(io.BytesIO(audio_recording), sr=16000) #soundfile.read(audio_path)

    # target_sample_rate = 16000
    # audio_data_resampled = librosa.resample(y=waveform, orig_sr=sample_rate, target_sr=target_sample_rate)

    # Preprocess the audio file
    # input_values = tokenizer(waveform, return_tensors="pt").input_values

    # # Ensure model is in evaluation mode and move tensors to appropriate device
    # model.eval()
    # input_values = input_values.to(torch.device("cuda" if torch.cuda.is_available() else "cpu"))

    # # Obtain the model's logits
    # with torch.no_grad():
    #     logits = model(input_values).logits

    # # Identify the predicted tokens
    # predicted_ids = torch.argmax(logits, dim=-1)

    # # Decode the ids to text
    # transcription = tokenizer.batch_decode(predicted_ids)[0]

    # transcription = transcription.lower()
    input_values = tokenizer(audio_data, return_tensors="pt").input_values
    logits = model(input_values).logits

    predicted_ids = torch.argmax(logits, dim=-1)
    text = tokenizer.batch_decode(predicted_ids)[0]
    text = text.lower()

    return text

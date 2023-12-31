import librosa
import soundfile
import streamlit as st
from audio_to_text import audio_to_text, audio_to_text_our_model
from st_audiorec import st_audiorec
from scipy.io import wavfile
import io
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor, Wav2Vec2Tokenizer

st.set_page_config(page_title="My webpage", page_icon=":tada:",
                   layout="wide")


st.title("Singaporean English Speech to Text")

# @st.cache(hash_funcs={"MyUnhashableClass": lambda _: None})
          
@st.cache_resource
def load_model():
    tokenizer = Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-base-960h")
    model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")
    model1 = Wav2Vec2ForCTC.from_pretrained('beatrice-yap/wav2vec2-base-nsc-demo-3')

    return tokenizer, model, model1

tokenizer, model, model1 = load_model() 

left_column, right_column = st.columns(2)

with right_column:
    st.markdown(
        f"""
        <img src="https://mustsharenews.com/wp-content/uploads/2019/09/pck-yellow-boots.jpg" width="275" height="600">
        """,
        unsafe_allow_html=True,
    )

with left_column:
    st.subheader("Record an audio:")
    audio_path = "audio.wav"  # Define the path to save the audio file in the current working directory
    audio_recording = st_audiorec() #"Click to record", "Click to stop recording")

    if audio_recording is not None:
        # st.audio(audio_recording, format='audio/wav') 
        # st.audio(audio_recording, format='audio/wav')

    # if len(audio_recording) > 0:
    #     st.audio(audio_recording.export().read())
    #     st.write(f"Frame rate: {audio_recording.frame_rate}, Frame width: {audio_recording.frame_width}, Duration: {audio_recording.duration_seconds} seconds") 
        audio_data, sample_rate = librosa.core.load(io.BytesIO(audio_recording), sr=16000)
        
        try:
            # Open and process the audio file
            # audio_recording.export(audio_path, format="wav")  # Save the recorded audio
            # audio_data, sample_rate = librosa.load(audio_recording, sr=None) #audio_path
            # audio_data, sample_rate = librosa.core.load(io.BytesIO(audio_recording), sr=16000)
            
            text = audio_to_text(audio_data, tokenizer, model)
            st.subheader("Baseline Transcription:")
            st.write(text)
        except Exception as e:
            st.error(f"Error (Baseline Transcription): {str(e)}")

        try:
            #audio_data, sample_rate = librosa.load(audio_path, sr=None)
            text = audio_to_text_our_model(audio_data, tokenizer, model1)
            st.subheader("Transcription:")
            st.write(text)
        except Exception as e:
            st.error(f"Error (Transcription): {str(e)}")




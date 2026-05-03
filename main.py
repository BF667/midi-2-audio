from midi2audio import FluidSynth
import IPython.display as ipd


def main_func(midi_file, soundfont_path):
    # Initialize FluidSynth with your SoundFont
    fs = FluidSynth(sound_font=soundfont_path)
    
    # Convert MIDI to WAV
    output_audio = "output.wav"
    fs.midi_to_audio(midi_file, output_audio)
    print(f"✅ Conversion complete! Audio saved as: {output_audio}")
    return output_audio

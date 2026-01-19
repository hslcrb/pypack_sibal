import sys
import os
import time
import threading
import random
import wave
import struct
import math
import tempfile
import subprocess

def create_siren_wav(filename, duration=2.0, sample_rate=44100):
    """Generates a complex, chaotic 'Symphony of Emergency' (SIBAL Symphonia)."""
    n_samples = int(sample_rate * duration)
    with wave.open(filename, 'w') as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(sample_rate)
        
        # Multiple oscillators for peak chaos
        phase_lead = 0.0
        phase_bass = 0.0
        phase_mod = 0.0
        
        for i in range(n_samples):
            t = i / n_samples
            
            # 1. Screaming Lead (High pitched FM)
            # LFO for frequency wobbling
            mod_freq = 5.0 + 10.0 * math.sin(2.0 * math.pi * t) 
            mod_index = 200.0
            phase_mod += 2.0 * math.pi * mod_freq / sample_rate
            
            # Main lead frequency that rises and falls
            base_freq = 800.0 + 400.0 * math.sin(4.0 * math.pi * t)
            current_lead_freq = base_freq + mod_index * math.sin(phase_mod)
            phase_lead += 2.0 * math.pi * current_lead_freq / sample_rate
            # Harmonic richness using saw-like wave via multiple sines
            lead_wave = (math.sin(phase_lead) + 0.5 * math.sin(2 * phase_lead) + 0.3 * math.sin(3 * phase_lead))
            
            # 2. Distorted Sub-Bass (Deep growl)
            bass_freq = 50.0 + 20.0 * math.sin(8.0 * math.pi * t)
            phase_bass += 2.0 * math.pi * bass_freq / sample_rate
            # Distortion via tanh clipping
            bass_wave = math.tanh(5.0 * math.sin(phase_bass)) 
            
            # 3. Chaotic Percussion (Filtered-like noise bursts)
            noise = random.uniform(-1.0, 1.0)
            # High speed gating
            gate = 1.0 if math.sin(64.0 * math.pi * t) > 0.7 else 0.0
            noise_burst = noise * gate * 0.4
            
            # Mix the layers
            mixed = (lead_wave * 0.4) + (bass_wave * 0.4) + (noise_burst * 0.3)
            
            # Hard limiter
            final_val = max(-0.95, min(0.95, mixed))
            sample = int(final_val * 32767)
            wav_file.writeframesraw(struct.pack('<h', sample))

def play_siren_loop(wav_path):
    """Plays the siren sound in a continuous loop."""
    # Try different players commonly found on Linux
    players = ['aplay', 'paplay', 'ffplay', 'vlc']
    player = None
    for p in players:
        if subprocess.run(['which', p], capture_output=True).returncode == 0:
            player = p
            break
            
    if not player:
        # Fallback to terminal bell
        while True:
            sys.stdout.write('\a')
            sys.stdout.flush()
            time.sleep(0.5)
        return

    while True:
        if player == 'aplay':
            subprocess.run(['aplay', '-q', wav_path], capture_output=True)
        elif player == 'paplay':
            subprocess.run(['paplay', wav_path], capture_output=True)
        elif player == 'ffplay':
            subprocess.run(['ffplay', '-nodisp', '-autoexit', wav_path], capture_output=True)
        elif player == 'vlc':
            subprocess.run(['cvlc', '--play-and-exit', wav_path], capture_output=True)
        time.sleep(0.1)

def rainbow_madness(original_excepthook, type, value, traceback):
    """The main emergency handler."""
    # Clear screen
    os.system('clear' if os.name == 'posix' else 'cls')
    
    # Create temp siren file
    temp_dir = tempfile.gettempdir()
    wav_path = os.path.join(temp_dir, "sibal_siren.wav")
    create_siren_wav(wav_path)
    
    # Start siren thread
    siren_thread = threading.Thread(target=play_siren_loop, args=(wav_path,), daemon=True)
    siren_thread.start()
    
    colors = [
        "\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[95m", "\033[96m",
        "\033[1;91m", "\033[1;92m", "\033[1;93m", "\033[1;94m", "\033[1;95m", "\033[1;96m",
        "\033[5;91m", "\033[5;92m", "\033[5;93m" # Blinking
    ]
    reset = "\033[0m"
    
    messages = [
        "SIBAL!!! EMERGENCY!!!",
        "씨발!!! 에러 났다!!!",
        "비상사태! 비상사태!",
        "PYTHON IS DYING!!!",
        "YOUR CODE IS SHIT!!!",
        "SIBAL SIBAL SIBAL!!!",
        "!!!!!!!!!!!!!!!!!",
        "ERRRROOOOOORRRRR!!!!"
    ]
    
    try:
        while True:
            color = random.choice(colors)
            msg = random.choice(messages)
            padding = " " * random.randint(0, 30)
            prefix = "".join(random.choice("!@#$%^&*()_+-=") for _ in range(5))
            suffix = "".join(random.choice("!@#$%^&*()_+-=") for _ in range(5))
            
            # Change background color randomly
            bg_color = f"\033[{random.choice([40, 41, 42, 43, 44, 45, 46, 47])}m"
            
            print(f"{bg_color}{color}{padding}{prefix} {msg} {suffix}{reset}")
            
            # Occasionally print the actual error message in big letters
            if random.random() < 0.05:
                print(f"\n\033[1;41;37m ERROR: {value} \033[0m\n")
                
            # Random screen shakes (just vertical scroll)
            if random.random() < 0.02:
                print("\n" * 5)
                
            time.sleep(random.uniform(0.01, 0.05))
    except KeyboardInterrupt:
        print("\n\033[1;31mSIBAL... YOU ESCAPED...\033[0m")
        sys.exit(1)

def init():
    """Activates the sibal emergency hook."""
    original_hook = sys.excepthook
    sys.excepthook = lambda t, v, tb: rainbow_madness(original_hook, t, v, tb)

# Auto-init on import
init()

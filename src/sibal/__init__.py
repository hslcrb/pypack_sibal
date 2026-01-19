# ⚠️ DISCLAIMER: This package is for prank and stress testing purposes only.
# The creator is not responsible for any noise, visual stimuli, or resulting physical/mental damage.
# Use at your own risk. DO NOT use in public places.
# 면책사항: 이 패키지는 장난 및 스트레스 테스트 목적으로 제작되었습니다.
# 발생하는 소음, 시각적 자극 및 이로 인한 피해에 대해 제작자는 책임을 지지 않습니다.

import sys
import os
import time
import threading
import random
import subprocess

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
    
    # Locate bundled siren file
    package_dir = os.path.dirname(__file__)
    wav_path = os.path.join(package_dir, "hell_symphony.wav")
    
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

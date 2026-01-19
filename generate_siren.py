import wave
import struct
import math
import random
import os

def create_siren_wav(filename, duration=2.0, sample_rate=44100):
    """지옥의 비상 교향곡 (SIBAL Symphonia)을 생성합니다."""
    n_samples = int(sample_rate * duration)
    with wave.open(filename, 'w') as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(sample_rate)
        
        # 멀티 오실레이터 레이어
        phase_lead = 0.0
        phase_bass = 0.0
        phase_mod = 0.0
        
        for i in range(n_samples):
            t = i / n_samples
            
            # 1. 스크리밍 리드 (주파수 변조 고음)
            mod_freq = 5.0 + 10.0 * math.sin(2.0 * math.pi * t) 
            mod_index = 200.0
            phase_mod += 2.0 * math.pi * mod_freq / sample_rate
            
            base_freq = 800.0 + 400.0 * math.sin(4.0 * math.pi * t)
            current_lead_freq = base_freq + mod_index * math.sin(phase_mod)
            phase_lead += 2.0 * math.pi * current_lead_freq / sample_rate
            # 톱니파 느낌을 내기 위해 배음(Harmonics) 추가
            lead_wave = (math.sin(phase_lead) + 0.5 * math.sin(2 * phase_lead) + 0.3 * math.sin(3 * phase_lead))
            
            # 2. 디스토션 베이스 (심장을 울리는 저음)
            bass_freq = 50.0 + 20.0 * math.sin(8.0 * math.pi * t)
            phase_bass += 2.0 * math.pi * bass_freq / sample_rate
            # Tanh 함수를 이용한 강력한 디스토션
            bass_wave = math.tanh(5.0 * math.sin(phase_bass)) 
            
            # 3. 카오틱 노이즈 (불규칙한 기계음 및 노이즈)
            noise = random.uniform(-1.0, 1.0)
            gate = 1.0 if math.sin(64.0 * math.pi * t) > 0.7 else 0.0
            noise_burst = noise * gate * 0.4
            
            # 모든 레이어 믹싱
            mixed = (lead_wave * 0.4) + (bass_wave * 0.4) + (noise_burst * 0.3)
            
            # 리미터 (피크 방지)
            final_val = max(-0.95, min(0.95, mixed))
            sample = int(final_val * 32767)
            wav_file.writeframesraw(struct.pack('<h', sample))
    
    print(f"지옥의 교향곡 '{filename}' 생성 완료!")

if __name__ == "__main__":
    create_siren_wav("hell_symphony.wav")

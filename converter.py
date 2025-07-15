import os
import subprocess

input_folder = "audios-originais"
output_folder = "audios-convertidos"

# Cria a pasta de saída se não existir
os.makedirs(output_folder, exist_ok=True)

# Extensões de entrada suportadas
extensoes_suportadas = (".mp4", ".m4a", ".mp3", ".aac", ".mov", ".flac", ".ogg", ".wav")

# Para cada arquivo na pasta de entrada
for filename in os.listdir(input_folder):
    if filename.lower().endswith(extensoes_suportadas):
        input_path = os.path.join(input_folder, filename)
        nome_base = os.path.splitext(filename)[0]  # Nome sem extensão
        output_filename = f"{nome_base}.wav"
        output_path = os.path.join(output_folder, output_filename)

        # Converter para wav (mono, 16000 Hz)
        command = f'ffmpeg -y -i "{input_path}" -ac 1 -ar 16000 "{output_path}"'
        subprocess.run(command, shell=True)

        print(f"Convertido: {filename} -> {output_filename}")

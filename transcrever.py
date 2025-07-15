import os
import whisper
import ffmpeg
import glob

# Pastas
AUDIO_INPUT_DIR = "audios"  # Pasta para os áudios originais
AUDIO_DIR = "audios-convertidos"  # Pasta para os áudios convertidos em WAV
OUTPUT_DIR = "transcricoes"

# Criar todas as pastas necessárias
os.makedirs(AUDIO_INPUT_DIR, exist_ok=True)
os.makedirs(AUDIO_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

def converter_para_wav():
    # Formatos suportados
    formatos = ['*.mp3', '*.m4a', '*.ogg', '*.wma', '*.aac']
    
    # Procurar por arquivos de áudio em todos os formatos
    arquivos_audio = []
    for formato in formatos:
        arquivos_audio.extend(glob.glob(os.path.join(AUDIO_INPUT_DIR, formato)))
    
    print(f"🔍 Encontrados {len(arquivos_audio)} arquivos para converter")
    
    # Converter cada arquivo para WAV
    for arquivo in arquivos_audio:
        nome_arquivo = os.path.basename(arquivo)
        nome_sem_extensao = os.path.splitext(nome_arquivo)[0]
        arquivo_wav = os.path.join(AUDIO_DIR, f"{nome_sem_extensao}.wav")
        
        # Pular se já existir
        if os.path.exists(arquivo_wav):
            print(f"⏭️ Arquivo já existe: {arquivo_wav}")
            continue
        
        print(f"🔄 Convertendo: {nome_arquivo}")
        try:
            # Usar ffmpeg para converter
            stream = ffmpeg.input(arquivo)
            stream = ffmpeg.output(stream, arquivo_wav)
            ffmpeg.run(stream, capture_stdout=True, capture_stderr=True, overwrite_output=True)
            print(f"✅ Convertido com sucesso: {arquivo_wav}")
        except ffmpeg.Error as e:
            print(f"❌ Erro ao converter {nome_arquivo}: {str(e.stderr.decode())}")
        except Exception as e:
            print(f"❌ Erro ao converter {nome_arquivo}: {str(e)}")

print("Transcrição de Áudio Local (com Whisper)")

# Primeiro converter os áudios para WAV
print("\n1. Convertendo áudios para WAV...")
converter_para_wav()

print("\n2. Carregando modelo Whisper...")
# Carrega o modelo Whisper
model = whisper.load_model("base")  # Troque para "small" ou "medium" para mais qualidade

# Listar arquivos de áudio locais
def list_local_audio_files(directory, extension=".wav"):
    return [
        os.path.join(directory, f)
        for f in os.listdir(directory)
        if f.endswith(extension)
    ]

# Transcrever com Whisper
def transcrever_audio_whisper(audio_path, language="pt"):
    result = model.transcribe(audio_path, language=language)
    return result["text"]

# Processar todos os arquivos
audio_files = list_local_audio_files(AUDIO_DIR)
print("Áudios encontrados:", audio_files)

for path in audio_files:
    nome_arquivo = os.path.splitext(os.path.basename(path))[0]
    print(f"\n🗣 Transcrevendo: {nome_arquivo}")

    texto = transcrever_audio_whisper(path)
    print(texto)

    # Salvar a transcrição em .txt
    output_path = os.path.join(OUTPUT_DIR, f"{nome_arquivo}.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(texto)

    print(f"💾 Transcrição salva em: {output_path}")

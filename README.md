# Conversor e Transcritor de Áudio com Whisper

Este projeto permite converter arquivos de áudio de diferentes formatos para WAV e realizar a transcrição do conteúdo usando o modelo Whisper da OpenAI.

## 🎯 Funcionalidades

- Conversão de múltiplos formatos de áudio para WAV (MP3, M4A, OGG, WMA, AAC)
- Transcrição automática de áudio usando Whisper
- Suporte para língua portuguesa
- Salvamento das transcrições em arquivos de texto

## 📋 Pré-requisitos

Antes de começar, você precisa ter instalado em seu sistema:

- Python 3.8 ou superior
- pip (gerenciador de pacotes do Python)
- ffmpeg (para conversão de áudio)

### Instalando o ffmpeg

**No Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install ffmpeg
```

**No Windows:**
1. Baixe o ffmpeg do site oficial: https://ffmpeg.org/download.html
2. Extraia os arquivos
3. Adicione o caminho da pasta bin ao PATH do sistema

## 🚀 Instalação

1. Clone o repositório:
```bash
git clone [URL_DO_SEU_REPOSITORIO]
cd Converter-Extrair-info-audio-whisper
```

2. Crie e ative um ambiente virtual:
```bash
# Criar ambiente virtual
python -m venv .venv

# Ativar ambiente virtual
# No Windows:
.venv\Scripts\activate
# No Linux/Mac:
source .venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## 📁 Estrutura de Pastas

O projeto criará automaticamente as seguintes pastas:

- `audios/` - Coloque aqui seus arquivos de áudio originais
- `audios-convertidos/` - Arquivos convertidos para WAV (gerado automaticamente)
- `transcricoes/` - Arquivos de texto com as transcrições (gerado automaticamente)

## 💻 Como Usar

1. Coloque seus arquivos de áudio na pasta `audios/`

2. Execute o script:
```bash
python transcrever.py
```

3. O script irá:
   - Converter todos os áudios para WAV
   - Realizar a transcrição
   - Salvar os resultados na pasta `transcricoes/`

## 📝 Formatos de Áudio Suportados

- MP3 (.mp3)
- M4A (.m4a)
- OGG (.ogg)
- WMA (.wma)
- AAC (.aac)
- WAV (.wav)

## ⚙️ Configurações

No arquivo `transcrever.py`, você pode ajustar:

- Modelo do Whisper:
  ```python
  model = whisper.load_model("base")  # Opções: "tiny", "base", "small", "medium", "large"
  ```
  - `tiny`: Mais rápido, menos preciso
  - `base`: Bom equilíbrio entre velocidade e precisão
  - `small`/`medium`: Mais precisos, mais lentos
  - `large`: Melhor qualidade, requer mais recursos

## 🚨 Solução de Problemas

1. **Erro de ffmpeg não encontrado:**
   - Verifique se o ffmpeg está instalado: `ffmpeg -version`
   - Reinstale o ffmpeg se necessário

2. **Erro de memória:**
   - Use um modelo menor do Whisper
   - Processe arquivos menores
   - Aumente a memória RAM disponível

3. **Erro de importação de módulos:**
   - Verifique se está no ambiente virtual
   - Reinstale as dependências: `pip install -r requirements.txt`

## 📈 Desempenho

O tempo de processamento depende de:
- Tamanho do arquivo de áudio
- Modelo do Whisper escolhido
- Capacidade de processamento do computador
- Memória RAM disponível

## 🤝 Contribuindo

Sinta-se à vontade para:
- Reportar bugs
- Sugerir melhorias
- Enviar pull requests

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
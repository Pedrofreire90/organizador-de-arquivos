# 🗂️ Organizador de Arquivos

Script Python que organiza automaticamente os arquivos de uma pasta,
separando-os em subpastas por categoria.

## 📋 O que ele faz

- Lê todos os arquivos de uma pasta alvo (padrão: `~/Downloads`)
- Classifica cada arquivo pela sua extensão
- Move para subpastas organizadas automaticamente
- Exibe um resumo ao final com quantos arquivos foram movidos

## 📁 Categorias

| Pasta | Extensões |
|-------|-----------|
| Imagens | .jpg, .png, .gif, .svg... |
| Documentos | .pdf, .doc, .xlsx, .pptx... |
| Videos | .mp4, .avi, .mkv... |
| Audio | .mp3, .wav, .flac... |
| Compactados | .zip, .rar, .tar... |
| Programas | .exe, .deb, .apk... |
| Codigo | .py, .js, .html, .sql... |
| Outros | Tudo que não se encaixa acima |

## 🚀 Como usar

1. Clone o repositório:
```bash
   git clone https://github.com/Pedrofreire90/organizador-de-arquivos.git
```

2. Abra o arquivo e configure a pasta alvo:
```python
   PASTA_ALVO = os.path.expanduser("~/Downloads")  # mude aqui
```

3. Execute:
```bash
   python organizador_arquivos.py
```

4. O script mostra um preview da pasta e pede confirmação antes de mover qualquer arquivo.

## 🛠️ Tecnologias

- Python 3
- Bibliotecas nativas: `os` e `shutil` (sem instalação extra)
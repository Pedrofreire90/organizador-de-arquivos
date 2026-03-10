import os
import shutil

# ============================================================
#   AUTOMATIZADOR DE ARQUIVOS - Seu primeiro projeto Python!
# ============================================================

# 🔧 CONFIGURAÇÃO: mude este caminho para a pasta que quer organizar
PASTA_ALVO = os.path.expanduser("~/Downloads")  # Pasta Downloads do seu usuário

# 📁 Dicionário que mapeia cada tipo de arquivo para uma subpasta
TIPOS_DE_ARQUIVO = {
    # Imagens
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".ico"],
    # Documentos
    "Documentos": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx", ".odt"],
    # Videos
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".wmv", ".flv"],
    # Audio
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    # Compactados
    "Compactados": [".zip", ".rar", ".tar", ".gz", ".7z"],
    # Programas e instaladores
    "Programas": [".exe", ".msi", ".dmg", ".pkg", ".deb", ".apk"],
    # Código
    "Codigo": [".py", ".js", ".html", ".css", ".json", ".xml", ".sql", ".java", ".cpp"],
}


def organizar_pasta(caminho):
    """
    Função principal que organiza os arquivos de uma pasta.
    
    O que ela faz:
    1. Lista todos os arquivos da pasta
    2. Para cada arquivo, descobre a extensão (ex: .pdf, .jpg)
    3. Move o arquivo para a subpasta correta
    """
    
    # Verifica se a pasta existe
    if not os.path.exists(caminho):
        print(f"❌ Erro: A pasta '{caminho}' não existe!")
        return
    
    print(f"\n📂 Organizando a pasta: {caminho}")
    print("=" * 50)
    
    arquivos_movidos = 0
    arquivos_ignorados = 0

    # os.listdir() lista tudo que tem dentro da pasta
    for nome_arquivo in os.listdir(caminho):
        
        # Monta o caminho completo do arquivo
        caminho_completo = os.path.join(caminho, nome_arquivo)
        
        # Ignora subpastas (só queremos arquivos)
        if os.path.isdir(caminho_completo):
            continue
        
        # os.path.splitext separa o nome da extensão
        # Ex: "foto.jpg" → ("foto", ".jpg")
        _, extensao = os.path.splitext(nome_arquivo)
        extensao = extensao.lower()  # deixa em minúsculo para comparar

        # Procura em qual categoria o arquivo se encaixa
        pasta_destino = None
        for categoria, extensoes in TIPOS_DE_ARQUIVO.items():
            if extensao in extensoes:
                pasta_destino = categoria
                break
        
        # Se não achou categoria, vai para "Outros"
        if pasta_destino is None:
            pasta_destino = "Outros"
        
        # Cria a subpasta de destino se ela não existir
        caminho_destino = os.path.join(caminho, pasta_destino)
        os.makedirs(caminho_destino, exist_ok=True)
        
        # Move o arquivo!
        caminho_final = os.path.join(caminho_destino, nome_arquivo)
        
        # Evita sobrescrever arquivos com o mesmo nome
        if os.path.exists(caminho_final):
            print(f"⚠️  Ignorado (já existe): {nome_arquivo}")
            arquivos_ignorados += 1
            continue
        
        shutil.move(caminho_completo, caminho_final)
        print(f"✅ {nome_arquivo}  →  {pasta_destino}/")
        arquivos_movidos += 1

    # Resumo final
    print("=" * 50)
    print(f"\n🎉 Concluído!")
    print(f"   Arquivos movidos:   {arquivos_movidos}")
    print(f"   Arquivos ignorados: {arquivos_ignorados}")


def visualizar_pasta(caminho):
    """
    Função bônus: mostra um resumo do que tem na pasta
    antes de organizar.
    """
    print(f"\n🔍 Conteúdo atual de: {caminho}")
    print("=" * 50)
    
    contagem = {}
    for nome in os.listdir(caminho):
        caminho_completo = os.path.join(caminho, nome)
        if os.path.isfile(caminho_completo):
            _, ext = os.path.splitext(nome)
            ext = ext.lower() if ext else "(sem extensão)"
            contagem[ext] = contagem.get(ext, 0) + 1
    
    for ext, qtd in sorted(contagem.items()):
        print(f"  {ext:15} → {qtd} arquivo(s)")
    
    print(f"\n  Total: {sum(contagem.values())} arquivo(s)")


# ============================================================
#   EXECUÇÃO DO PROGRAMA
# ============================================================

if __name__ == "__main__":
    
    print("🗂️  ORGANIZADOR DE ARQUIVOS")
    print("Desenvolvido para aprender Python na prática!\n")
    
    # Mostra o que tem na pasta antes de organizar
    visualizar_pasta(PASTA_ALVO)
    
    # Pergunta se o usuário quer continuar
    print(f"\nDeseja organizar a pasta '{PASTA_ALVO}'?")
    resposta = input("Digite 's' para sim ou qualquer tecla para cancelar: ")
    
    if resposta.lower() == "s":
        organizar_pasta(PASTA_ALVO)
    else:
        print("\n❌ Operação cancelada.")

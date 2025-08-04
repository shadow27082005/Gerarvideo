import os
from pynfe.processamento.comunicacao import ComunicacaoSefaz

# === CONFIGURAÇÕES ===
CERT_PATH = "certificado.pfx"          # Nome exato do seu .pfx
CERT_PASSWORD = "225407eb"             # Substitua pela senha real do certificado
CHAVES_FILE = "chaves.txt"             # Arquivo com uma chave por linha
OUTPUT_DIR = "xmls"                    # Pasta onde os XMLs serão salvos
UF = "SP"                              # Estado (ex: SP, RJ, PR, MG...)
HOMOLOGACAO = False                    # False = Produção | True = Homologação

# === GARANTIR QUE A PASTA DE SAÍDA EXISTE ===
os.makedirs(OUTPUT_DIR, exist_ok=True)

# === INICIALIZA COMUNICAÇÃO COM SEFAZ ===
print("[🔐] Iniciando comunicação com a SEFAZ...")
con = ComunicacaoSefaz(uf=UF, certificado=CERT_PATH, senha=CERT_PASSWORD, homologacao=HOMOLOGACAO)

# === LÊ CHAVES DE ACESSO ===
with open(CHAVES_FILE, "r") as f:
    chaves = [linha.strip() for linha in f if linha.strip()]

print(f"[📋] Total de chaves a processar: {len(chaves)}")

# === LOOP PARA BAIXAR XMLs ===
for chave in chaves:
    print(f"[⬇️] Baixando NF-e: {chave}")
    try:
        resposta = con.consulta_notas_cnpj(cnpj=None, nsu=None, chave_nfe=chave)
        if resposta.status_code == 200:
            caminho = os.path.join(OUTPUT_DIR, f"{chave}.xml")
            with open(caminho, "wb") as xml_file:
                xml_file.write(resposta.text.encode("utf-8"))
            print(f"   ✅ XML salvo em: {caminho}")
        else:
            print(f"   ❌ Falha HTTP ({resposta.status_code}) ao baixar {chave}")
    except Exception as e:
        print(f"   ❌ Erro ao processar {chave}: {e}")

print("\n✅ Finalizado.")
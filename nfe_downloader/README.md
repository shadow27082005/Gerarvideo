# NFe Downloader

Script para baixar XMLs de NF-e diretamente da SEFAZ usando certificado A1.

## 📁 Estrutura
```
nfe_downloader/
├── chaves.txt                      # Uma chave por linha
├── certificado.pfx                 # Seu certificado A1 (renomeado)
├── baixar_nfes.py                  # Script Python
├── requirements.txt                # Dependências
└── xmls/                           # Onde os XMLs serão salvos
```

## 🚀 Como usar

1. **Instalar dependências:**
```bash
cd nfe_downloader
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. **Configurar arquivos:**
   - Coloque seu certificado `.pfx` na pasta e renomeie para `certificado.pfx`
   - Edite `chaves.txt` com uma chave de acesso por linha
   - Verifique se a senha no script está correta (linha 7)

3. **Executar:**
```bash
python baixar_nfes.py
```

## ⚙️ Configurações

- **Ambiente:** 1 = Produção, 2 = Homologação (linha 20)
- **Senha do certificado:** Configurada na linha 7
- **Pasta de saída:** `xmls/` (configurável na linha 9)

Os XMLs baixados serão salvos como `{chave_de_acesso}.xml` na pasta `xmls/`.
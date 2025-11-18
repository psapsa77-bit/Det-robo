# ⚡ DET Robot - Automação para Domicílio Eletrônico Trabalhista

Sistema profissional de automação para o **portal DET (Domicílio Eletrônico Trabalhista)** com comandos em linguagem natural.

---

## 🎯 Descrição

DET Robot é uma ferramenta de automação focada exclusivamente em facilitar o acesso e gerenciamento do **Domicílio Eletrônico Trabalhista**. Com uma interface intuitiva e comandos em português, você pode:

- ⚡ **Acessar o portal DET** automaticamente
- 👤 **Trocar perfis de empresas** rapidamente (por nome ou CNPJ)
- 📬 **Verificar mensagens não lidas** instantaneamente
- 📋 **Listar e abrir mensagens** do DET
- 📸 **Capturar telas** para documentação
- 🤖 **Comandos inteligentes** em linguagem natural

---

## 📦 Pré-requisitos

Antes de começar, você precisa ter instalado:
- **Python 3.7 ou superior** - [Download aqui](https://www.python.org/downloads/)
- **Google Chrome** - [Download aqui](https://www.google.com/chrome/)

---

## ⚡ Instalação RÁPIDA (2 Cliques!)

### 🪟 Windows

**Opção 1: Instalador Completo (Recomendado)**
1. **Duplo-clique em `INSTALAR_WINDOWS.bat`** → Instala com verificações completas
2. **Duplo-clique em `ABRIR.bat`** → Inicia o DET Robot

**Opção 2: Instalador Rápido**
1. **Duplo-clique em `INSTALAR_SIMPLES.bat`** → Instalação rápida sem verificações
2. **Duplo-clique em `VERIFICAR.bat`** → (Opcional) Testa a instalação
3. **Duplo-clique em `ABRIR.bat`** → Inicia o DET Robot

### 🐧 Linux/Mac

**Opção 1: Instalador Completo (Recomendado)**
1. **Execute `bash INSTALAR_LINUX.sh`** → Instala com verificações completas
2. **Execute `bash ABRIR.sh`** → Inicia o DET Robot

**Opção 2: Instalador Rápido**
1. **Execute `bash INSTALAR_SIMPLES.sh`** → Instalação rápida sem verificações
2. **Execute `bash VERIFICAR.sh`** → (Opcional) Testa a instalação
3. **Execute `bash ABRIR.sh`** → Inicia o DET Robot

**Pronto!** O sistema abrirá automaticamente em http://localhost:5000

---

## 🚀 Como Usar

### 1. Fluxo Básico

1. **Execute `ABRIR.bat` (Windows) ou `bash ABRIR.sh` (Linux/Mac)**
2. **Clique em "Iniciar Sistema"** (ou digite: "inicie o navegador")
3. **Clique em "Acessar DET"** (ou digite: "acesse o DET")
4. **Faça login manualmente** no portal DET
5. **Use os comandos** para automatizar suas tarefas!

### 2. Comandos Disponíveis

#### 🏢 Acesso e Navegação
```
"acesse o DET"
"abra o domicílio eletrônico"
```

#### 👤 Gerenciamento de Perfil
```
"trocar perfil"
"mudar empresa"
"trocar perfil para [Nome da Empresa]"
"trocar perfil para [00.000.000/0001-00]"
```

#### 📬 Mensagens
```
"verificar mensagens"          → Mostra quantidade de não lidas
"acessar mensagens"            → Vai para área de mensagens
"listar mensagens"             → Lista as mensagens não lidas
"abrir primeira mensagem"      → Abre a primeira não lida
```

#### 📸 Utilidades
```
"tire um screenshot"
"capture a tela"
```

### 3. Interface - Botões Rápidos

A interface oferece 3 botões de ação rápida:

- **▶️ Iniciar Sistema** - Ativa o navegador automatizado
- **🏢 Acessar DET** - Abre o portal DET
- **📧 Verificar Mensagens** - Checa mensagens não lidas

### 4. Painel de Comandos Inteligentes

Digite comandos em **linguagem natural** no campo principal:

![Campo de Comandos]

Exemplos clicáveis estão disponíveis para facilitar o uso.

---

## 📊 Funcionalidades Principais

### ✨ Automação Inteligente
- Reconhece comandos em português brasileiro
- Suporta variações naturais de linguagem
- Feedback em tempo real de todas as ações

### 🔄 Troca Rápida de Perfil
- Busca por nome da empresa
- Busca por CNPJ (com ou sem formatação)
- Abertura automática do seletor

### 📧 Gestão de Mensagens
- Contagem automática de não lidas
- Listagem detalhada
- Abertura automática da primeira mensagem

### 📸 Documentação
- Screenshots com timestamp
- Salvos automaticamente na pasta `screenshots/`

---

## 🏗️ Estrutura do Projeto

```
Det-robo/
│
├── INSTALAR_WINDOWS.bat       # Instalador completo Windows
├── INSTALAR_LINUX.sh          # Instalador completo Linux/Mac
├── INSTALAR_SIMPLES.bat       # Instalador rápido Windows
├── INSTALAR_SIMPLES.sh        # Instalador rápido Linux/Mac
├── ABRIR.bat                  # Executar no Windows
├── ABRIR.sh                   # Executar no Linux/Mac
├── VERIFICAR.bat              # Testar instalação Windows
├── VERIFICAR.sh               # Testar instalação Linux/Mac
│
├── app.py                     # Servidor Flask + API REST
├── requirements.txt           # Dependências Python
│
├── det_robot/                 # Pacote modular principal
│   ├── __init__.py           # Exports do pacote
│   ├── config.py             # Configurações centralizadas
│   ├── automation.py         # Automação DET com context manager
│   ├── extractor.py          # Extração de dados estruturados
│   └── reporter.py           # Geração de relatórios HTML/JSON
│
├── browser_controller.py      # Controle Selenium avançado (legado)
├── det_automation.py          # Automação DET (legado)
├── command_processor.py       # Processamento de linguagem natural
│
├── templates/
│   └── index.html            # Interface web profissional
│
├── static/
│   ├── style.css             # Design moderno e responsivo
│   └── script.js             # Lógica da interface
│
├── docs/
│   └── COMO_USAR.md          # Guia completo em português
│
├── exports/                   # Relatórios gerados (HTML/JSON)
├── logs/                      # Logs do sistema
└── screenshots/               # Screenshots com timestamp
```

---

## 🛠️ Tecnologias

- **Backend**: Python 3.7+, Flask
- **Automação**: Selenium WebDriver
- **Frontend**: HTML5, CSS3 (design moderno), JavaScript
- **NLP**: Processamento de linguagem natural em português

---

## 💡 Dicas de Uso

### Para Melhor Desempenho:

1. **Sempre inicie o sistema primeiro** antes de acessar o DET
2. **Faça login manualmente** no portal (por segurança)
3. **Aguarde o carregamento** completo das páginas antes de executar comandos
4. **Use comandos específicos** para melhor precisão

### Resolução de Problemas:

**"Falha ao instalar dependências"**
- Verifique sua conexão com a internet
- Use o instalador simples: `INSTALAR_SIMPLES.bat` ou `INSTALAR_SIMPLES.sh`
- Tente manualmente: `pip install flask selenium`

**"Módulo det_robot não encontrado"**
- Execute `VERIFICAR.bat` ou `bash VERIFICAR.sh` para diagnóstico
- Reinstale com `INSTALAR_SIMPLES`

**"Elemento não encontrado"**
- O portal DET pode estar lento
- Aguarde mais tempo entre comandos
- Verifique se você está logado

**"Navegador não está em execução"**
- Clique em "Iniciar Sistema" primeiro
- Aguarde o navegador abrir completamente

**Screenshots não salvam**
- Verifique se a pasta `screenshots/` existe
- Verifique permissões de escrita

---

## 🔒 Segurança

- ✅ **Não armazena senhas** ou credenciais
- ✅ **Login manual** pelo usuário (mais seguro)
- ✅ **Execução local** (sem envio de dados externos)
- ✅ **Código aberto** e auditável

---

## 📝 Notas Importantes

- Este robô **automatiza navegação**, não faz login automático
- Os seletores DET podem variar conforme atualizações do portal
- Recomendado para uso em **ambiente controlado**
- Screenshots incluem timestamp para rastreabilidade

---

## 🆘 Suporte

Se encontrar problemas:

1. **Teste a instalação**: Execute `VERIFICAR.bat` (Windows) ou `bash VERIFICAR.sh` (Linux/Mac)
2. **Verifique pré-requisitos**: Python 3.7+ e Google Chrome instalados
3. **Reinstale**: Use `INSTALAR_SIMPLES` para instalação rápida
4. **Logs**: Consulte a pasta `logs/` para detalhes de erro
5. **Documentação**: Leia `docs/COMO_USAR.md` para instruções completas

---

## 📜 Licença

Código aberto sob licença MIT.

---

## 👨‍💻 Desenvolvimento

Desenvolvido com foco em **produtividade** e **facilidade de uso** para profissionais que trabalham com o portal DET.

**Versão**: 2.0 (Arquitetura Modular)
**Status**: Estável e Funcional

### Novidades v2.0:
- ✨ Arquitetura modular profissional (`det_robot/` package)
- 📊 Extração de dados estruturados (mensagens, perfis, dashboard)
- 📄 Geração de relatórios HTML e JSON
- 🔧 Scripts de instalação melhorados (completo e simples)
- ✅ Script de verificação de instalação
- 📝 Documentação completa em português
- 🔒 Logging estruturado
- ⚙️ Configuração centralizada com suporte a variáveis de ambiente

---

**Simplifique seu trabalho com o DET Robot!** ⚡

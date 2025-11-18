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

1. **Duplo-clique em `install.bat`** → Instala tudo automaticamente
2. **Duplo-clique em `run.bat`** → Inicia o DET Robot

### 🐧 Linux/Mac

1. **Execute `bash install.sh`** → Instala tudo
2. **Execute `bash run.sh`** → Inicia o DET Robot

**Pronto!** O sistema abrirá automaticamente em http://localhost:5000

---

## 🚀 Como Usar

### 1. Fluxo Básico

1. **Execute `run.bat` (Windows) ou `bash run.sh` (Linux/Mac)**
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
├── run.bat / run.sh           # Scripts de execução
├── install.bat / install.sh   # Scripts de instalação
│
├── app.py                     # Servidor Flask + API
├── browser_controller.py      # Controle Selenium avançado
├── det_automation.py          # Automação específica DET
├── command_processor.py       # Processamento de linguagem natural
│
├── templates/
│   └── index.html            # Interface web profissional
│
├── static/
│   ├── style.css             # Design moderno e responsivo
│   └── script.js             # Lógica da interface
│
└── screenshots/              # Screenshots gerados
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

1. Verifique se Python e Chrome estão instalados
2. Execute `install.bat` / `install.sh` novamente
3. Verifique se está na versão mais recente
4. Consulte os logs de erro no terminal

---

## 📜 Licença

Código aberto sob licença MIT.

---

## 👨‍💻 Desenvolvimento

Desenvolvido com foco em **produtividade** e **facilidade de uso** para profissionais que trabalham com o portal DET.

**Versão**: 1.0
**Status**: Estável e Funcional

---

**Simplifique seu trabalho com o DET Robot!** ⚡

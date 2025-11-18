# 🤖 Robô Simples - Controle de Navegador

Um robô simples e intuitivo para controlar seu navegador web de forma fácil através de uma interface web moderna com **comandos em linguagem natural** e **automação DET**!

## 📋 Descrição

Este projeto oferece uma interface web intuitiva para controlar o Google Chrome através do Selenium. Você pode:

- 🎤 **Controlar por comandos em português** (ex: "abra google.com", "pesquise python")
- 🏢 **Automatizar o DET** - Domicílio Eletrônico Trabalhista (trocar perfis, ver mensagens)
- ✅ Iniciar e fechar o navegador
- 🌐 Navegar para qualquer URL
- ⬅️ Voltar e avançar no histórico
- 🔄 Atualizar páginas
- 📸 Tirar screenshots
- 🎯 Acessar sites populares com um clique

## 🚀 Funcionalidades

### 🎤 Comandos em Linguagem Natural
Digite o que você quer em português e o robô executa! Exemplos:
- `"abra youtube.com"` - Navega para o YouTube
- `"pesquise receitas de bolo"` - Faz uma busca no Google
- `"tire um screenshot"` - Captura a tela
- `"volte"` - Volta para a página anterior
- `"atualize a página"` - Atualiza a página atual
- `"role para baixo"` - Rola a página
- `"feche o navegador"` - Fecha o navegador

### 🏢 Automação DET - Domicílio Eletrônico Trabalhista (NOVO!)
Comandos específicos para automatizar o portal DET:
- `"acesse o DET"` ou `"abra o domicílio eletrônico"` - Acessa o portal DET
- `"trocar perfil"` ou `"mudar empresa"` - Abre o seletor de perfil/empresa
- `"trocar perfil para [nome]"` - Troca para empresa específica por nome
- `"trocar perfil para [CNPJ]"` - Troca para empresa específica por CNPJ
- `"verificar mensagens"` - Verifica quantas mensagens não lidas
- `"acessar mensagens"` - Vai para a área de mensagens
- `"listar mensagens"` - Lista as mensagens não lidas
- `"abrir primeira mensagem"` - Abre a primeira mensagem não lida

### Controle do Navegador
- Iniciar o Google Chrome nativo
- Fechar o navegador
- Monitorar status em tempo real

### Navegação
- Navegação por URL personalizada
- Botões de voltar/avançar
- Atualização de página
- Captura de screenshots
- Scroll automático (cima, baixo, topo, fim)

### Atalhos Rápidos
- Google
- YouTube
- GitHub
- Wikipedia

## 📦 Pré-requisitos

Antes de começar, você precisa ter instalado:
- **Python 3.7 ou superior** - [Download aqui](https://www.python.org/downloads/)
- **Google Chrome** - [Download aqui](https://www.google.com/chrome/)

## ⚡ Instalação e Execução RÁPIDA (2 Cliques!)

### Windows

1. **Duplo-clique em `install.bat`** - Instala tudo automaticamente
2. **Duplo-clique em `run.bat`** - Inicia o robô e abre no navegador

### Linux/Mac

1. **Duplo-clique em `install.sh`** (ou execute `bash install.sh`) - Instala tudo
2. **Duplo-clique em `run.sh`** (ou execute `bash run.sh`) - Inicia o robô

**Pronto!** O navegador vai abrir automaticamente em http://localhost:5000

---

## 🔧 Instalação Manual (Opcional)

Se preferir instalar manualmente:

### 1. Clone o repositório
```bash
git clone <seu-repositorio>
cd Det-robo
```

### 2. Execute o instalador automático

**Windows:**
```bash
install.bat
```

**Linux/Mac:**
```bash
bash install.sh
```

### 3. Execute o robô

**Windows:**
```bash
run.bat
```

**Linux/Mac:**
```bash
bash run.sh
```

## 🎮 Como Usar

Após executar o `run.bat` ou `run.sh`, o navegador abrirá automaticamente.
Se não abrir, acesse manualmente: **http://localhost:5000**

### Guia de Uso

#### Modo Recomendado: Comandos em Linguagem Natural 🎤
1. **Iniciar**: Digite `"inicie o navegador"` e pressione Enter (ou clique em Executar)
2. **Navegar**: Digite `"abra google.com"` ou `"vá para youtube.com"`
3. **Pesquisar**: Digite `"pesquise receitas de bolo"` ou `"busque python tutorial"`
4. **Controlar**: Digite `"volte"`, `"avance"`, `"atualize a página"`
5. **Screenshot**: Digite `"tire um screenshot"`
6. **Fechar**: Digite `"feche o navegador"`

#### Uso do DET - Domicílio Eletrônico Trabalhista 🏢
1. **Acessar DET**: Digite `"acesse o DET"` ou clique no exemplo "acesse o DET"
2. **Fazer login**: Faça login manualmente no portal (o robô aguarda)
3. **Trocar empresa**: Digite `"trocar perfil"` ou `"trocar perfil para [nome da empresa]"`
4. **Ver mensagens**: Digite `"verificar mensagens"` para ver quantas não lidas
5. **Listar mensagens**: Digite `"listar mensagens"` para ver detalhes
6. **Abrir mensagem**: Digite `"abrir primeira mensagem"` para ler

**Dica**: Os comandos DET funcionam melhor após fazer login manualmente no portal.

#### Modo Tradicional: Botões
1. **Iniciar Navegador**: Clique em "▶️ Iniciar Navegador"
2. **Navegar**: Digite uma URL no campo de texto e clique em "🌐 Ir" ou pressione Enter
3. **Usar Atalhos**: Clique em um dos botões de atalho (Google, YouTube, etc.)
4. **Controlar Navegação**: Use os botões de voltar, avançar e atualizar
5. **Screenshot**: Clique em "📸 Screenshot" para capturar a tela
6. **Fechar**: Quando terminar, clique em "⏹️ Fechar Navegador"

## 📁 Estrutura do Projeto

```
Det-robo/
│
├── app.py                  # Aplicação Flask principal
├── browser_controller.py   # Controlador do navegador (Selenium)
├── command_processor.py    # Processador de comandos em linguagem natural
├── det_automation.py       # Automação específica para DET
├── requirements.txt        # Dependências do projeto
├── README.md              # Este arquivo
│
├── templates/
│   └── index.html         # Interface HTML
│
├── static/
│   ├── style.css          # Estilos CSS
│   └── script.js          # JavaScript da interface
│
└── screenshots/           # Pasta para screenshots (criada automaticamente)
```

## 🛠️ Tecnologias Utilizadas

- **Backend**: Python, Flask
- **Automação**: Selenium WebDriver
- **Frontend**: HTML5, CSS3, JavaScript
- **Design**: Interface moderna e responsiva

## 🔌 API Endpoints

O robô expõe os seguintes endpoints REST:

### Comandos em Linguagem Natural
- `POST /api/command/process` - Processa um comando em linguagem natural (português)

### Controle do Navegador
- `POST /api/browser/start` - Inicia o navegador
- `POST /api/browser/stop` - Fecha o navegador
- `POST /api/browser/navigate` - Navega para uma URL
- `POST /api/browser/back` - Volta para a página anterior
- `POST /api/browser/forward` - Avança para a próxima página
- `POST /api/browser/refresh` - Atualiza a página atual
- `POST /api/browser/screenshot` - Tira um screenshot
- `GET /api/browser/status` - Retorna o status do navegador

## 🐛 Solução de Problemas

### Chrome não inicia
- Certifique-se de que o Google Chrome está instalado
- Verifique se o ChromeDriver está instalado corretamente
- Tente reinstalar o Selenium: `pip install --upgrade selenium`

### Erro de permissão
- Execute o script com permissões adequadas
- Verifique se o Chrome não está bloqueado por firewall

### Interface não carrega
- Verifique se o Flask está rodando na porta 5000
- Tente acessar http://127.0.0.1:5000

## 📝 Notas

- Screenshots são salvos na pasta `screenshots/` com timestamp
- O navegador é iniciado em modo maximizado
- A interface atualiza o status automaticamente a cada 5 segundos
- Compatível com sistemas Linux, Windows e Mac

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## 📄 Licença

Este projeto é de código aberto e está disponível sob a licença MIT.

## 👨‍💻 Desenvolvedor

Desenvolvido com ❤️ usando Python, Flask e Selenium.

---

**Divirta-se controlando seu navegador!** 🚀

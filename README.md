# 🤖 Robô Simples - Controle de Navegador

Um robô simples e intuitivo para controlar seu navegador web de forma fácil através de uma interface web moderna.

## 📋 Descrição

Este projeto oferece uma interface web intuitiva para controlar o Google Chrome através do Selenium. Você pode:

- ✅ Iniciar e fechar o navegador
- 🌐 Navegar para qualquer URL
- ⬅️ Voltar e avançar no histórico
- 🔄 Atualizar páginas
- 📸 Tirar screenshots
- 🎯 Acessar sites populares com um clique

## 🚀 Funcionalidades

### Controle do Navegador
- Iniciar o Google Chrome nativo
- Fechar o navegador
- Monitorar status em tempo real

### Navegação
- Navegação por URL personalizada
- Botões de voltar/avançar
- Atualização de página
- Captura de screenshots

### Atalhos Rápidos
- Google
- YouTube
- GitHub
- Wikipedia

## 📦 Requisitos

### Pré-requisitos
- Python 3.7 ou superior
- Google Chrome instalado no sistema
- ChromeDriver (geralmente instalado automaticamente)

## 🔧 Instalação

### 1. Clone o repositório
```bash
git clone <seu-repositorio>
cd Det-robo
```

### 2. Crie um ambiente virtual (recomendado)
```bash
python -m venv venv
```

### 3. Ative o ambiente virtual

**Linux/Mac:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

### 4. Instale as dependências
```bash
pip install -r requirements.txt
```

## 🎮 Como Usar

### 1. Inicie o servidor
```bash
python app.py
```

### 2. Acesse a interface
Abra seu navegador e acesse:
```
http://localhost:5000
```

### 3. Use a interface

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

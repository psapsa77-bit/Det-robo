# 📘 Como Usar o DET Robot

**Guia Completo para Usuários**

---

## 🚀 Início Rápido (2 Minutos)

### Passo 1: Instalação
```bash
# Windows
INSTALAR_WINDOWS.bat

# Linux/Mac
bash INSTALAR_LINUX.sh
```

### Passo 2: Executar
```bash
# Windows
ABRIR.bat

# Linux/Mac
bash ABRIR.sh
```

### Passo 3: Usar
1. Abra o navegador em: **http://localhost:5000**
2. Clique em "**Iniciar Sistema**"
3. Clique em "**Acessar DET**"
4. **Faça login** no portal DET (manualmente)
5. Use os **comandos** ou **botões** para automatizar!

---

## 💬 Comandos Disponíveis

### 🏢 Acesso e Navegação
```
"acesse o DET"
"abra o domicílio eletrônico"
```

### 👤 Gerenciamento de Perfil
```
"trocar perfil"
"mudar empresa"
"trocar perfil para Empresa ABC"
"trocar perfil para 12.345.678/0001-90"
```

### 📬 Mensagens
```
"verificar mensagens"       → Quantidade de não lidas
"acessar mensagens"         → Ir para área de mensagens
"listar mensagens"          → Detalhes das mensagens
"abrir primeira mensagem"   → Abre primeira não lida
```

### 📊 Extração de Dados
```
"extrair mensagens"         → Exporta todas as mensagens
"gerar relatório"           → Cria relatório HTML/JSON
"exportar dados"            → Salva dados estruturados
```

### 📸 Utilidades
```
"tire um screenshot"
"capture a tela"
```

---

## 🎯 Casos de Uso Comuns

### Caso 1: Verificar Mensagens Não Lidas
```
1. "acesse o DET"
2. [Faça login manualmente]
3. "verificar mensagens"
```

### Caso 2: Trocar Entre Empresas
```
1. "acesse o DET"
2. [Faça login]
3. "trocar perfil para CNPJ 12.345.678/0001-90"
```

### Caso 3: Extrair e Gerar Relatório
```
1. "acesse o DET"
2. [Faça login]
3. "extrair mensagens"
4. "gerar relatório"
→ Relatório HTML salvo em /exports/
```

---

## 📁 Estrutura de Arquivos

```
Det-robo/
├── ABRIR.bat                 ← Execute para iniciar
├── INSTALAR_WINDOWS.bat      ← Execute para instalar
│
├── det_robot/                ← Pacote principal
│   ├── automation.py         ← Automação core
│   ├── extractor.py          ← Extração de dados
│   ├── reporter.py           ← Geração de relatórios
│   └── config.py             ← Configurações
│
├── exports/                  ← Relatórios gerados
├── logs/                     ← Logs do sistema
├── screenshots/              ← Capturas de tela
│
└── docs/                     ← Documentação
    └── COMO_USAR.md          ← Este arquivo
```

---

## ⚙️ Configurações Avançadas

### Arquivo de Configuração

Edite `det_robot/config.py` para customizar:

```python
# Timeouts
DEFAULT_TIMEOUT = 10          # Timeout padrão (segundos)
PAGE_LOAD_TIMEOUT = 30        # Timeout de carregamento

# Chrome
HEADLESS = False              # True = modo invisível
WINDOW_SIZE = (1920, 1080)    # Tamanho da janela

# Extração
MAX_MESSAGES_TO_EXTRACT = 50  # Máximo de mensagens
EXTRACT_ATTACHMENTS = True    # Extrair anexos

# Relatórios
REPORT_FORMAT = "html"        # html, pdf, json
INCLUDE_SCREENSHOTS = True    # Incluir capturas
```

### Variáveis de Ambiente

```bash
# Linux/Mac
export HEADLESS=true
export LOG_LEVEL=DEBUG

# Windows (PowerShell)
$env:HEADLESS="true"
$env:LOG_LEVEL="DEBUG"
```

---

## 🔍 Solução de Problemas

### Problema: "Navegador não está em execução"
**Solução**: Clique em "Iniciar Sistema" primeiro

### Problema: "Elemento não encontrado"
**Possíveis causas**:
- Portal DET está lento
- Você não está logado
- Estrutura do portal mudou

**Soluções**:
1. Aguarde mais tempo entre comandos
2. Verifique se está logado
3. Atualize o DET Robot para versão mais recente

### Problema: "ChromeDriver não encontrado"
**Solução**:
```bash
# Execute novamente o instalador
INSTALAR_WINDOWS.bat  # ou INSTALAR_LINUX.sh
```

### Problema: Screenshots não salvam
**Solução**:
1. Verifique se a pasta `screenshots/` existe
2. Verifique permissões de escrita
3. Verifique espaço em disco

---

## 📊 Relatórios e Exportações

### Tipos de Relatório

**1. HTML (Padrão)**
- Visual e interativo
- Abre em qualquer navegador
- Inclui gráficos e tabelas

**2. JSON**
- Dados estruturados
- Fácil integração com outros sistemas
- Ideal para processamento automático

**3. PDF (Futuro)**
- Formato profissional
- Ideal para impressão
- Compartilhamento fácil

### Localização dos Arquivos

Todos os arquivos gerados ficam em:
- **Relatórios**: `/exports/`
- **Screenshots**: `/screenshots/`
- **Logs**: `/logs/`

---

## 🔒 Segurança e Privacidade

### ✅ O que o DET Robot FAZ
- Automatiza navegação no portal
- Extrai dados visíveis
- Gera relatórios locais
- Salva logs de atividades

### ❌ O que o DET Robot NÃO FAZ
- **NÃO armazena** senhas ou credenciais
- **NÃO faz** login automático
- **NÃO envia** dados para servidores externos
- **NÃO modifica** dados no portal DET

### Boas Práticas
1. **Sempre** faça logout após usar
2. **Não** compartilhe relatórios com dados sensíveis
3. **Mantenha** o software atualizado
4. **Use** em rede segura

---

## 💡 Dicas de Produtividade

### 1. Use Botões Rápidos
Clique nos cards coloridos no topo para ações comuns

### 2. Use Chips de Comando
Clique nos chips abaixo do campo de comando para preencher automaticamente

### 3. Aproveite os Logs
O painel de "Registro de Atividades" mostra tudo que está acontecendo

### 4. Gere Relatórios Regulares
Crie relatórios diários/semanais para rastrear mensagens

### 5. Use Screenshots
Capture telas importantes para documentação

---

## 🆘 Suporte

### Precisa de Ajuda?

1. **Consulte os logs**: `/logs/det_robot_YYYYMMDD.log`
2. **Verifique a documentação**: `/docs/`
3. **Execute diagnóstico**:
   ```bash
   python -m det_robot.diagnostics
   ```

### Reportar Problemas

Ao reportar um problema, inclua:
- Versão do DET Robot
- Sistema operacional
- Mensagem de erro completa
- Arquivo de log relevante

---

## 📚 Recursos Adicionais

- **README.md** - Visão geral do projeto
- **Código fonte** - Totalmente auditável
- **Logs** - Rastreabilidade completa

---

## 🎓 Tutoriais em Vídeo (Futuro)

- Instalação passo a passo
- Primeiro uso
- Casos de uso avançados
- Resolução de problemas

---

**Versão**: 1.0
**Atualizado**: 2024
**Status**: Estável

---

💡 **Dica Final**: Comece simples! Use os botões rápidos e comandos básicos antes de explorar funcionalidades avançadas.

**Bom uso!** ⚡

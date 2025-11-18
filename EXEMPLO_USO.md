# 📖 Exemplo de Uso - DET Robot

## Caso de Uso: Verificar mensagens não lidas de 50 CNPJs

### Passo 1: Preparar arquivo de CNPJs

Edite o arquivo `cnpjs.txt`:

```txt
# Lista de CNPJs para processar
# Empresa A
12.345.678/0001-90

# Empresa B
98.765.432/0001-00

# Empresa C
11.222.333/0001-44

# ... adicione quantos CNPJs precisar
```

### Passo 2: Executar processamento

**Windows:**
```batch
PROCESSAR.bat
```

**Linux/Mac:**
```bash
bash PROCESSAR.sh
```

### Passo 3: Acompanhar execução

O sistema exibirá:

```
============================================================
   DET ROBOT - PROCESSADOR AUTOMATIZADO DE CNPJs
============================================================

📋 Encontrados 50 CNPJs para processar:
   1. 12.345.678/0001-90
   2. 98.765.432/0001-00
   3. 11.222.333/0001-44
   4. 22.333.444/0001-55
   5. 33.444.555/0001-66
   ... e mais 45 CNPJs

Deseja continuar? (S/N): S

============================================================
INICIANDO PROCESSAMENTO...
============================================================

Iniciando navegador...
OK: Navegador iniciado

Acessando portal DET...
OK: Portal acessado

============================================================
ATENÇÃO: Faça login manualmente no portal DET
O processamento iniciará em 30 segundos...
============================================================

[1/50] Processando CNPJ 12.345.678/0001-90...
Trocando perfil para 12.345.678/0001-90...
Acessando mensagens...
Extraindo mensagens não lidas...
✓ 12.345.678/0001-90: 3 mensagens não lidas

[2/50] Processando CNPJ 98.765.432/0001-00...
Trocando perfil para 98.765.432/0001-00...
Acessando mensagens...
Extraindo mensagens não lidas...
✓ 98.765.432/0001-00: 0 mensagens não lidas

[3/50] Processando CNPJ 11.222.333/0001-44...
...
```

### Passo 4: Resultados

Após processar todos os CNPJs:

```
============================================================
PROCESSAMENTO CONCLUÍDO!
============================================================

Total de CNPJs: 50
Processados com sucesso: 48
CNPJs com mensagens: 12
Total de mensagens: 27
Erros: 2
Tempo total: 245.3s
============================================================

✅ PROCESSAMENTO CONCLUÍDO COM SUCESSO!
============================================================

📊 Estatísticas:
   Total de CNPJs: 50
   CNPJs com mensagens: 12
   Total de mensagens: 27
   Erros: 2

📄 Relatório gerado:
   exports/relatorio_cnpjs_20241118_143522.html

============================================================
```

### Passo 5: Visualizar relatório

Abra o arquivo HTML gerado em `exports/`:

**O relatório mostrará:**

📊 **Dashboard com estatísticas:**
- Total de CNPJs processados
- CNPJs com mensagens
- Total de mensagens encontradas
- Quantidade de erros
- Tempo total de execução

📧 **Seção: CNPJs com Mensagens (12)**
```
┌─────────────────────────────────────────────────┐
│ 12.345.678/0001-90          [3 mensagens]      │
├─────────────────────────────────────────────────┤
│ ✉️ Notificação de Autuação                     │
│    De: Ministério do Trabalho | 15/11/2024     │
│                                                 │
│ ✉️ Solicitação de Documentos                   │
│    De: Fiscal Silva | 14/11/2024               │
│                                                 │
│ ✉️ Prazo para Manifestação                     │
│    De: Sistema DET | 13/11/2024                │
└─────────────────────────────────────────────────┘

... mais 11 CNPJs com mensagens
```

✓ **Seção: CNPJs sem Mensagens (36)**
```
✓ 98.765.432/0001-00 - Sem mensagens
✓ 22.333.444/0001-55 - Sem mensagens
... mais 34 CNPJs
```

⚠️ **Seção: CNPJs com Erros (2)**
```
❌ 99.888.777/0001-00
   Erro: Botão de trocar perfil não encontrado

❌ 88.777.666/0001-00
   Erro: Timeout ao acessar mensagens
```

---

## Vantagens desta abordagem

✅ **Totalmente automatizado** - Processa dezenas/centenas de CNPJs sem intervenção

✅ **Relatório visual** - HTML profissional e fácil de compartilhar

✅ **Organizado** - Separa CNPJs com/sem mensagens e erros

✅ **Auditável** - Logs detalhados de cada operação

✅ **Rápido** - Processa ~5 segundos por CNPJ (aprox.)

✅ **Seguro** - Login manual, sem armazenar credenciais

---

## Dicas de Uso

💡 **Para grandes volumes:**
- Divida em lotes de 100 CNPJs
- Execute em horários de menor tráfego no DET

💡 **Se encontrar erros:**
- Verifique logs na pasta `logs/`
- Reexecute apenas os CNPJs com erro

💡 **Para relatórios recorrentes:**
- Mantenha o `cnpjs.txt` atualizado
- Execute diariamente/semanalmente
- Compare relatórios anteriores

💡 **Screenshots automáticos:**
- Ativados automaticamente em erros
- Salvos em `screenshots/` com timestamp
- Úteis para troubleshooting

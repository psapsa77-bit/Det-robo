// Funções de API
async function apiCall(endpoint, method = 'POST', data = null) {
    try {
        const options = {
            method: method,
            headers: {
                'Content-Type': 'application/json',
            }
        };

        if (data) {
            options.body = JSON.stringify(data);
        }

        const response = await fetch(endpoint, options);
        const result = await response.json();
        return result;
    } catch (error) {
        return {
            success: false,
            message: `Erro de conexão: ${error.message}`
        };
    }
}

// Funções de controle do navegador
async function startBrowser() {
    showMessage('Iniciando navegador...', 'info');
    const result = await apiCall('/api/browser/start');
    showMessage(result.message, result.success ? 'success' : 'error');

    if (result.success) {
        setTimeout(updateStatus, 1000);
    }
}

async function stopBrowser() {
    showMessage('Fechando navegador...', 'info');
    const result = await apiCall('/api/browser/stop');
    showMessage(result.message, result.success ? 'success' : 'error');

    if (result.success) {
        updateStatusDisplay(false, null, null);
    }
}

async function navigateToUrl() {
    const url = document.getElementById('urlInput').value.trim();

    if (!url) {
        showMessage('Por favor, digite uma URL', 'error');
        return;
    }

    showMessage(`Navegando para ${url}...`, 'info');
    const result = await apiCall('/api/browser/navigate', 'POST', { url: url });
    showMessage(result.message, result.success ? 'success' : 'error');

    if (result.success) {
        setTimeout(updateStatus, 1000);
    }
}

async function navigateTo(url) {
    document.getElementById('urlInput').value = url;
    await navigateToUrl();
}

async function goBack() {
    showMessage('Voltando...', 'info');
    const result = await apiCall('/api/browser/back');
    showMessage(result.message, result.success ? 'success' : 'error');

    if (result.success) {
        setTimeout(updateStatus, 1000);
    }
}

async function goForward() {
    showMessage('Avançando...', 'info');
    const result = await apiCall('/api/browser/forward');
    showMessage(result.message, result.success ? 'success' : 'error');

    if (result.success) {
        setTimeout(updateStatus, 1000);
    }
}

async function refresh() {
    showMessage('Atualizando página...', 'info');
    const result = await apiCall('/api/browser/refresh');
    showMessage(result.message, result.success ? 'success' : 'error');
}

async function takeScreenshot() {
    showMessage('Capturando screenshot...', 'info');
    const result = await apiCall('/api/browser/screenshot');
    showMessage(result.message, result.success ? 'success' : 'error');
}

async function updateStatus() {
    const result = await apiCall('/api/browser/status', 'GET');

    if (result.success && result.status) {
        const status = result.status;
        updateStatusDisplay(status.running, status.url, status.title);
    }
}

// Funções de interface
function updateStatusDisplay(running, url, title) {
    const statusDot = document.querySelector('.status-dot');
    const statusText = document.getElementById('statusText');
    const pageInfo = document.getElementById('pageInfo');

    if (running) {
        statusDot.classList.remove('offline');
        statusDot.classList.add('online');
        statusText.textContent = 'Navegador Ativo';
        pageInfo.textContent = title || 'Carregando...';

        if (url) {
            pageInfo.title = url;
        }
    } else {
        statusDot.classList.remove('online');
        statusDot.classList.add('offline');
        statusText.textContent = 'Navegador Desligado';
        pageInfo.textContent = 'Nenhuma';
        pageInfo.title = '';
    }
}

function showMessage(message, type) {
    const messagesDiv = document.getElementById('messages');

    const messageEl = document.createElement('div');
    messageEl.className = `message ${type}`;
    messageEl.textContent = message;

    messagesDiv.appendChild(messageEl);

    // Remove mensagens antigas (mantém apenas as últimas 5)
    const messages = messagesDiv.querySelectorAll('.message');
    if (messages.length > 5) {
        messages[0].remove();
    }

    // Auto-remove após 5 segundos
    setTimeout(() => {
        messageEl.style.opacity = '0';
        setTimeout(() => messageEl.remove(), 300);
    }, 5000);
}

function handleUrlKeypress(event) {
    if (event.key === 'Enter') {
        navigateToUrl();
    }
}

// Atualiza status periodicamente
setInterval(updateStatus, 5000);

// Atualiza status ao carregar a página
window.addEventListener('load', updateStatus);

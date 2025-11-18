"""
Robô Simples - Aplicação Flask para controlar o navegador
"""
from flask import Flask, render_template, request, jsonify
from browser_controller import BrowserController

app = Flask(__name__)
browser = BrowserController()


@app.route('/')
def index():
    """Página principal com interface do robô"""
    return render_template('index.html')


@app.route('/api/browser/start', methods=['POST'])
def start_browser():
    """Inicia o navegador"""
    try:
        browser.start()
        return jsonify({'success': True, 'message': 'Navegador iniciado com sucesso!'})
    except Exception as e:
        return jsonify({'success': False, 'message': f'Erro ao iniciar navegador: {str(e)}'})


@app.route('/api/browser/stop', methods=['POST'])
def stop_browser():
    """Fecha o navegador"""
    try:
        browser.stop()
        return jsonify({'success': True, 'message': 'Navegador fechado com sucesso!'})
    except Exception as e:
        return jsonify({'success': False, 'message': f'Erro ao fechar navegador: {str(e)}'})


@app.route('/api/browser/navigate', methods=['POST'])
def navigate():
    """Navega para uma URL"""
    try:
        data = request.get_json()
        url = data.get('url', '')

        if not url:
            return jsonify({'success': False, 'message': 'URL não fornecida'})

        browser.navigate(url)
        return jsonify({'success': True, 'message': f'Navegando para {url}'})
    except Exception as e:
        return jsonify({'success': False, 'message': f'Erro ao navegar: {str(e)}'})


@app.route('/api/browser/back', methods=['POST'])
def go_back():
    """Volta para a página anterior"""
    try:
        browser.go_back()
        return jsonify({'success': True, 'message': 'Voltou para página anterior'})
    except Exception as e:
        return jsonify({'success': False, 'message': f'Erro ao voltar: {str(e)}'})


@app.route('/api/browser/forward', methods=['POST'])
def go_forward():
    """Avança para a próxima página"""
    try:
        browser.go_forward()
        return jsonify({'success': True, 'message': 'Avançou para próxima página'})
    except Exception as e:
        return jsonify({'success': False, 'message': f'Erro ao avançar: {str(e)}'})


@app.route('/api/browser/refresh', methods=['POST'])
def refresh():
    """Atualiza a página atual"""
    try:
        browser.refresh()
        return jsonify({'success': True, 'message': 'Página atualizada'})
    except Exception as e:
        return jsonify({'success': False, 'message': f'Erro ao atualizar: {str(e)}'})


@app.route('/api/browser/screenshot', methods=['POST'])
def take_screenshot():
    """Tira uma captura de tela"""
    try:
        filename = browser.take_screenshot()
        return jsonify({'success': True, 'message': f'Screenshot salva: {filename}'})
    except Exception as e:
        return jsonify({'success': False, 'message': f'Erro ao tirar screenshot: {str(e)}'})


@app.route('/api/browser/status', methods=['GET'])
def get_status():
    """Retorna o status do navegador"""
    try:
        status = browser.get_status()
        return jsonify({'success': True, 'status': status})
    except Exception as e:
        return jsonify({'success': False, 'message': f'Erro ao obter status: {str(e)}'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

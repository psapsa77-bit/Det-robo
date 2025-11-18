"""
Robô Simples - Aplicação Flask para controlar o navegador
"""
from flask import Flask, render_template, request, jsonify
from browser_controller import BrowserController
from command_processor import CommandProcessor

app = Flask(__name__)
browser = BrowserController()
command_processor = CommandProcessor()


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


@app.route('/api/command/process', methods=['POST'])
def process_command():
    """Processa um comando em linguagem natural"""
    try:
        data = request.get_json()
        command_text = data.get('command', '')

        if not command_text:
            return jsonify({
                'success': False,
                'message': 'Comando não fornecido'
            })

        # Processa o comando
        action, param, suggestion = command_processor.process(command_text)

        # Se não reconheceu, retorna sugestão
        if action is None:
            return jsonify({
                'success': False,
                'message': suggestion
            })

        # Obtém descrição da ação
        description = command_processor.get_action_description(action, param)

        # Executa a ação correspondente
        result = execute_action(action, param)

        return jsonify({
            'success': result['success'],
            'message': result['message'],
            'action': action,
            'description': description
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Erro ao processar comando: {str(e)}'
        })


def execute_action(action, param):
    """Executa a ação correspondente ao comando"""
    try:
        if action == 'navigate':
            browser.navigate(param)
            return {'success': True, 'message': f'Navegando para {param}'}

        elif action == 'search':
            search_url = command_processor.get_search_url(param)
            browser.navigate(search_url)
            return {'success': True, 'message': f'Pesquisando: {param}'}

        elif action == 'back':
            browser.go_back()
            return {'success': True, 'message': 'Voltou para página anterior'}

        elif action == 'forward':
            browser.go_forward()
            return {'success': True, 'message': 'Avançou para próxima página'}

        elif action == 'refresh':
            browser.refresh()
            return {'success': True, 'message': 'Página atualizada'}

        elif action == 'screenshot':
            filename = browser.take_screenshot()
            return {'success': True, 'message': f'Screenshot salva: {filename}'}

        elif action == 'start':
            browser.start()
            return {'success': True, 'message': 'Navegador iniciado'}

        elif action == 'stop':
            browser.stop()
            return {'success': True, 'message': 'Navegador fechado'}

        elif action == 'scroll_down':
            browser.scroll('down')
            return {'success': True, 'message': 'Rolou para baixo'}

        elif action == 'scroll_up':
            browser.scroll('up')
            return {'success': True, 'message': 'Rolou para cima'}

        elif action == 'scroll_top':
            browser.scroll('top')
            return {'success': True, 'message': 'Foi para o topo'}

        elif action == 'scroll_bottom':
            browser.scroll('bottom')
            return {'success': True, 'message': 'Foi para o final'}

        elif action == 'info':
            status = browser.get_status()
            return {
                'success': True,
                'message': f"Título: {status['title']}\nURL: {status['url']}"
            }

        else:
            return {'success': False, 'message': f'Ação não implementada: {action}'}

    except Exception as e:
        return {'success': False, 'message': str(e)}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

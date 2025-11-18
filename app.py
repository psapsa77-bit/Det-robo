"""
DET Robot - Aplicação Flask para automação DET
Sistema modular profissional para automação do Domicílio Eletrônico Trabalhista
"""
from flask import Flask, render_template, request, jsonify
from browser_controller import BrowserController
from command_processor import CommandProcessor

# Nova estrutura modular
from det_robot import DETConfig, DETAutomation, DETExtractor, DETReporter

app = Flask(__name__)

# Configuração e instâncias
config = DETConfig()
browser = BrowserController()
command_processor = CommandProcessor()

# Instância de automação DET (será recriada quando necessário)
det_automation = None
det_extractor = None
det_reporter = None


def get_det_automation():
    """Obtém ou cria instância de automação DET"""
    global det_automation, det_extractor, det_reporter

    if det_automation is None:
        det_automation = DETAutomation(config)
        det_extractor = DETExtractor(det_automation, config)
        det_reporter = DETReporter(config)

    return det_automation


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

        # Ações DET - usando nova estrutura modular
        elif action == 'det_acessar':
            det = get_det_automation()
            return det.access_det()

        elif action == 'det_trocar_perfil':
            det = get_det_automation()
            # Se param contém nome ou CNPJ
            if param:
                # Verifica se parece com CNPJ (números)
                if param.replace('.', '').replace('/', '').replace('-', '').isdigit():
                    return det.switch_profile(cnpj=param)
                else:
                    return det.switch_profile(company_name=param)
            else:
                # Sem parâmetro, só abre o seletor
                return det.switch_profile()

        elif action == 'det_verificar_mensagens':
            # Usa o extrator para verificar mensagens
            det = get_det_automation()
            if det_extractor:
                result = det_extractor.extract_unread_messages()
                if result['success']:
                    return {
                        'success': True,
                        'message': f"Encontradas {result['count']} mensagens não lidas"
                    }
                return result
            return {'success': False, 'message': 'Extrator não disponível'}

        elif action == 'det_acessar_mensagens':
            det = get_det_automation()
            return det.access_messages()

        elif action == 'det_listar_mensagens':
            # Usa o extrator para listar mensagens
            det = get_det_automation()
            if det_extractor:
                result = det_extractor.extract_unread_messages()
                if result['success'] and result['count'] > 0:
                    messages_text = '\n'.join([
                        f"- {msg['subject']} ({msg['sender']})"
                        for msg in result['messages'][:5]
                    ])
                    return {
                        'success': True,
                        'message': f"Mensagens não lidas:\n{messages_text}"
                    }
                return result
            return {'success': False, 'message': 'Extrator não disponível'}

        elif action == 'det_abrir_primeira_mensagem':
            det = get_det_automation()
            return det.click_first_unread_message()

        else:
            return {'success': False, 'message': f'Ação não implementada: {action}'}

    except Exception as e:
        return {'success': False, 'message': str(e)}


@app.route('/api/det/extract/messages', methods=['POST'])
def extract_messages():
    """Extrai mensagens não lidas estruturadas"""
    try:
        det = get_det_automation()
        if det_extractor:
            result = det_extractor.extract_unread_messages()
            return jsonify(result)
        return jsonify({'success': False, 'message': 'Extrator não disponível'})
    except Exception as e:
        return jsonify({'success': False, 'message': f'Erro: {str(e)}'})


@app.route('/api/det/extract/profiles', methods=['POST'])
def extract_profiles():
    """Extrai perfis/empresas disponíveis"""
    try:
        det = get_det_automation()
        if det_extractor:
            result = det_extractor.extract_available_profiles()
            return jsonify(result)
        return jsonify({'success': False, 'message': 'Extrator não disponível'})
    except Exception as e:
        return jsonify({'success': False, 'message': f'Erro: {str(e)}'})


@app.route('/api/det/extract/dashboard', methods=['POST'])
def extract_dashboard():
    """Extrai dados do dashboard"""
    try:
        det = get_det_automation()
        if det_extractor:
            result = det_extractor.extract_dashboard_data()
            return jsonify(result)
        return jsonify({'success': False, 'message': 'Extrator não disponível'})
    except Exception as e:
        return jsonify({'success': False, 'message': f'Erro: {str(e)}'})


@app.route('/api/det/report/generate', methods=['POST'])
def generate_report():
    """Gera relatório das mensagens"""
    try:
        data = request.get_json()
        format_type = data.get('format', 'html')  # html ou json
        title = data.get('title', 'Relatório DET')

        det = get_det_automation()
        if not det_extractor or not det_reporter:
            return jsonify({'success': False, 'message': 'Serviços não disponíveis'})

        # Extrai dados
        messages_data = det_extractor.extract_unread_messages()

        if not messages_data['success']:
            return jsonify(messages_data)

        # Gera relatório
        if format_type == 'html':
            filepath = det_reporter.generate_html_report(messages_data, title)
        else:
            filepath = det_reporter.export_json(messages_data)

        return jsonify({
            'success': True,
            'message': f'Relatório gerado com sucesso!',
            'filepath': str(filepath)
        })

    except Exception as e:
        return jsonify({'success': False, 'message': f'Erro: {str(e)}'})


if __name__ == '__main__':
    print("\n" + "="*50)
    print("  DET ROBOT - Sistema Iniciado")
    print("="*50)
    print(f"  Porta: 5000")
    print(f"  URL: http://localhost:5000")
    print(f"  Logs: {config.LOGS_DIR}")
    print(f"  Exports: {config.EXPORTS_DIR}")
    print("="*50 + "\n")

    app.run(debug=True, host='0.0.0.0', port=5000)

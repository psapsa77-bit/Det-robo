#!/usr/bin/env python3
"""
Script Standalone para Processar CNPJs
Executa o fluxo completo de automação DET
"""
import sys
import logging
from pathlib import Path

# Adiciona diretório raiz ao path
sys.path.insert(0, str(Path(__file__).parent))

from det_robot import CNPJProcessor, DETConfig


def main():
    """
    Função principal do processamento
    """
    print("\n" + "="*70)
    print(" "*15 + "⚡ DET ROBOT - PROCESSADOR DE CNPJs")
    print("="*70)
    print()
    print("Este script irá:")
    print("  1. Ler a lista de CNPJs do arquivo cnpjs.txt")
    print("  2. Acessar o portal DET")
    print("  3. Para cada CNPJ:")
    print("     - Trocar o perfil")
    print("     - Verificar mensagens não lidas")
    print("     - Coletar os dados")
    print("  4. Gerar relatório consolidado HTML")
    print()
    print("="*70)
    print()

    # Verifica se arquivo de CNPJs existe
    cnpj_file = Path("cnpjs.txt")
    if not cnpj_file.exists():
        print("❌ ERRO: Arquivo cnpjs.txt não encontrado!")
        print()
        print("Por favor:")
        print("  1. Crie o arquivo cnpjs.txt")
        print("  2. Adicione seus CNPJs (um por linha)")
        print("  3. Execute este script novamente")
        print()
        return 1

    # Lê e exibe CNPJs
    with open(cnpj_file, 'r', encoding='utf-8') as f:
        cnpjs_raw = [line.strip() for line in f if line.strip() and not line.strip().startswith('#')]

    if not cnpjs_raw:
        print("❌ ERRO: Nenhum CNPJ encontrado no arquivo cnpjs.txt!")
        print()
        print("Adicione CNPJs ao arquivo (um por linha) e tente novamente.")
        print()
        return 1

    print(f"📋 Encontrados {len(cnpjs_raw)} CNPJs para processar:")
    for i, cnpj in enumerate(cnpjs_raw[:5], 1):
        print(f"   {i}. {cnpj}")
    if len(cnpjs_raw) > 5:
        print(f"   ... e mais {len(cnpjs_raw) - 5} CNPJs")
    print()

    # Confirmação
    resposta = input("Deseja continuar? (S/N): ").strip().upper()
    if resposta != 'S':
        print("\n❌ Processamento cancelado pelo usuário.\n")
        return 0

    print()
    print("="*70)
    print("INICIANDO PROCESSAMENTO...")
    print("="*70)
    print()

    # Inicializa processador
    config = DETConfig()
    processor = CNPJProcessor(config)

    try:
        # Executa processamento completo
        resultado = processor.run(cnpj_file)

        print()
        print("="*70)

        if resultado['success']:
            print("✅ PROCESSAMENTO CONCLUÍDO COM SUCESSO!")
            print("="*70)
            print()
            print(f"📊 Estatísticas:")
            stats = resultado.get('stats', {})
            print(f"   Total de CNPJs: {stats.get('total_cnpjs', 0)}")
            print(f"   CNPJs com mensagens: {stats.get('com_mensagens', 0)}")
            print(f"   Total de mensagens: {stats.get('total_mensagens', 0)}")
            print(f"   Erros: {stats.get('erros', 0)}")
            print()
            print(f"📄 Relatório gerado:")
            print(f"   {resultado.get('report_path', 'N/A')}")
            print()
            print("="*70)
            return 0
        else:
            print("❌ ERRO NO PROCESSAMENTO")
            print("="*70)
            print()
            print(f"Mensagem: {resultado.get('message', 'Erro desconhecido')}")
            print()
            return 1

    except KeyboardInterrupt:
        print("\n\n❌ Processamento interrompido pelo usuário (Ctrl+C)\n")
        return 1

    except Exception as e:
        print(f"\n\n❌ ERRO FATAL: {str(e)}\n")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())

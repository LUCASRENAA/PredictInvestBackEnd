import json
import os

SEVERITY_EMOJI = {
    'LOW': '🟢',
    'MEDIUM': '🟡',
    'HIGH': '🔴'
}

def load_bandit_report(file_path):
    """Carrega o relatório do Bandit a partir de um arquivo JSON."""
    if not os.path.exists(file_path):
        print(f'❌ Arquivo "{file_path}" não encontrado.')
        return None

    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(f'❌ Erro ao decodificar o arquivo "{file_path}". Verifique se é um JSON válido.')
        return None

def format_vulnerability(vuln):
    """Formata a exibição de uma vulnerabilidade de forma legível."""
    severity = vuln.get("issue_severity", "N/A").upper()
    severity_emoji = SEVERITY_EMOJI.get(severity, '❓')
    issue_text = vuln.get("issue_text", "Descrição não disponível")
    filename = vuln.get("filename", "Desconhecido")
    line_number = vuln.get("line_number", "Desconhecida")
    test_id = vuln.get("test_id", "N/A")
    test_name = vuln.get("test_name", "N/A")
    more_info = vuln.get("more_info", "N/A")
    code = vuln.get("code", "").strip()

    return f"""{severity_emoji} {severity} - {issue_text}
    📄 Arquivo: {filename}
    📌 Linha: {line_number}
    🧪 Teste: {test_id} - {test_name}
    🔗 Mais info: {more_info}
    💻 Código:
{code}
"""

def print_vulnerabilities(results):
    """Imprime as vulnerabilidades encontradas no relatório."""
    if not results:
        print('✅ Nenhuma vulnerabilidade encontrada pelo Bandit.')
        return

    print(f'🔍 {len(results)} vulnerabilidades encontradas:\n')
    for r in results:
        print(format_vulnerability(r))

def main():
    """Função principal para processar o relatório do Bandit."""
    report = load_bandit_report('bandit-report.json')
    if report:
        results = report.get('results', [])
        print_vulnerabilities(results)

if __name__ == '__main__':
    main()
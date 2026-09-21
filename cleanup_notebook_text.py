import json
from pathlib import Path

path = Path("c:/Users/vinic/OneDrive/Desktop/GIT/sensored-walkability-review/notebooks/06_1_v8_Walkability_Dimension_Classification.ipynb")

replacements = {
    "Macro-dimensões: 5\\n": "Macro-dimensions: 5\\n",
    "Total de subdomínios: 60\\n": "Total subdomains: 60\\n",
    "Macro-dimensões: 5\n": "Macro-dimensions: 5\n",
    "Total de subdomínios: 60\n": "Total subdomains: 60\n",
    "[v2 (tópico)      ]": "[v2 (topic)      ]",
    "[v3 (medição)     ]": "[v3 (measurement)]",
    "[estética sem medir]": "[aesthetics without measurement]",
    "  sem margem :": "  without margin :",
    "  com margem :": "  with margin :",
    "Combinação macro em uso: MACRO_COMBINATION = 'mean_margin'": "Macro combination in use: MACRO_COMBINATION = 'mean_margin'",
    "Distribuição por âncora disparada (entre esses):": "Distribution by fired anchor (among these):",
    "Macro (subdomínio + verificação macro − margem negativa):": "Macro (subdomain + macro verification − negative margin):",
    "Distribuição por âncora disparada, entre os positivos indevidamente rejeitados:": "Distribution by fired anchor among incorrectly rejected positives:",
    "Títulos:": "Titles:",
    "Atribuições ao estilo v2 (só melhor subdomínio):": "Assignments in v2 style (best subdomain only):",
    "Atribuições v3 (com verificação macro):": "Assignments in v3 (with macro verification):",
    "Diferença:": "Difference:",
    "reagrega dos subdomínios, com mapeamento exato.": "re-aggregates the subdomains with exact mapping.",
    "João's companion sensor-type notebook": "the companion sensor-type notebook",
    "run João's sensor-type classification notebook first": "run the sensor-type classification notebook first",
    "run João's sensor-type classification notebook ": "run the sensor-type classification notebook ",
    "João's": "",
    "Macro-dimensões:": "Macro-dimensions:",
    "Total de subdomínios:": "Total subdomains:",
    "v2 (tópico)": "v2 (topic)",
    "v3 (medição)": "v3 (measurement)",
    "Subdomínio": "Subdomain",
    "subdomínio": "subdomain",
    "macro-dimensão": "macro-dimension",
    "macro-dimensões": "macro-dimensions",
    "Atribuições ao estilo v2": "Assignments in v2 style",
    "Atribuições v3": "Assignments in v3",
    "Distribuição por âncora disparada": "Distribution by fired anchor",
    "com verificação macro": "with macro verification",
    "por subdomínio isolado": "by isolated subdomain",
    "FIM": "END",
    "só melhor subdomínio": "best subdomain only",
    "sem margem": "without margin",
    "com margem": "with margin",
    "estética sem medir": "aesthetics without measurement",
}

def walk(obj):
    if isinstance(obj, dict):
        for key, value in list(obj.items()):
            if isinstance(value, str):
                s = value
                for old, new in replacements.items():
                    s = s.replace(old, new)
                obj[key] = s
            else:
                walk(value)
    elif isinstance(obj, list):
        for item in obj:
            walk(item)


text = path.read_text(encoding="utf-8")
for old, new in replacements.items():
    text = text.replace(old, new)
path.write_text(text, encoding="utf-8")

print("Updated notebook text to English.")

# Fenômenos Mecânicos

## Laboratório de Física 1

### Motivação

Este projeto visa o estudo e a utilização de métricas para processamento e análise de dados laboratoriais em Física 1.

- Aprofundamento em física e métricas de análise
- Uso de pandas para ler e explorar dados
- Modularização de projetos em Python
- Prática de `clean code`

---

## Estrutura do Projeto

```
├── data/                # Planilhas de dados laboratoriais (.csv)
├── shared/              # Configurações e utilitários compartilhados
├── src/
│   ├── main.py          # Ponto de entrada do projeto
│   ├── modules/         # Módulos de métricas e utilidades
│   └── experiments/     # Experimentos organizados por pasta
├── requirements.txt     # Dependências do projeto
└── README.md            # Este arquivo
```

---

## Materiais Necessários

- Planilhas de dados laboratoriais no formato `.csv` (exemplos em `data/`)
- Python 3.10+ recomendado
- Dependências listadas em `requirements.txt`

---

## Instalação

1. Clone este repositório:
   ```sh
   git clone <url-do-repositorio>
   cd FEMEC
   ```

2. Crie um ambiente virtual (opcional, mas recomendado):
   ```sh
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

---

## Como Usar

1. Adicione suas planilhas de dados em `data/` seguindo o formato dos exemplos (`lab1.csv`, `lab2.csv`).

2. Execute o programa principal:
   ```sh
   python src/main.py
   ```

3. Siga as instruções do menu interativo para:
   - Calcular média e desvio padrão
   - Calcular valores experimentais
   - Realizar propagação de erros

---

## Exemplo de Uso

```
LABORATÓRIO DE FÍSICA 1 - MECÂNICA CLÁSSICA

Opções de Análise de Dados:
Lista de planilhas em data/: lab1, media

Digite o nome do planilha de dados: lab1

==================================================
1. Desvio Padrão de Média
2. Valores Experimentais (requer [mean] e [std]):
3. Propagação de Erros (requer [std])
q. Sair
==================================================
Escolha uma opção [1/2/3/q]:
```

---

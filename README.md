# test_github_actions

Este repositório é um projeto de estudo para aprender e demonstrar o uso do GitHub Actions.
O objetivo é criar workflows que verifiquem automaticamente o código em Pull Requests para a branch `main` — executando checks de `pre-commit` e os testes unitários com `pytest`.

## Estrutura

- `src/` - código fonte do estudo
- `tests/` - testes unitários (pytest)
- `.github/workflows/` - onde ficam os workflows do GitHub Actions (ex.: `ci.yml`)
- `requirements.txt` - dependências do projeto

## O que este projeto demonstra

- Como executar verificações automáticas (pre-commit)
- Como executar a suíte de testes automaticamente (pytest)
- Como configurar um workflow que roda em Pull Requests direcionados à branch `main`

## Como rodar localmente (Windows PowerShell)

Recomendo usar um ambiente virtual. Exemplo de passos no PowerShell:

```powershell
# criar e ativar venv
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# instalar dependências
pip install -r requirements.txt

# instalar pre-commit (se não estiver no requirements)
pip install pre-commit

# instalar os hooks de pre-commit no repositório
pre-commit install

# rodar todos os hooks em todos os arquivos
pre-commit run --all-files

# rodar os testes
pytest -v
```

Observação: ajuste a versão do Python conforme seu ambiente; este projeto funciona com Python 3.13

## Workflows (GitHub Actions)

Os workflows ficam em `.github/workflows/` e o que se espera neste repositório é um arquivo (`ci.yml` ou `ci.yaml`) que:

- roda em Pull Requests com destino `main`;
- configura o Python com `actions/setup-python`;
- instala dependências (cache de pip opcional);
- executa `pre-commit run --all-files`;
- executa `pytest` e falha se os testes não passarem.

# 📘 Assignment: Automated Data Pipeline with Python

## 🎯 Objective

Crie um script Python que obtenha dados JSON de uma API pública, valide e transforme os registros, salve-os em CSV e gere um resumo. Você vai praticar automação e integrar conceitos de APIs e análise de dados.

## 📝 Tasks

### 🛠️ Buscar Dados da API

#### Descrição
Complete `fetch_posts()` para obter os posts do endpoint JSONPlaceholder e converter a resposta JSON em dados Python.

#### Requisitos
O programa concluído deve:

- Fazer uma requisição GET ao endpoint configurado, com tempo limite.
- Decodificar a resposta JSON e confirmar que ela contém uma lista de registros.
- Informar falhas de rede, respostas HTTP inválidas ou JSON malformado sem exibir um traceback.

### 🛠️ Validar e Transformar Registros

#### Descrição
Complete `normalize_posts()` para validar os campos necessários e converter cada post em um registro pronto para análise.

#### Requisitos
O programa concluído deve:

- Exigir que cada registro tenha `id`, `userId`, `title` e `body` com os tipos esperados.
- Produzir para cada post os campos `id`, `user_id`, `title` e `word_count`.
- Calcular `word_count` contando as palavras no corpo do post e rejeitar registros inválidos com uma mensagem clara.

### 🛠️ Exportar e Automatizar o Relatório

#### Descrição
Complete `save_posts()` e `print_report()` e conecte as funções em `main()` para executar o pipeline de ponta a ponta.

#### Requisitos
O programa concluído deve:

- Salvar os registros em CSV com as colunas `id`, `user_id`, `title` e `word_count`.
- Exibir a quantidade de posts, a quantidade de usuários distintos e a média de palavras por post.
- Aceitar `--url` e `--output` na linha de comando, com valores padrão funcionais.
- Encerrar com uma mensagem de erro clara se a requisição, a validação ou a gravação falhar.
- Executar usando apenas a biblioteca padrão do Python.

Para testar, use o endpoint padrão `https://jsonplaceholder.typicode.com/posts`. Exemplo:

```text
python starter-code.py --output posts.csv
```
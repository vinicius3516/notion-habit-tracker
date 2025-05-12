
# 📅 Notion Habit Tracker Automation

Automação de criação semanal de hábitos no **Notion** usando **Python**, **AWS Lambda**, **GitHub Actions** e integração com a **Notion API**.  
Ideal para quem organiza sua semana com hábitos e quer **gerar automaticamente os dias** da semana toda com apenas um clique — ou melhor, nenhum 😄

Obs.: Como DevOps Engineer, eu não poderia deixar passar a chance de colocar uma pipeline para automatizar o deploy — mesmo sendo um projeto simples. A ideia é sempre aproveitar pra praticar e mostrar como dá pra aplicar automação e boas práticas em qualquer solução, por menor que pareça.
---

## ✨ O que esse projeto faz?

> Toda semana, no **domingo às 18h**, este projeto cria **automaticamente 7 novos dias** com os seguintes dados em seu banco de hábitos no Notion:

| Dia      | Data        | Campos de hábito                          |
|----------|-------------|-------------------------------------------|
| Domingo  | YYYY-MM-DD  | Exercise, English, Read Books...          |
| Segunda  | YYYY-MM-DD  | Todos os hábitos configuráveis            |
| ...      | ...         |                                           |

Além disso:
- ✅ Evita duplicações
- ✅ Totalmente automatizado
- ✅ Sem custo (usa AWS Lambda e GitHub Actions no free tier)
- ✅ Fácil de clonar, adaptar e escalar

---

## 🧠 O que mais você pode automatizar com a API do Notion?

Você pode:
- Criar páginas ou blocos de texto
- Adicionar tarefas com prazos em bancos de dados
- Atualizar valores de checkboxes
- Filtrar, buscar e listar conteúdo do seu workspace
- Conectar com Webhooks para ações reativas

---

## 🚀 Como rodar localmente (desenvolvimento)

### 1. Faça um **fork** deste repositório

Clique em "Fork" no topo da página para criar sua própria cópia.

---

### 2. Clone o repositório

```bash
git clone https://github.com/SEU_USUARIO/notion-habit-tracker.git
cd notion-habit-tracker
```

---

### 3. Crie e ative o ambiente virtual

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

---

### 5. Crie um arquivo `.env` com suas credenciais do Notion

```env
NOTION_TOKEN=seu_token_aqui
DATABASE_ID=seu_database_id_aqui
```

> ⚠️ Nunca suba seu `.env` para o GitHub!

---

### 6. Rode o script

```bash
python main.py
```

---

## 🛠 Como configurar o deploy automático na AWS Lambda

### 📦 O que está incluído:

- `lambda_function.py`: script adaptado para Lambda
- `.github/workflows/deploy.yml`: CI/CD para enviar à AWS
- Deploy automático a cada `git push` na branch `main`

---

### 1. Crie um usuário IAM na AWS

- Vá até IAM Console
- Crie um usuário com:
  - Acesso programático ✅
  - Permissão `AWSLambda_FullAccess`

---

### 2. No GitHub, adicione os secrets

Vá em Settings > Secrets > Actions e adicione:

| Nome                   | Valor (copiado da AWS)  |
|------------------------|--------------------------|
| `AWS_ACCESS_KEY_ID`    | sua chave pública        |
| `AWS_SECRET_ACCESS_KEY`| sua chave secreta        |

---

### 3. Configure variáveis na Lambda

Na AWS Lambda:

- Vá até sua função (ex: `habit-notion-lambda`)
- Clique em **Configuração > Variáveis de ambiente**
- Adicione:

```env
NOTION_TOKEN=seu_token_do_notion
DATABASE_ID=seu_database_id
```

---

### 4. Crie um agendamento (gatilho)

Use o EventBridge (CloudWatch Events):

- Cron: `cron(0 18 ? * 1 *)` → roda todo domingo às 18h
- Ação: chama sua função `habit-notion-lambda`

---

### ✅ Pronto! CI/CD ativo com deploy automático

Sempre que fizer um `git push` para `main`, o GitHub irá:

- Empacotar a função
- Fazer o deploy no Lambda
- Manter tudo sincronizado com seu código

---

## 📁 Estrutura do projeto

```bash
notion-habit-tracker/
├── .github/workflows/deploy.yml   # CI/CD
├── lambda_function.py             # Código da função Lambda
├── main.py                        # Execução local
├── requirements.txt               # Dependências do projeto
├── .gitignore                     # Ignora .env e venv
└── README.md                      # Documentação ✨
```

---

## 📌 Atenção

| Item                          | Necessário? | Observação                              |
|-------------------------------|-------------|------------------------------------------|
| `.env`                        | ✅           | Nunca suba ele ao repositório            |
| `venv/`                       | ✅           | Ambiente virtual — também ignorado       |
| `requirements.txt`            | ✅           | Deve sempre estar atualizado             |
| GitHub Secrets (IAM)          | ✅           | Permite deploy automático                 |
| Notion Internal Integration   | ✅           | Compartilhe o banco com a integração     |

---

## 🙌 Créditos

Este projeto foi idealizado e implementado por **Vinícius**!

---

## 📬 Licença

MIT — fique à vontade para adaptar e melhorar!
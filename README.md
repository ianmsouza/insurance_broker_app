# Insurance Broker App (Corretor Virtual de Seguros de Vida)

## Índice
- [Sobre](#sobre)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Uso](#uso)

## Sobre
Projeto da Disciplina 
IA generativa para linguagem 
LLM (Large Language Model)
24E2_3

## Pré-requisitos
Lista de pré-requisitos necessários para rodar o projeto:
- [Docker](https://www.docker.com/products/docker-desktop)
- [Git](https://git-scm.com/downloads)
- [VsCode](https://code.visualstudio.com/download)

## Instalação
Passos para instalar e configurar o ambiente de desenvolvimento local:
1. Clone o repositório:
   ```bash
   git clone https://github.com/ianmsouza/insurance_broker_app.git
   ```
2. Execute o app:
   ```bash
   streamlit run src/insurance_broker_app/app.py
   ```
4. Acesse localhost:8501
   ```bash
   http://localhost:8501/
   ```

## Uso
1. No campo "Conte-nos sobre você...", informe um prompt descrevendo duas caracteristicas como idade, ocupação, condição de saúde, histórico médico familiar, estilo de vida e hábitos como tabagismo e prática de exercícios físicos.
Exemplo: 
```bash
Tenho 50 anos, sou desenvolvedor de sistemas, sou obeso, tenho 110 quilos, 1,75cm de altura, pratico atividade física 2 vezes por semana, sempre faço check-up médico e exames de sangue regularmente e tenho pré-diabetes.
```
2. Clique no botão "Obter Sugestões de Seguro"
3. Será apresentado os "Planos de Seguro Sugeridos" pelo App com 3 opções de seguro de vida.


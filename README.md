# Chapada a dois · Julho de 2027

Aplicativo Streamlit com o roteiro mobile completo: nove dias, fotos e créditos,
links de trilhas, mapa local com trajetos e quilômetros, orçamento, favoritos e checklist.

## Publicar

1. Coloque o conteúdo desta pasta em um repositório GitHub próprio para o roteiro.
2. Entre em https://share.streamlit.io e escolha Create app / Deploy from GitHub.
3. Selecione o repositório, a branch e `streamlit_app.py` como arquivo principal.
4. Selecione Python 3.12 ou 3.13 e clique em Deploy.
5. Compartilhe o endereço `https://…streamlit.app` pelo WhatsApp.

Documentação: https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy

## Executar localmente

```sh
python -m pip install -r requirements.txt
python -m streamlit run streamlit_app.py
```

O componente serve `site/index.html` diretamente, sem Node ou compilação no servidor.
As fotos e novos cálculos de rotas requerem internet. As geometrias dos nove trajetos
estão incluídas. Favoritos e checklist são individuais por navegador.
Não há banco de dados, credenciais, tokens ou segredos necessários ao aplicativo.

Validação realizada: sintaxe Python e JavaScript e integridade do HTML.
Execução no Streamlit ainda depende de instalar os requisitos e concluir o deploy.

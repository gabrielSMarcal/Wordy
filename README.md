# Wordy

Wordy é um projeto em Python para gerar imagens sintéticas de letras maiúsculas e minúsculas, treinar um modelo de classificação e produzir relatórios com métricas, exemplos de predição e matriz de confusão.

## Visão Geral

O projeto segue este fluxo:

1. Gera um dataset sintético de letras com ruído.
2. Divide os dados em treino e teste.
3. Treina uma rede neural MLP.
4. Realiza previsões no conjunto de teste.
5. Gera relatórios e imagens com os resultados.

## Funcionalidades

- Geração automática de imagens sintéticas de letras.
- Classificação entre letras minúsculas e maiúsculas.
- Treinamento com `MLPClassifier` do scikit-learn.
- Relatório textual com métricas de desempenho.
- Salvamento de exemplos de classificação em imagem.
- Geração de matriz de confusão.
- Criação automática da pasta de relatórios.

## Estrutura do Projeto

```text
Wordy/
├── main.py
├── README.md
├── requirements.txt
├── wordy.bat
├── relatorio/
│   ├── classificacao/
│   ├── img/
│   └── matriz/
└── src/
    ├── classificador.py
    ├── gerador.py
    └── reporte.py
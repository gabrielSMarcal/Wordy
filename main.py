import numpy as np
from sklearn.model_selection import train_test_split

from src.gerador import GeradorLetraImagem
from src.classificador import Classificador
from src.reporte import GeradorReporte

TAMANHO_IMAGEM = 32

def main():
    print('Iniciando o processo de classificação de letras...')
    
    # 1. Geração de Dados
    gerador = GeradorLetraImagem(tamanho_img=TAMANHO_IMAGEM)
    X, y = gerador.criar_dataset(num_amostras=2000)
    print(f'Dataset gerado: {len(X)} amostras.')
    
    # 2. Divisão em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=642)
    print(f'Dados divididos: {len(X_train)} para treino e {len(X_test)} para teste.')
    
    # 3. Treinamento do modelo
    classificador = Classificador()
    classificador.treinar(X_train, y_train)
    
    # 4. Previsão
    y_pred = classificador.prever(X_test)
    print('Previsões realizadas.')
    
    # 5. Geração de Relatórios e Visualizações
    reporte = GeradorReporte(tamanho_img=TAMANHO_IMAGEM)
    
    # Relatório de Classificação
    reporte_classificacao = classificador.validar(y_test, y_pred)
    caminho_reporte = reporte.salvar_classificacao_reporte(reporte_classificacao)
    
    # Imagens de Exemplo
    caminho_exemplo = reporte.salvar_exemplo_imagens(X_test, y_test, y_pred)
    
    # Matriz de Confusão
    caminho_matriz = reporte.salvar_matriz_confusao(y_test, y_pred)
    
    print('\nProcesso concluído. Verifique os arquivos gerados no diretório atual.')
    
if __name__ == '__main__':
    main()
    
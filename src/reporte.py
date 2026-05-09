from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import numpy as np
import os

class GeradorReporte:
    """
    Classe para gerar e salvar relatórios e visualizações.
    """
    
    def __init__(self, tamanho_img=32, output_dir='.'):
        self.tamanho_img = tamanho_img
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        
    def salvar_classificacao_reporte(self, reporte, arquivo='metricas.txt'):
        """
        Salva o relatório de classificação em um arquivo.
        """
        
        caminho = os.path.join(self.output_dir, arquivo)
        with open(caminho, 'w') as f:
            f.write(reporte)
        print(f'Relatório de classificação salvo como "{caminho}"')
        
        return caminho
    
    def salvar_exemplo_imagens(self, X_test, y_test, y_pred, arquivo='exemplos_classificacao.png', exemplos=20):
        """
        Salva uma imagem com exemplos de classificação.
        """
        
        X_test_img = X_test.reshape((-1, self.tamanho_img, self.tamanho_img))
        fig, axs = plt.subplots(exemplos // 5, 5, figsize=(12, (exemplos // 5) * 2.5))
        for i, ax in enumerate(axs.ravel()):
            if i < exemplos:
                ax.imshow(X_test_img[i], cmap='gray')
                real = 'Maiúscula' if y_test[i] == 1 else 'Minúscula'
                pred = 'Maiúscula' if y_pred[i] == 1 else 'Minúscula'
                color = 'green' if y_test[i] == y_pred[i] else 'red'
                ax.set_title(f'Real: {real}\nPred: {pred}', color=color)
                ax.axis('off')
        plt.tight_layout()
        caminho = os.path.join(self.output_dir, arquivo)
        plt.savefig(caminho)
        print(f'Imagem de exemplos salva como "{caminho}"')
        return caminho
    
    def salvar_matriz_confusao(self, y_test, y_pred, target_names=['Minúscula', 'Maiúscula'], arquivo='matriz_confusao.png'):
        """
        Salva a matriz de confusão como uma imagem.
        """
        
        plt.figure(figsize=(8, 6))
        disp = ConfusionMatrixDisplay.from_predictions(
            y_test, y_pred,
            display_labels=target_names,
            cmap='Blues'
        )
        plt.title('Matriz de Confusão - Letras')
        caminho = os.path.join(self.output_dir, arquivo)
        plt.savefig(caminho)
        print(f'Matriz de confusão salva como "{caminho}"')
        
        return caminho
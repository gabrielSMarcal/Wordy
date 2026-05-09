from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import numpy as np
import os

class GeradorReporte:
    '''
    Classe para gerar e salvar relatórios e visualizações.
    '''
    
    def __init__(self, tamanho_img=32, output_dir='relatorio'):
        self.tamanho_img = tamanho_img
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        
    def salvar_classificacao_reporte(self, reporte, arquivo='metricas.txt'):
        '''
        Salva o relatório de classificação em um arquivo.
        '''
        
        dirc = os.path.join(self.output_dir, 'classificacao')
        os.makedirs(dirc, exist_ok=True)
        caminho = self._proximo_caminho(dirc, arquivo)
        with open(caminho, 'w', encoding='utf-8') as f:
            f.write(reporte)
        print(f'Relatório de classificação salvo como "{caminho}"')
        return caminho
    
    def salvar_exemplo_imagens(self, X_test, y_test, y_pred, arquivo='exemplos_classificacao.png', exemplos=20):
        '''
        Salva uma imagem com exemplos de classificação.
        '''
        
        dirimg = os.path.join(self.output_dir, 'img')
        os.makedirs(dirimg, exist_ok=True)

        X_test_img = X_test.reshape((-1, self.tamanho_img, self.tamanho_img))
        exemplos = min(exemplos, X_test_img.shape[0])
        n_rows = max(1, (exemplos + 4) // 5)
        fig, axs = plt.subplots(n_rows, 5, figsize=(12, n_rows * 2.5))
        for i, ax in enumerate(axs.ravel()):
            if i < exemplos:
                ax.imshow(X_test_img[i], cmap='gray')
                real = 'Maiúscula' if y_test[i] == 1 else 'Minúscula'
                pred = 'Maiúscula' if y_pred[i] == 1 else 'Minúscula'
                color = 'green' if y_test[i] == y_pred[i] else 'red'
                ax.set_title(f'Real: {real}\nPred: {pred}', color=color)
            ax.axis('off')
        plt.tight_layout()
        caminho = self._proximo_caminho(dirimg, arquivo)
        fig.savefig(caminho)
        plt.close(fig)
        print(f'Imagem de exemplos salva como "{caminho}"')
        return caminho
    
    def salvar_matriz_confusao(self, y_test, y_pred, target_names=['Minúscula', 'Maiúscula'], arquivo='matriz_confusao.png'):
        '''
        Salva a matriz de confusão como uma imagem.
        '''
        
        dirmat = os.path.join(self.output_dir, 'matriz')
        os.makedirs(dirmat, exist_ok=True)

        disp = ConfusionMatrixDisplay.from_predictions(
            y_test, y_pred,
            display_labels=target_names,
            cmap='Blues'
        )
        disp.ax_.set_title('Matriz de Confusão - Letras')
        caminho = self._proximo_caminho(dirmat, arquivo)
        disp.figure_.savefig(caminho)
        plt.close(disp.figure_)
        print(f'Matriz de confusão salva como "{caminho}"')
        return caminho

    def _proximo_caminho(self, pasta, arquivo):
        base, ext = os.path.splitext(arquivo)
        caminho = os.path.join(pasta, arquivo)
        indice = 1

        while os.path.exists(caminho):
            caminho = os.path.join(pasta, f"{base}_{indice}{ext}")
            indice += 1

        return caminho
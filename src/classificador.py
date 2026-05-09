from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report

class Classificador:
    '''
    Classe para treinar e avaliar o modelo de classificação de letras.
    '''
    
    def __init__(self, hidden_layer_sizes=(100, 50), activation='relu', solver='adam', max_iter=500, random_state=642):
        self.modelo = MLPClassifier(
            hidden_layer_sizes=hidden_layer_sizes,
            activation=activation,
            solver=solver,
            max_iter=max_iter,
            random_state=random_state
        )
        
    def treinar(self, X_train, y_train):
        '''
        Treina o modelo com os dados fornecidos.
        '''
        
        print('Treinando o modelo...')
        self.modelo.fit(X_train, y_train)
    
    def prever(self, X_test):
        '''
        Faz previsões dos dados de teste.
        '''
        
        return self.modelo.predict(X_test)
    
    def validar(self, y_test, y_pred, target_names=['Minúscula', 'Maiúscula']):
        '''
        Avalia o modelo e retorna o relatório de classificação.
        '''
        
        reporte = classification_report(y_test, y_pred, target_names=target_names)
        print('\n--- Métrica de Desempenho ---')
        print(reporte)
        
        return reporte
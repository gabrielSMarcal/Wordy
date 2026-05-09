import numpy as np
import cv2
import random
import string

class GeradorLetraImagem:
    '''
    Classe responsável por gerar imagens sintéticas de letras.
    '''
    
    def __init__(self,  tamanho_img=32):
        self.tamanho_img = tamanho_img
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        
    def _gerar_letra(self, letra, tamanho_fonte=1.0, espessura=2):
        '''
        Gera uma imagem de uma única letra com ruído.
        '''
        
        img = np.zeros((self.tamanho_img, self.tamanho_img), dtype=np.uint8)
        
        # Correção: cv2.getTextSize retorna (largura, altura) do texto
        tamanho_texto = cv2.getTextSize(letra, self.font, tamanho_fonte, espessura)[0]
        texto_x = (self.tamanho_img - tamanho_texto[0]) // 2
        texto_y = (self.tamanho_img + tamanho_texto[1]) // 2
        
        # O argumento tamanho_fonte em putText é um fator de escala, não o tamanho em pixels
        cv2.putText(img, letra, (texto_x, texto_y), self.font, tamanho_fonte, 255, espessura, cv2.LINE_AA)
        
        ruido = np.random.randint(0, 50, (self.tamanho_img, self.tamanho_img), dtype=np.uint8)
        img = cv2.add(img, ruido)
        
        return img
    
    def criar_dataset(self, num_amostras=2000):
        '''
        Cria um dataset de letras maiúsculas e minúsculas.
        '''
        
        x = []
        y = []
        
        letras_maiusculas = string.ascii_uppercase
        letras_minusculas = string.ascii_lowercase
        
        for _ in range(num_amostras):
            
            # Correção: A escolha entre maiúscula e minúscula deve ser booleana
            is_maiuscula = random.choice([True, False])
            
            if is_maiuscula:
                letter = random.choice(letras_maiusculas)
                label = 1  # 1 para maiúscula
            else:
                letter = random.choice(letras_minusculas)
                label = 0  # 0 para minúscula
                
            img = self._gerar_letra(letter)
            
            x.append(img)
            y.append(label)
            
        # Flatten das imagens para entrada na rede neural (MLP) e normalização
        x_flat = np.array(x).reshape(len(x), -1) / 255.0
        return x_flat, np.array(y)
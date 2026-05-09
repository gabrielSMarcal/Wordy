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
        
        tamanho_fonte = cv2.getTextSize(letra, self.font, tamanho_fonte, espessura)[0]
        texto_x = (self.tamanho_img - tamanho_fonte[0]) // 2
        texto_y = (self.tamanho_img + tamanho_fonte[1]) // 2
        
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
            
            maiusculo = random.choice(letras_maiusculas)
            
            if maiusculo:
                letter = random.choice(letras_maiusculas)
                label = 1
            else:
                letter = random.choice(letras_minusculas)
                label = 0
                
            img = self._gerar_letra(letter)
            
            x.append(img)
            y.append(label)
            
        return np.array(x), np.array(y)
        
    
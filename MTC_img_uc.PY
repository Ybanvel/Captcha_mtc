from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec #Tipo de condicion se necesita
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys # para pulsar teclas especiales
from appsdriver.iniciar_webdriver_uc import iniciar_webdriver
import time
import pickle
import os
import sys
import wget

def Ingresar_MTC():
        print("Ingresamos a la pagina")
        #Comprobamos si existe el archivo de cookies
        driver.get("https://slcp.mtc.gob.pe/")
        #Comprobamos si el login por cookies es correcto
        try:
            elemento = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR,  "select[id]")))
            print("Ingreso a pagina: OK")
            return "OK"
        except TimeoutException:
            print("No Se pudo Ingresar")
            sys.exit()
                     

def descargar_imagenes(valor):
        dat=0
        n=0   #numero de foto en curso 
        carpeta="imagenes_carp" 
        url_fotos=set()      
        #Descarga las imagenes
        while dat < valor:
            dat+=1
            #time.sleep(3)
            try:
                e = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "i.fa.fa-refresh.fa-2x")))
                e.click()
            except TimeoutException:
                return
            time.sleep(2)
            try:
                e = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "i.fa.fa-refresh.fa-2x")))
            except TimeoutException:
                return
            ele = driver.find_element(By.CSS_SELECTOR, "img#imgCaptcha").get_attribute("src")
            print(ele)
            url_fotos.add(ele)
            
        if not os.path.exists(carpeta):
            os.mkdir(carpeta)     
        for url_foto in url_fotos:
            n+=1
            print(f'Descargando {n} de {len(url_fotos)}')
            # Tuvimos problemas al descargar las fotos de captcha ya q nos descaragaba con otra extension 
            # y con el mismo nombre, por lo cual se garbaba solo dos valores se chancaba
            nombre_archivo = wget.download(url_foto ,out='Captcha_.jpg')          
            print(f'descargado {nombre_archivo}')
            print()
        return len(url_fotos)



if __name__ == '__main__':
# iniciamos selenium
    driver=iniciar_webdriver(headless=False, pos = "izquierda")
# configuramos el tiempo de espera para cargar elementos 
    wait=WebDriverWait (driver,5)
# Ingresamos a la pagina
    Ingresar_MTC()
    data= int(input("ingresar nro de imagenes:  "))
    descargar_imagenes(data)
    print("Termino de Decarga")
    driver.quit() 
    sys.exit()
                                                                    



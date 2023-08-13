import undetected_chromedriver as uc

def iniciar_webdriver (headless=False, pos="maximizada"):
    #Inici un navegador chrome y devueleve el objeto webdriver instanciado
    # pos indica la posicion del navegador en al pantalla

    # Instanciamos las opciones de chrome
    options = uc.ChromeOptions()
    # Desactivamos el guardado de credenciales
    options.add_argument("--password-store=basic")
    options.add_experimental_option(
        "prefs" ,
        {
            "credentials_enable_service": False,
            "profile.pasword_manage_enable":False,
        }
    )
    # Iniciamos el driver
    driver = uc.Chrome (
        options = options,
        headless = headless,
        log_level = 3,
    )
    # Posicionamos la ventana
    if not headless:
        driver.maximize_window()
        if pos != "maximizada":
        # obtenemos la reslucion de la ventana
            ancho, alto = driver.get_window_size().values()
            if pos == "izquierda":
                driver.set_window_rect(x=0, y =0, width=ancho//2, height=alto)
            elif pos == "derecha":
                driver.set_window_rect(x=ancho//2, y =0, width=ancho//2, height=alto)

    return driver
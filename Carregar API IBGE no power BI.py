# Importando API do IBGE "Nomes"
# Automatizando o tratamento de dados na ferramenta de Power BI


import time
import pyautogui        # interação com mouse e teclado
import pyperclip        # multiplataforma para copiar e colar funções da área de transferência


Nome = 'Escreva o nome da pessoa que se deseja consultar os dados'
API = 'Endereço Web API nomes IBGE' 
# Buscar no site: https://servicodados.ibge.gov.br/api/docs/censos/nomes?versao=2
# Utilize o pyautogui.position() para descobrir a posição do mouse

pyautogui.moveTo(240, 125, duration=0.25) #Move o mouse para "Obter dados do Power Bi"
pyautogui.click(240, 125, button='left', duration=0.25)

pyautogui.moveTo(261, 388, duration=0.25) #Move o mouse para "Importar da web"
pyautogui.click(261, 388, button='left', duration=0.25)

time.sleep(2)
pyautogui.moveTo(374, 370, duration=0.25) #Move o mouse para o endereço da busca
pyautogui.click(374, 370, button='left', duration=0.25)

pyperclip.copy(API) 
pyautogui.hotkey("ctrl","v")
pyautogui.moveTo(907, 434, duration=0.5) #Move o mouse para "ok"
pyautogui.click(907, 434, button='left', duration=0.5)
time.sleep(5)


pyautogui.moveTo(30, 85, duration=0.25) #Move o mouse para "Para a tabela" do power query
pyautogui.click(30, 85, button='left', duration=0.25)
time.sleep(2)

pyautogui.moveTo(895, 458, duration=0.25) #Move o mouse para "ok" do power query
pyautogui.click(895, 458, button='left', duration=0.25)
time.sleep(2)

pyautogui.moveTo(447,194, duration=0.25) #Expande a 1º seleção
pyautogui.click(447, 194, button='left', duration=0.25)
pyautogui.moveTo(332,431, duration=0.25) 
pyautogui.click(332, 431, button='left', duration=0.25)


pyautogui.moveTo(609,195, duration=0.25) #Expande a 2º seleção
pyautogui.click(609, 195, button='left', duration=0.25)
pyautogui.moveTo(551,215, duration=0.25) 
pyautogui.click(551, 215, button='left', duration=0.25)


pyautogui.moveTo(608,193, duration=0.25) #Expande a 3º seleção
pyautogui.click(608, 193, button='left', duration=0.25)
pyautogui.moveTo(506,432, duration=0.25) 
pyautogui.click(506, 432, button='left', duration=0.25)


pyautogui.moveTo(880,197, duration=0.25) #Adicionando coluna de exemplo
pyautogui.click(880, 197, button='left', duration=0.25)
pyautogui.moveTo(309,36, duration=0.25) 
pyautogui.click(309, 36, button='left', duration=0.25)
pyautogui.moveTo(53,106, duration=0.25) 
pyautogui.click(53, 106, button='left', duration=0.25)
pyautogui.moveTo(69,151, duration=0.25) 
pyautogui.click(69, 151, button='left', duration=0.25)
pyautogui.moveTo(901,260, duration=0.25) 
pyautogui.click(901, 260, button='left', duration=0.25)
pyperclip.copy('Nome')                  #Nome da coluna nova
pyautogui.hotkey("ctrl","v")
pyautogui.moveTo(892,283, duration=0.25) 
pyautogui.click(892, 283, button='left', duration=0.25)
pyperclip.copy(Nome)                #Nome pessoa
pyautogui.hotkey("ctrl","v")
pyautogui.moveTo(884,305, duration=0.25) 
pyautogui.click(884, 305, button='left', duration=0.25)
pyperclip.copy(Nome)                  #Nome pessoa
pyautogui.hotkey("ctrl","v")
pyautogui.moveTo(983,224, duration=0.25) 
pyautogui.click(983, 224, button='left', duration=0.25)
time.sleep(3)

pyautogui.moveTo(111,37, duration=0.25)  # Voltando para "Pagina Inicial"
pyautogui.click(111, 37, button='left', duration=0.25)


pyautogui.moveTo(38,77, duration=0.25)  # Fechar e Aplicar
pyautogui.click(38, 77, button='left', duration=0.25)
time.sleep(5)
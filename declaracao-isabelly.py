import sys
import time

def efeito_digitacao(texto, delay=0.005):
    """Exibe o texto letra por letra."""
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def exibir_animacao():
    # Código ANSI para a cor laranja no terminal
    COR_LARANJA = "\033[93m"
    COR_RESET = "\033[0m"
    
    arte_texto = """
  ███████╗██╗   ██╗    ████████╗███████╗    █████╗ ███╗   ███╗ ██████╗ 
  ██╔════╝██║   ██║    ╚══██╔══╝██╔════╝   ██╔══██╗████╗ ████║██╔═══██╗
  █████╗  ██║   ██║       ██║   █████╗     ███████║██╔████╔██║██║   ██║
  ██╔══╝  ██║   ██║       ██║   ██╔══╝     ██╔══██║██║╚██╔╝██║██║   ██║
  ███████╗╚██████╔╝       ██║   ███████╗   ██║  ██║██║ ╚═╝ ██║╚██████╔╝
  ╚══════╝ ╚═════╝        ╚═╝   ╚══════╝   ╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ 

   ██╗███████╗ █████╗ ██████╗ ███████╗██╗     ██╗    ██╗   ██╗
   ██║██╔════╝██╔══██╗██╔══██╗██╔════╝██║     ██║    ╚██╗ ██╔╝
   ██║███████╗███████║██████╔╝█████╗  ██║     ██║     ╚████╔╝ 
   ██║╚════██║██╔══██║██╔══██╗██╔══╝  ██║     ██║      ╚██╔╝  
   ██║███████║██║  ██║██████╔╝███████╗███████╗███████╗  ██║   
   ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝╚══════╝  ╚═╝   
"""
    
    # Aplica a cor e o efeito de digitação no texto principal
    sys.stdout.write(COR_LARANJA)
    efeito_digitacao(arte_texto)
    sys.stdout.write(COR_RESET)
    
    coracao = """
        ██████╗     ██████╗
      ██████████╗ ██████████╗
      ██████████████████████║
      ╚████████████████████╔╝
        ╚████████████████╔╝
          ╚████████████╔╝
            ╚████████╔╝
              ╚████╔╝
                ╚═╝
"""
    
    print("\n" * 1)
    print("Pressione Ctrl+C para encerrar a animação.")
    time.sleep(1)

    # Loop infinito para fazer o coração piscar
    try:
        while True:
            # Liga a cor laranja e mostra o coração
            sys.stdout.write(COR_LARANJA + coracao + COR_RESET)
            sys.stdout.flush()
            time.sleep(0.6)
            
            # Limpa as linhas do coração para dar o efeito de piscar
            linhas_coracao = coracao.strip("\n").count("\n") + 1
            for _ in range(linhas_coracao):
                sys.stdout.write("\033[F\033[K")
            sys.stdout.flush()
            time.sleep(0.4)
            
    except KeyboardInterrupt:
        print("\n\nAnimação encerrada.\nEspero que tenha gostado.")

if __name__ == "__main__":
    exibir_animacao()

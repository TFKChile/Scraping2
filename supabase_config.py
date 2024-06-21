from supabase import create_client
from datetime import datetime
import sys

from config import SUPABASE_URL, SUPABASE_KEY

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
id_url_paracom = -1

def validar_url(linkscrap, minero):
    global id_url_paracom
    try:
        response = supabase.table('URLS').select('ruta').eq('ruta', linkscrap).execute()
        if response.data:
            print(f"La URL {linkscrap} ya ha sido scrappeada anteriormente. Omitiendo.")
            return False
        else:
            insert_response = supabase.table('URLS').insert({
                'ruta': linkscrap,
                'minero': minero,
                'fecha_add': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'red_social': "Reddit"
            }).execute()

            if insert_response.data:
                url_id = insert_response.data[0]['id_url']
                print(f"La URL {linkscrap} ha sido registrada con ID: {url_id}")
                id_url_paracom = url_id
                return True
            else:
                print(f"Error al insertar la URL {linkscrap}.")
                return False
    except Exception as e:
        print(f"Error al validar o insertar la URL {linkscrap}:", e)
        return False

def insertar_comentarios(comentarios_array, minero):
    try:
        for comentario in comentarios_array:
            supabase.table('Comentarios').insert({
                'usuario': comentario['autor'],
                'comentario': comentario['comentario'],
                'fecha_com': comentario['fecha'],
                'minero': minero,  
                'fecha_add': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'id_url': id_url_paracom,
            }).execute()
        print("Comentarios añadidos.")
    except Exception as e:
        print("Error al insertar comentarios:", e)

import flet as ft
from pymongo import MongoClient
import json

# Conexión a MongoDB Atlas
uri = "mongodb+srv://Giochar:Maquiniitas2002@cluster0.4xn6wds.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)
db = client["farmacia_ujat"]
farmaco = db["farmaco"]
medicamento = db["medicamento"]

def main(page: ft.Page):
    page.title = "Subir datos JSON a MongoDB"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    caja_json = ft.TextField(label="Pega aquí el JSON de los datos", width=600, height=200, multiline=True)
    resultado = ft.Text("")

    def subir_datos(e):
        try:
            datos = json.loads(caja_json.value)
            if isinstance(datos, list) and datos and "clave" in datos[0]:
                medicamento.insert_many(datos)
                resultado.value = "Datos insertados en la colección 'medicamento'."
            elif isinstance(datos, list) and datos and "nombre" in datos[0]:
                farmaco.insert_many(datos)
                resultado.value = "Datos insertados en la colección 'farmaco'."
            else:
                resultado.value = "El JSON no corresponde a la estructura esperada."
        except Exception as ex:
            resultado.value = f"Error: {ex}"
        page.update()

    btn_subir = ft.ElevatedButton("Subir datos", on_click=subir_datos)

    page.add(
        ft.Column([
            caja_json,
            btn_subir,
            resultado
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )

if __name__ == "__main__":
    ft.app(target=main)
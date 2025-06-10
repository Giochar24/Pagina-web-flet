# conexion_mongo.py
from pymongo import MongoClient

# Reemplaza con tu cadena de conexión real
uri = "mongodb+srv://Giochar:Maquiniitas2002@cluster0.4xn6wds.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)

db = client["farmacia_ujat"]
farmaco = db["farmaco"]
medicamento = db["medicamento"]

# Insertar varios medicamentos
farmacos = [
    {
        "nombre": "Acarbosa",
        "descripcion": "Cada TABLETA contiene: Acarbosa de 50 mg",
        "categoria": "Antidiabético",
        "interacciones": "Interactúa con antiácidos y sulfonilureas"
    },
    {
        "nombre": "Aceite de ricino",
        "descripcion": "Cada frasco con SOLUCIÓN contiene: Aceite de ricino 70 ml",
        "categoria": "Laxante",
        "interacciones": "Reduce absorción de otros medicamentos"
    },
    {
        "nombre": "Aciclovir",
        "descripcion": "Cada frasco ámpula con liofilizado contiene: Aciclovir 250 mg",
        "categoria": "Antiviral",
        "interacciones": "Aumenta efectos con probenecid"
    },
    {
        "nombre": "Ácido acetilsalicílico",
        "descripcion": "Tabletas de 500 mg",
        "categoria": "Analgésico, antiinflamatorio",
        "interacciones": "Potencia efecto de anticoagulantes"
    },
    {
        "nombre": "Ácido ascórbico",
        "descripcion": "Cada AMPOLLETA contiene Ácido ascórbico de 1g",
        "categoria": "Vitamina",
        "interacciones": "Interfiere con bishidroxicumarina"
    },
    {
        "nombre": "Albendazol",
        "descripcion": "Cada ml de SUSPENSIÓN contiene: Albendazol 20 mg/ml",
        "categoria": "Antiparasitario",
        "interacciones": "Aumenta concentración con dexametasona"
    },
    {
        "nombre": "Alprazolam",
        "descripcion": "Cada Tableta contiene: 0.25 y 2 mg",
        "categoria": "Ansiolítico",
        "interacciones": "Potencia depresores del SNC"
    },
    {
        "nombre": "Amikacina",
        "descripcion": "Cada frasco ámpula contiene: 100mg",
        "categoria": "Antibiótico",
        "interacciones": "Incompatible con beta-lactámicos"
    },
    {
        "nombre": "Amoxicilina",
        "descripcion": "Cada CÁPSULA contiene: 250 y 500 mg",
        "categoria": "Antibiótico",
        "interacciones": "Antagonizado por bacteriostáticos"
    },
    {
        "nombre": "Ampicilina",
        "descripcion": "Cada CÁPSULA contiene: 250 y 500 mg",
        "categoria": "Antibiótico",
        "interacciones": "Mayor riesgo de erupción con alopurinol"
    },
    {
        "nombre": "Azitromicina",
        "descripcion": "Cada TABLETA contiene: 500 mg",
        "categoria": "Antibiótico",
        "interacciones": "Reduce concentración con antiácidos"
    },
    {
        "nombre": "Beclometasona",
        "descripcion": "Cada 100 g de SOLUCIÓN presurizada contienen: 0.058 g",
        "categoria": "Corticosteroide",
        "interacciones": "Ninguna conocida"
    },
    {
        "nombre": "Bencilpenicilina",
        "descripcion": "Cada frasco ámpula con POLVO contiene: Bencilpenicilina sódica",
        "categoria": "Antibiótico",
        "interacciones": "Prolonga efecto con probenecid"
    },
    {
        "nombre": "Benzonatato",
        "descripcion": "Cada PERLA contiene: Benzonatato 100 mg",
        "categoria": "Antitusivo",
        "interacciones": "Potencia depresores del SNC"
    },
    {
        "nombre": "Carbamazepina",
        "descripcion": "Tabletas de 200 mg",
        "categoria": "Antiepiléptico",
        "interacciones": "Reduce niveles de fenitoína"
    },
    {
        "nombre": "Cefalexina",
        "descripcion": "Cápsulas de 500 mg",
        "categoria": "Antibiótico",
        "interacciones": "Diarrea, náusea, erupción cutánea"
    },
    {
        "nombre": "Ciprofloxacino",
        "descripcion": "Tabletas de 500 mg",
        "categoria": "Antibacteriano",
        "interacciones": "Evitar con antiácidos"
    },
    {
        "nombre": "Clindamicina",
        "descripcion": "Cápsulas de 300 mg",
        "categoria": "Antibiótico",
        "interacciones": "Riesgo de colitis"
    },
    {
        "nombre": "Dicloxacilina",
        "descripcion": "Cápsulas de 500 mg",
        "categoria": "Antibiótico",
        "interacciones": "No usar con tetraciclinas"
    },
    {
        "nombre": "Doxiciclina",
        "descripcion": "Cápsulas de 100 mg",
        "categoria": "Antibiótico",
        "interacciones": "Disminuye efecto de anticonceptivos"
    }
]
medicamentos = [
    {
        "clave": "S/C",
        "descripcion": "Ácido Acetilsalicílico 100 mg de liberación Prolongada",
        "presentacion": "Caja con 30 tabletas",
        "clasificacion": "Analgesia",
        "nivel_atencion": "1er Nivel",
        "nombre_farmaco": "Ácido acetilsalicílico"
    },
    {
        "clave": "010.000.5943.00",
        "descripcion": "Ibuprofeno 2g suspensión oral",
        "presentacion": "Envase con 120 ml",
        "clasificacion": "Analgesia",
        "nivel_atencion": "1er Nivel",
        "nombre_farmaco": "Ibuprofeno"
    },
    {
        "clave": "010.000.0104.00",
        "descripcion": "Paracetamol 500 mg Tableta",
        "presentacion": "Envase con 20 tabletas",
        "clasificacion": "Analgesia",
        "nivel_atencion": "1er Nivel",
        "nombre_farmaco": "Paracetamol"
    },
    {
        "clave": "010.000.2128.01",
        "descripcion": "Amoxicilina 500 mg Cápsula",
        "presentacion": "Caja con 15 cápsulas",
        "clasificacion": "Antibiótico",
        "nivel_atencion": "1er Nivel",
        "nombre_farmaco": "Amoxicilina"
    },
    {
        "clave": "010.000.1929.00",
        "descripcion": "Ampicilina 500 mg Tableta",
        "presentacion": "Envase con 20 tabletas",
        "clasificacion": "Antibiótico",
        "nivel_atencion": "1er Nivel",
        "nombre_farmaco": "Ampicilina"
    },
    {
        "clave": "010.000.1969.01",
        "descripcion": "Azitromicina 500 mg Tableta",
        "presentacion": "Caja con 3 tabletas",
        "clasificacion": "Antibiótico",
        "nivel_atencion": "1er Nivel",
        "nombre_farmaco": "Azitromicina"
    },
    {
        "clave": "010.000.1925.00",
        "descripcion": "Benzatina Bencilpenicilina 1 200 000 UI",
        "presentacion": "Frasco ámpula con diluyente",
        "clasificacion": "Antibiótico",
        "nivel_atencion": "1er Nivel",
        "nombre_farmaco": "Bencilpenicilina"
    },
    {
        "clave": "010.000.2462.00",
        "descripcion": "Ambroxol 30 mg Comprimido",
        "presentacion": "Caja con 20 comprimidos",
        "clasificacion": "Antitusivo",
        "nivel_atencion": "1er Nivel",
        "nombre_farmaco": "Ambroxol"
    },
    {
        "clave": "010.000.2433.00",
        "descripcion": "Benzonatato 100 mg Perla",
        "presentacion": "Envase con 20 perlas",
        "clasificacion": "Antitusivo",
        "nivel_atencion": "1er Nivel",
        "nombre_farmaco": "Benzonatato"
    },
    {
        "clave": "040.000.2608.00",
        "descripcion": "Carbamazepina 200 mg Tableta",
        "presentacion": "Envase con 20 tabletas",
        "clasificacion": "Antiepiléptico",
        "nivel_atencion": "1er Nivel",
        "nombre_farmaco": "Carbamazepina"
    },
    {
        "clave": "010.000.1939.00",
        "descripcion": "Cefalexina 500 mg Cápsula",
        "presentacion": "Envase con 20 cápsulas",
        "clasificacion": "Antibiótico",
        "nivel_atencion": "1er Nivel",
        "nombre_farmaco": "Cefalexina"
    },
    {
        "clave": "010.000.1344.00",
        "descripcion": "Albendazol 200 mg Tableta",
        "presentacion": "Caja con 6 tabletas",
        "clasificacion": "Antiparasitario",
        "nivel_atencion": "1er Nivel",
        "nombre_farmaco": "Albendazol"
    },
    {
        "clave": "010.000.1308.01",
        "descripcion": "Metronidazol 500 mg Tableta",
        "presentacion": "Envase con 30 tabletas",
        "clasificacion": "Antibiótico",
        "nivel_atencion": "1er Nivel",
        "nombre_farmaco": "Metronidazol"
    },
    {
        "clave": "010.000.1911.00",
        "descripcion": "Nitrofurantoína 100 mg Cápsula",
        "presentacion": "Envase con 40 cápsulas",
        "clasificacion": "Antibiótico",
        "nivel_atencion": "1er Nivel",
        "nombre_farmaco": "Nitrofurantoína"
    },
    {
        "clave": "010.000.1904.00",
        "descripcion": "Trimetoprima-Sulfametoxazol 40mg/200mg Suspensión",
        "presentacion": "Envase con 120 ml",
        "clasificacion": "Antibiótico",
        "nivel_atencion": "1er Nivel",
        "nombre_farmaco": "Trimetoprima/sulfametoxazol"
    },
    {
        "clave": "010.000.0574.00",
        "descripcion": "Captopril 25 mg Tableta",
        "presentacion": "Envase con 30 tabletas",
        "clasificacion": "Cardiología",
        "nivel_atencion": "1er Nivel",
        "nombre_farmaco": "Captopril"
    },
    {
        "clave": "010.000.0561.00",
        "descripcion": "Clortalidona 50 mg Tableta",
        "presentacion": "Envase con 20 tabletas",
        "clasificacion": "Diurético",
        "nivel_atencion": "1er Nivel",
        "nombre_farmaco": "Clortalidona"
    },
    {
        "clave": "010.000.2501.00",
        "descripcion": "Enalapril 10 mg Tableta",
        "presentacion": "Envase con 30 tabletas",
        "clasificacion": "Cardiología",
        "nivel_atencion": "1er Nivel",
        "nombre_farmaco": "Enalapril"
    },
    {
        "clave": "010.000.0592.00",
        "descripcion": "Isosorbida 5 mg Tableta sublingual",
        "presentacion": "Envase con 20 tabletas",
        "clasificacion": "Cardiología",
        "nivel_atencion": "1er Nivel",
        "nombre_farmaco": "Isosorbida"
    },
    {
        "clave": "010.000.1042.00",
        "descripcion": "Glibenclamida 5 mg Tableta",
        "presentacion": "Envase con 50 tabletas",
        "clasificacion": "Antidiabético",
        "nivel_atencion": "1er Nivel",
        "nombre_farmaco": "Glibenclamida"
    }
]

medicamento.insert_many(medicamentos)
print("Medicamentos insertados correctamente.")

# Consultar y mostrar un medicamento de la colección
primer_medicamento = medicamento.find_one()
print("Primer medicamento en la colección:")
print(primer_medicamento)

# Insertar varios farmacos
farmaco.insert_many(farmacos)
print("Fármacos insertados correctamente.")

# Consultar y mostrar un farmaco de la colección
primer_farmaco = farmaco.find_one()
print("Primer fármaco en la colección:")
print(primer_farmaco)
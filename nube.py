from pyairtable.orm import Model
from pyairtable.orm import fields as F

class Receta(Model):
    medicamento = F.TextField("medicamento")
    interacciones = F.TextField("interacciones")
    class Meta:
        api_key = "patHYKNiG4xgUj6qT.538291219ebcf4a3b91c944f0aaa0bbfa1289c67e17a496c6672bea5829b287e"
        base_id = "appGRxK5Z9lbDWzig"
        table_name = "receta"

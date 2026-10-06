import random
import uuid
from datetime import timedelta
import pandas as pd
from faker import Faker

ESTADOS = ["Abierto", "en_curso", "EN CURSO", "Cerrado", " Cerrado "]

IDS_EMPRESA = [
    "e1000000-0000-0000-0000-000000000001",
    "e1000000-0000-0000-0000-000000000002",
    "e1000000-0000-0000-0000-000000000003",
]

IDS_CATEGORIA = [
    "c2000000-0000-0000-0000-000000000001",
    "c2000000-0000-0000-0000-000000000002",
    "c2000000-0000-0000-0000-000000000003",
]

IDS_PRIORIDAD = [
    "p3000000-0000-0000-0000-000000000001",
    "p3000000-0000-0000-0000-000000000002",
]


def generar_retos(n=500):
    Faker.seed(42)
    random.seed(42)

    fake = Faker("es_CO")
    filas = []

    for _ in range(n):
        ret_id = str(uuid.uuid4())
        nombre = fake.sentence(nb_words=6).rstrip(".")
        descripcion = fake.sentence(nb_words=12)
        fecha_inicio_dt = fake.date_between(start_date="-1y", end_date="+3m")
        fecha_fin_dt = fecha_inicio_dt + timedelta(
            days=random.randint(15, 180)
        )

        estado = random.choice(ESTADOS)
        id_empresa = random.choice(IDS_EMPRESA)
        id_categoria = random.choice(IDS_CATEGORIA)
        id_prioridad = random.choice(IDS_PRIORIDAD)

        if random.random() < 0.10:
            nombre = f"  {nombre}   "

        if random.random() < 0.12:
            descripcion = None

        if random.random() < 0.50:
            fecha_inicio_str = fecha_inicio_dt.strftime("%Y-%m-%d")
        else:
            fecha_inicio_str = fecha_inicio_dt.strftime("%d/%m/%Y")

        prob_fin = random.random()
        if prob_fin < 0.08:
            fecha_fin_str = None
        elif prob_fin < 0.13: 
            fecha_fin_err = fecha_inicio_dt - timedelta(
                days=random.randint(1, 30)
            )
            fecha_fin_str = fecha_fin_err.strftime("%Y-%m-%d")
        else:
            fecha_fin_str = fecha_fin_dt.strftime("%Y-%m-%d")

        if random.random() < 0.20:
            estado = random.choice(["en_curso", "EN CURSO", " Cerrado "])

        filas.append(
            {
                "id": ret_id,
                "nombre": nombre,
                "descripcion": descripcion,
                "fecha_inicio": fecha_inicio_str,
                "fecha_fin": fecha_fin_str,
                "estado": estado,
                "id_empresa": id_empresa,
                "id_categoria": id_categoria,
                "id_prioridad": id_prioridad,
            }
        )

    df = pd.DataFrame(filas)

    num_duplicados = int(n * 0.05)
    if num_duplicados > 0:
        duplicados = df.sample(n=num_duplicados, random_state=42)
        df = pd.concat([df, duplicados], ignore_index=True)

    return df


if __name__ == "__main__":
    df = generar_retos(500)
    print("--- SHAPE ---")
    print(df.shape)
    print("\n--- HEAD ---")
    print(df.head())
    print("\n--- NULOS POR COLUMNA ---")
    print(df.isna().sum())
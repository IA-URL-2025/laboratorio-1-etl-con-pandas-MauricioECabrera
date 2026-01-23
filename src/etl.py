import pandas as pd


def run_etl():

    input_path = "data/citas_clinica.csv"
    output_path = "data/output.csv"

    df = pd.read_csv(input_path)

    df["paciente"] = df["paciente"].astype(str).str.title()
    df["especialidad"] = df["especialidad"].astype(str).str.upper()

    df["fecha_cita"] = pd.to_datetime(df["fecha_cita"], errors="coerce")
    df = df[df["fecha_cita"].notna()]

    df = df[df["estado"] == "CONFIRMADA"]
    df = df[df["costo"] > 0]

    df["telefono"] = df["telefono"].fillna("NO REGISTRA")

    df.to_csv(output_path, index=False)


def main():
    run_etl()


if __name__ == "__main__":
    main()

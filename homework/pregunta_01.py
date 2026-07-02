# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt


def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """
    os.makedirs("docs", exist_ok=True)

    df = pd.read_csv("files/input/shipping-data.csv")

    fig, ax = plt.subplots()
    df["Warehouse_block"].value_counts().sort_index().plot(kind="bar", ax=ax)
    ax.set_title("Shipping per Warehouse")
    ax.set_xlabel("Warehouse Block")
    ax.set_ylabel("Count")
    fig.tight_layout()
    fig.savefig("docs/shipping_per_warehouse.png")
    plt.close(fig)

    fig, ax = plt.subplots()
    df["Mode_of_Shipment"].value_counts().plot(kind="bar", ax=ax)
    ax.set_title("Mode of Shipment")
    ax.set_xlabel("Mode")
    ax.set_ylabel("Count")
    fig.tight_layout()
    fig.savefig("docs/mode_of_shipment.png")
    plt.close(fig)

    fig, ax = plt.subplots()
    df["Customer_rating"].value_counts().sort_index().plot(kind="bar", ax=ax)
    ax.set_title("Average Customer Rating")
    ax.set_xlabel("Rating")
    ax.set_ylabel("Count")
    fig.tight_layout()
    fig.savefig("docs/average_customer_rating.png")
    plt.close(fig)

    fig, ax = plt.subplots()
    df["Weight_in_gms"].plot(kind="hist", bins=30, ax=ax)
    ax.set_title("Weight Distribution")
    ax.set_xlabel("Weight (gms)")
    ax.set_ylabel("Frequency")
    fig.tight_layout()
    fig.savefig("docs/weight_distribution.png")
    plt.close(fig)

    html = """
<!DOCTYPE html>
<html>
<head>
    <title>Shipping Dashboard</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f4f4f4;
        }
        h1 {
            text-align: center;
            color: #333;
        }
        .grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            max-width: 1200px;
            margin: 0 auto;
        }
        .card {
            background: white;
            border-radius: 8px;
            padding: 15px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        .card img {
            width: 100%;
            height: auto;
            display: block;
        }
    </style>
</head>
<body>
    <h1>Shipping Dashboard</h1>
    <div class="grid">
        <div class="card">
            <img src="shipping_per_warehouse.png" alt="Shipping per Warehouse">
        </div>
        <div class="card">
            <img src="mode_of_shipment.png" alt="Mode of Shipment">
        </div>
        <div class="card">
            <img src="average_customer_rating.png" alt="Average Customer Rating">
        </div>
        <div class="card">
            <img src="weight_distribution.png" alt="Weight Distribution">
        </div>
    </div>
</body>
</html>
"""
    with open("docs/index.html", "w", encoding="utf-8") as f:
        f.write(html)

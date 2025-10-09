# !pip install ipywidgets fileupload seaborn openpyxl --quiet
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import io
from ipywidgets import FileUpload, Button, VBox, Output
from IPython.display import display

# Widget d'upload
uploader = FileUpload(accept='.xlsx', multiple=False)
output = Output()

# Fonction pour lire et analyser le fichier uploadé
def analyse_fichier(change):
    output.clear_output()
    if not uploader.value:
        with output:
            print("Veuillez uploader un fichier .xlsx d'abord.")
        return
    infos = list(uploader.value.values())[0]
    df = pd.read_excel(io.BytesIO(infos['content']))
    # Création du dossier visuals/
    os.makedirs("visuals", exist_ok=True)
    with output:
        print("Dimensions du dataset :", df.shape)
        print("\nTypes des colonnes :\n", df.dtypes)
        print("\nValeurs manquantes par colonne :\n", df.isna().sum())
        print("\nStatistiques descriptives :\n", df.describe(include='all'))

        # Histogrammes et boxplots
        numerical_cols = df.select_dtypes(include='number').columns
        for col in numerical_cols:
            fig, axes = plt.subplots(1,2, figsize=(12,4))
            sns.histplot(df[col].dropna(), kde=True, ax=axes[0])
            axes[0].set_title(f'Histogramme - {col}')
            sns.boxplot(x=df[col], ax=axes[1])
            axes[1].set_title(f'Boxplot - {col}')
            plt.tight_layout()
            plt.savefig(f"visuals/{col}_dist.png")
            plt.close()

        # Matrice de corrélation + heatmap
        plt.figure(figsize=(14,10))
        corr = df[numerical_cols].corr()
        sns.heatmap(corr, annot=False, cmap="coolwarm", center=0)
        plt.title("Heatmap de corrélation")
        plt.savefig("visuals/correlation_heatmap.png")
        plt.close()

        # Corrélations avec risk ou incidence
        target_col = "risk" if "risk" in df.columns else ("incidence" if "incidence" in df.columns else None)
        if target_col:
            target_corr = corr[target_col].drop(target_col).abs().sort_values(ascending=False)
            top3 = target_corr.head(3).index.tolist()
            print(f"Top 3 variables les plus corrélées à {target_col} : {top3}")
            for var in top3:
                plt.figure()
                sns.scatterplot(x=df[var], y=df[target_col])
                plt.title(f"Scatterplot : {var} vs {target_col}")
                plt.savefig(f"visuals/scatter_{var}_vs_{target_col}.png")
                plt.close()
            pd.Series(top3, name="Top_correlated_with_"+target_col).to_csv(f"visuals/top3_corr_{target_col}.csv", index=False)
        print("\nAnalyse EDA complète : tout est sauvegardé dans le dossier visuals/")

# Bouton d'exécution
button = Button(description="Charger et analyser le fichier")
button.on_click(analyse_fichier)

display(VBox([uploader, button, output]))

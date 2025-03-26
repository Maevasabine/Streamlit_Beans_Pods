import streamlit as st
from pandas import read_csv
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt 

#chargement des donnees
try:
    fichier='data/BeansDataSet.csv'
    data=read_csv(fichier)
    st.title("Bienvenu sur ce site d'Analyse des ventes Beans & Pods")
    print(data)
except:
    print('erreur de lecture')

st.sidebar.title('BEANS & PODS')
menu=st.sidebar.selectbox('Navigation',['Accueil','Visualisation','Analyse et Recommendations'])

if menu=="Accueil":
    st.write('nombre de lignes et colonnes du data')
    st.write(data.shape)
    st.write('statistique descriptive')
    st.write(data.describe())
    #verification des valeurs manquantes
    st.write('valeurs manquantes')
    st.write(data.isnull().sum())

elif menu=="Visualisation":
    #filtres selectifs
    canal=st.selectbox('Selectionnez le canal de vente',['Tous']+list(data['Channel'].unique()))
    region=st.multiselect('Selectionnez la region',data['Region'].unique(),default=data['Region'].unique())

    if canal != "Tous":
        data = data[data['Channel'] == canal]

    if region:
        data = data[data['Region'].isin(region)]



    #repartition des ventes par regions
    st.write('repartition des ventes par region')
    fig,ax=plt.subplots()
    sns.countplot(x='Region',data=data,ax=ax)
    plt.title('Nombre de ventes par region')
    st.pyplot(fig)

    # Histogramme
    st.write("Histogramme")
    # layout = nombre de ligne et colonne donc 3 lignes et 3 colonnes
    plt.figure(figsize=(20, 15))
    data.hist(bins=15,figsize=(20,15),layout=(3,3))
    plt.suptitle('Histogramme')
    st.pyplot(plt)


    #graphique circualire et pourcentage de vente par region
    st.write("pourcentage de vente par region")
    fig, ax = plt.subplots()
    data['Region'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90, ax=ax)
    plt.title('Repartition des ventes par région')
    plt.ylabel('')  # Cacher le label de l'axe Y
    st.pyplot(fig)

    #Vente par type de produit
    st.write('vente par type de produit')
    fig,ax=plt.subplots()
    data[['Robusta','Arabica','Espresso','Lungo','Latte','Cappuccino']].sum().plot(kind='bar', ax=ax)
    plt.title('ventes totales par type de produit')
    st.pyplot(fig)

    #correlation entre les ventes
    st.write('corelation entre les ventes')
    fig,ax=plt.subplots(figsize=(8,6))
    sns.heatmap(data[['Robusta','Arabica','Espresso','Lungo','Latte','Cappuccino']].corr(),cmap='coolwarm', annot=True, fmt='.2f',ax=ax)
    plt.title('Matrice de correlation')
    st.pyplot(fig)

    #correlation entre le canal de vente et le produit
    st.write('vente par type de produit et le canal de vente')

    #ventes par canal et type de produit
    canal=data.groupby('Channel')[['Robusta','Arabica','Espresso','Lungo','Latte','Cappuccino']].sum()
    fig,ax=plt.subplots(figsize=(8,5))
    canal.plot(kind='bar',ax=ax)
    plt.title('vente par type de produit et le canal de vente')
    plt.xticks(rotation=45)
    st.pyplot(fig)

    #vente par region et types de produit
    st.write('vente par region et type de produit')
    region=data.groupby('Region')[['Robusta','Arabica','Espresso','Lungo','Latte','Cappuccino']].sum()
    fig,ax=plt.subplots(figsize=(8,5))
    region.plot(kind='bar',ax=ax)
    plt.title('vente par region et type de produit')
    plt.xticks(rotation=45)
    st.pyplot(fig)


else:
    st.write("Recommandations")
    st.markdown("""
    ### Canal de vente
    - Augmenter la disponibilité des gousses Robusta,Lungo et Cappuccino en magasin.  
    - Proposer des promotions spécifiques en ligne pour l'Arabica,l'Espresso et le Latte.  
    - Créer un programme de fidélité différencié pour le magasin et le site en ligne.  

    ### Région
    Après une étude sur le nombre de ventes par région,  
    on constate que les produits sont plus vendus dans le Sud que dans le Nord et le Centre.  

    Pour augmenter les revenus, il serait préférable de maximiser les distributions dans le Sud  
    par rapport aux autres régions.  
    - Adapter le stock régional en fonction de la demande locale.  
    - Lancer des campagnes publicitaires régionales ciblées.  
    - Créer des offres spéciales basées sur les habitudes de consommation régionales.  

    ### Type de produit
    Après une répartition des ventes par type de produit,  
    on relève que le Robusta est le produit le plus vendu, suivi de l'Espresso,  
    et que le Cappuccino est le produit le moins vendu de tous.  

    Il serait judicieux de maximiser la distribution du Robusta et de l'Espresso  
    et de lancer des promotions pour attirer de nouveaux clients.  

    ### Vente par région et type de produit
    **Centre :**  
    - On constate que le Robusta y est le plus vendu, suivi de l'Espresso.  
    - Le Cappuccino et le Lungo sont les produits les moins vendus.  

    **Nord :**  
    - On constate que le Robusta y est le plus vendu, suivi de l'Espresso.  
    - Le Cappuccino et le Lungo sont également les produits les moins vendus.  

    **Sud :**  
    - Comme mentionné plus haut, le Sud est la région où tous les produits se vendent le mieux.  
    - Le taux de vente est très élevé dans cette région, quel que soit le produit,  
    comparé aux deux autres régions.  

    **Recommandation :**  
    Une stratégie pourrait consister à retirer les produits qui ne se vendent presque pas  
    dans le Nord et le Centre, afin d'augmenter la quantité des produits à forte demande.  
    Miser sur les ventes plutôt que sur les pertes.  

    ### Vente par type de produit et canal de vente
    On constate que certains produits se vendent mieux en magasin qu'en ligne.  

    **Online :**  
    - Les produits comme l'Espresso, l'Arabica et le Latte sont plus vendus en ligne qu'en magasin.  

    **Store :**  
    - Les produits comme le Robusta, le Lungo et le Cappuccino sont plus vendus en magasin.  
    Il faudrait s'assurer qu'il y ait toujours du stock disponible pour éviter les pénuries  
    et la frustration des employés en magasin.  


    ### Données supplémentaires qu'on pourrait collecter pour une analyse plus approfondie :  
    - La moyenne d'âge des clients qui consomment le plus dans les différentes régions.  
    - La fréquence d'achat et le prix moyen par transaction.  
    - Les données saisonnières (ventes mensuelles).  
    - Le retour client pour ajuster l'offre.  
    """)





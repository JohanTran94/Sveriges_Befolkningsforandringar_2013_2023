# **ETL_och_Visualisering_av_Sveriges_Befolkningsforandringar_2013_2023**

## **Projektbeskrivning**

Detta är ett grupparbete inom kursen Data Science, där vi arbetar med ett dataset från [Dataportal.se](https://www.dataportal.se/datasets/43_55874). Projektet fokuserar på att extrahera, transformera och ladda (ETL) data samt visualisera befolkningsförändringar i Sverige över tid. Dessutom implementerar vi en enkel maskininlärningsmodell för att förutsäga framtida befolkningstillväxt.

## **Dataset**

- **Källa:** [Dataportal.se](https://www.dataportal.se/datasets/43_55874)
- **Filformat:** CSV

## **Använda bibliotek**

Projektet använder följande Python-bibliotek:

- **pandas** – Hantering och transformation av dataset
- **matplotlib** – Visualisering av data
- **numpy** – Numeriska beräkningar
- **sklearn.linear_model.LinearRegression** – Enkel linjär regression för prediktioner

## **ETL-process**

### **Extraktion**

- Ladda in CSV-filen med befolkningsdata.

### **Transformation**

- Sortera data efter år.
- Beräkna procentuell förändring av befolkningen.
- Beräkna födelsetal, dödstal och naturlig befolkningstillväxt.

### **Laddning**

- Förbereda data för analys och visualisering.

## **Visualiseringar**

- **Procentuell förändring av folkmängden per år** – Area chart.
- **Relation mellan födda och döda** – Stapeldiagram.
- **Födelsetal, dödstal och naturlig befolkningstillväxt** – Gruppade staplar.
- **Prediktion av befolkningstillväxt med linjär regression** – Linjediagram med framtida förutsägelser.
- **Invandring och utvandring per år** – Linjediagram.

## **Machine Learning**

Vi använder en **linjär regressionsmodell** för att förutsäga befolkningstillväxt baserat på historiska data. Modellen tränas på befintliga data och genererar prognoser för de kommande 10 åren.

## Kontakt
Om du har frågor eller förslag, vänligen kontakta oss via Linkedin. (www.linkedin.com/in/johan-data)


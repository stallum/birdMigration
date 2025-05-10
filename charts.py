import plotly.express as px
import pandas as pd

def createFigures(df):

    fig1 = px.histogram(df, x = 'Flight_Distance_km', nbins = 30,
                        title = 'Distribuição da Distância de Voo km',
                        color_discrete_sequence = ['skyblue'])
        
    speciesCount = df['Species'].value_counts().reset_index()
    speciesCount.columns = ['Species', 'Count']

    fig2 = px.bar(speciesCount, x = 'Species', y = 'Count', color = 'Species',
                  title = 'Contagem de Aves por Espécie')
    
    sucess = (
        df.groupby('Species')['Migration_Success'].value_counts(normalize = True).unstack().fillna(0) * 100
    ).reset_index()
    fig3 = px.bar(sucess, x='Species', y=['Successful', 'Failed'],
                  title = 'Taxa de Sucesso (%)', barmode = 'stack')
    
    interruptionReasons = df['Interrupted_Reason'].value_counts().reset_index()
    interruptionReasons.columns = ['Reasons', 'Count']
    fig4 = px.pie(interruptionReasons, names = 'Reasons', values = 'Count', 
                  title = 'Causas de Interrupção')
    
    tagWeight_by_success = df.groupby("Migration_Success")["Tag_Weight_g"].mean().reset_index()
    fig5 = px.bar(tagWeight_by_success, x = 'Migration_Success', y = 'Tag_Weight_g',
                  title = 'Peso Médio do Rastreador', color = 'Migration_Success')
    
    return fig1, fig2, fig3, fig4, fig5
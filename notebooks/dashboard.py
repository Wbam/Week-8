from flask import Flask, jsonify, send_from_directory
import pandas as pd
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Initialize Flask application
server = Flask(__name__)

# Load data
fraud_data = pd.read_csv('C:/Users/bam/Documents/Data/Fraud_Data.csv')

# Flask endpoint for summary statistics
@server.route('/api/stats')
def stats():
    total_transactions = len(fraud_data)
    total_frauds = fraud_data['class'].sum()
    fraud_percentage = (total_frauds / total_transactions) * 100

    return jsonify({
        'total_transactions': total_transactions,
        'total_frauds': total_frauds,
        'fraud_percentage': fraud_percentage
    })

# Create Dash app
app = Dash(__name__, server=server, url_base_pathname='/dashboard/')

# Layout of the dashboard
app.layout = html.Div([
    html.H1("Fraud Detection Dashboard"),
    dcc.Interval(id='interval-component', interval=1*1000, n_intervals=0),
    html.Div(id='summary-boxes'),
    dcc.Graph(id='fraud-trend'),
    dcc.Graph(id='device-browser-chart'),
    dcc.Graph(id='geo-fraud-chart')
])


@app.callback(
    Output('summary-boxes', 'children'),
    Input('interval-component', 'n_intervals')
)
def update_summary_boxes(n):
    response = requests.get('http://localhost:5000/api/stats')
    data = response.json()

    return [
        html.Div(f"Total Transactions: {data['total_transactions']}"),
        html.Div(f"Total Fraud Cases: {data['total_frauds']}"),
        html.Div(f"Fraud Percentage: {data['fraud_percentage']:.2f}%")
    ]


@app.callback(
    Output('fraud-trend', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_fraud_trend(n):
    fraud_over_time = fraud_data.groupby('purchase_time').sum().reset_index()
    fig = px.line(fraud_over_time, x='purchase_time', y='class', title='Fraud Cases Over Time')
    return fig


@app.callback(
    Output('device-browser-chart', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_device_browser_chart(n):
    device_browser_data = fraud_data.groupby(['device_id', 'browser']).sum().reset_index()
    fig = px.bar(device_browser_data, x='device_id', y='class', color='browser', title='Fraud Cases by Device and Browser')
    return fig

# Update geographic fraud chart
@app.callback(
    Output('geo-fraud-chart', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_geo_fraud_chart(n):
    geo_fraud_data = fraud_data.groupby('country').sum().reset_index()
    fig = px.bar(geo_fraud_data, x='country', y='class', title='Fraud Cases by Country')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)

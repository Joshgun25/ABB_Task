import plotly.graph_objs as go
from plotly.subplots import make_subplots
import pandas as pd
from sqlalchemy import create_engine
from wordcloud import WordCloud

# Connect to PostgreSQL database
connection_string = 'postgresql://postgres:yeGAMAjBuJIbApwgbYziYqRXcGrEuKsx@monorail.proxy.rlwy.net:40117/railway'
engine = create_engine(connection_string)

# Function to generate frequently asked questions plot using Plotly
def generate_frequently_asked_questions():
    # Query data from the database
    query = 'SELECT text FROM webapp_question'
    questions_df = pd.read_sql(query, engine)

    # Calculate frequency of each question
    question_freq = questions_df['text'].value_counts()

    # Prepare data for Plotly chart
    top_10_questions = question_freq.head(10)
    data = [go.Bar(x=top_10_questions.index, y=top_10_questions.values)]

    # Define layout for the chart
    layout = go.Layout(
        title='Top 10 Most Frequently Asked Questions',
        xaxis=dict(title='Question'),
        yaxis=dict(title='Frequency')
    )

    # Create the Plotly chart figure
    fig = go.Figure(data=data, layout=layout)

    # Convert the Plotly figure to JSON format
    chart_json = fig.to_json()

    return chart_json

# Function to generate length of the questions and answers plot using Plotly
def generate_length_of_questions_answers():
    qa_df = pd.read_sql('SELECT q.text AS question_text, a.text AS answer_text '
                        'FROM webapp_question q INNER JOIN webapp_answer a ON q.id = a.question_id', engine)

    # Calculate lengths of questions and answers
    qa_df['question_length'] = qa_df['question_text'].apply(len)
    qa_df['answer_length'] = qa_df['answer_text'].apply(len)

    # Create histograms using Plotly
    fig = make_subplots(rows=1, cols=2, subplot_titles=('Distribution of Question Length', 'Distribution of Answer Length'))

    # Add histograms for question and answer lengths
    fig.add_trace(go.Histogram(x=qa_df['question_length'], marker_color='lightblue', name='Question Length'), row=1, col=1)
    fig.add_trace(go.Histogram(x=qa_df['answer_length'], marker_color='lightgreen', name='Answer Length'), row=1, col=2)

    # Update layout
    fig.update_layout(title_text='Question and Answer Length Distributions', showlegend=True)

    # Convert Plotly figure to JSON format
    chart_json = fig.to_json()

    return chart_json

# Function to generate time series plot using Plotly
def generate_time_series():
    # Query timestamp data from database
    timestamp_df = pd.read_sql('SELECT timestamp FROM webapp_question', engine)

    # Convert timestamp to datetime format
    timestamp_df['timestamp'] = pd.to_datetime(timestamp_df['timestamp'])

    # Extract date and count occurrences
    date_count = timestamp_df['timestamp'].dt.date.value_counts().sort_index()

    # Create time series plot using Plotly
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=date_count.index, y=date_count.values, mode='lines+markers', marker_color='orange'))

    # Update layout
    fig.update_layout(title='Number of Questions Over Time', xaxis_title='Date', yaxis_title='Number of Questions')

    # Convert Plotly figure to JSON format
    chart_json = fig.to_json()

    return chart_json

# Function to generate word cloud plot using Plotly
def generate_word_cloud():
    
    qa_df = pd.read_sql('SELECT q.text AS question_text, a.text AS answer_text '
                        'FROM webapp_question q INNER JOIN webapp_answer a ON q.id = a.question_id', engine)

    # Create word cloud of question text
    question_text = ' '.join(qa_df['question_text'])

    # Font Path
    font_path='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
    wordcloud = WordCloud(width=800, height=400, background_color='white',
                              font_path=font_path, collocations=False,
                              stopwords=None, normalize_plurals=False).generate(question_text)

    # Convert word cloud to Plotly figure
    fig = go.Figure(go.Image(z=wordcloud.to_array(), hoverinfo='skip'))

    # Convert Plotly figure to JSON format
    chart_json = fig.to_json()

    return chart_json
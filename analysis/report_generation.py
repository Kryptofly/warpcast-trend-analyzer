import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from jinja2 import Environment, FileSystemLoader
import pdfkit

def generate_report(trend_results, username):
    report_path = f'reports/{username}_trend_report.pdf'
    
    # Create visualizations
    plt.figure(figsize=(10, 6))
    sns.barplot(data=trend_results.head(10), x='count', y='keyword')
    plt.title('Top 10 Trending Keywords')
    plt.xlabel('Count')
    plt.ylabel('Keyword')
    plt.savefig(f'static/{username}_top_keywords.png')
    plt.close()

    # Load template
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('report.html')

    # Render template
    html_out = template.render(username=username, img_path=f'static/{username}_top_keywords.png')
    
    # Generate PDF
    pdfkit.from_string(html_out, report_path)
    
    return report_path

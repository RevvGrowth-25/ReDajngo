from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    context = {
        "automations": [
            ("CRM Auto-Updates", "Leads from ads → CRM in real-time."),
            ("Slack Bots", "Daily reports, alerts, Q&A inside Slack."),
            ("Google Sheets → BI", "Live dashboards without manual copy-paste."),
            ("Lead Scoring AI", "ChatGPT scores every lead in seconds."),
        ]
    }
    return render(request, 'index.html', context)
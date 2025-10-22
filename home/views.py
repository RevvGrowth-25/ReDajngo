from django.shortcuts import render
from datetime import datetime


def ceo_dashboard(request):
    """
    Enhanced CEO Dashboard with more realistic automation data
    """

    data = {
        "kpi": {
            "all": {
                "automations": 50,
                "handover": 47,
                "hrsSaved": 1840,
                "production": 25
            },
            "Ayush": {
                "automations": 45,
                "handover": 45,
                "hrsSaved": 920,
                "production": 20
            },
            "Divya": {
                "automations": 30,
                "handover": 27,
                "hrsSaved": 80,
                "production": 3
            },
        },
        "bar": {
            "all": {
                "labels": ["Karthick", "Sales and Data", "HR", "SEO and PPC", "Content Team", "Design and Social Media", "AI"],
                "data": [5, 7, 3, 8, 3, 4, 4]
            },
            "Ayush": {
                "labels": ["Karthick", "Sales and Data", "HR", "SEO and PPC", "Content Team", "Design and Social Media", "AI"],
                "data": [5, 6, 3,18,3,4,4]
            },
            "Divya": {
                "labels": ["Karthick", "Sales and Data", "HR", "SEO and PPC", "Content Team", "Design and Social Media", "AI"],
                "data": [2, 7, 0, 12, 2, 4, 3]
            },
        },
        "pie": {
            "all": {
                "labels": ["Ayush", "Divya"],
                "data": [45,30]
            },
            "Ayush": {
                "labels": ["Ayush"],
                "data": [45]
            },
            "Divya": {
                "labels": ["Divya"],
                "data": [30]
            },
        },
        "line": {
    "all": {
        "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        "data":  [0, 2, 3, 4, 7, 8, 9, 4, 6, 13]   # total = 45
    },
    "Ayush": {
        "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        "data":  [0, 2, 3, 4, 5, 6, 5, 3, 7, 8]   # total = 43
    },
            "Divya": {
                "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                "data": [0, 0, 0, 0, 0, 0, 8, 9, 3, 10]
            },
        },
        "rows": [
    {
        "process": "Blog Summarizer",
        "owner": "Ayush and Divya",
        "Department": "Content",
        "hrsSaved": 6,
        "accuracy": 96,
        "status": "Live"
    },
    {
        "process": "Reddit AI Agent",
        "owner": "Ayush and Divya",
        "Department": "Content",
        "hrsSaved": 2,
        "accuracy": 94,
        "status": "Testing"
    },
    {
        "process": "Click Up Task Automation",
        "owner": "Ayush and Divya",
        "Department": "Design",
        "hrsSaved": 0.5,
        "accuracy": 95,
        "status": "Live"
    },
    {
        "process": "Hiring Automation",
        "owner": "Ayush",
        "Department": "HR",
        "hrsSaved": 4,
        "accuracy": 92,
        "status": "Live"
    },
    {
        "process": "Instant CV Reader",
        "owner": "Ayush",
        "Department": "HR",
        "hrsSaved": 6,
        "accuracy": 92,
        "status": "Live"
    },
    {
        "process": "TO-Do Automation",
        "owner": "Ayush",
        "Department": "HR",
        "hrsSaved": 4,
        "accuracy": 91,
        "status": "Live"
    },
    {
        "process": "Clickup Automation",
        "owner": "Ayush",
        "Department": "Karthick",
        "hrsSaved": 4,
        "accuracy": 97,
        "status": "Live"
    },
    {
        "process": "Landing Page Automation",
        "owner": "Ayush and Divya",
        "Department": "Karthick",
        "hrsSaved": 8,
        "accuracy": 98,
        "status": "Testing"
    },
    {
        "process": "Proposal Automation",
        "owner": "Ayush and Divya",
        "Department": "Karthick",
        "hrsSaved": 8,
        "accuracy": 89,
        "status": "Live"
    },
    {
        "process": "Prospect Email Automation",
        "owner": "Ayush",
        "Department": "Karthick",
        "hrsSaved": 4,
        "accuracy": 90,
        "status": "Live"
    },
    {
        "process": "Proposal Follow Up Notif",
        "owner": "Ayush and Divya",
        "Department": "Sales",
        "hrsSaved": 0.5,
        "accuracy": 94,
        "status": "Live"
    },
    {
        "process": "Weekly Report Automation",
        "owner": "Ayush and Divya",
        "Department": "Sales",
        "hrsSaved": 0.5,
        "accuracy": 94,
        "status": "Live"
    },
    {
        "process": "RFI Automation",
        "owner": "Ayush and Divya",
        "Department": "Sales",
        "hrsSaved": 4,
        "accuracy": 94,
        "status": "Live"
    },
    {
        "process": "Series A Automation",
        "owner": "Ayush",
        "Department": "Data",
        "hrsSaved": 4,
        "accuracy": 94,
        "status": "Live"
    },
    {
        "process": "Trello X Google Sheets",
        "owner": "Ayush",
        "Department": "Data",
        "hrsSaved": 4,
        "accuracy": 94,
        "status": "Live"
    },
    {
        "process": "Website Leads",
        "owner": "Ayush",
        "Department": "Sales",
        "hrsSaved": 4,
        "accuracy": 94,
        "status": "Live"
    },
    {
        "process": "AI Outreach Engine V1",
        "owner": "Ayush",
        "Department": "SEO",
        "hrsSaved": 4,
        "accuracy": 94,
        "status": "Live"
    },
    {
        "process": "Competitor kwd Analysis",
        "owner": "Ayush and Divya",
        "Department": "SEO",
        "hrsSaved": 5,
        "accuracy": 94,
        "status": "Live"
    },
    {
        "process": "Google ads customgpt",
        "owner": "Ayush and Divya",
        "Department": "PPC",
        "hrsSaved": 6,
        "accuracy": 94,
        "status": "Live"
    },
    {
        "process": "Content Audit Automation",
        "owner": "Ayush and Divya",
        "Department": "SEO",
        "hrsSaved": 5,
        "accuracy": 94,
        "status": "Live"
    },
    {
        "process": "Lead Qualifications",
        "owner": "Ayush",
        "Department": "SEO",
        "hrsSaved": 6,
        "accuracy": 94,
        "status": "Live"
    },
    {
        "process": "Scrape Communities Automation",
        "owner": "Ayush",
        "Department": "SEO",
        "hrsSaved": 2,
        "accuracy": 94,
        "status": "Live"
    },
    {
        "process": "Revv AI Blog Gen",
        "owner": "Ayush and Divya",
        "Department": "SEO",
        "hrsSaved": 6,
        "accuracy": 94,
        "status": "Live"
    },
    {
        "process": "Keyword Brief",
        "owner": "Ayush and Divya",
        "Department": "SEO",
        "hrsSaved": 4,
        "accuracy": 94,
        "status": "Testing"
    },
    {
        "process": "Click Bait Automation",
        "owner": "Ayush and Divya",
        "Department": "Social Media",
        "hrsSaved": 4,
        "accuracy": 94,
        "status": "Live"
    },
    {
        "process": "Linkedin Outreach Automation",
        "owner": "Ayush",
        "Department": "Social Media",
        "hrsSaved": 3,
        "accuracy": 94,
        "status": "Live"
    },
    {
        "process": "LinkedIn trending Posts",
        "owner": "Ayush and Divya",
        "Department": "Social Media",
        "hrsSaved": 3,
        "accuracy": 94,
        "status": "Live"
    },
    {
        "process": "AI Tools Automation",
        "owner": "Ayush",
        "Department": "AI",
        "hrsSaved": 6,
        "accuracy": 94,
        "status": "Live"
    },
    {
        "process": "Documentations Automation",
        "owner": "Ayush and Divya",
        "Department": "AI",
        "hrsSaved": 2,
        "accuracy": 94,
        "status": "Live"
    },
    {
        "process": "RIVA bot",
        "owner": "Ayush and Divya",
        "Department": "AI",
        "hrsSaved": 8,
        "accuracy": 94,
        "status": "Live"
    },
],
        "metadata": {
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "total_processes": 46,
            "avg_accuracy": 94,
            "total_Department": 7
        }
    }

    return render(request, "index.html", {"data": data})


# Alternative view for API endpoint (if needed)
def dashboard_api(request):
    """
    JSON API endpoint for dashboard data
    """
    from django.http import JsonResponse

    # Get user filter from query params
    user_filter = request.GET.get('user', 'all')

    # Reuse the same data structure
    view_data = ceo_dashboard.__wrapped__(request)

    return JsonResponse(view_data.context_data['data'])
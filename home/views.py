from django.shortcuts import render
from datetime import datetime

def dash(request):
    data = {
        "kpi": {
    "all": {
        "automations": 48,
        "handover": 41,
        "hrsSaved": 350,
        "production": 41
    },
    "Ayush": {
        "automations": 48,
        "handover": 41,
        "hrsSaved": 250,
        "production": 41
    },
    "Divya": {
        "automations": 21,
        "handover": 14,
        "hrsSaved": 60,
        "production": 14
    },
},
        "bar": {
    "all": {
        "labels": ["Karthick", "Sales and Data", "HR", "SEO and PPC", "Content Team", "Design and Social Media", "AI"],
        "data": [9, 7, 3, 16, 4, 6, 3]
    },
    "Ayush": {
        "labels": ["Karthick", "Sales and Data", "HR", "SEO and PPC", "Content Team", "Design and Social Media", "AI"],
        "data": [8, 6, 3, 14, 3, 5, 2]
    },
    "Divya": {
        "labels": ["Karthick", "Sales and Data", "HR", "SEO and PPC", "Content Team", "Design and Social Media", "AI"],
        "data": [3, 1, 0, 2, 1, 3, 1]
    },
},
        "pie": {
    "all": {
        "labels": ["Ayush", "Divya"],
        "data": [48, 21]
    },
    "Ayush": {
        "labels": ["Ayush"],
        "data": [48]
    },
    "Divya": {
        "labels": ["Divya"],
        "data": [21]
    },
},
        "line": {
    "all": {
        "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        "data": [1, 2, 3, 4, 4, 5, 5, 6, 7, 14]  # total = 35
    },
    "Ayush": {
        "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        "data": [1, 2, 3, 4, 4, 5, 5, 6, 7, 14]  # total = 28
    },
    "Divya": {
        "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        "data": [0, 0, 0, 0, 0, 0, 3, 3, 3, 12]  # total = 7
    },
},
        "rows": [
    {
        "process": "Blog Summarizer",
        "owner": "Ayush and Divya",
        "Department": "Content",
        "hrsSaved": 6,
        "accuracy": 96,
        "status": "Testing"
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
        "status": "Live"
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
    {
        "process": "Composio and MINDPAL MCP",
        "owner": "Ayush",
        "Department": "SEO",
        "hrsSaved": 2,
        "accuracy": 94,
        "status": "Live"
    },
    {
        "process": "Capture first & Referring Page",
        "owner": "Ayush",
        "Department": "SEO",
        "hrsSaved": 4,
        "accuracy": 94,
        "status": "Live"
    },
    {
        "process": "LinkedIn Post Finder",
        "owner": "Ayush",
        "Department": "SEO",
        "hrsSaved": 2,
        "accuracy": 94,
        "status": "Live"
    },
    {
        "process": "MINDPAL Custom Tool",
        "owner": "Ayush",
        "Department": "SEO",
        "hrsSaved": 6,
        "accuracy": 94,
        "status": "Live"
    },
    {
        "process": "Webflow Automation",
        "owner": "Ayush",
        "Department": "SEO",
        "hrsSaved": 6,
        "accuracy": 94,
        "status": "Live"
    },
    {
        "process": "Linkedin Ads Automations ",
        "owner": "Ayush",
        "Department": "PPC",
        "hrsSaved": 2,
        "accuracy": 94,
        "status": "Live"
    },
    {
        "process": "MQL/SQL Leads Qualifications ",
        "owner": "Ayush",
        "Department": "SEO",
        "hrsSaved": 2,
        "accuracy": 94,
        "status": "Live"
    },
    {
        "process": "Karthick Email into Notions",
        "owner": "Ayush",
        "Department": "Karthick",
        "hrsSaved": 6,
        "accuracy": 94,
        "status": "Live"
    },
    {
        "process": "Blog Outline Gen",
        "owner": "Ayush",
        "Department": "Content",
        "hrsSaved": 2,
        "accuracy": 94,
        "status": "Live"
    },
    {
        "process": "Keyword Researcher[Gumloop]",
        "owner": "Ayush",
        "Department": "SEO",
        "hrsSaved": 3,
        "accuracy": 94,
        "status": "Live"
    },
    {
        "process": "Scraping Resturant Data",
        "owner": "Ayush",
        "Department": "Data",
        "hrsSaved": 6,
        "accuracy": 94,
        "status": "Live"
    },
    {
        "process": "SEO Forecasting Tool",
        "owner": "Ayush",
        "Department": "SEO",
        "hrsSaved": 2,
        "accuracy": 94,
        "status": "Live"
    },
    {
        "process": "Mass Mailer Blog Scraper",
        "owner": "Ayush",
        "Department": "SEO",
        "hrsSaved": 2,
        "accuracy": 94,
        "status": "Live"
    },
    {
        "process": "Googttle Search Console with Claude ",
        "owner": "Ayush",
        "Department": "SEO",
        "hrsSaved": 2,
        "accuracy": 94,
        "status": "Live"
    }
],
        "metadata": {
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "total_processes": 46,
            "avg_accuracy": 94,
            "total_Department": 7
        }
    }

    # return render(request, "index.html", {"data": data})
    
    return render(request,'dashboard.html',{"data": data})

def ceo_dashboard(request):
    """
    Enhanced CEO Dashboard with more realistic automation data
    """

    data = {
        "kpi": {
    "all": {
        "automations": 44,
        "handover": 41,
        "hrsSaved": 310,
        "production": 41
    },
    "Ayush": {
        "automations": 44,
        "handover": 41,
        "hrsSaved": 250,
        "production": 41
    },
    "Divya": {
        "automations": 17,
        "handover": 14,
        "hrsSaved": 60,
        "production": 14
    },
},
        "bar": {
    "all": {
        "labels": ["Karthick", "Sales and Data", "HR", "SEO and PPC", "Content Team", "Design and Social Media", "AI"],
        "data": [7, 7, 3, 16, 4, 4, 3]
    },
    "Ayush": {
        "labels": ["Karthick", "Sales and Data", "HR", "SEO and PPC", "Content Team", "Design and Social Media", "AI"],
        "data": [6, 6, 3, 14, 3, 3, 2]
    },
    "Divya": {
        "labels": ["Karthick", "Sales and Data", "HR", "SEO and PPC", "Content Team", "Design and Social Media", "AI"],
        "data": [1, 1, 0, 2, 1, 1, 1]
    },
},
        "pie": {
    "all": {
        "labels": ["Ayush", "Divya"],
        "data": [35, 17]
    },
    "Ayush": {
        "labels": ["Ayush"],
        "data": [35]
    },
    "Divya": {
        "labels": ["Divya"],
        "data": [17]
    },
},
        "line": {
    "all": {
        "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        "data": [1, 2, 3, 4, 4, 5, 5, 6, 7, 10]  # total = 35
    },
    "Ayush": {
        "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        "data": [1, 2, 3, 4, 4, 5, 5, 6, 7, 10]  # total = 28
    },
    "Divya": {
        "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        "data": [0, 0, 0, 0, 0, 0, 3, 3, 3, 8]  # total = 7
    },
},
        "rows": [
    {
        "process": "Blog Summarizer",
        "owner": "Ayush and Divya",
        "Department": "Content",
        "hrsSaved": 6,
        "accuracy": 96,
        "status": "Testing"
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
        "status": "Live"
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
    {
        "process": "Composio and MINDPAL MCP",
        "owner": "Ayush",
        "Department": "SEO",
        "hrsSaved": 2,
        "accuracy": 94,
        "status": "Live"
    },
    {
        "process": "Capture first & Referring Page",
        "owner": "Ayush",
        "Department": "SEO",
        "hrsSaved": 4,
        "accuracy": 94,
        "status": "Live"
    },
    {
        "process": "LinkedIn Post Finder",
        "owner": "Ayush",
        "Department": "SEO",
        "hrsSaved": 2,
        "accuracy": 94,
        "status": "Live"
    },
    {
        "process": "MINDPAL Custom Tool",
        "owner": "Ayush",
        "Department": "SEO",
        "hrsSaved": 6,
        "accuracy": 94,
        "status": "Live"
    },
    {
        "process": "Webflow Automation",
        "owner": "Ayush",
        "Department": "SEO",
        "hrsSaved": 6,
        "accuracy": 94,
        "status": "Live"
    },
    {
        "process": "Linkedin Ads Automations ",
        "owner": "Ayush",
        "Department": "PPC",
        "hrsSaved": 2,
        "accuracy": 94,
        "status": "Live"
    },
    {
        "process": "MQL/SQL Leads Qualifications ",
        "owner": "Ayush",
        "Department": "SEO",
        "hrsSaved": 2,
        "accuracy": 94,
        "status": "Live"
    },
    {
        "process": "Karthick Email into Notions",
        "owner": "Ayush",
        "Department": "Karthick",
        "hrsSaved": 6,
        "accuracy": 94,
        "status": "Live"
    },
    {
        "process": "Blog Outline Gen",
        "owner": "Ayush",
        "Department": "Content",
        "hrsSaved": 2,
        "accuracy": 94,
        "status": "Live"
    },
    {
        "process": "Keyword Researcher[Gumloop]",
        "owner": "Ayush",
        "Department": "SEO",
        "hrsSaved": 3,
        "accuracy": 94,
        "status": "Live"
    },
    {
        "process": "Scraping Resturant Data",
        "owner": "Ayush",
        "Department": "Data",
        "hrsSaved": 6,
        "accuracy": 94,
        "status": "Live"
    },
    {
        "process": "SEO Forecasting Tool",
        "owner": "Ayush",
        "Department": "SEO",
        "hrsSaved": 2,
        "accuracy": 94,
        "status": "Live"
    },
    {
        "process": "Mass Mailer Blog Scraper",
        "owner": "Ayush",
        "Department": "SEO",
        "hrsSaved": 2,
        "accuracy": 94,
        "status": "Live"
    },
    {
        "process": "Google Search Console with Claude ",
        "owner": "Ayush",
        "Department": "SEO",
        "hrsSaved": 2,
        "accuracy": 94,
        "status": "Live"
    },
            {
                "process": "Reporting Dashboard ",
                "owner": "Ayush and Divya",
                "Department": "Karthick",
                "hrsSaved": 2,
                "accuracy": 94,
                "status": "Testing"
            },
            {
                "process": "Click Up Bot",
                "owner": "Ayush and Divya",
                "Department": "Karthick",
                "hrsSaved": 2,
                "accuracy": 94,
                "status": "Testing"
            },
            {
                "process": "Linkedin AI Agent ",
                "owner": "Ayush and Divya",
                "Department": "Social Media",
                "hrsSaved": 2,
                "accuracy": 94,
                "status": "Testing"
            },
            {
                "process": " Newsletter and linkedin post generater",
                "owner": "Ayush and Divya",
                "Department": "Social Media",
                "hrsSaved": 2,
                "accuracy": 94,
                "status": "Testing"
            }
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

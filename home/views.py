from django.shortcuts import render
from datetime import datetime


def ceo_dashboard(request):
    """
    Enhanced CEO Dashboard with more realistic automation data
    """

    data = {
        "kpi": {
            "all": {
                "automations": 15,
                "handover": 12,
                "hrsSaved": 1840,
                "production": 10
            },
            "Ayush": {
                "automations": 8,
                "handover": 6,
                "hrsSaved": 920,
                "production": 5
            },
            "Divya": {
                "automations": 7,
                "handover": 6,
                "hrsSaved": 920,
                "production": 5
            },
        },

        "bar": {
            "all": {
                "labels": ["Operations", "Finance", "HR", "Sales", "Support"],
                "data": [520, 380, 340, 320, 280]
            },
            "Ayush": {
                "labels": ["Operations", "Finance", "Sales"],
                "data": [280, 200, 180]
            },
            "Divya": {
                "labels": ["HR", "Support", "Operations"],
                "data": [280, 260, 180]
            },
        },

        "pie": {
            "all": {
                "labels": ["Ayush", "Divya"],
                "data": [920, 920]
            },
            "Ayush": {
                "labels": ["Ayush"],
                "data": [920]
            },
            "Divya": {
                "labels": ["Divya"],
                "data": [920]
            },
        },

        "line": {
            "all": {
                "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun","Jul","Aug","Sep","Oct","Nov","Dec"],
                "data": [0, 2, 5, 6, 8, 14,8,23,]
            },
            "Ayush": {
                "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
                "data": [90, 120, 160, 190, 225, 260]
            },
            "Divya": {
                "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
                "data": [90, 120, 160, 190, 225, 260]
            },
        },

        "rows": [
            {
                "process": "Invoice Processing Bot",
                "owner": "Ayush",
                "Department": "HR",
                "hrsSaved": 180,
                "accuracy": 96,
                "status": "Live"
            },
            {
                "process": "HR Onboarding Automation",
                "owner": "Divya",
                "Department": "HR",
                "hrsSaved": 140,
                "accuracy": 94,
                "status": "Live"
            },
            {
                "process": "Purchase Order Tracker",
                "owner": "Ayush",
                "Department": "HR",
                "hrsSaved": 120,
                "accuracy": 95,
                "status": "Live"
            },
            {
                "process": "Customer Support Classifier",
                "owner": "Divya",
                "Department": "HR",
                "hrsSaved": 160,
                "accuracy": 92,
                "status": "Live"
            },
            {
                "process": "Expense Report Validator",
                "owner": "Ayush",
                "Department": "HR",
                "hrsSaved": 95,
                "accuracy": 93,
                "status": "Live"
            },
            {
                "process": "Contract Review Assistant",
                "owner": "Divya",
                "Department": "HR",
                "hrsSaved": 110,
                "accuracy": 91,
                "status": "Testing"
            },
            {
                "process": "Inventory Management Bot",
                "owner": "Ayush",
                "Department": "HR",
                "hrsSaved": 130,
                "accuracy": 97,
                "status": "Live"
            },
            {
                "process": "Leave Application Processor",
                "owner": "Divya",
                "Department": "HR",
                "hrsSaved": 85,
                "accuracy": 98,
                "status": "Live"
            },
            {
                "process": "Sales Lead Qualifier",
                "owner": "Ayush",
                "Department": "HR",
                "hrsSaved": 145,
                "accuracy": 89,
                "status": "Live"
            },
            {
                "process": "Email Response Generator",
                "owner": "Divya",
                "Department": "HR",
                "hrsSaved": 200,
                "accuracy": 90,
                "status": "Live"
            },
            {
                "process": "Data Entry Bot",
                "owner": "Ayush",
                "Department": "HR",
                "hrsSaved": 75,
                "accuracy": 94,
                "status": "Testing"
            },

        ],

        # Additional metadata
        "metadata": {
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "total_processes": 15,
            "avg_accuracy": 94,
            "total_Department": 28550
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
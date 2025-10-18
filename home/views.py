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
            "anuj": {
                "automations": 8,
                "handover": 6,
                "hrsSaved": 920,
                "production": 5
            },
            "vaishali": {
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
            "anuj": {
                "labels": ["Operations", "Finance", "Sales"],
                "data": [280, 200, 180]
            },
            "vaishali": {
                "labels": ["HR", "Support", "Operations"],
                "data": [280, 260, 180]
            },
        },

        "pie": {
            "all": {
                "labels": ["Anuj", "Vaishali"],
                "data": [920, 920]
            },
            "anuj": {
                "labels": ["Anuj"],
                "data": [920]
            },
            "vaishali": {
                "labels": ["Vaishali"],
                "data": [920]
            },
        },

        "line": {
            "all": {
                "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
                "data": [180, 240, 320, 380, 450, 520]
            },
            "anuj": {
                "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
                "data": [90, 120, 160, 190, 225, 260]
            },
            "vaishali": {
                "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
                "data": [90, 120, 160, 190, 225, 260]
            },
        },

        "rows": [
            {
                "process": "Invoice Processing Bot",
                "owner": "Anuj",
                "volume": 2400,
                "hrsSaved": 180,
                "accuracy": 96,
                "status": "Live"
            },
            {
                "process": "HR Onboarding Automation",
                "owner": "Vaishali",
                "volume": 1800,
                "hrsSaved": 140,
                "accuracy": 94,
                "status": "Live"
            },
            {
                "process": "Purchase Order Tracker",
                "owner": "Anuj",
                "volume": 1500,
                "hrsSaved": 120,
                "accuracy": 95,
                "status": "Live"
            },
            {
                "process": "Customer Support Classifier",
                "owner": "Vaishali",
                "volume": 3200,
                "hrsSaved": 160,
                "accuracy": 92,
                "status": "Live"
            },
            {
                "process": "Expense Report Validator",
                "owner": "Anuj",
                "volume": 1200,
                "hrsSaved": 95,
                "accuracy": 93,
                "status": "Live"
            },
            {
                "process": "Contract Review Assistant",
                "owner": "Vaishali",
                "volume": 800,
                "hrsSaved": 110,
                "accuracy": 91,
                "status": "Testing"
            },
            {
                "process": "Inventory Management Bot",
                "owner": "Anuj",
                "volume": 2000,
                "hrsSaved": 130,
                "accuracy": 97,
                "status": "Live"
            },
            {
                "process": "Leave Application Processor",
                "owner": "Vaishali",
                "volume": 1600,
                "hrsSaved": 85,
                "accuracy": 98,
                "status": "Live"
            },
            {
                "process": "Sales Lead Qualifier",
                "owner": "Anuj",
                "volume": 2800,
                "hrsSaved": 145,
                "accuracy": 89,
                "status": "Live"
            },
            {
                "process": "Email Response Generator",
                "owner": "Vaishali",
                "volume": 4500,
                "hrsSaved": 200,
                "accuracy": 90,
                "status": "Live"
            },
            {
                "process": "Data Entry Bot",
                "owner": "Anuj",
                "volume": 1100,
                "hrsSaved": 75,
                "accuracy": 94,
                "status": "Testing"
            },
            {
                "process": "Meeting Scheduler",
                "owner": "Vaishali",
                "volume": 900,
                "hrsSaved": 60,
                "accuracy": 95,
                "status": "Testing"
            },
            {
                "process": "Document Classifier",
                "owner": "Anuj",
                "volume": 1700,
                "hrsSaved": 105,
                "accuracy": 93,
                "status": "Live"
            },
            {
                "process": "Payroll Automation",
                "owner": "Vaishali",
                "volume": 1300,
                "hrsSaved": 115,
                "accuracy": 99,
                "status": "Testing"
            },
            {
                "process": "Compliance Checker",
                "owner": "Anuj",
                "volume": 950,
                "hrsSaved": 85,
                "accuracy": 92,
                "status": "Testing"
            },
        ],

        # Additional metadata
        "metadata": {
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "total_processes": 15,
            "avg_accuracy": 94,
            "total_volume": 28550
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
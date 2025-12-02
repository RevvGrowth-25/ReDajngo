from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
import requests
import json
from dateutil import parser
def feedback(request):
    return render(request,'feedback.html')

def ceo_dashboard(request):
    """
    Enhanced CEO Dashboard with more realistic automation data
    """
    data = {
        "kpi": {
            "all": {
                "automations": 50,
                "handover": 44,
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
                "labels": ["Karthick", "Sales and Data", "HR", "SEO and PPC", "Content Team", "Design and Social Media",
                           "AI"],
                "data": [9, 7, 3, 18, 4, 6, 3]
            },
            "Ayush": {
                "labels": ["Karthick", "Sales and Data", "HR", "SEO and PPC", "Content Team", "Design and Social Media",
                           "AI"],
                "data": [8, 6, 3, 15, 3, 5, 2]
            },
            "Divya": {
                "labels": ["Karthick", "Sales and Data", "HR", "SEO and PPC", "Content Team", "Design and Social Media",
                           "AI"],
                "data": [3, 1, 0, 4, 1, 3, 1]
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
                "data": [1, 2, 3, 4, 4, 5, 5, 6, 7, 14,2]
            },
            "Ayush": {
                "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                "data": [1, 2, 3, 4, 4, 5, 5, 6, 7, 14,1]
            },
            "Divya": {
                "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                "data": [0, 0, 0, 0, 0, 0, 3, 3, 3, 12,2]
            },
        },
        "rows": [
            {
                "process": "Blog Summarizer",
                "owner": "Ayush and Divya",
                "Department": "Content",
                "hrsSaved": 6,
                "accuracy": 96,
                "status": "Testing",
                "workflowID": "ORwODhPEbCMkXtCr"  # Changed to match actual n8n workflow
            },
            {
                "process": "Reddit AI Agent",
                "owner": "Ayush and Divya",
                "Department": "Content",
                "hrsSaved": 2,
                "accuracy": 94,
                "status": "Testing",
                "workflowID": "RoLEBOUSnK8oVYRj"
            },
            {
                "process": "Click Up Task Automation",
                "owner": "Ayush and Divya",
                "Department": "Design",
                "hrsSaved": 0.5,
                "accuracy": 95,
                "status": "Live",
                "workflowID":"nkexdQHzN38g1yEd"
            },
            {
                "process": "Hiring Automation",
                "owner": "Ayush",
                "Department": "HR",
                "hrsSaved": 4,
                "accuracy": 92,
                "status": "Live",
                "disable":"False",
                "workflowID":""
            },
            {
                "process": "Instant CV Reader",
                "owner": "Ayush",
                "Department": "HR",
                "hrsSaved": 6,
                "accuracy": 92,
                "status": "Live",
                "disable":"False",
                "workflowID":""
            },
            {
                "process": "TO-Do Automation",
                "owner": "Ayush",
                "Department": "HR",
                "hrsSaved": 4,
                "accuracy": 91,
                "status": "Live",
                "disable":"False",
                "workflowID":""
            },
            {
                "process": "Clickup Automation",
                "owner": "Ayush",
                "Department": "Karthick",
                "hrsSaved": 4,
                "accuracy": 97,
                "status": "Live",
                "workflowID":"nBet5npnfp5XevBg"
            },
            {
                "process": "Landing Page Automation",
                "owner": "Ayush and Divya",
                "Department": "Karthick",
                "hrsSaved": 8,
                "accuracy": 98,
                "status": "Testing",
                "workflowID":"ceZCJHxpo044mssA"
            },
            {
                "process": "Proposal Automation",
                "owner": "Ayush and Divya",
                "Department": "Karthick",
                "hrsSaved": 8,
                "accuracy": 89,
                "status": "Live",
                "workflowID":"ta5g7bb05euWCxCk"
            },
            {
                "process": "Prospect Email Automation",
                "owner": "Ayush",
                "Department": "Karthick",
                "hrsSaved": 4,
                "accuracy": 90,
                "status": "Live",
                "workflowID":"WIcJazEMuViqNhd4"
            },
            {
                "process": "Proposal Follow Up Notif",
                "owner": "Ayush and Divya",
                "Department": "Sales",
                "hrsSaved": 0.5,
                "accuracy": 94,
                "status": "Live",
                "workflowID":""
            },
            {
                "process": "Weekly Report Automation",
                "owner": "Ayush and Divya",
                "Department": "Sales",
                "hrsSaved": 0.5,
                "accuracy": 94,
                "status": "Live",
                "workflowID":"KjWtBVddRaHcsAoL"
            },
            {
                "process": "RFI Automation",
                "owner": "Ayush and Divya",
                "Department": "Sales",
                "hrsSaved": 4,
                "accuracy": 94,
                "status": "Live",
                "workflowID":"2pQCtFsYEB3BdzcV"
            },
            {
                "process": "Series A Automation",
                "owner": "Ayush",
                "Department": "Data",
                "hrsSaved": 4,
                "accuracy": 94,
                "status": "Live",
                "workflowID":"rlQn6ENPiamoUIgj"
            },
            {
                "process": "Trello X Google Sheets",
                "owner": "Ayush",
                "Department": "Data",
                "hrsSaved": 4,
                "accuracy": 94,
                "status": "Live",
                "disable":"False",
                "workflowID":""
            },
            {
                "process": "Website Leads",
                "owner": "Ayush",
                "Department": "Sales",
                "hrsSaved": 4,
                "accuracy": 94,
                "status": "Live",
                "disable":"False",
                "workflowID":""
            },
            {
                "process": "AI Outreach Engine V1",
                "owner": "Ayush",
                "Department": "SEO",
                "hrsSaved": 4,
                "accuracy": 94,
                "status": "Live",
                "disable":"False",
                "workflowID":""
            },
            {
                "process": "Competitor kwd Analysis",
                "owner": "Ayush and Divya",
                "Department": "SEO",
                "hrsSaved": 5,
                "accuracy": 94,
                "status": "Live",
                "workflowID":"1mcP3gr3w3Ai3WZQ"
            },
            {
                "process": "Google ads customgpt",
                "owner": "Ayush and Divya",
                "Department": "PPC",
                "hrsSaved": 6,
                "accuracy": 94,
                "status": "Live",
                "disable":"False",
                "workflowID":""
            },
            {
                "process": "Content Audit Automation",
                "owner": "Ayush and Divya",
                "Department": "SEO",
                "hrsSaved": 5,
                "accuracy": 94,
                "status": "Live",
                "workflowID":"YSLtvDYiiL6iSANb"
            },
            {
                "process": "Lead Qualifications",
                "owner": "Ayush",
                "Department": "SEO",
                "hrsSaved": 6,
                "accuracy": 94,
                "status": "Live",
                "disable":"False",
                "workflowID":""
            },
            {
                "process": "Scrape Communities Automation",
                "owner": "Ayush",
                "Department": "SEO",
                "hrsSaved": 2,
                "accuracy": 94,
                "status": "Live",
                "workflowID":""
            },
            {
                "process": "Revv AI Blog Gen",
                "owner": "Ayush and Divya",
                "Department": "SEO",
                "hrsSaved": 6,
                "accuracy": 94,
                "status": "Live",
                "workflowID":"tyeI2wrHhElPvCeY"
            },
            {
                "process": "Keyword Brief",
                "owner": "Ayush and Divya",
                "Department": "SEO",
                "hrsSaved": 4,
                "accuracy": 94,
                "status": "Live",
                "disable":"False",
                "workflowID":""
            },
            {
                "process": "Click Bait Automation",
                "owner": "Ayush and Divya",
                "Department": "Social Media",
                "hrsSaved": 4,
                "accuracy": 94,
                "status": "Live",
                "workflowID":"IkG9PNmYXGEIO1sd"
            },
            {
                "process": "Linkedin Outreach Automation",
                "owner": "Ayush",
                "Department": "Social Media",
                "hrsSaved": 3,
                "accuracy": 94,
                "status": "Live",
                "disable":"False",
                "workflowID":""
            },
            {
                "process": "LinkedIn trending Posts",
                "owner": "Ayush and Divya",
                "Department": "Social Media",
                "hrsSaved": 3,
                "accuracy": 94,
                "status": "Live",
                "disable":"False",
                "workflowID":""
            },
            {
                "process": "AI Tools Automation",
                "owner": "Ayush",
                "Department": "AI",
                "hrsSaved": 6,
                "accuracy": 94,
                "status": "Live",
                "workflowID":"IXhaW6XTANVDhocc"
            },
            {
                "process": "Documentations Automation",
                "owner": "Ayush and Divya",
                "Department": "AI",
                "hrsSaved": 2,
                "accuracy": 94,
                "status": "Live",
                "workflowID":"EEHbxKQFbCt8cMNy"
            },
            {
                "process": "RIVA bot",
                "owner": "Ayush and Divya",
                "Department": "AI",
                "hrsSaved": 8,
                "accuracy": 94,
                "status": "Live",
                "workflowID":"E8Hd9KcUzVHlhLKQ"
            },
            {
                "process": "Composio and MINDPAL MCP",
                "owner": "Ayush",
                "Department": "SEO",
                "hrsSaved": 2,
                "accuracy": 94,
                "status": "Live",
                "disable":"False",
                "workflowID":""
            },
            {
                "process": "Capture first & Referring Page",
                "owner": "Ayush",
                "Department": "SEO",
                "hrsSaved": 4,
                "accuracy": 94,
                "status": "Live",
                "disable":"False",
                "workflowID":""
            },
            {
                "process": "LinkedIn Post Finder",
                "owner": "Ayush",
                "Department": "SEO",
                "hrsSaved": 2,
                "accuracy": 94,
                "status": "Live",
                "disable":"False",
                "workflowID":""
            },
            {
                "process": "MINDPAL Custom Tool",
                "owner": "Ayush",
                "Department": "SEO",
                "hrsSaved": 6,
                "accuracy": 94,
                "status": "Live",
                "disable":"False",
                "workflowID":""
            },
            {
                "process": "Webflow Automation",
                "owner": "Ayush",
                "Department": "SEO",
                "hrsSaved": 6,
                "accuracy": 94,
                "status": "Live",
                "disable":"False",
                "workflowID":""
            },
            {
                "process": "Linkedin Ads Automations ",
                "owner": "Ayush",
                "Department": "PPC",
                "hrsSaved": 2,
                "accuracy": 94,
                "status": "Live",
                "disable":"False",
                "workflowID":""
            },
            {
                "process": "MQL/SQL Leads Qualifications ",
                "owner": "Ayush",
                "Department": "SEO",
                "hrsSaved": 2,
                "accuracy": 94,
                "status": "Live",
                "disable":"False",
                "workflowID":""
            },
            {
                "process": "Karthick Email into Notions",
                "owner": "Ayush",
                "Department": "Karthick",
                "hrsSaved": 6,
                "accuracy": 94,
                "status": "Live",
                "disable": "False",
                "workflowID":""
            },
            {
                "process": "Blog Outline Gen",
                "owner": "Ayush",
                "Department": "Content",
                "hrsSaved": 2,
                "accuracy": 94,
                "status": "Live",
                "disable":"False",
                "workflowID":""
            },
            {
                "process": "Keyword Researcher[Gumloop]",
                "owner": "Ayush",
                "Department": "SEO",
                "hrsSaved": 3,
                "accuracy": 94,
                "status": "Live",
                "disable":"False",
                "workflowID":""
            },
            {
                "process": "Scraping Resturant Data",
                "owner": "Ayush",
                "Department": "Data",
                "hrsSaved": 6,
                "accuracy": 94,
                "status": "Live",
                "disable":"False",
                "workflowID":""
            },
            {
                "process": "SEO Forecasting Tool",
                "owner": "Ayush",
                "Department": "SEO",
                "hrsSaved": 2,
                "accuracy": 94,
                "status": "Live",
                "disable":"False",
                "workflowID":""
            },
            {
                "process": "Mass Mailer Blog Scraper",
                "owner": "Ayush",
                "Department": "SEO",
                "hrsSaved": 2,
                "accuracy": 94,
                "status": "Live",
                "disable":"False",
                "workflowID":""
            },
            {
                "process": "Google Search Console with Claude ",
                "owner": "Ayush",
                "Department": "SEO",
                "hrsSaved": 2,
                "accuracy": 94,
                "status": "Live",
                "disable":"False",
                "workflowID":""
            },
            {
                "process": "Reporting Dashboard ",
                "owner": "Ayush and Divya",
                "Department": "Karthick",
                "hrsSaved": 2,
                "accuracy": 94,
                "status": "Testing",
                "workflowID":"dtZAb90qxdBsuTXu"
            },
            {
                "process": "Click Up Bot",
                "owner": "Ayush and Divya",
                "Department": "Karthick",
                "hrsSaved": 2,
                "accuracy": 94,
                "status": "Live",
                "workflowID":"HHVUJosFwXL0AnQZ"
            },
            {
                "process": "Linkedin AI Agent ",
                "owner": "Ayush and Divya",
                "Department": "Social Media",
                "hrsSaved": 2,
                "accuracy": 94,
                "status": "Live",
                "workflowID":"aU2d5IIQHMePdNWy"
            },
            {
                "process": " Newsletter and linkedin post generater",
                "owner": "Ayush and Divya",
                "Department": "Social Media",
                "hrsSaved": 2,
                "accuracy": 94,
                "status": "Live",
                "workflowID":"0vjzitT78ZmTiMsb"
            },
            {
                "process": "PPC BOT",
                "owner": "Ayush and Divya",
                "Department": "PPC",
                "hrsSaved": 2,
                "accuracy": 94,
                "status": "Testing",
                "disable":"False",
                "workflowID":""
            },
            {
                "process": "Keyword Brief CustomGPT",
                "owner": "Divya",
                "Department": "SEO",
                "hrsSaved": 2,
                "accuracy": 95,
                "status": "Testing",
                "disable":"False",
                "workflowID":""
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


@csrf_exempt
def get_workflow_report(request):
    """
    Fetch workflow report from n8n and return processed stats
    """
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST allowed'}, status=405)

    try:
        body = json.loads(request.body)
        workflow_id = body.get('workflowID')

        if not workflow_id:
            return JsonResponse({'error': 'workflowID required'}, status=400)

        print(f"🔍 Fetching data for workflow: {workflow_id}")

        # 1. Hit n8n webhook
        webhook_url = 'https://n8n.srv992398.hstgr.cloud/webhook/2fe18d5a-6797-4199-9e34-9b28aa5af44c'
        webhook_payload = {'workflowID': workflow_id}
        print(f"📤 Sending payload to n8n: {webhook_payload}")

        resp = requests.post(
            webhook_url,
            json=webhook_payload,
            headers={'Content-Type': 'application/json'},
            timeout=30
        )

        if resp.status_code != 200:
            print(f"❌ n8n webhook failed: {resp.status_code}")
            return JsonResponse({'error': f'n8n returned {resp.status_code}'}, status=500)

        raw = resp.json()
        print(f"✅ Received response from webhook")
        print(f"📦 Raw response structure: {type(raw)}")

        # 2. Extract executions from nested structure
        executions = []
        if isinstance(raw, list):
            if len(raw) > 0 and isinstance(raw[0], dict):
                if 'data' in raw[0]:
                    executions = raw[0]['data']
                    print(f"   └─ Found 'data' key with {len(executions)} executions")
                elif 'workflowId' in raw[0]:
                    executions = raw
                    print(f"   └─ Direct execution list with {len(executions)} items")
        elif isinstance(raw, dict):
            if 'data' in raw:
                executions = raw['data']
                print(f"   └─ Found 'data' key with {len(executions)} executions")

        print(f"📊 Total executions extracted: {len(executions)}")

        # Debug: Print first execution's workflowId to see what we're getting
        if executions and len(executions) > 0:
            first_workflow = executions[0].get('workflowId', 'NO_WORKFLOW_ID')
            print(f"🔍 First execution's workflowId: {first_workflow}")
            print(f"🔍 Requested workflowId: {workflow_id}")
            print(f"🔍 IDs match: {first_workflow == workflow_id}")

            # Check if there are multiple workflow IDs in the response
            unique_workflows = set(ex.get('workflowId') for ex in executions)
            print(f"🔍 Unique workflow IDs in response: {unique_workflows}")

        # 3. Filter by workflowId (case-insensitive comparison)
        filtered = [ex for ex in executions if ex.get('workflowId', '').lower() == workflow_id.lower()]
        print(f"🎯 Filtered executions for {workflow_id}: {len(filtered)}")

        if len(filtered) == 0:
            print(f"⚠️ No executions found for workflow {workflow_id}")
            return JsonResponse({
                'totalRuns': 0,
                'successRate': 0,
                'avgDuration': 0,
                'lastRun': 'No executions found',
                'statusCount': {'success': 0, 'failed': 0, 'running': 0},
                'dailyTrend': {
                    'labels': ['No Data'],
                    'success': [0],
                    'failed': [0],
                    'total': [0]
                },
                'timeline': {
                    'all': [],
                    'success': [],
                    'failed': []
                }
            })

        # 4. Calculate stats
        total = len(filtered)
        success = sum(1 for ex in filtered if ex.get('finished') is True)
        failed = sum(1 for ex in filtered if ex.get('finished') is False)
        running = sum(1 for ex in filtered if ex.get('finished') is None)
        success_rate = round((success / total) * 100, 1) if total else 0

        print(f"📈 Stats - Total: {total}, Success: {success}, Failed: {failed}, Running: {running}")

        # 5. Calculate average duration
        durations = []
        for ex in filtered:
            if ex.get('startedAt') and ex.get('stoppedAt'):
                try:
                    start = parser.parse(ex['startedAt'])
                    stop = parser.parse(ex['stoppedAt'])
                    duration = (stop - start).total_seconds()
                    durations.append(duration)
                except Exception as e:
                    print(f"⚠️ Duration parse error: {e}")
                    continue

        avg_duration = round(sum(durations) / len(durations), 2) if durations else 0
        print(f"⏱️ Average duration: {avg_duration}s")

        # 6. Get last run timestamp
        last_run = 'N/A'
        if filtered:
            try:
                latest = max(filtered, key=lambda x: x.get('startedAt', ''))
                last_run_dt = parser.parse(latest['startedAt'])
                last_run = last_run_dt.strftime('%d %b %Y, %I:%M %p')
            except Exception as e:
                print(f"⚠️ Last run parse error: {e}")
                last_run = latest.get('startedAt', 'N/A')

        # 7. Daily trend (last 7 days) - Split by success/failure
        from collections import defaultdict
        daily_success = defaultdict(int)
        daily_failed = defaultdict(int)
        daily_total = defaultdict(int)

        for ex in filtered:
            try:
                dt = parser.parse(ex['startedAt'])
                day_key = dt.strftime('%b %d')
                daily_total[day_key] += 1

                if ex.get('finished') is True:
                    daily_success[day_key] += 1
                elif ex.get('finished') is False:
                    daily_failed[day_key] += 1
            except:
                continue

        # Get last 7 days
        all_days = sorted(set(list(daily_success.keys()) + list(daily_failed.keys()) + list(daily_total.keys())))[-7:]

        if all_days:
            trend_labels = all_days
            trend_success = [daily_success.get(day, 0) for day in all_days]
            trend_failed = [daily_failed.get(day, 0) for day in all_days]
            trend_total = [daily_total.get(day, 0) for day in all_days]
        else:
            trend_labels = ['No Data']
            trend_success = [0]
            trend_failed = [0]
            trend_total = [0]

        print(f"📅 Daily trend: {trend_labels}")
        print(f"   ✅ Success: {trend_success}")
        print(f"   ❌ Failed: {trend_failed}")
        print(f"   📊 Total: {trend_total}")

        # 8. Build timeline data for execution duration graphs
        timeline_all = []
        timeline_success = []
        timeline_failed = []

        for ex in filtered:
            try:
                started_at = parser.parse(ex['startedAt'])
                stopped_at = parser.parse(ex.get('stoppedAt', ex['startedAt']))
                duration = (stopped_at - started_at).total_seconds()

                timeline_entry = {
                    'time': started_at.strftime('%d %b %Y, %I:%M %p'),
                    'duration': round(duration, 2)
                }

                timeline_all.append(timeline_entry)

                if ex.get('finished') is True:
                    timeline_success.append(timeline_entry)
                elif ex.get('finished') is False:
                    timeline_failed.append(timeline_entry)
            except Exception as e:
                print(f"⚠️ Timeline parse error: {e}")
                continue

        # Sort by time
        timeline_all.sort(key=lambda x: x['time'])
        timeline_success.sort(key=lambda x: x['time'])
        timeline_failed.sort(key=lambda x: x['time'])

        print(
            f"📊 Timeline data - All: {len(timeline_all)}, Success: {len(timeline_success)}, Failed: {len(timeline_failed)}")

        # 9. Build response
        response_data = {
            'totalRuns': total,
            'successRate': success_rate,
            'avgDuration': avg_duration,
            'lastRun': last_run,
            'statusCount': {
                'success': success,
                'failed': failed,
                'running': running
            },
            'dailyTrend': {
                'labels': trend_labels,
                'success': trend_success,
                'failed': trend_failed,
                'total': trend_total
            },
            'timeline': {
                'all': timeline_all,
                'success': timeline_success,
                'failed': timeline_failed
            }
        }

        print(f"✅ Returning response")
        return JsonResponse(response_data)

    except json.JSONDecodeError as e:
        print(f"❌ JSON decode error: {e}")
        return JsonResponse({'error': 'Invalid JSON in request body'}, status=400)
    except requests.RequestException as e:
        print(f"❌ Request error: {e}")
        return JsonResponse({'error': f'Failed to connect to n8n: {str(e)}'}, status=500)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        return JsonResponse({'error': f'Server error: {str(e)}'}, status=500)


@csrf_exempt
def test_webhook_raw(request):
    """
    Test endpoint to see raw webhook response
    """
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST allowed'}, status=405)

    try:
        body = json.loads(request.body)
        workflow_id = body.get('workflowID', 'PRFxoRmqI2UrXSQ4')

        webhook_url = 'https://n8n.srv992398.hstgr.cloud/webhook/2fe18d5a-6797-4199-9e34-9b28aa5af44c'
        resp = requests.post(
            webhook_url,
            json={'workflowID': workflow_id},
            headers={'Content-Type': 'application/json'},
            timeout=30
        )

        raw = resp.json()

        return JsonResponse({
            'status': 'success',
            'workflowID': workflow_id,
            'responseType': str(type(raw)),
            'rawResponse': raw,
            'firstItemKeys': list(raw[0].keys()) if isinstance(raw, list) and len(raw) > 0 else None
        }, safe=False)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

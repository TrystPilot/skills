#!/usr/bin/env python3
"""
Productivity Analysis Script

Reads daily review data and generates trend analysis and metrics.
Usage:
  python analyze_productivity.py <reviews_file> [--days N]

Where reviews_file is a JSON file containing daily reviews.
"""

import json
import sys
from datetime import datetime, timedelta
from collections import defaultdict

def load_reviews(file_path):
    """Load reviews from JSON file."""
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        # Handle both single review and array of reviews
        if isinstance(data, list):
            return data
        return [data]
    except FileNotFoundError:
        print(f"Error: File {file_path} not found")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in {file_path}")
        sys.exit(1)

def calculate_metrics(reviews, days_to_analyze=None):
    """Calculate aggregate metrics from reviews."""
    if days_to_analyze:
        cutoff_date = datetime.now().date() - timedelta(days=days_to_analyze)
        reviews = [r for r in reviews if datetime.fromisoformat(r.get('date', '')).date() >= cutoff_date]

    if not reviews:
        return None

    metrics = {
        'total_days': len(reviews),
        'date_range': f"{reviews[0].get('date')} to {reviews[-1].get('date')}",
        'accomplishments': [],
        'blockers': defaultdict(int),
        'metrics': {
            'avg_tasks_completed': 0,
            'avg_focused_hours': 0,
            'avg_interruptions': 0,
            'avg_energy': 0,
            'avg_stress': 0,
            'completion_rate': 0,
        },
    }

    total_tasks = 0
    total_focused = 0
    total_interruptions = 0
    total_energy = 0
    total_stress = 0
    completed_days = 0

    for review in reviews:
        # Collect accomplishments
        if 'accomplishments' in review:
            metrics['accomplishments'].extend(review['accomplishments'])

        # Analyze blockers
        if 'blockers' in review:
            for blocker in review['blockers']:
                category = blocker.get('category', 'unknown')
                metrics['blockers'][category] += 1

        # Aggregate metrics
        if 'metrics' in review:
            m = review['metrics']
            total_tasks += m.get('tasks_completed', 0)
            total_focused += m.get('focused_hours', 0)
            total_interruptions += m.get('interruptions', 0)
            total_energy += m.get('energy_level', 0)
            total_stress += m.get('stress_level', 0)
            completed_days += 1

    # Calculate averages
    if completed_days > 0:
        metrics['metrics']['avg_tasks_completed'] = round(total_tasks / completed_days, 1)
        metrics['metrics']['avg_focused_hours'] = round(total_focused / completed_days, 1)
        metrics['metrics']['avg_interruptions'] = round(total_interruptions / completed_days, 1)
        metrics['metrics']['avg_energy'] = round(total_energy / completed_days, 1)
        metrics['metrics']['avg_stress'] = round(total_stress / completed_days, 1)
        metrics['metrics']['completion_rate'] = round((total_tasks / (completed_days * 5)) * 100, 1)

    return metrics

def format_report(metrics):
    """Format metrics into a readable report."""
    if not metrics:
        return "No data available"

    report = []
    report.append("=" * 60)
    report.append("PRODUCTIVITY ANALYSIS REPORT")
    report.append("=" * 60)
    report.append(f"\nAnalysis Period: {metrics['date_range']}")
    report.append(f"Total Days Tracked: {metrics['total_days']}")

    report.append("\n" + "-" * 60)
    report.append("KEY METRICS")
    report.append("-" * 60)
    m = metrics['metrics']
    report.append(f"Average Tasks Completed:    {m['avg_tasks_completed']} per day")
    report.append(f"Average Focused Hours:      {m['avg_focused_hours']} hours per day")
    report.append(f"Average Interruptions:      {m['avg_interruptions']} per day")
    report.append(f"Average Energy Level:       {m['avg_energy']}/5")
    report.append(f"Average Stress Level:       {m['avg_stress']}/5")
    report.append(f"Estimated Completion Rate:  {m['completion_rate']}%")

    if metrics['blockers']:
        report.append("\n" + "-" * 60)
        report.append("TOP BLOCKERS")
        report.append("-" * 60)
        sorted_blockers = sorted(metrics['blockers'].items(), key=lambda x: x[1], reverse=True)
        for blocker, count in sorted_blockers:
            report.append(f"  • {blocker.title()}: {count} occurrences")

    report.append("\n" + "-" * 60)
    report.append("INSIGHTS & RECOMMENDATIONS")
    report.append("-" * 60)

    # Generate insights
    if m['avg_interruptions'] > 5:
        report.append("⚠ HIGH INTERRUPTIONS: Consider time-blocking or do-not-disturb hours")

    if m['avg_focused_hours'] < 4:
        report.append("⚠ LOW FOCUS TIME: Try batching meetings or using pomodoro technique")

    if m['avg_energy'] < 3:
        report.append("⚠ LOW ENERGY: Review sleep, breaks, and workload distribution")

    if m['avg_stress'] > 3.5:
        report.append("⚠ HIGH STRESS: Consider delegating, saying no to less important work")

    # Positive insights
    if m['avg_focused_hours'] >= 5:
        report.append("✓ STRONG FOCUS TIME: You're maintaining good deep work blocks")

    if m['completion_rate'] >= 80:
        report.append("✓ HIGH COMPLETION: Great planning and execution alignment")

    if len(metrics['blockers']) == 0:
        report.append("✓ NO MAJOR BLOCKERS: Momentum is high!")

    report.append("\n" + "=" * 60)

    return "\n".join(report)

def main():
    if len(sys.argv) < 2:
        print("Usage: python analyze_productivity.py <reviews_file> [--days N]")
        print("Example: python analyze_productivity.py reviews.json --days 30")
        sys.exit(1)

    reviews_file = sys.argv[1]
    days = None

    if len(sys.argv) > 3 and sys.argv[2] == '--days':
        days = int(sys.argv[3])

    reviews = load_reviews(reviews_file)
    metrics = calculate_metrics(reviews, days)

    if metrics:
        print(format_report(metrics))
        return metrics
    else:
        print("No data to analyze")
        sys.exit(1)
        return None

if __name__ == '__main__':
    main()

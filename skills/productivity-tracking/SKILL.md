---
name: productivity-tracking
description: Conduct daily productivity reviews and track performance metrics over time. Use this skill whenever users want to log their daily accomplishments, identify blockers, plan the next day, or analyze their productivity patterns and trends. Helps maintain focus and continuous improvement through structured reflection and data-driven insights.
license: Complete terms in LICENSE.txt
---

# Productivity Tracking

A skill for conducting daily reviews and tracking productivity performance over time. This helps users stay accountable, identify patterns in their work, and continuously improve their performance.

## Quick Start

The productivity tracking workflow has two main components:

1. **Daily Review** - A structured reflection on the day's work (5-10 minutes)
2. **Metrics Analysis** - Trend analysis and performance insights across multiple days

## Daily Review Framework

When a user wants to conduct a daily review, guide them through this framework:

### Part 1: Reflection (5 minutes)

Ask the user to reflect on:

**✓ Accomplishments** - What did you complete today? List specific outcomes, not just activities.
- Example: "Completed Q1 budget review", "Shipped feature X", "Resolved 3 client tickets"
- NOT: "Worked on budget", "Did coding", "Handled support"

**⚠ Blockers & Challenges** - What slowed you down or prevented progress?
- Example: "Waiting on design feedback from team", "Database query optimization needed", "Meeting interruptions"
- Categorize: External (waiting on others), Internal (skill gap, unclear requirements), Environmental (distractions, tools)

**⭐ Key Metrics** - Quantify your day:
- Tasks completed
- Hours of focused work
- Interruptions/context switches
- Energy level (1-5)
- Stress level (1-5)

**→ Next Day Plan** - What are your top 3 priorities for tomorrow?
- Be specific about outcomes, not tasks
- Example: "Ship PR for auth feature" not "Work on auth"

### Part 2: Data Capture

Capture the review in a structured format. Use the JSON template below to save daily reviews:

```json
{
  "date": "2026-03-29",
  "accomplishments": [
    "Completed task A",
    "Fixed bug B"
  ],
  "blockers": [
    {
      "issue": "Waiting for feedback",
      "category": "external",
      "impact": "2 hours"
    }
  ],
  "metrics": {
    "tasks_completed": 5,
    "focused_hours": 6.5,
    "interruptions": 3,
    "energy_level": 3,
    "stress_level": 2
  },
  "next_day_priorities": [
    "Priority 1",
    "Priority 2",
    "Priority 3"
  ],
  "notes": "Additional context or observations"
}
```

## Metrics Tracking

### Available Metrics

Track these metrics to identify patterns:

| Metric | Purpose | Interpretation |
|--------|---------|-----------------|
| **Completion Rate** | Tasks completed / tasks planned | Higher = better focus and estimation |
| **Focused Work Hours** | Actual productive hours | Identify your peak productivity capacity |
| **Interruptions** | Count of context switches | Higher = more fragmentation |
| **Energy Level** | Self-reported (1-5) | Correlates with output quality and quantity |
| **Blocker Frequency** | Count and types of blockers | Identify systemic issues |
| **Time to Impact** | Days between plan and completion | Measures planning accuracy |

### Analyzing Trends

Use these insights to improve:

1. **Weekly Summary** - Aggregate daily metrics to see weekly patterns
2. **Blocker Analysis** - Which blockers appear most often? What can you control?
3. **Energy Correlation** - Does energy level correlate with output? Adjust schedule accordingly
4. **Interruption Impact** - How do interruptions affect completion rates?
5. **Priority Success** - What % of planned priorities actually got done?

## Using This Skill

### Scenario 1: User wants to conduct today's review
1. Guide them through the reflection questions above
2. Help them capture their answers in the JSON format
3. Save to their productivity tracking file
4. Offer to show trends if they have previous reviews

### Scenario 2: User wants to analyze their productivity
1. Read their existing review data
2. Calculate key metrics (completion rate, average energy, blocker types)
3. Identify patterns and trends
4. Offer specific, actionable recommendations

### Scenario 3: User wants to improve in a specific area
1. Review recent blocker data
2. Analyze what's within their control vs. external
3. Suggest strategies: reduce interruptions, batch similar work, delegate, etc.
4. Help them set measurable improvement goals

## Best Practices

**Consistency** - Reviews work best when done at the same time daily (end of day or start of next day)

**Specificity** - Avoid vague entries. "Made progress" tells you nothing. "Completed auth module tests" is actionable.

**Honesty** - Be truthful about blockers and metrics. This data is for you to improve, not to impress anyone.

**Action-oriented** - Don't just log data. Use insights to adjust your approach: time blocking, delegation, priority shifting.

**Balance** - Track enough metrics to spot patterns, not so many that the review becomes burdensome (aim for 5-7 key metrics).

## Common Questions

**Q: How long should daily reviews take?**
A: 5-10 minutes if done consistently. The discipline is more important than perfection.

**Q: What if I miss a day?**
A: Just start the next day. One missed review won't affect the trend. But consistency matters for accurate patterns.

**Q: Should I share this data?**
A: It's personal. For 1-on-1s with a manager, you can extract summaries. The raw data is for your own improvement.

**Q: How long until I see patterns?**
A: 2-3 weeks of data is enough to spot basic patterns. 6-8 weeks shows more robust trends.

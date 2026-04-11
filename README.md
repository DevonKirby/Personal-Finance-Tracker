# Personal Finance Tracker

A full-stack web application that automatically ingests your bank transactions, categorizes them using AI, and gives you a clear picture of where your money is going.

> **Status:** In active development — see the [project roadmap](https://github.com/users/DevonKirby/projects/1) for progress.

---

## What it does

This app removes the friction of manually entering transactions by letting you either connect your bank directly or drop in a CSV export — and it handles the rest.

Once your transactions are imported, the app automatically classifies each one into a spending category (Food & Drink, Transport, Bills, etc.) using the Claude AI API. You can override any categorization manually if needed. From there, a dashboard gives you a breakdown of your spending by category, trends over time, and budget tracking so you can see at a glance whether you're on track for the month.

**Core features:**

- **Automatic transaction import** via Plaid (live bank connection) or CSV export from your bank
- **AI-powered categorization** — transaction descriptions are classified automatically on import
- **Deduplication** — importing the same transaction twice (via CSV overlap or CSV + Plaid) is handled gracefully, no duplicates
- **Spending dashboard** — summary cards, category breakdown, and monthly trend charts
- **Budget tracking** — set spending limits per category and track progress throughout the month
- **Manual overrides** — edit any transaction's category if the AI gets it wrong

---

## Getting started

> Setup instructions will be added as each phase is completed.
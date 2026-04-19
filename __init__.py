"""
outbound-agents
===============

Multi-agent SDR pipeline built on Google ADK + A2A. Services:

- Lead Finder: discovers potential business leads via Google Maps + BigQuery
- SDR Agent: researches, drafts proposals, runs voice + email outreach
- Lead Manager: tracks conversion status, schedules meetings
- UI Client: web dashboard for monitoring and control
- Gmail PubSub: ingests reply events and routes them back into the pipeline
"""

__version__ = "1.0.0"
__author__ = "aaryapatel09"

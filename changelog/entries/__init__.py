import json
import logging

from changelog import celery
from changelog.entry.models import ChangelogEntry

logger = logging.getLogger()


@celery.task
def get(service=None, version=None):
    entries = ChangelogEntry.objects
    if service:
        entries = entries.filter(service__iexact=service)
    if version:
        entries = entries.filter(version=version)
    return json.loads(entries.to_json())

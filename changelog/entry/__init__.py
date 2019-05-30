import json
import logging

from changelog import celery
from changelog.entry.models import ChangelogEntry

logger = logging.getLogger()


@celery.task
def get(changelog_entry_id):
    return json.loads(ChangelogEntry.objects.get(id=changelog_entry_id).to_json())


@celery.task
def post(service, version, header, body):
    entry = ChangelogEntry.objects(service=service, version=version, header=header, body=body).first()
    if not entry:
        entry = ChangelogEntry(service=service, version=version, header=header, body=body)
        entry.save()

    return json.loads(entry.to_json())

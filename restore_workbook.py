"""Reconstruct the exact original workbook and verify its SHA-256."""
from pathlib import Path
import hashlib
import json

root = Path(__file__).resolve().parent
parts = root / 'data' / 'workbook_parts'
manifest = json.loads((parts / 'manifest.json').read_text())
chunks = []
for part in manifest['parts']:
    data = (parts / part['name']).read_bytes()
    if len(data) != part['size_bytes'] or hashlib.sha256(data).hexdigest() != part['sha256']:
        raise ValueError('Part verification failed: ' + part['name'])
    chunks.append(data)
data = b''.join(chunks)
if len(data) != manifest['size_bytes'] or hashlib.sha256(data).hexdigest() != manifest['sha256']:
    raise ValueError('Workbook verification failed')
target = root / manifest['file_name']
target.write_bytes(data)
print('Restored and verified:', target.name, len(data), 'bytes')

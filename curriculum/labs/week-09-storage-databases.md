# Week 9 Lab: Persist application data

[← Practical labs](README.md) · [← Week 9 guide](../weeks/week-09.md) · [Starter app](starter-app/README.md)

## Mission
Use Python's standard-library SQLite module to persist structured records, then compare a database with object/file storage. Local-first: no cloud account, billing, Docker or third-party package required.

**Time:** 60–90 minutes · **Cost:** Free

## Part A — Choose storage
| Need | Storage concept | Example |
|---|---|---|
| Query records, relationships and constraints | Relational database | Users, orders |
| Store large unstructured objects | Object storage | Images, PDFs |
| Fast disposable values | Cache | Temporary data |

Managed object storage adds APIs, access controls, durability and lifecycle policies; a local file is not equivalent.

## Part B — Create a SQLite database
```bash
mkdir -p ~/cloud-track-week-09 && cd ~/cloud-track-week-09
python3 --version
cat > storage_lab.py <<'PY'
import sqlite3

db = sqlite3.connect("cloud_track.db")
db.execute("""
CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    body TEXT NOT NULL
)
""")
db.execute(
    "INSERT INTO notes (title, body) VALUES (?, ?)",
    ("first note", "This record survives a process restart.")
)
db.commit()
for row in db.execute("SELECT id, title, body FROM notes"):
    print(row)
db.close()
PY
python3 storage_lab.py
python3 storage_lab.py
ls -lh cloud_track.db
```

Rows remain after the process exits. Running twice inserts two records. Explain why SQL uses placeholders (`?`), not string concatenation.

## Part C — Query persisted data
```bash
python3 - <<'PY'
import sqlite3
db = sqlite3.connect("cloud_track.db")
print("Rows:", db.execute("SELECT COUNT(*) FROM notes").fetchone()[0])
print("Newest:", db.execute(
    "SELECT id, title FROM notes ORDER BY id DESC LIMIT 1"
).fetchone())
db.close()
PY
```

## Part D — Compare file/object storage
```bash
mkdir -p objects
printf 'Synthetic demo attachment only\n' > objects/demo.txt
sha256sum objects/demo.txt
file objects/demo.txt
```

Discuss whether a large image belongs in a relational row or in object storage with a database record holding its key and metadata.

## Core challenge
Create a table with a non-null category, insert three synthetic records and query one category using parameterized SQL.

## Intermediate stretch
Add a unique constraint and demonstrate a duplicate error; create a backup with SQLite's backup API; explain transactions, indexes, retention and restore testing. Explain why a database file inside an ephemeral container is not durable cloud storage.

## Optional managed-service comparison
Only in a facilitator-approved project, compare the design with an approved managed database or object-storage service. Use synthetic data and approved identities. Do not create resources or enable billing independently.

## Troubleshooting and cleanup
Work in a directory you own if permission is denied. Close other processes if SQLite reports a lock. Duplicate rows are expected because the script inserts on every run.
```bash
cd ~
rm -rf ~/cloud-track-week-09
```

Remove only the lab directory you created.

## Evidence
Submit `week-09-evidence.md` with schema, query output, persistence proof, storage comparison, one trade-off and cleanup confirmation. Use synthetic data only.

# ChronoCore

Workflow analysis and history engine for ComfyUI workflows.

ChronoCore converts workflow data into an analyzable structure,
creates snapshots, tracks changes, supports branching,
timeline analysis and querying.

---

# Features

- ComfyUI workflow inspection
- Node graph analysis
- Prompt/model/sampler extraction
- Workflow snapshots
- History tracking
- Branch management
- Timeline reconstruction
- Diff comparison
- Query engine
- Snapshot index
- JSON serialization

---

# Installation

Clone the repository:

```bash
git clone <repository-url>
cd ChronoCore
````

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Quick Start

```python
from chrono_core import Session

session = Session(workflow)

print(session.model)
print(session.sampler)
print(session.prompts)
```

---

# Repository API

For advanced workflows:

```python
from chrono_core import WorkflowRepository

repo = WorkflowRepository()

repo.add(report)

timeline = repo.timeline()

history = repo.history()
```

---

# Timeline

ChronoCore can reconstruct workflow evolution:

```python
timeline = repo.timeline()

events = timeline.stream()

graph = timeline.graph()
```

---

# Query

Query workflow snapshots:

```python
result = (
    repo
    .snapshot_index()
    .find(
        sampler__steps=20
    )
    .order_by(
        "sampler.steps"
    )
)
```

Query results support:

* filtering
* ordering
* slicing
* selection
* aggregation

Example:

```python
result.limit(10)
```

---

# Branches

Create independent workflow histories:

```python
repo.create_branch(
    "experiment"
)

repo.checkout(
    "experiment"
)
```

---

# Serialization

Save history:

```python
repo.save(
    "history.json"
)
```

Load:

```python
repo.load(
    "history.json"
)
```

---

# Package API

```python
from chrono_core import (
    Session,
    WorkflowRepository,
    WorkflowReport,
    WorkflowTimeline,
    WorkflowQuery,
    QueryResult,
)
```

---

# Project Status

Version: 1.0.0

Tests:

```
126 passed
```

---

# Architecture

ChronoCore is organized into several layers. Each layer has a single responsibility:
workflow data flows from input adapters through analysis into immutable history and queryable timeline structures.

```text
ChronoCore
│
├── Input Layer
│   ├── adapters/
│   └── io/
│
├── Analysis Layer
│   ├── inspector/
│   ├── analyzers/
│   ├── extractors/
│   └── conditioning/
│
├── Domain Layer
│   ├── graph/
│   ├── report/
│   ├── history/
│   ├── branches/
│   ├── events/
│   └── diff/
│
├── Query Layer
│   ├── timeline/
│   ├── query/
│   └── index/
│
├── Persistence Layer
│   ├── serialization/
│   └── storage/
│
└── Public API
    ├── api/
    └── repository/
````

---

# License

TBD

class WorkflowTimeline:
    """
    Преобразует историю snapshot
    в последовательность событий.
    """


    def __init__(
        self,
        history,
    ):

        self.history = history


    def build(self):

        snapshots = self.history.all()

        if not snapshots:
            return []


        events = []


        events.append(
            {
                "type": "created",
                "message": "Initial workflow",
                "snapshot": snapshots[0].id,
            }
        )


        for index in range(
            1,
            len(snapshots)
        ):

            previous = snapshots[index - 1]

            current = snapshots[index]


            diff = previous.compare(
                current
            )


            if (
                diff["changed"]
                or diff["added"]
                or diff["removed"]
            ):

                events.append(
                    {
                        "type": "changed",
                        "snapshot": current.id,
                        "changes": self._normalize_diff(
                            diff
                        ),
                    }
                )


        return events
        
    def _normalize_diff(
        self,
        diff,
    ):

        if "changed" in diff:
            return diff["changed"]


        return diff

    def events(self):

        return [
            event.to_dict()
            for event in self.history.events()
        ]       
        
    def stream(self):

        stream = []


        for event in self.history.events():

            stream.append(
                event.to_dict()
            )


        return sorted(
            stream,
            key=lambda item:
                item["created"]
        )        
        
    def filter(
        self,
        type=None,
        after=None,
        before=None
    ):

        items = self.stream()


        result = []


        for item in items:

            if type is not None:

                if item.get("type") != type:
                    continue


            created = item.get(
                "created"
            )


            if after is not None:

                if created <= after:
                    continue


            if before is not None:

                if created >= before:
                    continue


            result.append(
                item
            )


        return result

    def summary(self):

        stream = self.stream()


        result = {
            "total": len(stream),
            "snapshots": 0,
            "branches": 0,
            "changes": 0,
        }


        for item in stream:

            event_type = item.get(
                "type"
            )


            if event_type == "snapshot_created":
                result["snapshots"] += 1


            elif event_type == "branch_created":
                result["branches"] += 1


            elif event_type == "changed":
                result["changes"] += 1


        return result 

    def changed(
        self,
        key,
    ):

        result = []


        for event in self.build():

            if event["type"] != "changed":
                continue


            changes = event.get(
                "changes",
                {}
            )


            if key not in changes:
                continue


            result.append(
                changes[key]
            )


        return result        
        
    def history_of(
        self,
        path,
    ):

        result = []


        parts = path.split(
            "."
        )


        for snapshot in self.history.all():

            value = snapshot.report.to_dict()


            try:

                for part in parts:

                    value = value[part]


                result.append(
                    value
                )


            except (
                KeyError,
                TypeError,
            ):

                continue


        return result

    def branch_history(
        self,
        branch,
    ):

        if branch not in self.history.branches:
            return []


        result = []


        target = self.history.branches[
            branch
        ]


        for snapshot in target.all():

            result.append(
                {
                    "snapshot": snapshot.id,
                    "report": snapshot.report.to_dict(),
                }
            )


        return result
        
    def compare_branches(
        self,
        old_branch,
        new_branch,
    ):

        old_history = self.branch_history(
            old_branch
        )

        new_history = self.branch_history(
            new_branch
        )


        if not old_history or not new_history:
            return {
                "changed": {},
                "added": {},
                "removed": {},
            }


        from ..diff import WorkflowDiff
        from ..report import WorkflowReport


        old_report = WorkflowReport.from_dict(
            old_history[-1]["report"]
        )

        new_report = WorkflowReport.from_dict(
            new_history[-1]["report"]
        )


        return WorkflowDiff().compare(
            old_report,
            new_report
        )        
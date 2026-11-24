# Issue tracker: GitHub

Work items for this repo live as GitHub Issues in `kastico/WaterHawk` (private). Use the `gh` CLI.

- **Create**: `gh issue create --title "..." --body "..."` (heredoc for multi-line bodies)
- **Read**: `gh issue view <number> --comments`
- **List**: `gh issue list --state open --json number,title,body,labels`
- **Comment**: `gh issue comment <number> --body "..."`
- **Labels**: `gh issue edit <number> --add-label "..."` / `--remove-label "..."`
- **Close**: `gh issue close <number> --comment "..."`

When a skill says "publish to the issue tracker", create a GitHub issue. When it says "fetch the relevant ticket", run `gh issue view <number> --comments`.

## Pull requests as a triage surface

**PRs as a request surface: no.** `/triage` ignores pull requests.

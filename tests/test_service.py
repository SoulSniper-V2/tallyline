from app.service import export_markdown, run_case


def test_run_reconciles_duplicate_activity_row_and_keeps_uncertainty_visible():
    result = run_case()

    assert result.summary.supported == 3
    assert result.summary.needs_review == 1
    assert result.summary.blocked == 1
    assert result.claims[0].value == "128 households"
    assert result.claims[1].value == "124 kits"
    assert "duplicate-looking row" in result.report_markdown
    assert len([decision for decision in result.decisions if not decision.resolved]) == 3


def test_approval_resolves_only_the_requested_human_decision():
    result = run_case({"budget-variance": "Carry the balance forward to the fall heat-safety round."})
    finance = next(claim for claim in result.claims if claim.id == "claim-funds")
    story = next(claim for claim in result.claims if claim.id == "claim-story")

    assert finance.status == "resolved"
    assert finance.approved is True
    assert story.status == "blocked"
    assert "Carry the balance" in finance.detail


def test_export_has_traceability_index_and_open_decision_count():
    exported = export_markdown(run_case())

    assert "## Evidence index" in exported
    assert "`finance.csv`" in exported
    assert "**Open human decisions:** 3" in exported

"""Publish the Variance Diagnostic experiment."""

from website import publish_experiment

with open("exp_variance_diagnostic.html") as f:
    html = f.read()
with open("exp_variance_diagnostic.css") as f:
    css = f.read()
with open("exp_variance_diagnostic.js") as f:
    js = f.read()

result = publish_experiment(
    slug="the-variance-diagnostic",
    title="The Variance Diagnostic",
    description="One slider, three systems. Six Sigma's answer is correct in one of them. The diagnostic asks: is variance the enemy here, or the substrate of function?",
    tags=["six-sigma", "balancing-selection", "swarm-robotics", "heterogeneity", "diagnostic"],
    html_content=html,
    css_content=css,
    js_content=js,
)
print(result)

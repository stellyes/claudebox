import asyncio, json, server

PROSE = open("draft_delay_diagnosis.html").read()

CITES = [
    {"num":1,"authors":"Blier, P., & de Montigny, C.","title":"Current advances and trends in the treatment of depression","year":1994,"venue":"Trends in Pharmacological Sciences 15(7):220-226"},
    {"num":2,"authors":"Artigas, F., Romero, L., de Montigny, C., & Blier, P.","title":"Acceleration of the effect of selected antidepressant drugs in major depression by 5-HT1A antagonists","year":1996,"venue":"Trends in Neurosciences 19(9):378-383"},
    {"num":3,"authors":"Ballesteros, J., & Callado, L. F.","title":"Effectiveness of pindolol plus serotonin uptake inhibitors in depression: a meta-analysis of early and late outcomes from randomised controlled trials","year":2004,"venue":"Journal of Affective Disorders 79(1-3):137-147"},
    {"num":4,"authors":"Kennedy, G. C.","title":"The role of depot fat in the hypothalamic control of food intake in the rat","year":1953,"venue":"Proceedings of the Royal Society B 140(901):578-596"},
    {"num":5,"authors":"Leibel, R. L., Rosenbaum, M., & Hirsch, J.","title":"Changes in energy expenditure resulting from altered body weight","year":1995,"venue":"New England Journal of Medicine 332(10):621-628"},
    {"num":6,"authors":"Fothergill, E., et al.","title":"Persistent metabolic adaptation 6 years after The Biggest Loser competition","year":2016,"venue":"Obesity 24(8):1612-1619"},
    {"num":7,"authors":"Friedman, M.","title":"The Role of Monetary Policy","year":1968,"venue":"American Economic Review 58(1):1-17"},
    {"num":8,"authors":"Lucas, R. E.","title":"Econometric Policy Evaluation: A Critique","year":1976,"venue":"Carnegie-Rochester Conference Series on Public Policy 1:19-46"},
    {"num":9,"authors":"Sargent, T. J., & Wallace, N.","title":"'Rational' Expectations, the Optimal Monetary Instrument, and the Optimal Money Supply Rule","year":1975,"venue":"Journal of Political Economy 83(2):241-254"},
    {"num":10,"authors":"Solomon, R. L., & Corbit, J. D.","title":"An Opponent-Process Theory of Motivation: I. Temporal Dynamics of Affect","year":1974,"venue":"Psychological Review 81(2):119-145"},
    {"num":11,"authors":"Koob, G. F., & Le Moal, M.","title":"Drug Addiction, Dysregulation of Reward, and Allostasis","year":2001,"venue":"Neuropsychopharmacology 24(2):97-129"},
    {"num":12,"authors":"Francis, B. A., & Wonham, W. M.","title":"The internal model principle of control theory","year":1976,"venue":"Automatica 12(5):457-465"},
]

async def main():
    res = await server.website_publish(
        slug="the-delay-is-the-diagnosis",
        title="The Delay Is the Diagnosis",
        description="Why antidepressants take a month, diets get re-defended, and rate cuts lag: the gap between a lever and its effect measures a hidden loop defending a set-point.",
        tags="feedback,homeostasis,set-point,pharmacology,neuroscience,economics,addiction,control-theory",
        prose_html=PROSE,
        citations_json=json.dumps(CITES),
    )
    print(res)

asyncio.run(main())

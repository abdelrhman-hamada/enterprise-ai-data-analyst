import json


def build_ai_context(report):

    context = {
        "overview": report["overview"],
        "data_quality": report["data_quality"],
        "column_profiles": report["column_profiles"],
        "numerical_analysis": report["numerical_analysis"],
        "categorical_analysis": report["categorical_analysis"],
        "outliers": report["outliers"],
        "correlations": report["correlations"],
    }

    return json.dumps(
        context,
        indent=2,
        default=str
    )
# AWS IAM Policy Generator

This repo attempts to provide a very basic, POC of a web frontend for [policy_sentry](https://github.com/salesforce/policy_sentry). My goal is to create a web interface for those less experienced with AWS IAM to use it to generate least-privilege IAM policies with at least some standards in place.

## Usage

```bash
git clone https://github.com/1davidmichael/iam_generator && cd iam_generator
poetry install
poetry run uvicorn src.html:app --reload
```

Then access the url: <http://localhost:8000/>

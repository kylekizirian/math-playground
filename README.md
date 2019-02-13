# math-playground

[![CircleCI](https://circleci.com/gh/kylekizirian/math-playground.svg?style=svg)](https://circleci.com/gh/kylekizirian/math-playground)

A playground for learning both math and programming side-by-side, with most
code snippets coming out of working on
[Project Euler](https://projecteuler.net/) problems.

## Prequisites

- [Anaconda3](https://www.anaconda.com/download/#macos) or
[Miniconda3](https://conda.io/miniconda.html)

## Create Environment, pip install, and run tests

```bash
conda env create -f environment.yml
conda activate math_env
pip install -r requirements.txt
pip install -e .
pytest --doctest-modules
```

## Resources

This repo is like a much less cool version of 
[Peter Norvig's pytudes](https://github.com/norvig/pytudes)

My current favorite Python resource is
[Fluent Python](https://www.amazon.com/Fluent-Python-Concise-Effective-Programming/dp/1491946008)

My current favorite math resource is
[Concrete Mathematics](https://www.amazon.com/Concrete-Mathematics-Foundation-Computer-Science/dp/0201558025)
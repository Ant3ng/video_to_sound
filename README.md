- how to setup env
    - poetry config virtualenvs.in-project true
    - pyenv install 3.10
    - pyenv local 3.10
    - poetry env use $(pyenv which python3)
    - pyenv install --sync
    - and, `brew install ffmpeg`

- how to run
    -  `poetry run python3 convert_and_split.py <video_filename.mov>`
    -  `convert.py` is no longer used (at least currently).

- reference
    - https://zenn.dev/hiroga/articles/poetry-env-cannot-use-python3_10
    - https://sig9.org/archives/2467
    - https://stackoverflow.com/a/71083295

<!--

Hey, you!
Are you reading this in the generated README.md? Then you're in the wrong place!

The template and data used to generate the README is in `README.md.in` and `data.json`, respectively.

The README.md is generated using the following command: python3 generate_readme.py

-->

# 🛠️ Are Copilots Local Yet?

Current trends and state of the art for using open & local LLM models as copilots to complete code, generate projects, act as shell assistants, automatically fix bugs, and more.

📝 *Help keep this list relevant and up-to-date by [making edits][edit]!*

[edit]: https://github.com/ErikBjare/are-copilots-local-yet/edit/master/data/data.yaml

## 📋 Summary

Local Copilots are in an early experimental stage, with most being of MVP-quality.

The reasons for this are:

- 📉 Local models still being inferior to Copilot
- 🔧 Difficult to set up
- 💻 High hardware requirements

However, as models improve, and editor extensions get developed to use them, we're expected to get a renaissance of code-completion tools.

This document is a curated list of local Copilots, shell assistants, and related projects. It is intended to be a resource for those interested in a survey of the existing tools, and to help developers discover the state of the art for projects like these.

## 📚 Background

In 2021, GitHub released Copilot which quickly became popular among devs. Since then, with the flurry of AI developments around LLMs, local models that can run on consumer machines have become available, and it has seemed only a matter of time before Copilot will go local.

Many perceived limitations of GitHub's Copilot are related to its closed and cloud-hosted nature.

As an alternative, local Copilots enable:

- 🌐 Offline & private use
- ⚡ Improved responsiveness
- 📚 Better project/context awareness
- 🎯 The ability to run models specialized for a particular language/task
- 🔒 [Constraining the LLM output](https://twitter.com/ErikBjare/status/1656731582001020928) to fit a particular format/syntax.

## 🧩 Extensions

Editor extensions used to complete code using LLMs:

| Name          | Editor   | :star:  | Released | Notes     |
| ------------- | -------- | ------- | -------- | --------- |
| [GitHub Copilot](https://github.com/github/copilot.vim) | VSCode, vim | 6203 | 2021-6-29 | The GitHub Original, not local or open-source. |
| [Cursor](https://github.com/getcursor/cursor) | VSCode | 17825 | 2023-3-14 | Fork of VSCode, not open-source |
| [Fauxpilot](https://github.com/fauxpilot/fauxpilot) | VSCode | 13203 | 2022-9-3 | Early local PoC. Stale? |
| [Tabby](https://github.com/TabbyML/tabby) | VSCode | 10850 | 2023-9-30 | Completes the cursor selection |
| [turbopilot](https://github.com/ravenscroftj/turbopilot) | VSCode | 3839 | 2023-4-10 | Completions with FIM support, inspired by fauxpilot |
| [HuggingFace-vscode](https://github.com/huggingface/huggingface-vscode) | VSCode | 745 | 2023-6-19 | Fork of Tabnine, supports Starcoder |
| [localpilot](https://github.com/danielgross/localpilot) | VSCode | 427 | 2023-10-2 |  |
| [StarcoderEx](https://github.com/Lisoveliy/StarCoderEx) | VSCode | 79 |  | Completes the cursor selection |
| [WizardCoder-VSC](https://github.com/mzbac/wizardCoder-vsc) | VSCode | 107 |  | PoC, article available |


## 🛠️ Tools

Tools that try to generate projects/features from specification:

| Name           | :star:  | Released  | Notes |
| -------------- | ------- | --------- | ----- |
| [gpt-engineer](https://github.com/AntonOsika/gpt-engineer) | 44257 | 2023-6-6 | Specify what you want it to build, the AI asks for clarification, and then builds it. |
| [gpt-pilot](https://github.com/Pythagora-io/gpt-pilot) | 4599 | 2023-7-18 | Very similar to gpt-engineer |
| [continue](https://github.com/continuedev/continue) | 4288 | 2023-5-24 | VSCode extension. Task-based autocomplete |
| [aider](https://github.com/paul-gauthier/aider) | 3987 | 2023-6-8 | AI pair programming in your terminal, works well with pre-existing, larger codebases |
| [rift](https://github.com/morph-labs/rift) | 2599 | 2023-6-20 | VSCode extension. Lets you write code by chatting, makes your IDE agentic, AI engineer that works alongside you. |
| [mentat](https://github.com/biobootloader/mentat) | 1636 | 2023-7-25 | Mentat coordinates edits across multiple locations and files. |
| [clippinator](https://github.com/ennucore/clippinator) | 246 | 2023-4-15 | Uses a team of agents to plan, write, debug, and test |


## 🗨️ Chat Interfaces

Chat interfaces with shell/REPL/notebook access.
Similar to/inspired by ChatGPT's "Advanced Data Analysis" feature (previously "Code Interpreter").

| Name           | :star:  | Notes     |
| -------------- | ------- | --------- |
| [open-interpreter](https://github.com/KillianLucas/open-interpreter) | 27802 | open-source, locally running implementation of OpenAI's Code Interpreter |
| [gptme](https://github.com/ErikBjare/gptme) | 88 | Supporting open models. Developed by me, @ErikBjare |
| [octogen](https://github.com/dbpunk-labs/octogen) | 109 | Local Code Interpreter executing in Docker environment. |
| [terminal-x](https://github.com/davidfant/terminal-x) | 29 | Very early prototype that converts natural language into shell commands, unmaintained since Sept. 2021 |


## 🤖 Models

Models relevant for local Copilot-use. Ordered by most recent first.

| Name                            | Size       | Languages   | :star:  | Released   | Notes   |
| ------------------------------- | ---------- | ----------- | ------- | ---------- | ------- |
| [Phind CodeLlama v2](https://huggingface.co/Phind/Phind-CodeLlama-34B-v2) | 34B | Many | 332 | 2023-8-27 |  |
| [WizardCoder-Python](https://huggingface.co/WizardLM/WizardCoder-Python-34B-V1.0) | 7/13/34B | Python | 597 | 2023-8 |  |
| [CodeLlama](https://github.com/facebookresearch/codellama) | 7/13/34B | Many | 10166 | 2023-8 |  |
| [WizardCoder](https://huggingface.co/WizardLM/WizardCoder-15B-V1.0) | 15B | 80+ | 614 | 2023-6 | Fine-tuning of Starcoder |
| [replit-glaive](https://huggingface.co/sahil2801/replit-code-instruct-glaive) | 3B | 1? | 83 | 2023-7 | Small model fine-tuned on high-quality data with impressive performance. |
| [Starcoder](https://github.com/bigcode-project/starcoder) | 15B | 80+ | 6393 | 2023-5 |  |
| [replit-v1-3b](https://huggingface.co/replit/replit-code-v1-3b) | 3B | 20+ | 674 | 2023-5 |  |
| [SantaCoder](https://huggingface.co/bigcode/santacoder) | 1.1B | Python, Java, JavaScript | 298 | 2023-4 | Tiny model selectively trained on 3 languages from 'The Stack' |


**Note:** due to the pace of new model releases, this section is doomed to be out of date.

## 📚 Datasets

Datasets relevant for training models.

| Name                            | Size       | Languages   | :star:  | Released   | Notes   |
| ------------------------------- | ---------- | ----------- | ------- | ---------- | ------- |
| [The Stack](https://huggingface.co/datasets/bigcode/the-stack) | 3TB (v1.0), 6TB (v1.1) | 358 | >500 | 2022-10 | Excludes weak-copyleft licenses (MPL, LGPL, EGL) since v1.1 |


## Tools

Misc relevant useful tools.

| Name                            | :star:  | Released   | Notes   |
| ------------------------------- | ------- | ---------- | ------- |
| [ollama](https://github.com/jmorganca/ollama) | 8075 | 2023-8-27 | Easily get up and running with large language models locally. |


## 📰 Misc

- 🐦 [Tweet announcing this repo][announce]

[announce]: https://twitter.com/ErikBjare/status/1681616666600394753

## 📈 Stats

Stargazers over time:

[![Stargazers over time](https://starchart.cc/ErikBjare/are-copilots-local-yet.svg)](https://starchart.cc/ErikBjare/are-copilots-local-yet)